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
                'tagline': "Master's Student in ML/Data Science",
                'about_text': """Computer Science Master's Candidate with experience in predictive modeling and full-stack Python development. Proven track record in building autonomous agent workflows (LangGraph) and computer vision pipelines. Skilled in translating statistical insights into actionable business strategies.

Location: Flint, MI
Phone: (810) 210-4720
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
                'degree': 'Masters of Science in Computer Science and Information Systems',
                'start_date': date(2025, 1, 1),
                'end_date': None,
                'description': 'Master of Science (In Progress)',
                'order': 1
            },
            {
                'institution': 'Tribhuvan University',
                'degree': 'Bachelor of Science in Computer Science and Information Technology',
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
                'position': 'Graduate Student Research Assistant',
                'start_date': date(2025, 5, 1),
                'end_date': date(2025, 6, 30),
                'description': """• Performed statistical analysis (descriptive statistics, ANOVA, correlation) on survey data using Python to identify significant trends
• Developed publication-ready visualizations (Matplotlib, Seaborn) including bar charts and correlation matrices to communicate key findings
• Authored key sections of a research paper on algorithmic bias, translating complex statistical results into clear, actionable insights""",
                'order': 1
            },
            {
                'company': 'Roshani Digital Private Limited',
                'position': 'Part Time Web Developer',
                'start_date': date(2024, 3, 1),
                'end_date': date(2024, 10, 31),
                'description': """• Engineered and maintained a Django Rest Framework API to manage complex data relationships between music, artists, and genres
• Designed and implemented database schemas and managed data persistence, ensuring data integrity and accessibility
• Managed the full deployment lifecycle using Git, Vercel, and PythonAnywhere, ensuring high availability""",
                'order': 2
            },
            {
                'company': 'Spyders Lab',
                'position': 'Junior Backend Developer',
                'start_date': date(2023, 9, 1),
                'end_date': date(2024, 1, 31),
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
            {'category': 'data_analysis', 'name': 'Predictive Modeling', 'order': 1},
            {'category': 'data_analysis', 'name': 'Computer Vision', 'order': 2},
            {'category': 'data_analysis', 'name': 'Statistical Analysis', 'order': 3},
            {'category': 'data_analysis', 'name': 'Data Visualization', 'order': 4},
            {'category': 'data_analysis', 'name': 'Pandas', 'order': 5},
            {'category': 'data_analysis', 'name': 'NumPy', 'order': 6},
            {'category': 'data_analysis', 'name': 'Scikit-learn', 'order': 7},
            {'category': 'data_analysis', 'name': 'Matplotlib', 'order': 8},
            {'category': 'data_analysis', 'name': 'Seaborn', 'order': 9},
            
            # Programming Languages
            {'category': 'programming', 'name': 'Python', 'order': 1},
            {'category': 'programming', 'name': 'R', 'order': 2},
            
            # Frameworks & Tools
            {'category': 'tools', 'name': 'Django', 'order': 1},
            {'category': 'tools', 'name': 'Django Rest Framework', 'order': 2},
            {'category': 'tools', 'name': 'Flask', 'order': 3},
            {'category': 'tools', 'name': 'React.js', 'order': 4},
            {'category': 'tools', 'name': 'Git', 'order': 5},
            {'category': 'tools', 'name': 'GitHub', 'order': 6},
            {'category': 'tools', 'name': 'Docker', 'order': 7},
            {'category': 'tools', 'name': 'Postman', 'order': 8},
            {'category': 'tools', 'name': 'Linux', 'order': 9},
            
            # Databases
            {'category': 'database', 'name': 'MSSQL', 'order': 1},
            {'category': 'database', 'name': 'MySQL', 'order': 2},
            {'category': 'database', 'name': 'SQLite', 'order': 3},
            {'category': 'database', 'name': 'MongoDB', 'order': 4},
        ]
        for skill_data in skills_data:
            Skill.objects.create(**skill_data)
        self.stdout.write(self.style.SUCCESS('✓ Skills updated'))

        # Update Services
        Service.objects.all().delete()
        services_data = [
            {'title': 'Machine Learning', 'icon_class': 'icon-layers', 'description': 'Predictive modeling and computer vision solutions', 'order': 1},
            {'title': 'Statistical Analysis', 'icon_class': 'icon-graph', 'description': 'ANOVA, correlation analysis, and data-driven insights', 'order': 2},
            {'title': 'Web Development', 'icon_class': 'icon-laptop', 'description': 'Full-stack Python development with Django and React', 'order': 3},
            {'title': 'Data Visualization', 'icon_class': 'icon-pencil', 'description': 'Publication-ready charts and interactive dashboards', 'order': 4},
            {'title': 'API Development', 'icon_class': 'icon-briefcase', 'description': 'RESTful APIs with Django Rest Framework', 'order': 5},
            {'title': 'Cloud & DevOps', 'icon_class': 'icon-cloud', 'description': 'AWS, Docker, and deployment automation', 'order': 6},
        ]
        for service_data in services_data:
            Service.objects.create(**service_data)
        self.stdout.write(self.style.SUCCESS('✓ Services updated'))

        # Update Statistics
        Statistic.objects.all().delete()
        statistics_data = [
            {'label': 'ML Projects', 'value': 2, 'icon_class': 'icon-layers', 'order': 1},
            {'label': 'Years Experience', 'value': 2, 'icon_class': 'icon-briefcase', 'order': 2},
            {'label': 'Technologies', 'value': 25, 'icon_class': 'icon-tools', 'order': 3},
            {'label': 'Certifications', 'value': 3, 'icon_class': 'icon-trophy', 'order': 4},
        ]
        for stat_data in statistics_data:
            Statistic.objects.create(**stat_data)
        self.stdout.write(self.style.SUCCESS('✓ Statistics updated'))

        # Update Projects
        Project.objects.all().delete()
        projects_data = [
            {
                'title': 'Autonomous Multi-Agent Research System',
                'category': 'data_science',
                'description': """Created a multi-agent workflow using LangGraph where autonomous agents collaborate to plan, execute, and critique complex market research tasks. Implemented Human-in-the-loop approval state for user intervention before final report generation. Optimized agent communication prompts, reducing token usage by 30% while maintaining output quality.

