from django.core.management.base import BaseCommand
from profiles.models import Profile
from bs4 import BeautifulSoup
from pathlib import Path

class Command(BaseCommand):
    help = 'Parse structured HTML profiles (with class names) and save them into the database.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dir',
            type=str,
            default='sample_profiles',
            help='Directory containing HTML profile files'
        )

    def handle(self, *args, **options):
        directory = Path(options['dir'])
        if not directory.exists():
            self.stdout.write(self.style.ERROR(f"Directory {directory} not found"))
            return

        count = 0
        for html_file in directory.glob("*.html"):
            html = html_file.read_text(encoding="utf-8", errors="ignore")
            soup = BeautifulSoup(html, "html.parser")

            profile_div = soup.find("div", class_="profile")
            if not profile_div:
                self.stdout.write(self.style.WARNING(f"Skipping {html_file.name}: no .profile div"))
                continue

            # Extract data by class names
            name = profile_div.find(class_="name")
            age = profile_div.find(class_="age")
            city = profile_div.find(class_="city")
            profession = profile_div.find(class_="profession")
            education = profile_div.find(class_="education")
            religion = profile_div.find(class_="religion")

            # Clean text safely
            def clean_text(tag):
                return tag.get_text(strip=True) if tag else ""

            name = clean_text(name)
            city = clean_text(city)
            profession = clean_text(profession)
            education = clean_text(education)
            religion = clean_text(religion)

            # Handle age carefully (convert to integer if possible)
            try:
                age_value = int(age.get_text(strip=True)) if age else None
            except ValueError:
                age_value = None

            if not name:
                self.stdout.write(self.style.WARNING(f"Skipping {html_file.name}: missing name"))
                continue

            Profile.objects.create(
                name=name,
                age=age_value,
                city=city,
                profession=profession,
                education=education,
                religion=religion,
            )
            count += 1
            self.stdout.write(self.style.SUCCESS(f"✅ Saved: {name} ({city})"))

        self.stdout.write(self.style.SUCCESS(f"✅ Done. {count} profiles added."))
