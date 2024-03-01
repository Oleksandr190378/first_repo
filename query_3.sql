SELECT s.name as subject_name, ROUND(AVG(g.grade), 2) AS average_grade_subject
from grades g 
join subjects s on g.subject_id = s.id 
where s.id = 3
GROUP BY s.id;