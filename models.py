class Student:
    def __init__(self, form):
        self.__prn = form['prn']
        self.__f_name = form['f_name']
        self.__l_name = form['l_name']
        self.__m_name = form['m_name']
        self.__branch = form['branch']
        self.__year = form['year']

    @property
    def prn(self):
        return self.__prn

    def to_doc(self):
        return {
            'prn': self.__prn,
            'f_name': self.__f_name,
            'l_name': self.__l_name,
            'm_name': self.__m_name,
            'branch': self.__branch,
            'year': self.__year
        }
