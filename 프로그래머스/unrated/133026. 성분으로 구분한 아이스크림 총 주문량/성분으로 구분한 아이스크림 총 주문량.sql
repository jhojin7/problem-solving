select ingredient_type, sum(total_order)
from first_half as a
join icecream_info as b
on a.flavor=b.flavor
group by b.ingredient_type