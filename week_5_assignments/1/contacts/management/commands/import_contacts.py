import csv
from django.core.management.base import BaseCommand
from contacts.models import Contact
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Import contacts from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str,
                            help='The CSV file to import.')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        user = User.objects.get(username='Arman94v')

        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Contact.objects.get_or_create(
                    first_name=row['FirstName'],
                    last_name=row['LastName'],
                    phone_number=row['Phone'],
                    address=row['Address'],
                    user=user
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported contacts'))
