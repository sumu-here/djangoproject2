from faker import Faker
fake = Faker()
import random
from .models import * 
from django.db.models import Sum

def create_subject_marks(n):
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subjects = Subject.objects.all()
            for sub in subjects:
                SubjectMarks.objects.create(
                    student = student,
                    subject = sub,
                    marks = random.randint(0,100),
                )
    except Exception as e:
        print(e)


def seed_db(n=10) -> None:
    try:
        for _ in range(n):
            department_obj = Department.objects.all()
            random_index = random.randint(0,len(department_obj)-1)
            student_id = f'STD-0{random.randint(100,999)}'
            department = department_obj[random_index]
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id= student_id)

            student_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address,
            )
    except Exception as e:
        print(e)


def generate_report_card():
    print("calleddddd")
    ranks = Student.objects.annotate(marks= Sum('studentmarks__marks')).order_by('-marks','-student_age')
    i=1
    for rank in ranks:
        ReportCard.objects.create(
            student = rank,
            student_rank = i
        )
        i=i+1
