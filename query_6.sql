SELECT 
    s.id, 
    s.fullname, 
    g.name as group_name
from students s 
join "groups" g on s.group_id  = g.id 
where g.id = 2;