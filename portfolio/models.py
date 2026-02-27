from django.db import models
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    """Main profile information"""
    name = models.CharField(max_length=200, default="Ritik Gaire")
    tagline = models.CharField(max_length=200, default="I LOVE TO CODE")
    about_text = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)
    
    # Social Media Links
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
    
    def __str__(self):
        return self.name


class Education(models.Model):
    """Education history"""
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    
    class Meta:
        ordering = ['order', '-end_date']
        verbose_name = "Education"
        verbose_name_plural = "Education"
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"


class Experience(models.Model):
    """Work experience"""
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False, help_text="Currently working here")
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    
    class Meta:
        ordering = ['order', '-end_date']
        verbose_name = "Experience"
        verbose_name_plural = "Experience"
    
    def __str__(self):
        return f"{self.position} at {self.company}"


class Skill(models.Model):
    """Skills and technologies"""
    CATEGORY_CHOICES = [
        ('programming', 'Programming Language'),
        ('database', 'Database'),
        ('data_analysis', 'Data Analysis Libraries'),
        ('web_framework', 'Web Frameworks'),
        ('tools', 'Other Tools'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0, help_text="Display order within category")
    
    class Meta:
        ordering = ['category', 'order', 'name']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Service(models.Model):
    """Services offered"""
    title = models.CharField(max_length=200)
    icon_class = models.CharField(max_length=100, help_text="Icon class (e.g., 'icon-laptop')")
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Service"
        verbose_name_plural = "Services"
    
    def __str__(self):
        return self.title


class Project(models.Model):
    """Portfolio projects"""
    CATEGORY_CHOICES = [
        ('data_science', 'Data Science'),
        ('machine_learning', 'Machine Learning'),
        ('web', 'Web Development'),
        ('ai', 'AI/LLM'),
    ]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, help_text="External image URL (used if no uploaded image)")
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-featured', 'order', '-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return self.title


class BlogPost(models.Model):
    """Blog posts"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    excerpt = models.TextField(max_length=500, help_text="Short summary for display")
    author = models.CharField(max_length=100, default="John Doe")
    company = models.CharField(max_length=100, default="Google Inc.", blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-featured', 'order', '-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
    
    def __str__(self):
        return self.title


class Statistic(models.Model):
    """Portfolio statistics/numbers"""
    label = models.CharField(max_length=100)
    value = models.IntegerField()
    icon_class = models.CharField(max_length=100, help_text="Icon class (e.g., 'icon-trophy')")
    order = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'label']
        verbose_name = "Statistic"
        verbose_name_plural = "Statistics"
    
    def __str__(self):
        return f"{self.label}: {self.value}"


class ContactMessage(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
    
    def __str__(self):
        return f"Message from {self.name} - {self.created_at.strftime('%Y-%m-%d')}"
