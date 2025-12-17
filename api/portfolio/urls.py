from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SkillViewSet, BlogViewSet, ProjectViewSet,
    ExperienceViewSet, EducationViewSet,
    CertificationViewSet, ContactInfoViewSet, AboutMeViewSet
)

router = DefaultRouter()
router.register('skills', SkillViewSet)
router.register('blogs', BlogViewSet)
router.register('projects', ProjectViewSet)
router.register('experiences', ExperienceViewSet)
router.register('education', EducationViewSet)
router.register('certifications', CertificationViewSet)
router.register('contact-info', ContactInfoViewSet)
router.register('about-me', AboutMeViewSet)

urlpatterns = [
    # Other URL patterns
    path('api/', include(router.urls)),
]
