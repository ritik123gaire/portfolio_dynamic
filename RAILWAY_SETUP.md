# Railway Deployment Guide

## Prerequisites
- Railway account (https://railway.app)
- Git repository connected to Railway
- Environment variables configured

## Environment Variables to Set in Railway Dashboard

Set these in your Railway project's Variables section:

```
DJANGO_SECRET_KEY=          # Generate with: python generate_secret_key.py
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com,*.up.railway.app
CSRF_TRUSTED_ORIGINS=https://your-domain.com,https://www.your-domain.com,https://*.up.railway.app
SECURE_SSL_REDIRECT=True
DB_SSL_REQUIRE=True
```

## Automatic Setup

Railway will:
1. Install dependencies from `requirements.txt`
2. Run migrations via `manage.py migrate`
3. Create superuser via `manage.py ensure_superuser`
4. Populate data via `manage.py populate_full_resume`
5. Collect static files via `manage.py collectstatic`
6. Start gunicorn server on port 8080

All commands are in `railway.json` under `deploy.startCommand`

## Database

Railway automatically provides a PostgreSQL database. The `DATABASE_URL` is set automatically, so no manual configuration needed.

## Custom Domain

1. Go to Railway project settings
2. Add custom domain (e.g., your-domain.com)
3. Update Django `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`

## Deploy

Push to your git repository and Railway will automatically deploy if connected.

```bash
git push origin main
```

## Logs

View logs in Railway dashboard or via CLI:
```bash
railway logs
```

## Environment Variables From .env.example

Use `.env.example` as reference for local development. Never commit `.env` file.
