select factory_id, factory_name, address
from food_factory
where substr(address from 1 for 3)="강원도"
order by factory_id