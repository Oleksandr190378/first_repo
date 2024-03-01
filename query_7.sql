select  s1.fullname, g.grade, s1.name as group_name, g.name as subject
from (select s.id, s.fullname, g1.name from students s join "groups" g1 on s.group_id  = g1.id  where g1.id = 2) as s1
join (select * from grades g2 join subjects s2 on g2.subject_id = s2.id where s2.id = 1) as g on g.student_id = s1.id;

--g1.id = 2 - id групи
--і2id = 1 - id редмету