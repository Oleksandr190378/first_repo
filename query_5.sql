select  t.fullname , s."name"  as subject
from subjects s 
join teachers t on s.teacher_id  = t.id 
where t.id = 1;