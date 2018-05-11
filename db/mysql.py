# coding=utf-8
"""
E-R模型
当前物理的数据库都是按照E-R模型进行设计的
E表示entry,实体
R表示relationship,关系
一个实体转换为数据库中的一个表
关系描述两个实体之间的对应规则,包括
一对一
一对多
多对多
关系转换为数据库表中的一个列 *在关系型数据库中一行就是一个对象

三范式
经过研究和对使用中问题的总结,对于设计数据库提出了一些规范,这些规范被称为范式
第一范式（1NF)：列不可拆分
第二范式（2NF)：唯一标识
第三范式（3NF)：引用主键
说明：后一个范式,都是在前一个范式的基础上建立的

数据完整性
一个数据库就是一个完整的业务单元,可以包含多张表,数据被存储在表中
在表中为了更加准确的存储数据,保证数据的正确有效,可以在创建表的时候,为表添加一些强制性的验证,包括数据字段的类型、约束

字段类型
在mysql中包含的数据类型很多,这里主要列出来常用的几种
数字：int,decimal
字符串：varchar,text
日期：datetime
布尔：bit

约束
主键: primary key
非空: not null
惟一: unique
默认: default
外键: foreign key

逻辑删除
对于重要数据,并不希望物理删除,一旦删除,数据无法找回
一般对于重要数据,会设置一个isDelete列,类型为bit,默认值0,要逻辑删除的写1,查询的时候查值为0的即可
大于大量增长的非重要数据,可以进行物理删除
数据的重要性,要根据实际开发决定

备份与恢复
数据备份
使用超级管理员权限: sudo -s
进入mysql库目录: cd /var/lib/mysql
运行mysqldump命令: mysqldump –uroot –p 要备份的数据库 > ~/Desktop/bac.sql;(其实就是在新的文件里create和insert)
                 按提示输入mysql的密码

数据恢复
连接mysql,先创建一个新的数据库,然后往这个新数据库里恢复数据
退出重新连接: mysql -uroot –p 新创建的数据库 < ~/Desktop/bac.sql
           根据提示输入mysql密码

获取部分行
当数据量过大时，在一页中查看数据是一件非常麻烦的事情
语法: select * from 表名 limit start,count;  --从start开始，获取count条数据,start从0开始,不写就默认从0开始
示例：分页
已知：每页显示m条数据，当前显示第n页
求第n页的数据: select * from students limit (n-1)*m,m

视图
定义：对于很复杂的查询sql,经常使用的话维护起来很麻烦,可以定义成视图,视图的本质就是对查询的封装,生成一个新的表
作用：隐藏数据复杂性,有利于用户对于数据库中某些列数据的访问,使用户查询变得简单
创建视图:
create view v_stu_score as
select students.*,scores.score from scores inner join students on scores.stuid=students.id;
查询视图:
select * from v_stu_score;

外键: 可以通过外键约束进行数据的有效性验证
alter table scores add constraint stu_sco foreign key(stuid) references students(id);
此时插入或者修改数据时，如果stuid的值在students表中不存在则会报错
也可以在创建表时直接外键约束
create table scores(
id int primary key auto_increment,
stuid int,
subid int,
score decimal(5,2),
foreign key(stuid) references students(id),
foreign key(subid) references subjects(id)
);
外键的级联操作
在删除students表的数据时，如果这个id值在scores中已经存在，默认会抛异常
级联操作类型包括：
restrict（限制）：默认值，抛异常
cascade（级联）：如果主表的记录删掉，则从表中相关联的记录都将被删除
set null：将外键设置为空
no action：什么都不做
alter table scores add constraint stu_sco foreign key(stuid) references students(id) on delete cascade;

关联查询
表A inner join 表B：表A与表B匹配的行会出现在结果中
表A left join 表B：表A与表B匹配的行会出现在结果中，外加表A中独有的数据，未对应的数据使用null填充
表A right join 表B：表A与表B匹配的行会出现在结果中，外加表B中独有的数据，未对应的数据使用null填充
在查询或条件中推荐使用“表名.列名”的语法
如果多个表中列名不重复可以省略“表名.”部分
如果表的名称太长，可以在表名后面使用' as 简写名'或' 简写名'，为表起个临时的简写名称

子查询
查询各学生的语文、数学、英语的成绩
select name,
(select sco.score from scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='语文' and stuid=stu.id) as 语文,
(select sco.score from  scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='数学' and stuid=stu.id) as 数学,
(select sco.score from  scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='英语' and stuid=stu.id) as 英语
from students stu;

索引
优点: 可以提高指定列的查询速度
缺点: 会降低更新表的速度(insert/update/delete),因为索引也需要维护,更新数据时mysql不仅要保存数据还要保存索引文件
     建立索引也会占用磁盘空间的索引文件
主键是特殊的索引,数据物理结构上默认就是按主键顺序存储的
单列索引: 一个索引只包含单个列,一个表可以有多个索引,但这不是组合索引
组合索引: 一个索引包含多个列
查看索引: show index from table;
创建索引: create index index_name on table(username(length),...);
删除索引:　drop index [index_name] on table;
查看执行时间: show profiles;

事务
在对数据库做更新操作时(insert/update/delete)要使用事务
事务四大特性(简称ACID)
原子性(Atomicity)：事务中的全部操作是不可分割的，要么全部完成，要么均不执行
一致性(Consistency)：几个并行执行的事务，其执行结果和执行顺序无关
隔离性(Isolation)：事务的执行不受其他事务的干扰，事务执行的中间结果对其他事务必须是透明的
持久性(Durability)：对于已提交事务，系统必须保证该事务对数据库的改变不被丢失，即使数据库出现故障
数据库引擎：INNODB是支持事务的;MYISAM用作全文检索
查看表的创建语句: show create table students;
修改表的类型: alter table '表名' engine=innodb;
事务语句
开启: begin;       --其实是在一个内存级的临时表里更新数据,begin之后要么commit要么rollback
提交：commit;      --begin后面的所有操作必须commit后才会生效
回滚：rollback;    --begin后面的所有操作在rollback后都不会生效

内置函数
字符串函数
查看字符的ascii码值,str是空串时返回0: select ascii('a');
查看ascii码值对应的字符: select char(97);
拼接字符串: select concat(12,34,'ab');
包含字符个数: select length('abc');
截取字符串
left(str,len)返回字符串str的左端len个字符
right(str,len)返回字符串str的右端len个字符
substring(str,pos,len)返回字符串str的位置pos起len个字符: select substring('abc123',2,3);
去除空格
ltrim(str)返回删除了左空格的字符串str
rtrim(str)返回删除了右空格的字符串str
trim([方向 remstr from str)返回从某侧删除remstr后的字符串str，方向词包括both、leading、trailing，表示两侧、左、右
select trim('  bar   ');
select trim(leading 'x' FROM 'xxxbarxxx');
select trim(both 'x' FROM 'xxxbarxxx');
select trim(trailing 'x' FROM 'xxxbarxxx');
返回由n个空格字符组成的一个字符串space(n): select space(10);
替换字符串replace(str,from_str,to_str): select replace('abc123','123','def');
大小写转换，函数如下
lower(str)
upper(str)
select lower('aBcD');

数学函数
求绝对值: select abs(-32);
求余数,等价于%: select mod(10,3);   <==>   select 10%3;
向下取整: select floor(2.3);
向上取整: select ceiling(2.3);
四舍五入: select round(1.6);
求x的y次幂: select pow(2,3);
获取圆周率PI(): select PI();
值为0-1.0的随机数: select rand();

日期时间函数
获取子值，语法如下
year(date)返回date的年份(范围在1000到9999)
month(date)返回date中的月份数值
day(date)返回date中的日期数值
hour(time)返回time的小时数(范围是0到23)
minute(time)返回time的分钟数(范围是0到59)
second(time)返回time的秒数(范围是0到59)
select year('2016-12-21');
日期计算，使用+-运算符，数字后面的关键字为year、month、day、hour、minute、second
select '2016-12-21'+interval 1 day;
日期格式化: select date_format('2016-12-21','%Y %m %d');
当前日期: select current_date();
当前时间: select current_time();
当前日期时间: select now();
"""