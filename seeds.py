import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Teacher, Student, Group, Subject, Grade


fake = Faker('uk-UA')


def insert_groups():
    for _ in range(3):
        group = Group(
            name=fake.word()
        )
        session.add(group)


def insert_teachers():
    for _ in range(4):
        teacher = Teacher(
            fullname=fake.name()
        )
        session.add(teacher)


def insert_students():
    groups = session.query(Group).all()
    for el in groups:
        for _ in range(10):
            student = Student(
                fullname=fake.name(),
                group_id=el.id
            )
            session.add(student)


def insert_subjects():
    teachers = session.query(Teacher).all()
    for el in teachers:
        for _ in range(2):
            subject = Subject(
                name=fake.word(),
                teacher_id=el.id
            )
            session.add(subject)


def combine_grades():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for student in students:
        for subject in subjects:
            for _ in range(2):
                rel = Grade(grade= random.randint(1, 15),date_of=fake.date_this_decade(), subjects_id=subject.id, student_id=student.id)
                session.add(rel)


def remove_teacher():
    teachers = session.query(Grade).all()
    #groups = session.query(Subject).all()
    for teacher in teachers:
        session.delete(teacher)
    session.commit()


if __name__ == '__main__':
    try:
        insert_groups()
        insert_teachers()
        #session.commit()
        insert_students()
        insert_subjects()
        session.commit()
        combine_grades()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
