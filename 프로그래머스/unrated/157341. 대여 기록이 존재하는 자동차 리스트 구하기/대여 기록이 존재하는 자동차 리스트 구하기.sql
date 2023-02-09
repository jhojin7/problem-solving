-- select a.car_id -- , date_format(start_date,"%m") as m
-- from car_rental_company_rental_history as a
-- -- inner join (select ccc.car_id from car_rental_company_car as ccc
-- --       where ccc.car_type like "세단") as b
-- -- on a.car_id=b.car_id
-- where date_format(start_date,"%m") =10
-- order by car_id desc


select distinct car.car_id 
from car_rental_company_car as car
right join (select hist.car_id from car_rental_company_rental_history as hist 
           where date_format(hist.start_date,"%m")=10) as h
on car.car_id=h.car_id
where car.car_type like "세단"
order by car.car_id desc