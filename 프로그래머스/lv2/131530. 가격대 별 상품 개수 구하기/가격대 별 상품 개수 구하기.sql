-- 코드를 입력하세요
SELECT
LEFT(PRICE/10000,1)*10000 as PRICE_GROUP,
count(PRODUCT_ID) as PRODUCTS
from PRODUCT
group by LEFT(PRICE/10000,1)
ORDER BY PRICE ASC