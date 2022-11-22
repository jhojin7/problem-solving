select a.rest_id, b.rest_name, b.food_type,
	b.favorites, b.address,
    round(avg(a.review_score),2) as score
from rest_review as a
join (select rest_id, rest_name, address, food_type,
      	favorites
      from rest_info 
      where substr(address,1,2)="서울"
     ) as b
on a.rest_id=b.rest_id
group by a.rest_id
order by score desc, b.favorites desc