select a.animal_id, a.name
from animal_ins as a
join animal_outs as b
on a.animal_id = b.animal_id
order by b.datetime-a.datetime desc
limit 2