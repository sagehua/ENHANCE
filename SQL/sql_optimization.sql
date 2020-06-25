1. 第一次错误

SELECT MAX(`auth_user`.`username`) AS `username__max`
FROM `auth_user`
WHERE `auth_user`.`username` LIKE BINARY '98%'
-- BINARY 导致索引扫描（index）（此语句为django ORM解释而来，不知为何有BINARY）（BINARY表示查询时区分字段值的大小写）

SELECT MAX(`auth_user`.`username`) AS `username__max`
FROM `auth_user`
WHERE `auth_user`.`username` LIKE '98%'
-- LIKE 后的表达式右边模糊，则是索引范围扫描（range）

SELECT MAX(`auth_user`.`username`) AS `username__max`
FROM `auth_user`
WHERE LENGTH(`auth_user`.`username`) = 11 AND`auth_user`.`username` BETWEEN  '90000000000' AND '99999999999'
-- 索引范围扫描（range）


2. 第二次错误

UPDATE `jct4_orders` SET `order_channel` = 'OTT'
WHERE `jct4_orders`.`user_id` IN
    (SELECT U0.`user_id` FROM `jct5_unified_binding_user_relation` U0 WHERE U0.`identity_type` = 'wxmp_ectv')
-- 索引扫描（index）
-- jct4_orders 中查询涉及到的记录太多

SELECT b.order_channel FROM jct5_unified_binding_user_relation a
INNER JOIN jct4_orders b ON a.user_id = b.user_id
WHERE a.identity_type = 'wxmp_ectv'
-- 改为连接查询。扫描方式优化，涉及的记录数减少