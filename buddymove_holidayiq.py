-- Number of characters
Select 
	COUNT (DISTINCT character_id)
From charactercreator_character

-- how many items total
SELECT 
	COUNT(DISTINCT item_id)
from armory_item

-- how many items are weapons
SELECT 
	COUNT(DISTINCT item_ptr_id)
from armory_weapon

-- how many weapons does each character have (first 20 rows)
SELECT 
	cci.character_id,
	count(aw.item_ptr_id) as weapon_count
from charactercreator_character_inventory as cci 
left join armory_weapon as aw on cci.item_id == aw.item_ptr_id
group by cci.character_id
limit 20

-- On average how many weapons does each character have 
Select AVG(weapon_count) as average_weapon
From (SELECT 
	cci.character_id,
	count(aw.item_ptr_id) as weapon_count
from charactercreator_character_inventory as cci 
left join armory_weapon as aw on cci.item_id == aw.item_ptr_id
group by cci.character_id
)

-- how many items does each character have (first 20 rows)
SELECT 
	cci.character_id,
	count(cci.item_id) as item_count
from charactercreator_character_inventory as cci 
group by cci.character_id
LIMIT 20

-- On average how many items does each character have 
Select AVG(item_count) as average_item
From(SELECT 
		cci.character_id,
		count(cci.item_id) as item_count
	from charactercreator_character_inventory as cci 
	group by cci.character_id
)