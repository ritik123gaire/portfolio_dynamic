from django.core.management.base import BaseCommand
from portfolio.models import (
    Profile, Education, Experience, Skill, Service,
    Project, BlogPost, Statistic
)
from datetime import date


class Command(BaseCommand):
    help = 'Populate database with complete resume data from Ritik Gaire'

    def handle(self, *args, **options):
        self.stdout.write('Populating database with complete resume data...')

        # Update Profile
        profile, created = Profile.objects.update_or_create(
            id=1,
            defaults={
                'name': 'Ritik Gaire',
                'tagline': "ML Researcher | Backend Engineer | Data Science",
                'about_text': """Graduate Machine Learning Researcher and Backend Engineer with expertise in predictive modeling, statistical analysis, and computer vision. Co-authored a peer-reviewed paper on algorithmic bias in AI systems. Skilled in building ML pipelines, feature engineering, model evaluation, and deploying scalable data systems.

Location: Flint, MI
Email: ritikg@umich.edu""",
                'linkedin_url': 'https://linkedin.com/in/ritik-gaire',
                'github_url': 'https://github.com/ritik123gaire',
            }
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Profile {"created" if created else "updated"}'))

        # Clear and update Education
        Education.objects.all().delete()
        education_data = [
            {
                'institution': 'University of Michigan-Flint',
                'degree': 'M.S. Computer Science & Information Systems (ML/Data Science)',
                'start_date': date(2025, 1, 1),
                'end_date': date(2026, 12, 31),
                'description': 'Master of Science (In Progress) | Flint, MI',
                'order': 1
            },
            {
                'institution': 'Tribhuvan University',
                'degree': 'B.S. Computer Science & Information Technology',
                'start_date': date(2019, 1, 1),
                'end_date': date(2023, 12, 31),
                'description': 'GPA: 3.7/4.0 | Kathmandu, Nepal',
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
                'company': 'University of Michigan-Flint',
                'position': 'Graduate Research Assistant (Summer Research)',
                'start_date': date(2025, 6, 1),
                'end_date': None,
                'current': True,
                'description': """• Analyzed survey responses to identify demographic bias patterns in AI and cloud-based systems
• Applied ANOVA and correlation analysis (Pearson, Spearman) to test 8 hypotheses across 5 independent variables at α = 0.05 significance level
• Produced 15 publication-quality visualizations with Python (Matplotlib, Seaborn) through 4 revision cycles for peer review
• Co-authored peer-reviewed journal article published in Applied Sciences (MDPI)""",
                'order': 1
            },
            {
                'company': 'Roshani Digital Pvt. Ltd.',
                'position': 'Backend Developer (Data Systems)',
                'start_date': date(2024, 3, 1),
                'end_date': date(2024, 11, 30),
                'current': False,
                'description': """• Built 5 FastAPI-based microservices handling 5,000+ daily requests with p95 latency under 350ms for 100+ concurrent users
• Optimized PostgreSQL indexing and query plans, slashing average request latency by 40%
• Enforced JWT authentication and containerized 3 ingestion pipelines processing 200,000+ records/day from JSON, CSV, and API sources
• Directed ETL pipeline enhancements to support AI initiatives, raising automated data throughput by 30% and integrating Apache Airflow with Dockerized modules""",
                'order': 2
            },
            {
                'company': 'Spyders Lab',
                'position': 'Junior Backend Developer',
                'start_date': date(2023, 9, 1),
                'end_date': date(2024, 1, 31),
                'current': False,
                'description': """• Developed and optimized backend features within a Python-Django environment, focusing on performance and scalability
• Built and validated RESTful APIs with Django Rest Framework for robust data exchange, using Postman for comprehensive testing
• Collaborated in an Agile environment using Git flow and feature-branching strategies for efficient version control""",
                'order': 3
            },
        ]
        for exp_data in experience_data:
            Experience.objects.create(**exp_data)
        self.stdout.write(self.style.SUCCESS('✓ Experience updated'))

        # Clear and update Skills
        Skill.objects.all().delete()
        skills_data = [
            # ML/Data Science
            {'category': 'data_analysis', 'name': 'Scikit-learn', 'order': 1},
            {'category': 'data_analysis', 'name': 'Pandas', 'order': 2},
            {'category': 'data_analysis', 'name': 'NumPy', 'order': 3},
            {'category': 'data_analysis', 'name': 'Feature Engineering', 'order': 4},
            {'category': 'data_analysis', 'name': 'Cross-Validation', 'order': 5},
            {'category': 'data_analysis', 'name': 'Ensemble Models', 'order': 6},
            {'category': 'data_analysis', 'name': 'ROC-AUC', 'order': 7},
            {'category': 'data_analysis', 'name': 'Hypothesis Testing', 'order': 8},
            {'category': 'data_analysis', 'name': 'ANOVA', 'order': 9},
            {'category': 'data_analysis', 'name': 'Matplotlib', 'order': 10},
            {'category': 'data_analysis', 'name': 'Seaborn', 'order': 11},
            
            # Computer Vision
            {'category': 'tools', 'name': 'OpenCV', 'order': 1},
            {'category': 'tools', 'name': 'YOLOv8', 'order': 2},
            {'category': 'tools', 'name': 'Object Detection', 'order': 3},
            {'category': 'tools', 'name': 'Video Analytics', 'order': 4},
            
            # Programming Languages
            {'category': 'programming', 'name': 'Python', 'order': 1},
            {'category': 'programming', 'name': 'SQL', 'order': 2},
            
            # Cloud & DevTools
            {'category': 'web_framework', 'name': 'FastAPI', 'order': 1},
            {'category': 'web_framework', 'name': 'Django', 'order': 2},
            {'category': 'web_framework', 'name': 'Django Rest Framework', 'order': 3},
            {'category': 'web_framework', 'name': 'LangGraph', 'order': 4},
            
            # Databases
            {'category': 'database', 'name': 'PostgreSQL', 'order': 1},
            {'category': 'database', 'name': 'MySQL', 'order': 2},
            {'category': 'database', 'name': 'SQLite', 'order': 3},
            
            # DevOps
            {'category': 'tools', 'name': 'AWS', 'order': 5},
            {'category': 'tools', 'name': 'Docker', 'order': 6},
            {'category': 'tools', 'name': 'Git', 'order': 7},
            {'category': 'tools', 'name': 'Linux', 'order': 8},
            {'category': 'tools', 'name': 'Apache Airflow', 'order': 9},
        ]
        for skill_data in skills_data:
            Skill.objects.create(**skill_data)
        self.stdout.write(self.style.SUCCESS('✓ Skills updated'))

        # Update Services
        Service.objects.all().delete()
        services_data = [
            {'title': 'Machine Learning', 'icon_class': 'icon-layers', 'description': 'Predictive modeling, ensemble classifiers, feature engineering, and model evaluation', 'order': 1},
            {'title': 'Statistical Analysis', 'icon_class': 'icon-bargraph', 'description': 'ANOVA, correlation analysis, hypothesis testing, and data-driven insights', 'order': 2},
            {'title': 'Computer Vision', 'icon_class': 'icon-camera', 'description': 'Object detection, player tracking, video analytics with OpenCV and YOLOv8', 'order': 3},
            {'title': 'Backend Development', 'icon_class': 'icon-laptop', 'description': 'FastAPI, Django REST Framework, PostgreSQL, and scalable microservices', 'order': 4},
            {'title': 'Data Engineering', 'icon_class': 'icon-briefcase', 'description': 'ETL pipelines, Apache Airflow, data processing at scale', 'order': 5},
            {'title': 'Cloud & DevOps', 'icon_class': 'icon-cloud', 'description': 'AWS, Docker containerization, and deployment automation', 'order': 6},
        ]
        for service_data in services_data:
            Service.objects.create(**service_data)
        self.stdout.write(self.style.SUCCESS('✓ Services updated'))

        # Update Statistics
        Statistic.objects.all().delete()
        statistics_data = [
            {'label': 'ML Projects', 'value': 2, 'icon_class': 'icon-layers', 'order': 1},
            {'label': 'Years Experience', 'value': 2, 'icon_class': 'icon-briefcase', 'order': 2},
            {'label': 'Technologies', 'value': 30, 'icon_class': 'icon-tools', 'order': 3},
            {'label': 'Publications', 'value': 1, 'icon_class': 'icon-trophy', 'order': 4},
        ]
        for stat_data in statistics_data:
            Statistic.objects.create(**stat_data)
        self.stdout.write(self.style.SUCCESS('✓ Statistics updated'))

        # Update Projects
        Project.objects.all().delete()
        projects_data = [
            {
                'title': 'Soccer Match Analytics System',
                'category': 'data_science',
                'description': """Built an end-to-end match outcome prediction pipeline using ensemble classifiers and cross-validation. Engineered 25+ rolling features from multi-season event data, including team form, possession proxies, and shot quality. Trained models on 2,000+ matches and evaluated performance via ROC-AUC and precision/recall. Integrated YOLOv8-based player and ball tracking for video-level tactical analysis.

Technologies: Python, Scikit-learn, Pandas, OpenCV, YOLOv8""",
                'image_url': 'https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=800',
                'github_url': 'https://github.com/ritik123gaire/Soccer_Analytics',
                'featured': True,
                'order': 1
            },
            {
                'title': 'Multi-Agent Research Automation System',
                'category': 'data_science',
                'description': """Architected 5-agent workflows automating 10 research task types across 8–12 steps, cutting manual research time by 50%. Executed 4 human-in-the-loop checkpoints decreasing hallucinations by 40% and factual errors by 45%. Lowered LLM token usage by 30% through prompt tuning, caching, and batching.

Technologies: Python, LangGraph, LLMs, GPT-4o""",
                'image_url': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800',
                'github_url': 'https://github.com/ritik123gaire/Autonomous_multi_agent_research',
                'featured': True,
                'order': 2
            },
        ]
        for project_data in projects_data:
            Project.objects.create(**project_data)
        self.stdout.write(self.style.SUCCESS('✓ Projects updated'))
        self.stdout.write(self.style.WARNING('  ⚠ Note: Project images need to be added through admin panel'))

        # Update Blog Posts
        BlogPost.objects.all().delete()
        blog_posts_data = [
            {
                'title': 'Public Perceptions of Algorithmic Bias and Fairness in Cloud-Based Decision Systems',
                'content': """Published peer-reviewed journal article in Applied Sciences (MDPI) examining demographic bias patterns in AI and cloud-based systems. Research involved statistical analysis using ANOVA and correlation methods to test hypotheses across multiple independent variables.""",
                'excerpt': 'Peer-reviewed research on algorithmic bias in cloud-based AI decision systems, published in Applied Sciences (MDPI).',
                'author': 'Ritik Gaire',
                'company': 'University of Michigan-Flint',
                'featured': True,
                'order': 1
            },
            {
                'title': 'Building Predictive ML Pipelines for Sports Analytics',
                'content': """Exploring how machine learning and computer vision techniques can extract valuable insights from soccer match footage. From player tracking with YOLOv8 to predicting match outcomes with ensemble classifiers and cross-validation.""",
                'excerpt': 'How ensemble classifiers and computer vision are revolutionizing soccer analytics through player tracking and match prediction.',
                'author': 'Ritik Gaire',
                'company': 'Personal Project',
                'featured': True,
                'order': 2
            },
            {
                'title': 'Multi-Agent AI Systems with Human-in-the-Loop',
                'content': """Learn how to create multi-agent workflows that can automate research tasks autonomously. This covers the architecture of LangGraph-based systems, human-in-the-loop validation strategies, and prompt optimization techniques that reduced token usage by 30%.""",
                'excerpt': 'Building autonomous multi-agent research systems with LangGraph, featuring human-in-the-loop validation and prompt optimization.',
                'author': 'Ritik Gaire',
                'company': 'Personal Project',
                'featured': True,
                'order': 3
            },
        ]
        for blog_data in blog_posts_data:
            BlogPost.objects.create(**blog_data)
        self.stdout.write(self.style.SUCCESS('✓ Blog posts updated'))

        self.stdout.write(self.style.SUCCESS('\n✅ Portfolio fully populated with complete resume data!'))
        self.stdout.write(self.style.WARNING('\n📸 Remember to:'))
        self.stdout.write(self.style.WARNING('   1. Add project images through the admin panel'))
        self.stdout.write(self.style.WARNING('   2. Upload your profile picture'))
        self.stdout.write(self.style.WARNING('   3. Customize any additional content as needed'))
