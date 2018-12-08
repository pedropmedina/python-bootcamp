import collections
import functools
import operator

students = [
    ('john', 29, 'male', ('bachelor', 'engineering')),
    ('jane', 33, 'female', ('master', 'biology')),
    ('johana', 22, 'female', ('associated', 'science')),
    ('jonas', 44, 'male', ('PHD', 'physics')),
]

sorted_list = sorted(students, key=operator.itemgetter(1))
# [('johana', 22, 'female'), ('john', 29, 'male'), ('jane', 33, 'female'), ('jonas', 44, 'male')]

factorial = functools.reduce(operator.mul, range(1, 5))  # 24

# attrgetter only works in objects
student_description = collections.namedtuple(
    'Student', ['name', 'age', 'gender', 'details']
)
career_info = collections.namedtuple('Details', ['path', 'major'])

students_namedtuples = [
    student_description(name, age, gender, career_info(path, major))
    for name, age, gender, (path, major) in students
]

attrs = operator.attrgetter('name', 'age')
print(attrs(students_namedtuples[0]))

for student in sorted(
    students_namedtuples, key=operator.attrgetter('details.major')
):
    print(student)