Technologies: LangGraph, Tavily API, GPT-4o""",
                'github_url': 'https://github.com/ritik123gaire',
                'featured': True,
                'order': 1
            },
            {
                'title': 'Soccer Analytics & Video Analysis',
                'category': 'data_science',
                'description': """Engineered a data pipeline to collect, clean, and process historical soccer match data for predictive modeling. Developing and evaluating machine learning models (Logistic Regression, Random Forest) to predict match outcomes. Implementing computer vision models with Python to perform player tracking and key event detection from match footage.

Technologies: Python, Scikit-learn, OpenCV, Pandas""",
                'github_url': 'https://github.com/ritik123gaire',
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
                'title': 'Building Autonomous AI Agents with LangGraph',
                'content': """Learn how to create multi-agent workflows that can plan, execute, and critique complex research tasks autonomously. This post covers the architecture of LangGraph-based systems, human-in-the-loop validation strategies, and prompt optimization techniques that reduced token usage by 30%.""",
                'excerpt': 'A deep dive into building autonomous multi-agent research systems with LangGraph, featuring human-in-the-loop validation and prompt optimization.',
                'author': 'Ritik Gaire',
                'company': 'University of Michigan-Flint',
                'featured': True,
                'order': 1
            },
            {
                'title': 'Computer Vision in Sports Analytics',
                'content': """Exploring how machine learning and computer vision techniques can extract valuable insights from soccer match footage. From player tracking with OpenCV to predicting match outcomes with ensemble models, discover the data science behind sports analytics.""",
                'excerpt': 'How machine learning models and computer vision are revolutionizing soccer analytics through player tracking and match prediction.',
                'author': 'Ritik Gaire',
                'company': 'University of Michigan-Flint',
                'featured': True,
                'order': 2
            },
            {
                'title': 'Statistical Analysis for Algorithmic Bias Research',
                'content': """A practical guide to performing statistical analysis (ANOVA, correlation) on survey data to identify algorithmic bias patterns. Learn how to create publication-ready visualizations and translate statistical results into actionable research insights.""",
                'excerpt': 'Using Python and statistical methods to quantify and communicate algorithmic bias across demographic groups.',
                'author': 'Ritik Gaire',
                'company': 'University of Michigan-Flint',
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
