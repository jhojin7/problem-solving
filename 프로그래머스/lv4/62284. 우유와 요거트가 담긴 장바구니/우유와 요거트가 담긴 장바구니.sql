-- select cart_id, group_concat(name) as prods
-- from cart_products
-- group by cart_id
-- order by cart_id
select cart_id
from cart_products
where name="Yogurt" and cart_id in (select cart_id
       from cart_products
       where name="Milk"
       group by cart_id)
order by cart_id asc