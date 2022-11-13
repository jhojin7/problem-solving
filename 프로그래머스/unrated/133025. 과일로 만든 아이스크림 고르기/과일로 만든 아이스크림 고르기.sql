select FLAVOR
from first_half 
where total_order>3000
and first_half.flavor=(select flavor from icecream_info 
            where ingredient_type="fruit_based"
           and flavor=first_half.flavor)