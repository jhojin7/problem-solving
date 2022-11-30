select ins.name as NAME, ins.datetime as DATETIME
from animal_ins as ins 
left outer join animal_outs as outs
on ins.animal_id = outs.animal_id
where outs.animal_id is null
#order by (outs.datetime-ins.datetime) desc
order by DATETIME
limit 3