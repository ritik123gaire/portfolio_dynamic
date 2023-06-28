from django.db import models

class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    proficiency = models.IntegerField(default=0, help_text='Proficiency level (0-100)')

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.CharField(max_length=200)
    project_url = models.URLField(blank=True, null=True)
    repository_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    graduation_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.degree


class Certification(models.Model):
    title = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class AboutMe(models.Model):
    summary = models.TextField()
    profile_picture = models.ImageField(upload_to='aboutme/', blank=True, null=True)
    resume = models.FileField(upload_to='aboutme/', blank=True, null=True)

    def __str__(self):
        return 'About Me'
