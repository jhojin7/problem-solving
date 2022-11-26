select b.product_code, sum(b.price*a.sales_amount)
from offline_sale as a
join product as b
on a.product_id = b.product_id
group by a.product_id
order by sum(b.price*a.sales_amount) desc, b.product_code asc