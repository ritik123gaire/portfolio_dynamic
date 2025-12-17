from django.contrib import admin
from .models import (
    Profile, Education, Experience, Skill, Service, 
    Project, BlogPost, Statistic, ContactMessage
)

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'tagline', 'about_text', 'profile_image', 'cv_file')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'twitter_url', 'linkedin_url', 'github_url', 'youtube_url')
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'start_date', 'end_date', 'order']
    list_editable = ['order']
    ordering = ['order', '-end_date']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'start_date', 'end_date', 'current', 'order']
    list_editable = ['order', 'current']
    list_filter = ['current']
    ordering = ['order', '-end_date']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']
    list_editable = ['order']
    list_filter = ['category']
    ordering = ['category', 'order']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_class', 'order', 'active']
    list_editable = ['order', 'active']
    list_filter = ['active']
    ordering = ['order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'order', 'created_at']
    list_editable = ['order', 'featured']
    list_filter = ['category', 'featured']
    search_fields = ['title', 'description']
    ordering = ['-featured', 'order', '-created_at']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'featured', 'order', 'created_at']
    list_editable = ['order', 'featured']
    list_filter = ['featured', 'created_at']
    search_fields = ['title', 'content', 'excerpt']
    ordering = ['-featured', 'order', '-created_at']


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ['label', 'value', 'icon_class', 'order', 'active']
    list_editable = ['value', 'order', 'active']
    list_filter = ['active']
    ordering = ['order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_editable = ['read']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    ordering = ['-created_at']
