DROP TABLE IF EXISTS `jct6_shuhua_activity_works`;
CREATE TABLE `jct6_shuhua_activity_works` (
    `id`                int(11) NOT NULL AUTO_INCREMENT,
    `user_id`           int(11) NOT NULL COMMENT '作者ID',
    `user_name`         varchar(16) DEFAULT NULL COMMENT '联系人姓名',
    `phone`             varchar(16) DEFAULT NULL COMMENT '联系人手机号',
    `channel`           varchar(32) DEFAULT NULL COMMENT '渠道',
    `baby_name`         varchar(16) DEFAULT NULL COMMENT '宝贝名字',
    `baby_age`          int(11) DEFAULT NULL COMMENT '宝贝年龄',
    `group`             varchar(8) DEFAULT NULL COMMENT '作品所属分组(幼儿组、小学组、中学组)',
    `work_url`          varchar(256) DEFAULT NULL COMMENT '作品地址',
    `introduce`         varchar(256) DEFAULT NULL COMMENT '作品简介',
    `status`            varchar(8) DEFAULT NULL COMMENT '作品状态(待审核、已通过、未通过)',
    `reject_reason`     varchar(64) DEFAULT NULL COMMENT '未通过原因',
    `auditor_id`        int(11) DEFAULT NULL COMMENT '审核人ID',
    `audit_time`        datetime DEFAULT NULL COMMENT '审核时间',
    `vote_num`          int(11) DEFAULT 0 COMMENT '作品获得的投票数',
    `create_time`       int(11) DEFAULT NULL COMMENT '提交作品时间',
    PRIMARY KEY (`id`),
    KEY `IDX_USERID` (`user_id`) USING BTREE,
    KEY `IDX_STATUS_GROUP_VOTE_CREATE` (`status`, `group`, `vote_num`, `create_time`) USING BTREE,
    KEY `IDX_STATUS_CREATE` (`status`, `create_time`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `jct6_shuhua_activity_vote_log`;
CREATE TABLE `jct6_shuhua_activity_vote_log` (
    `id`                int(11) NOT NULL AUTO_INCREMENT,
    `work_id`           int(11) NOT NULL COMMENT '作品ID',
    `vote_uid`          varchar(32) DEFAULT NULL COMMENT '投票人ID(用户ID/微信openid)',
    `nickname`          varchar(16) DEFAULT NULL COMMENT '微信昵称',
    `headimg`           varchar(256) DEFAULT NULL COMMENT '微信头像',
    `vote_date`         varchar(16) DEFAULT NULL COMMENT '投票日期(yyyymmdd)',
    `create_time`       datetime DEFAULT NULL COMMENT '投票时间',
    PRIMARY KEY (`id`),
    KEY `IDX_WORK_DATE_USER` (`work_id`, `vote_date`, `vote_uid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
