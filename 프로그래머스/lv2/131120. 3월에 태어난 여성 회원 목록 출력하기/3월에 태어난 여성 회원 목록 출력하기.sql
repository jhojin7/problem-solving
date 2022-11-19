select member_id, member_name, gender, date_format(date_of_birth,"%Y-%m-%d") as date_of_birth
from member_profile
where (gender="W"
    and month(date_of_birth)=3
	and member_profile.tlno is not NULL)
order by member_id asc