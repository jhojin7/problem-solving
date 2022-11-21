select member_name, review_text, date_format(review_date,"%Y-%m-%d") as review_date
from rest_review as a
join member_profile as b on a.member_id = b.member_id
where a.member_id = (
    select member_id -- , count(review_id) as cnt
    from rest_review
    group by member_id
    order by count(review_id) desc
    limit 1
)
order by a.review_date asc, a.review_text asc