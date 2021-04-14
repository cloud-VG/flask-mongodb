"""Database functionalities with MongoDB
"""

__author__ = 'Vishwajeet Ghatage'
__date__ = '14/04/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Built-in imports
from pymongo import MongoClient
from decouple import config
from typing import List, Dict
from models import Student
from flask import request

MONGO_URL = config('MONGO_URL')

client = MongoClient('mongodb+srv://admin:admin1234@cluster0.ww4ix.mongodb.net/student?retryWrites=true&w=majority')
db = client['student']
collection = db['students']


def get_students() -> List[Dict]:
    """Return List of All students."""
    students = []
    results = collection.find()
    for student in results:
        students.append(student)
    return students


def add_student(form: request.form) -> None:
    """Add student document to database.

    Parameters:
    -----------
        form: flask.request.form, ImmutableMultiDict

    Returns:
    -----------
        None
    """
    student = Student(form)
    if not collection.find_one({'prn': student.prn}):
        collection.insert_one(student.to_doc())


def update_student(prn: str, form: request.form) -> None:
    """Update student document.

    Parameters:
    -----------
        prn: PRN, str
        form: flask.request.form, ImmutableMultiDict

    Returns:
    -----------
        None
    """
    student = Student(form)
    collection.update_one({'prn': prn}, {'$set': student.to_doc()})


def delete_student(prn: str) -> None:
    """Delete student document.

    Parameters:
    -----------
        prn: PRN, str

    Returns:
    -----------
        None
    """
    collection.delete_one({'prn': prn})


def get_student(prn: str) -> Dict:
    """Return single document with matching PRN.

    Parameters:
    -----------
        prn: PRN, str

    Returns:
    -----------
        dict
    """
    return collection.find_one({'prn': prn})
