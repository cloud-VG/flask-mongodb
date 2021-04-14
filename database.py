from pymongo import MongoClient
from decouple import config
from typing import List, Dict
from models import Student

MONGO_URL = config('MONGO_URL')

client = MongoClient(MONGO_URL)
db = client['student']
collection = db['students']


def get_students() -> List[Dict]:
    students = []
    results = collection.find()
    for student in results:
        students.append(student)
    return students


def add_student(form) -> None:
    student = Student(form)
    if not collection.find_one({'prn': student.prn}):
        collection.insert_one(student.to_doc())


def update_student(prn, form) -> None:
    student = Student(form)
    collection.update_one({'prn': prn}, {'$set': student.to_doc()})


def delete_student(prn) -> None:
    collection.delete_one({'prn': prn})


def find_student(prn) -> Dict:
    return collection.find_one({'prn': prn})
