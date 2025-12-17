from django.core.management.base import BaseCommand
from portfolio.models import (
    Profile, Education, Experience, Skill, Service,
    Project, BlogPost, Statistic
)
from datetime import date


class Command(BaseCommand):
    help = 'Update portfolio with latest resume data'

    def handle(self, *args, **options):
        self.stdout.write('Updating portfolio with latest resume data...')

        # Update Profile
        profile = Profile.objects.first()
        if profile:
            profile.name = 'Ritik Gaire'
            profile.tagline = 'I LOVE TO CODE'
            profile.about_text = 'Machine Learning Engineer with hands-on experience building end-to-end ML pipelines, performing statistical analysis, and applying computer vision models to real-world data. Strong foundation in feature engineering, model evaluation, and error analysis, with applied experience deploying ML-backed systems using Python.\n\nLocation: Flint, MI\nEmail: ritikg@umich.edu\nPhone: (810) 210-4720'
            profile.linkedin_url = 'https://www.linkedin.com/in/ritik-gaire'
            profile.github_url = 'https://github.com/ritik123gaire'
            profile.save()
            self.stdout.write(self.style.SUCCESS('✓ Profile updated'))

        # Clear and update Education
        Education.objects.all().delete()
        education_data = [
            {
                'institution': 'University of Michigan–Flint',
                'degree': 'Master of Science in Computer Science & Information Systems',
                'start_date': date(2025, 1, 1),
                'end_date': date(2026, 12, 31),
                'description': 'Expected graduation: Dec 2026',
                'order': 1
            },
            {
                'institution': 'Tribhuvan University',
                'degree': 'Bachelor of Science in Computer Science & Information Technology',
                'start_date': date(2019, 1, 1),
                'end_date': date(2023, 12, 31),
                'description': 'GPA: 3.7 / 4.0 | Kathmandu, Nepal',
                'order': 2
            },
        ]
        for edu_data in education_data:
            Education.objects.create(**edu_data)
        self.stdout.write(self.style.SUCCESS('✓ Education updated'))

        # Clear and update Experience
        Experience.objects.all().delete()
        experience_data = [
            {
                'company': 'University of Michigan–Flint',
                'position': 'Graduate Research Assistant (Machine Learning & Statistics)',
                'start_date': date(2025, 5, 1),
                'end_date': date(2025, 6, 30),
                'description': '• Analyzed 500+ survey responses to quantify algorithmic bias across demographic groups using statistical methods\n• Applied ANOVA and correlation analysis to identify significant patterns and validate research hypotheses\n• Interpreted statistical results to support conclusions incorporated into an academic research paper\n• Built visualizations to communicate model insights and statistical findings to faculty stakeholders',
                'order': 1
            },
            {
                'company': 'Roshani Digital Pvt. Ltd.',
                'position': 'Backend Developer (Data-Driven Systems)',
                'start_date': date(2024, 3, 1),
                'end_date': date(2024, 10, 31),
                'description': '• Designed data-centric REST APIs to support analytics-heavy application workflows\n• Optimized relational database queries and schema design, reducing response latency by approximately 40 percent\n• Collaborated with cross-functional teams to ensure reliable data ingestion and downstream processing',
                'order': 2
            },
            {
                'company': 'Spyders Lab',
                'position': 'Junior Backend Developer (Intern)',
                'start_date': date(2023, 9, 1),
                'end_date': date(2024, 1, 31),
                'description': '• Implemented data validation, authentication, and CRUD pipelines supporting analytics dashboards\n• Integrated 10+ API endpoints consumed by frontend visualization components',
                'order': 3
            },
        ]
        for exp_data in experience_data:
            Experience.objects.create(**exp_data)
        self.stdout.write(self.style.SUCCESS('✓ Experience updated'))

        # Clear and update Skills
        Skill.objects.all().delete()
        skills_data = [
            # ML & Data
            {'category': 'data_analysis', 'name': 'Scikit-learn', 'order': 1},
            {'category': 'data_analysis', 'name': 'Statistical Modeling', 'order': 2},
            {'category': 'data_analysis', 'name': 'Feature Engineering', 'order': 3},
            {'category': 'data_analysis', 'name': 'Model Evaluation', 'order': 4},
            {'category': 'data_analysis', 'name': 'Error Analysis', 'order': 5},
            {'category': 'data_analysis', 'name': 'OpenCV', 'order': 6},
            
            # Programming
            {'category': 'programming', 'name': 'Python', 'order': 1},
            {'category': 'programming', 'name': 'SQL', 'order': 2},
            
            # ML Systems & Tools
            {'category': 'tools', 'name': 'LangGraph', 'order': 1},
            {'category': 'tools', 'name': 'Docker', 'order': 2},
            {'category': 'tools', 'name': 'Git', 'order': 3},
            {'category': 'tools', 'name': 'AWS', 'order': 4},
            {'category': 'tools', 'name': 'Linux', 'order': 5},
            
            # Backend (Supporting)
            {'category': 'web_framework', 'name': 'Django', 'order': 1},
            {'category': 'web_framework', 'name': 'Django REST Framework', 'order': 2},
            {'category': 'web_framework', 'name': 'Flask', 'order': 3},
            
            # Databases
            {'category': 'database', 'name': 'MySQL', 'order': 1},
            {'category': 'database', 'name': 'MongoDB', 'order': 2},
        ]
        for skill_data in skills_data:
            Skill.objects.create(**skill_data)
        self.stdout.write(self.style.SUCCESS('✓ Skills updated'))

        # Update Services
        Service.objects.all().delete()
        services_data = [
            {'title': 'Machine Learning', 'icon_class': 'icon-layers', 'description': 'Building end-to-end ML pipelines and predictive models', 'order': 1},
            {'title': 'Computer Vision', 'icon_class': 'icon-eye', 'description': 'Object detection and tracking using YOLO and OpenCV', 'order': 2},
            {'title': 'Statistical Analysis', 'icon_class': 'icon-graph', 'description': 'ANOVA, correlation analysis, and hypothesis testing', 'order': 3},
            {'title': 'Backend Development', 'icon_class': 'icon-laptop', 'description': 'REST APIs and data-driven systems with Django', 'order': 4},
            {'title': 'AI Agent Systems', 'icon_class': 'icon-tools', 'description': 'Multi-agent systems using LangGraph and LLMs', 'order': 5},
            {'title': 'Cloud & DevOps', 'icon_class': 'icon-cloud', 'description': 'AWS, Docker, and deployment automation', 'order': 6},
        ]
        for service_data in services_data:
            Service.objects.create(**service_data)
        self.stdout.write(self.style.SUCCESS('✓ Services updated'))

        # Update Projects
        Project.objects.all().delete()
        projects_data = [
            {
                'title': 'Soccer Match Analytics System',
                'category': 'data_science',
                'description': 'Built an end-to-end machine learning pipeline to predict soccer match outcomes using historical performance data. Engineered features capturing team form, possession, and match dynamics. Applied YOLO-based computer vision models for player and ball tracking to extract visual performance indicators. Evaluated model performance using classification metrics and analyzed failure cases.',
                'github_url': 'https://github.com/ritik123gaire',
                'featured': True,
                'order': 1
            },
            {
                'title': 'Multi-Agent Research System',
                'category': 'data_science',
                'description': 'Designed a multi-agent system to autonomously plan, execute, and validate research workflows using LangGraph and LLMs. Implemented human-in-the-loop checkpoints to mitigate error propagation and hallucination risks. Optimized agent execution and prompt strategies, reducing LLM token usage by approximately 30 percent.',
                'github_url': 'https://github.com/ritik123gaire',
                'featured': True,
                'order': 2
            },
        ]
        for project_data in projects_data:
            # Need image - will use placeholder
            Project.objects.create(**project_data)
        self.stdout.write(self.style.SUCCESS('✓ Projects updated'))
        self.stdout.write(self.style.WARNING('  ⚠ Note: Project images need to be added through admin panel'))

        # Update Statistics
        Statistic.objects.all().delete()
        statistics_data = [
            {'label': 'ML Projects', 'value': 2, 'icon_class': 'icon-layers', 'order': 1},
            {'label': 'Years Experience', 'value': 2, 'icon_class': 'icon-briefcase', 'order': 2},
            {'label': 'Technologies', 'value': 15, 'icon_class': 'icon-tools', 'order': 3},
            {'label': 'Certifications', 'value': 1, 'icon_class': 'icon-trophy', 'order': 4},
        ]
        for stat_data in statistics_data:
            Statistic.objects.create(**stat_data)
        self.stdout.write(self.style.SUCCESS('✓ Statistics updated'))

        # Update Blog Posts with relevant ML/AI topics
        BlogPost.objects.all().delete()
        blog_posts_data = [
            {
                'title': 'Building End-to-End ML Pipelines',
                'content': 'Learn how to build production-ready machine learning pipelines from data ingestion to model deployment. Covers feature engineering, model evaluation, and error analysis best practices.',
                'excerpt': 'A comprehensive guide to building production-ready ML pipelines with proper feature engineering and model evaluation.',
                'author': 'Ritik Gaire',
                'company': 'University of Michigan-Flint',
                'featured': True,
                'order': 1
            },
            {
                'title': 'Computer Vision in Sports Analytics',
                'content': 'Exploring how YOLO-based object detection and tracking can extract valuable performance indicators from sports footage. Real-world applications in soccer match analysis.',
                'excerpt': 'How computer vision and YOLO models are transforming sports analytics through automated player and ball tracking.',
                'author': 'Ritik Gaire',
                'company': 'University of Michigan-Flint',
                'featured': True,
                'order': 2
            },
            {
                'title': 'Multi-Agent AI Systems',
                'content': 'Deep dive into building autonomous multi-agent systems using LangGraph. Learn about human-in-the-loop validation, error mitigation, and LLM optimization strategies.',
                'excerpt': 'Building autonomous AI agent systems with LangGraph while maintaining reliability through human-in-the-loop checkpoints.',
                'author': 'Ritik Gaire',
                'company': 'University of Michigan-Flint',
                'featured': True,
                'order': 3
            },
        ]
        for blog_data in blog_posts_data:
            BlogPost.objects.create(**blog_data)
        self.stdout.write(self.style.SUCCESS('✓ Blog posts updated'))

        self.stdout.write(self.style.SUCCESS('\n✅ Portfolio updated successfully with latest resume data!'))
        self.stdout.write(self.style.WARNING('\n📸 Remember to:'))
        self.stdout.write(self.style.WARNING('   1. Add project images through the admin panel'))
        self.stdout.write(self.style.WARNING('   2. Upload your profile picture'))
        self.stdout.write(self.style.WARNING('   3. Review and customize content as needed'))
