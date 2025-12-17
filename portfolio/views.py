from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (
    Profile, Education, Experience, Skill, Service,
    Project, BlogPost, Statistic, ContactMessage
)

# Create your views here.

def home(request):
    """Main portfolio page"""
    # Get or create profile
    profile = Profile.objects.first()
    
    # Get all data
    education_list = Education.objects.all()
    experience_list = Experience.objects.all()
    
    # Group skills by category
    skills = {}
    for skill in Skill.objects.all():
        category = skill.get_category_display()
        if category not in skills:
            skills[category] = []
        skills[category].append(skill.name)
    
    services = Service.objects.filter(active=True)
    projects = Project.objects.all()
    blog_posts = BlogPost.objects.all()[:3]  # Latest 3 blog posts
    statistics = Statistic.objects.filter(active=True)
    
    context = {
        'profile': profile,
        'education_list': education_list,
        'experience_list': experience_list,
        'skills': skills,
        'services': services,
        'projects': projects,
        'blog_posts': blog_posts,
        'statistics': statistics,
    }
    
    return render(request, 'portfolio/index.html', context)


def contact_form(request):
    """Handle contact form submission"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(request, 'Thank you for your message! I will get back to you soon.')
        return redirect('home')
    
    return redirect('home')
