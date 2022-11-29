select year(sales_date) as y,
     month(sales_date) as m,
     t.gender, count(distinct t.user_id)
from (
    select a.sales_date, a.user_id, b.gender
    from online_sale as a
    left join (select user_id,gender from user_info) as b
    on a.user_id = b.user_id
    where gender is not NULL
) t
group by year(t.sales_date), month(t.sales_date), t.gender
order by y,m,t.gender