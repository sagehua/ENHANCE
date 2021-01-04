# 一条 SQL 查询语句是如何执行的

*. MySQL 的逻辑架构：客户端、Server（连接器、分析器、优化器、执行器）、存储引擎

1. 客户端使用 TCP 连接到 Server 上
  - show processlist 可以看到连接情况
  - 空闲的连接：连接完成后，如果没有后续的动作，这个连接就处于空闲状态（show processlist 中的 Command 列为 Sleep）
  - 连接的自动断开：客户端如果太长时间没有动静，连接器就会自动将它断开（这个时间由 wait_timeout 控制，默认是 8 小时）
  - 错误：在连接被断开之后，如果客户端再次发送请求，就会收到一个错误提醒“Lost connection to MySQL server during query.”
  
  **数据库的长连接、短连接** 怎样选择长连接、短连接？

2. 查询缓存
  - MySQL 8.0 版本以后没有查询缓存

3. 分析器
  确定要执行的操作
  - 词法分析
  - 语法分析

4. 优化器
  选择效率最高 的执行方案
  - 在有多个索引时，决定使用哪个索引
  - 在有多表关联时，决定各表的连接顺序

  **mysql> select * from t1 join t2 using(ID)  where t1.c=10 and t2.d=20; -- USING 的用法**

5. 执行器
  通过表的引擎提供的接口获得数据
  - 重复调用接口，扫描完全表（或者全索引）
  - 将扫描过程中所有满足条件的行组成结果集返回给客户端

# 一条 SQL 更新语句是如何执行的
