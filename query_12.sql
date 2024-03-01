select  g2.student_name , g2.grade , s."name" as subject_name, g2.grade_date
from (select g.student_name , g.grade, g.subject_id, g.grade_date 
from (select * from grades g1 join (select s3.fullname as student_name, s3.id
from students s3 join "groups" gr on s3.group_id = gr.id where gr.id = 3) s2 on g1.student_id = s2.id) as g 
group by g.student_name , g.grade, g.subject_id, g.grade_date   
having g.grade_date= (select max(g3.grade_date) from grades g3)) as g2
join subjects s on g2.subject_id = s.id where s.id = 1;

--пошук по id предмету s.id=1 та id групи gr.id = 3
