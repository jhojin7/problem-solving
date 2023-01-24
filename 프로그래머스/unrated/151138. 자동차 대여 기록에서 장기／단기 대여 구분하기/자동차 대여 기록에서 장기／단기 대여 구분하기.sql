select t.history_id, t.car_id, 
    date_format(t.start_date,"%Y-%m-%d") as start_date,
    date_format(t.end_date,"%Y-%m-%d") as end_date,
    -- t.end_date-t.start_date as diff,
    if (datediff(t.end_date,t.start_date)>=29,"장기 대여","단기 대여") as rent_type
from car_rental_company_rental_history as t
where date_format(t.start_date,"%Y-%m") = "2022-09"
order by t.history_id desc
