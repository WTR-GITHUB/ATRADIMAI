import os
import django
from datetime import datetime, timedelta

# Nustatykite Django aplinką
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ATRADIMAI.settings')
django.setup()

from users.models import User

# Atskaitos data
reference_date = datetime(2024, 1, 1)

# Funkcija, kuri apskaičiuoja gimimo datą pagal amžių
def calculate_birth_date(age):
    return reference_date - timedelta(days=age * 365)

# Sukurkite vartotojų įrašus
users_data = [
    {"email": "admin1@example.com", "name": "Admin1", "surname": "Surname1", "birth_day": calculate_birth_date(30), "group": "administrator"},
    {"email": "admin2@example.com", "name": "Admin2", "surname": "Surname2", "birth_day": calculate_birth_date(35), "group": "administrator"},
    {"email": "admin3@example.com", "name": "Admin3", "surname": "Surname3", "birth_day": calculate_birth_date(40), "group": "administrator"},
    {"email": "mentor1@example.com", "name": "Mentor1", "surname": "Surname1", "birth_day": calculate_birth_date(25), "group": "mentor"},
    {"email": "mentor2@example.com", "name": "Mentor2", "surname": "Surname2", "birth_day": calculate_birth_date(28), "group": "mentor"},
    {"email": "mentor3@example.com", "name": "Mentor3", "surname": "Surname3", "birth_day": calculate_birth_date(32), "group": "mentor"},
    {"email": "curator1@example.com", "name": "Curator1", "surname": "Surname1", "birth_day": calculate_birth_date(29), "group": "curator"},
    {"email": "curator2@example.com", "name": "Curator2", "surname": "Surname2", "birth_day": calculate_birth_date(33), "group": "curator"},
    {"email": "curator3@example.com", "name": "Curator3", "surname": "Surname3", "birth_day": calculate_birth_date(27), "group": "curator"},
    {"email": "student1@example.com", "name": "Student1", "surname": "Surname1", "birth_day": calculate_birth_date(17), "group": "student"},
    {"email": "student2@example.com", "name": "Student2", "surname": "Surname2", "birth_day": calculate_birth_date(16), "group": "student"},
    {"email": "student3@example.com", "name": "Student3", "surname": "Surname3", "birth_day": calculate_birth_date(15), "group": "student"},
    {"email": "student4@example.com", "name": "Student4", "surname": "Surname4", "birth_day": calculate_birth_date(14), "group": "student"},
    {"email": "student5@example.com", "name": "Student5", "surname": "Surname5", "birth_day": calculate_birth_date(13), "group": "student"},
    {"email": "student6@example.com", "name": "Student6", "surname": "Surname6", "birth_day": calculate_birth_date(12), "group": "student"},
    {"email": "student7@example.com", "name": "Student7", "surname": "Surname7", "birth_day": calculate_birth_date(11), "group": "student"},
    {"email": "student8@example.com", "name": "Student8", "surname": "Surname8", "birth_day": calculate_birth_date(10), "group": "student"},
    {"email": "student9@example.com", "name": "Student9", "surname": "Surname9", "birth_day": calculate_birth_date(9), "group": "student"},
    {"email": "student10@example.com", "name": "Student10", "surname": "Surname10", "birth_day": calculate_birth_date(8), "group": "student"},
    {"email": "student11@example.com", "name": "Student11", "surname": "Surname11", "birth_day": calculate_birth_date(7), "group": "student"},
]

# Įterpkite vartotojų įrašus į duomenų bazę
for user_data in users_data:
    User.objects.create(**user_data)

print("Vartotojų įrašai sėkmingai sukurti.")