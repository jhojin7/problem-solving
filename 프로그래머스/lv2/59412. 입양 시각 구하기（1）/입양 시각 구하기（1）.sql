select hour(datetime) as HOUR, count(animal_id)
from animal_outs
where hour(datetime) between 9 and 19
group by HOUR
order by HOUR