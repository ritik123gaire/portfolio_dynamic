import os

from django.conf import settings
from django.http import HttpResponseForbidden


class AdminIPRestrictionMiddleware:
    """Optionally restrict access to the Django admin by client IP.

    - Controlled via the ALLOWED_ADMIN_IPS env var (comma-separated list).
    - If ALLOWED_ADMIN_IPS is empty or not set, this middleware does nothing.
    - Designed for use behind a proxy (Railway), so it prefers X-Forwarded-For.
    """

    def __init__(self, get_response):
        self.get_response = get_response

        # Normalised admin prefix, always starting with '/'
        prefix = getattr(settings, "ADMIN_URL_PREFIX", "site-admin-ritik/")
        self.admin_prefix = "/" + prefix.lstrip("/")

        allowed_ips = os.getenv("ALLOWED_ADMIN_IPS", "").strip()
        if allowed_ips:
            self.allowed_ips = {ip.strip() for ip in allowed_ips.split(",") if ip.strip()}
        else:
            self.allowed_ips = set()

    def __call__(self, request):
        response = self.process_request(request)
        if response is not None:
            return response
        return self.get_response(request)

    def get_client_ip(self, request):
        """Best-effort client IP extraction, aware of proxies."""

        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            # First IP in the list is the original client
            return x_forwarded_for.split(",")[0].strip()
        return request.META.get("REMOTE_ADDR")

    def process_request(self, request):
        # If no IPs configured, allow everything
        if not self.allowed_ips:
            return None

        # Only apply restriction for admin URLs
        if request.path.startswith(self.admin_prefix):
            client_ip = self.get_client_ip(request)
            if client_ip not in self.allowed_ips:
                return HttpResponseForbidden("Forbidden")

        return None
