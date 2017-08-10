/*

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

SELECT prod_name
FROM Products
ORDER BY prod_name;

-- 首先按 prod_price 排序
SELECT prod_id, prod_price, prod_name
FROM Products
ORDER BY prod_price, prod_name;

-- 按位置选择字段排序
SELECT prod_id, prod_price, prod_name
FROM Products
ORDER BY 2, 3;

-- 降序 Z-A
SELECT prod_id
FROM Products
ORDER BY prod_id DESC;

-- 只作用于 DESC前面那个字段
SELECT prod_id, prod_name, prod_price
FROM Products
ORDER BY prod_price DESC, prod_id;

-- WHERE 支持多种操作符
-- 其中 BETWEEN 和 IS NULL 要记一下
SELECT prod_name, prod_price
FROM Products
WHERE prod_price = 3.49;

SELECT prod_name, prod_price
FROM Products
WHERE vend_id != 'DLL01';

-- 包括最大最小
SELECT prod_name, prod_price
FROM Products
WHERE prod_price BETWEEN 5.99 AND 9.49;

SELECT cust_name
FROM CUSTOMERS
WHERE cust_email IS NOT NULL;

SELECT prod_id, prod_price, prod_name
FROM Products
WHERE vend_id = 'DLL01' AND prod_price <= 4 AND prod_name = 'Bird bean bag toy';

SELECT prod_name
FROM Products
WHERE vend_id = 'DLL01' OR vend_id = 'BRS01';

-- AND 优先级高于 OR
SELECT prod_id, prod_price, prod_name
FROM Products
WHERE (vend_id = 'DLL01' OR vend_id = 'BRS01')
AND prod_price >= 10;

-- IN 比 OR 运行更快
SELECT prod_name, prod_price
FROM Products
WHERE vend_id IN ('DLL01', 'BRS01');


SELECT prod_name, prod_price
FROM Products
WHERE NOT vend_id IN ('DLL01', 'BRS01');

-- % 匹配任意字符
SELECT prod_name
FROM Products
WHERE prod_name LIKE '%bean%';

SELECT prod_name
FROM Products
WHERE prod_name LIKE '__ inch %';

-- 和 re 类似，[] 指里面任意一个
-- ^ 为否定
-- 但这个语法很多 DMBS 不支持
SELECT cust_contact
FROM Customers
WHERE cust_contact LIKE '[^JM]%';

-- concatenate
-- 在 MySQL 中是 Concat() 函数
SELECT vend_name || vend_country
FROM Vendors
ORDER BY vend_name;


SELECT RTRIM(vend_name) || '(' || LTRIM(vend_country) || ')'
FROM Vendors
ORDER BY vend_name;

SELECT vend_name || '(' || vend_country || ')'
    AS vend_title
FROM Vendors
ORDER BY vend_name;

*/

SELECT
    prod_id,
    quantity,
    item_price,
    quantity*item_price AS expanded_price
FROM
    OrderItems
WHERE
    order_num = 20008;
