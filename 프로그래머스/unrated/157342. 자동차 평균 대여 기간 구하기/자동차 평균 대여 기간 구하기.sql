-- select hist.car_id, 
--     hist.history_id, 
--     sum(hist.end_date-hist.start_date)/count(hist.history_id) as diffavg
-- from car_rental_company_rental_history as hist
-- group by hist.car_id
-- order by hist.car_id desc



select
    car_id, round(avg(datediff(hist.end_date,hist.start_date)+1),1) as average_duration
from car_rental_company_rental_history as hist
group by hist.car_id
having average_duration >= 7
order by 
	average_duration desc,
    hist.car_id desc