select count(USER_ID) as USERS
from USER_INFO
where age>=20 and age<=29 and year(joined)=2021