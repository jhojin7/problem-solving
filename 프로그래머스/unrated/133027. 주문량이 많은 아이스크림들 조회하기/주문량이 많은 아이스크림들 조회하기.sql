-- select flavor, sum(total_order) as s from july group by flavor order by s
select a.flavor -- , a.total_order+b.s as num
from first_half as a 
join (select flavor, sum(total_order) as s from july group by flavor ) as b
on a.flavor = b.flavor
order by  a.total_order+b.s desc
limit 3