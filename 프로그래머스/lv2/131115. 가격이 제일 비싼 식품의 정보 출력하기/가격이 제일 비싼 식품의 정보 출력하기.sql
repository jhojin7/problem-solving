select PRODUCT_ID,PRODUCT_NAME,PRODUCT_CD,CATEGORY,PRICE
from food_product
where PRICE=(select max(price) from food_product)