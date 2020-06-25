CREATE TABLE `jct5_ott_pay_contract` (
    `id`                int(11) NOT NULL AUTO_INCREMENT,
    `contract_id`       varchar(32) NOT NULL COMMENT '签约id',
    `contract_code`     varchar(64) DEFAULT NULL COMMENT '签约码',
    `salt`              varchar(32) DEFAULT NULL COMMENT '签约盐值',
    `is_active`         tinyint(1) DEFAULT 1 COMMENT '签约是否有效',
    `platform`          varchar(32) NOT NULL COMMENT '签约的平台（支付宝、微信……）',
    `order_oid`         varchar(32) DEFAULT NULL COMMENT '订单的oid',
    `order_price`       int(11) DEFAULT NULL COMMENT '订单的价格',
    `order_user_id`     int(11) DEFAULT NULL COMMENT '订单的用户id',
    `next_execute_time` datetime DEFAULT NULL COMMENT '下一次扣款时间',
    `sign_time`         datetime DEFAULT NULL COMMENT '签约时间',
    `signature`         varchar(64) DEFAULT NULL COMMENT '第一次支付（手动支付）的签名',
    `cancel_time`       datetime DEFAULT NULL COMMENT '解约时间',
    PRIMARY KEY (`id`),
    UNIQUE `IDX_CONTRACT_ID_PLATFORM` (`contract_id`, platform) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `jct5_ott_pay_contract_log` (
    `id`                int(11) NOT NULL AUTO_INCREMENT,
    `contract_id`       varchar(32) NOT NULL COMMENT '签约id',
    `contract_code`     varchar(64) DEFAULT NULL COMMENT '签约码',
    `app_id`            varchar(64) DEFAULT NULL COMMENT '接入方的应用id',
    `salt`              varchar(32) DEFAULT NULL COMMENT '签约盐值',
    `order_oid`         varchar(32) DEFAULT NULL COMMENT '（纳米盒）订单的oid',
    `sign`              varchar(128) DEFAULT NULL COMMENT '签名',
    `status`            tinyint(1) DEFAULT NULL COMMENT '签约的状态（1为签约成功，0为解约。解约后不再发送扣款请求）',
    `create_time`       datetime DEFAULT NULL COMMENT '创建时间',
    PRIMARY KEY (`id`),
    KEY `IDX_CONTRACT_ID` (`contract_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;