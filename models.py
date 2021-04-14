"""Models:
Helper classes for MongoDB
"""

__author__ = 'Vishwajeet Ghatage'
__date__ = '14/04/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'


# Built-in imports
from typing import Dict


class Student:
    """Document structure for students table.

    Parameters:
    ----------
        __prn: PRN, str
        __f_name: First Name, str
        __l_name: Last Name, str
        __m_name: Mother's Name, str
        __branch: Branch, str
        __year: Academic Year, str
    """
    def __init__(self, form):
        self.__prn = form['prn']
        self.__f_name = form['f_name']
        self.__l_name = form['l_name']
        self.__m_name = form['m_name']
        self.__branch = form['branch']
        self.__year = form['year']

    @property
    def prn(self) -> str:
        return self.__prn

    def to_doc(self) -> Dict:
        """Return Dictionary representation of Student.

        Used for MongoDB insertion operation.

        Parameters:
        ----------
            None

        Return:
        ----------
            dict
        """
        return {
            'prn': self.__prn,
            'f_name': self.__f_name,
            'l_name': self.__l_name,
            'm_name': self.__m_name,
            'branch': self.__branch,
            'year': self.__year
        }
