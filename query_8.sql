select  ROUND(AVG(g.grade), 2) AS average_grade_subject
from (select  s.id  from subjects s join teachers t on s.teacher_id = t.id where t.id = 2 ) as s1
join grades g on g.subject_id = s1.id;
--t.id = 2  id вчителя