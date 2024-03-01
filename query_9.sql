select distinct  w.fullname, s1.name as subject_name
from (select s.fullname, g.subject_id from students s join grades g on g.student_id =s.id where s.id = 20) as w
right join subjects s1 on w.subject_id = s1.id; 

--пошук по id студента s.id = 20
