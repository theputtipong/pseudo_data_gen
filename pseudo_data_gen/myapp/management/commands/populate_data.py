# myapp/management/commands/populate_data.py

from django.core.management.base import BaseCommand
from faker import Faker
from myapp.models import MyModel


class Command(BaseCommand):
    help = "Populate database with fake data"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):  # Adjust as needed
            title = fake.sentence(nb_words=4)
            description = fake.paragraph()
            MyModel.objects.create(title=title, description=description)
        self.stdout.write(self.style.SUCCESS("Data successfully populated"))
