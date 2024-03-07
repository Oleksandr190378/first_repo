from sqlalchemy import func, desc, select, and_
from conf.models import Teacher, Student, Group, Subject, Grade
from conf.db import session
from sqlalchemy.sql import exists

def select_1():
    """
    SELECT
    s.id,
    s.fullname,
    ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5;
    """
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade'))\
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    return result


def select_2():
    """
    SELECT
    s.id,
    s.fullname,
    ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    where g.subject_id = 3
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 1
    """
    result = (session.query(Student.id, Student.fullname,  func.round(func.avg(Grade.grade), 2).label('average_grade'))\
        .select_from(Grade).join(Student).filter(Grade.subjects_id == 50).group_by(Student.id).
              order_by(desc('average_grade')).limit(1).all())
    return result


def select_3():
    """
    SELECT s.name as subject_name, ROUND(AVG(g.grade), 2) AS average_grade_subject
    from grades g
    join subjects s on g.subject_id = s.id
    where s.id = 3
    GROUP BY s.id;
    """
    # id предмету = 5	
    result = session.query(Subject.name, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Subject).filter(Grade.subjects_id == 5).group_by(Subject.id).limit(1).all()
    return result


def select_4():
    """
    SELECT ROUND(AVG(g.grade), 2) AS average_grade_general
    from grades g;
    """
    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade'))\
            .select_from(Grade).all()
    return result


def select_5():
    """
     select  t.fullname , s."name"  as subject
    from subjects s
    join teachers t on s.teacher_id  = t.id
    where t.id = 1;
    """
    # id вчителя = 1	
    result = session.query(Teacher.fullname, Subject.name).select_from(Subject)\
        .join(Teacher).filter(and_(Subject.teacher_id == Teacher.id, Teacher.id == 1)).all()
    return result


def select_6():
    """
    SELECT
    s.id,
    s.fullname,
    g.name as group_name
    from students s
    join "groups" g on s.group_id  = g.id
    where g.id = 2;
    """
    # id групи = 3	
    result = session.query(Student.id, Student.fullname, Group.name)\
        .select_from(Student).join(Group)\
        .filter(and_(Student.group_id == Group.id, Group.id == 3)).all()
    return result


def select_7():
    """
    select  s1.fullname, g.grade, s1.name as group_name, g.name as subject
	from (select s.id, s.fullname, g1.name from students s join "groups" g1 on s.group_id  = g1.id  where g1.id = 8) as s1
	join (select * from grades g2 join subjects s2 on g2.subject_id = s2.id where s2.id = 50) as g on g.student_id = s1.id;
    """
    # id групи =  2 id предмету = 5	
    stmt = exists().where(and_(Student.group_id == Group.id, Group.id == 2))
    result = session.query(Student.fullname, Grade.grade, Subject.name).select_from(Grade)\
              .join(Subject).filter(and_(Grade.subjects_id == Subject.id, Subject.id == 5, stmt)).all()
    return result


def select_8():
    """
    select  ROUND(AVG(g.grade), 2) AS average_grade_subject
    from (select  s.id  from subjects s join teachers t on s.teacher_id = t.id where t.id = 2 ) as s1
    join grades g on g.subject_id = s1.id;
    """
    # id вчителя = 2	
    stmt = exists().where(and_(Subject.teacher_id == Teacher.id, Teacher.id == 2))
    result =session.query(func.round(func.avg(Grade.grade), 2).label('average_grade'))\
           .select_from(Subject).join(Grade)\
           .filter(and_(Grade.subjects_id == Subject.id, stmt)).all()
    return result

def select_9():
    """
    select distinct  w.fullname, s1.name as subject_name
    from (select s.fullname, g.subject_id from students s join grades g on g.student_id =s.id where s.id = 20) as w
    right join subjects s1 on w.subject_id = s1.id;
    """
    # id студента = 11	
    stmt = exists().where(and_(Grade.student_id == Student.id, Student.id == 111))
    result = session.query(Subject.name.distinct()).select_from(Grade)\
        .join(Subject).filter(and_(Grade.subjects_id == Subject.id, stmt)).all()
    return result


def select_10():
    """
    select distinct s2.fullname as student_name, g2.fullname as teacher_name, g2.sub as subject_name
    from (select g.student_id, s1.fullname, s1.sub from (select t.fullname, s.id, s.name as sub from teachers t join subjects s on s.teacher_id = t.id where t.id = 12) as s1
    join grades g on s1.id = g.subject_id) as g2
    join students s2 on g2.student_id = s2.id where s2.id = 100;
    :return:
    """
    # id студента = 10 id вчителя = 3	
    stmt = exists().where(and_(Subject.teacher_id == Teacher.id, Teacher.id == 3))
    result = session.query(Subject.name.distinct()).select_from(Grade)\
        .join(Student).filter(and_(Grade.student_id == Student.id, Student.id == 10, stmt)).all()
    return result


def select_11():
    # id вчителя = 3	
    stmt = exists().where(and_(Subject.teacher_id == Teacher.id, Teacher.id == 3))
    result = session.query(func.round(func.avg(Grade.grade), 2))\
        .select_from(Grade).join(Student)\
        .filter(and_(Grade.student_id == Student.id, Student.id == 92, Grade.subjects_id == Subject.id, stmt )).all()
    return result



def select_12():
    """
    select s.id, s.fullname, g.grade, g.date_of
    from grades g
    join students s on g.student_id =s.id
    where g.subject_id =4 and s.group_id = 3 and g.date_of = (
	select max(g2.date_of)
	from grades g2
	join students s2 on s2.id = g2.student_id
	where g2.subject_id =46 and s2.group_id = 9
	);
    """
    
	subquery = (select(func.max(Grade.date_of)).join(Student)\
                .filter(and_(Grade.subjects_id == 4, Student.group_id == 3))).scalar_subquery()
    result = session.query(Student.id, Student.fullname, Grade.grade, Grade.date_of)\
            .select_from(Grade).join(Student)\
            .filter(and_(Grade.subjects_id == 46, Student.group_id == 9, Grade.date_of == subquery)).all()
    return result




if __name__ == "__main__":
    #print(select_1())
    #print(select_2())
    #print(select_3())
    #print(select_4())
    #print(select_5())
    #print(select_6())
    #print(select_7())
    #print(select_8())
    #print(select_9())
    #print(select_10())
    print(select_11())
    #print(select_12())

