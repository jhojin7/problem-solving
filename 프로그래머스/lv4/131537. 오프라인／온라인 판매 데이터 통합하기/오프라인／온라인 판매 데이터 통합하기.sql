select date_format(t.sales_date,"%Y-%m-%d") as sales_date,
	product_id, user_id, sales_amount
from (
    select sales_date,product_id,user_id,sales_amount 
    from online_sale
    where date_format(sales_date,"%Y-%m")="2022-03"
    union all
    select sales_date,product_id,NULL,sales_amount 
    from offline_sale
    where date_format(sales_date,"%Y-%m")="2022-03"
) t
order by t.sales_date asc, t.product_id asc, t.user_id asc