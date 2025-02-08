import random
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from faker import Faker  
from users.models import CustomUser
from students.models import Student
from teachers.models import Teacher
from groups.models import Group
from subjects.models import Subject
from departments.models import Department

fake = Faker()

class Command(BaseCommand):
    help = "Fills the database with dummy data"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Starting database seeding..."))

        # Create Departments
        departments = []
        for _ in range(3):
            department = Department.objects.create(
                name=fake.word().capitalize() + " Department",
                head=None,  # We'll assign later
                description=fake.text(),
                location=fake.address(),
                contact_email=fake.email(),
                contact_phone=fake.phone_number()
            )
            departments.append(department)
        
        # Create Admin Users
        admin = CustomUser.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="admin123",
            role="admin"
        )
        
        # Create Teachers
        teachers = []
        for _ in range(5):
            user = CustomUser.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="password",
                role="teacher"
            )
            teacher = Teacher.objects.create(
                user=user,
                department=random.choice(departments),
                qualification=fake.job(),
                join_date=fake.date_between(start_date="-5y", end_date="today"),
                employment_type=random.choice(['full_time', 'part_time', 'contract']),
                phone_number=fake.phone_number(),
                address=fake.address()
            )
            teachers.append(teacher)
        
        # Assign Department Heads
        for department in departments:
            department.head = random.choice(teachers).user
            department.save()
        
        # Create Subjects
        subjects = []
        for _ in range(10):
            subject = Subject.objects.create(
                name=fake.word().capitalize() + " Studies",
                department=random.choice(departments),
                description=fake.text(),
                credit_hours=random.randint(1, 5),
                grade_level=random.randint(9, 12)
            )
            subjects.append(subject)
        
        # Create Groups
        groups = []
        for _ in range(4):
            group = Group.objects.create(
                name=fake.word().capitalize() + " Class",
                grade_level=random.randint(9, 12),
                class_teacher=random.choice(teachers),
                schedule=random.choice(['morning', 'afternoon', 'evening']),
                academic_year=str(fake.year()),
                max_students=random.randint(15, 30)
            )
            group.subjects.set(random.sample(subjects, k=random.randint(2, 5)))
            groups.append(group)
        
        # Create Students
        for _ in range(20):
            user = CustomUser.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="password",
                role="student"
            )
            Student.objects.create(
                user=user,
                date_of_birth=fake.date_of_birth(minimum_age=14, maximum_age=18),
                gender=random.choice(['male', 'female', 'other']),
                grade=random.randint(9, 12),
                group=random.choice(groups),
                phone_number=fake.phone_number(),
                address=fake.address(),
                parent_name=fake.name(),
                parent_phone=fake.phone_number(),
                parent_email=fake.email()
            )
        
        self.stdout.write(self.style.SUCCESS("Database successfully seeded!"))
