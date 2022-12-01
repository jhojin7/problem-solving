select a.animal_id, a.name,
ifnull((select "O" from animal_ins as b
where b.animal_id = a.animal_id
 	and (sex_upon_intake like "%Neutered%" 
	or sex_upon_intake like "%Spayed%")
),"X")
from animal_ins as a
