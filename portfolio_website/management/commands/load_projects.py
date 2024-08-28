import csv
from django.core.management.base import BaseCommand
from portfolio_website.models import Project


class Command(BaseCommand):
    help = 'Load projects from data.csv'

    def handle(self, *args, **kwargs):
        with open('data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                Project.objects.create(
                    title=row['title'],
                    description=row['description'],
                    url=row['url'],
                    image=row['image']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded projects'))
