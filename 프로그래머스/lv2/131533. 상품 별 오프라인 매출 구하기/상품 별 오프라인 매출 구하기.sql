select prod.product_code as PRODUCT_CODE, sum(sales_amount)*prod.price as SALES
from offline_sale as sale
left join product as prod on sale.product_id=prod.product_id 
group by sale.product_id
order by SALES desc, PRODUCT_CODE asc