SELECT cls.id, cls.course_id, cls.im_group_id, cls.name, cls.status, vcls.product_id,
    r.milesson_id, cls.student_count, vcls.class_memo, vcls.brief_info, vcls.special_info, MIN(schel.start_at) as whole_class_start_at,
    SUM(IF(schel.start_at > DATE_ADD(NOW(), INTERVAL + 10 MINUTE), 1, 0)) AS start_at_count, COUNT(1) AS all_count
FROM jct5_virtual_school_class cls
    JOIN jct5_virtual_school_class_schedule schel ON schel.vs_class_id = cls.id
    JOIN jct5_product_vclass vcls ON cls.course_id = vcls.id
    JOIN jct5_milesson_product_union r ON r.product_id = vcls.product_id
WHERE cls.status IN ('开班成功', '组班中')
    AND cls.tag = 'ott'
    -- AND cls.create_time > (NOW() - INTERVAL 10 DAY)
GROUP BY cls.id
HAVING start_at_count > 0


-- 内连接在左连接之后也可以
SELECT
  c.product_name, a.*, b.*
FROM jct5_milesson_product_union a
  LEFT JOIN jct5_product_vclass b
    ON a.product_id = b.product_id,
  jct4_products c
WHERE a.tag = 'ott'
  AND a.product_id = c.id
  AND b.id IS NOT NULL
  AND c.product_name NOT LIKE '%TV%';