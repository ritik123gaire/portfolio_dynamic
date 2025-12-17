from django.core.management.base import BaseCommand
from portfolio.models import (
    Profile, Education, Experience, Skill, Service,
    Project, BlogPost, Statistic
)


class Command(BaseCommand):
    help = 'Populate database with initial portfolio data'

    def handle(self, *args, **options):
        self.stdout.write('Starting data population...')

        # Create Profile
        profile, created = Profile.objects.get_or_create(
            id=1,
            defaults={
                'name': 'Ritik Gaire',
                'tagline': 'I LOVE TO CODE',
                'about_text': 'As a Graduate Computer Science student, I am passionate about data analysis and web development, and I am currently working on a project using Python Libraries. Along with data analysis and web development, I am also interested in Artificial Intelligence and Deep Learning.',
                'linkedin_url': 'https://www.linkedin.com/in/ritik-gaire/',
                'github_url': 'https://github.com/ritik123gaire',
            }
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Profile {"created" if created else "already exists"}'))

        # Create Education
        education_data = [
            {'institution': 'University of Michigan-Flint', 'degree': 'Masters of Computer Science and Information System', 'order': 1},
            {'institution': 'NCCS College, TU', 'degree': 'Bachelors of Computer Science and Information Technology', 'order': 2},
            {'institution': 'NSS, NIST', 'degree': '+2 Science', 'order': 3},
            {'institution': 'Sigma Higher Secondary School', 'degree': 'SLC', 'order': 4},
        ]
        for edu_data in education_data:
            edu, created = Education.objects.get_or_create(**edu_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Added education: {edu.institution}'))

        # Create Experience
        experience_data = [
            {'company': 'University of Michigan-Flint', 'position': 'Graduate Research Assistant', 'order': 1},
            {'company': 'Roshani Digital Pvt. Ltd', 'position': 'Web Developer', 'order': 2},
            {'company': 'Spyders Lab', 'position': 'Junior Developer', 'order': 3},
            {'company': 'Spyders Lab', 'position': 'Intern', 'order': 4},
        ]
        for exp_data in experience_data:
            exp, created = Experience.objects.get_or_create(**exp_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Added experience: {exp.position} at {exp.company}'))

        # Create Skills
        skills_data = [
            {'category': 'programming', 'name': 'Python', 'order': 1},
            {'category': 'programming', 'name': 'JavaScript', 'order': 2},
            {'category': 'programming', 'name': 'Java', 'order': 3},
            {'category': 'database', 'name': 'MSSQL', 'order': 1},
            {'category': 'database', 'name': 'SQLite', 'order': 2},
            {'category': 'database', 'name': 'MySQL', 'order': 3},
            {'category': 'data_analysis', 'name': 'Pandas', 'order': 1},
            {'category': 'data_analysis', 'name': 'Numpy', 'order': 2},
            {'category': 'data_analysis', 'name': 'Matplotlib', 'order': 3},
            {'category': 'web_framework', 'name': 'Django', 'order': 1},
            {'category': 'web_framework', 'name': 'Flask', 'order': 2},
            {'category': 'web_framework', 'name': 'React', 'order': 3},
            {'category': 'tools', 'name': 'GitHub', 'order': 1},
            {'category': 'tools', 'name': 'Linux', 'order': 2},
            {'category': 'tools', 'name': 'Docker', 'order': 3},
            {'category': 'tools', 'name': 'Postman', 'order': 4},
            {'category': 'tools', 'name': 'R Studio', 'order': 5},
        ]
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(**skill_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Added skill: {skill.name}'))

        # Create Services
        services_data = [
            {'title': 'Web Development', 'icon_class': 'icon-laptop', 'order': 1},
            {'title': 'Data Analysis', 'icon_class': 'icon-layers', 'order': 2},
            {'title': 'Graphic Design', 'icon_class': 'icon-pencil', 'order': 3},
            {'title': 'Database', 'icon_class': 'icon-briefcase', 'order': 4},
            {'title': 'Cloud', 'icon_class': 'icon-cloud', 'order': 5},
            {'title': 'Project Management', 'icon_class': 'icon-clipboard', 'order': 6},
        ]
        for service_data in services_data:
            service, created = Service.objects.get_or_create(**service_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Added service: {service.title}'))

        # Create Statistics
        statistics_data = [
            {'label': 'Awards Won', 'value': 3, 'icon_class': 'icon-trophy', 'order': 1},
            {'label': 'Projects Done', 'value': 11, 'icon_class': 'icon-layers', 'order': 2},
        ]
        for stat_data in statistics_data:
            stat, created = Statistic.objects.get_or_create(**stat_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Added statistic: {stat.label}'))

        # Create Blog Posts
        blog_posts_data = [
            {
                'title': 'Google Bard',
                'content': 'Phasellus luctus commodo ullamcorper a posuere rhoncus commodo elit. Aenean congue, risus utaliquam dapibus. Thanks!.',
                'excerpt': 'Phasellus luctus commodo ullamcorper a posuere rhoncus commodo elit. Aenean congue, risus utaliquam dapibus. Thanks!.',
                'author': 'John Doe',
                'company': 'Google Inc.',
                'order': 1
            },
            {
                'title': 'Flutter vs React Native',
                'content': 'Flutter uses Dart, offers customizable widgets, and provides fast UI rendering with a single codebase for native-like performance. React Native uses JavaScript, offers reusable components, and has a large community with strong cross-platform support and hot reload features.',
                'excerpt': 'Flutter uses Dart, offers customizable widgets, and provides fast UI rendering with a single codebase for native-like performance. React Native uses JavaScript, offers reusable components, and has a large community with strong cross-platform support and hot reload features.',
                'author': 'John Doe',
                'company': 'Google Inc.',
                'order': 2
            },
            {
                'title': 'MOJO vs Python',
                'content': 'Phasellus luctus commodo ullamcorper a posuere rhoncus commodo elit. Aenean congue, risus utaliquam dapibus. Thanks!.',
                'excerpt': 'Phasellus luctus commodo ullamcorper a posuere rhoncus commodo elit. Aenean congue, risus utaliquam dapibus. Thanks!.',
                'author': 'John Doe',
                'company': 'Google Inc.',
                'order': 3
            },
        ]
        for blog_data in blog_posts_data:
            blog, created = BlogPost.objects.get_or_create(
                title=blog_data['title'],
                defaults=blog_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Added blog post: {blog.title}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Data population completed successfully!'))
        self.stdout.write(self.style.WARNING('\n📝 Note: Project images need to be added through the admin panel.'))
        self.stdout.write(self.style.WARNING('    Your existing portfolio images are in the static/img/portfolio/ folder.'))
