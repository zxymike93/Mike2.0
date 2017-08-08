SELECT prod_name
FROM Products;

SELECT prod_id, prod_name, prod_price
FROM Products;

SELECT *
FROM Products;

SELECT DISTINCT vend_id
FROM Products;

SELECT prod_name
FROM Products
LIMIT 5;

-- 从第6行开始的5行数据（因为第一行的索引是0）
SELECT prod_name
FROM Products
LIMIT 5 OFFSET 5;
