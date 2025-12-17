from django.core.management.base import BaseCommand
from portfolio.models import Project


class Command(BaseCommand):
    help = 'Add project images'

    def handle(self, *args, **options):
        self.stdout.write('Adding project images...')

        # Update Soccer Analytics project
        soccer = Project.objects.filter(title='Soccer Match Analytics System').first()
        if soccer:
            soccer.image = 'projects/soccer_analytics.jpg'
            soccer.save()
            self.stdout.write(self.style.SUCCESS('✓ Soccer Analytics image added'))

        # Update Multi-Agent project
        multi_agent = Project.objects.filter(title='Multi-Agent Research System').first()
        if multi_agent:
            multi_agent.image = 'projects/multi_agent.jpg'
            multi_agent.save()
            self.stdout.write(self.style.SUCCESS('✓ Multi-Agent System image added'))

        self.stdout.write(self.style.SUCCESS('\n✅ Project images added successfully!'))
