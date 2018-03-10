-- sql:  structed结构化  query查询   language语言
select user();
select version();
show databases;

-- 创建自己的数据库
create database mydb1;
create database mydb2;
create database mydb3;

-- 查看当前所有数据库
show databases;

-- 创建表（要指明是在哪个数据库中）
use mydb1;

-- 查看当前选择的数据库
select database ();

-- 创建表   字段类型 int double varchar date
--         其中字符类型要有长度  lisi占4个字符
--         表中每个字段以逗号隔开，最后一个字段不需要逗号
create table user(
id int,
name varchar(20),
age int
);

-- 查看表结构
desc user;

--  删除表
drop table user;

-- 查看当前数据库有多少张表
show tables;

-- 向表中插入数据
--   数据库没有双引号，全部用单引号，赋值默认全字段赋值
insert into user(name,age)values('grubby',25);
insert into user values(1,'grubby',25);
insert into user values(1,'grubby',25);

-- 查看表数据
select id from user;
select id,name,age from user;
select * from user;        --  *  表示该表所有的字段

-- 删除库        root 超级管理员   默认4个库
drop database mydb2;
drop database mydb3;

-- mysql 常用数据类型
--    int  整形       double/nemeric  小数      varchar/char   字符型         date/timestamp  日期

use mydb1;

select * from user;  --  有没有问题?  重复 数据 冗余    多个记录之间没有区分  原因 表的设计没有做好!
-- 重新设计表  不能出现数据冗余  也可以区分不同记录     设计一个字段   唯一性 不能为null
--  主键约束  primary key   简称 Pk      主键=字段   --->特性   唯一 非空  这样一种字段 称之为: 主键  表必须要有主键  否则没有意义
drop table user;
create table user(
id int primary key,
name varchar(20),
age int
);
insert into user values(1,'lisi',23);  --  主键冲突
insert into user values(2,'lisi',23);
insert into user values(3,'lisi',23);
select * from user;
--  表是必须要存在主键  否则该表没有意义!!!

-- 拓展  Mysql  主键  自动增长  数据库自动帮助我们生成一个唯一 id
--  主键添加 自动增长的属性   auto_increment    自动增长

create  table user(
id int primary key auto_increment,
name varchar(20),
age int
);
insert into user values(null,'lisi',23);  --  插入数据  写法
select * from user;

--  注意 点:  主键自动增长 需要满足的条件   1:  该字段 必须是主键    2: 该字段必须是整型
--           唯一性 unique 约束,非空约束  该字段不能为 Null

drop table emp;
create table emp(
empno int primary key auto_increment,
ename varchar(20),
email varchar(20) unique not null
);
insert into emp values(null,'grubby','orc@163.com');
insert into emp values(null,'moon','hum@163.com');
insert into emp values(null,'sky','ud@163.com');
select * from emp;

-- 查看表结构
desc emp;

-- 增删改操作     关键字 alter(更改)

-- 在上面员工表的基础上增加一个image列。  column
alter table emp add column image varchar(20);

-- 在name后面添加job列，使其长度为60。  after
alter table emp add column job varchar(20) after ename;

-- 删除gender列     delete  删除  记录
alter table emp drop column image;

-- 修改字段属性  varchar(20)--->varcahr(60)   update  修改字段值
--  modify  只能修改属性
alter table emp modify column job varchar(60);
alter table emp modify column job int;
--  change  既可以修改属性  也可以修改 字段名称
alter table emp change column job job1 varchar(60);
alter table emp change column job1 job varchar(20);

-- 查看当前数据库内所有表
show tables;

--  查看数据库
select database();
--   显示默认创建的字符集
show create database mydb1;

-- CREATE DATABASE `mydb1` /*!40100 DEFAULT CHARACTER SET utf8 */

--   数据库表 记录 crud  数据库核心!!
select * from emp;
desc emp;
--  插入数据   3种   全字段插入     主键自增长插入(常用)    选择字段插入
insert into emp (empno,ename,job,email) values (5,'fly','销售','orc@152.com');

insert into emp values (null,'lyn','选手','orc@qq.com');

insert into emp (empno,job,email) values (null,'后勤','orc@122.com');


--  删除  操作 表中记录   delete
delete from emp; --  表示删除所有数据

--  按照一定条件删除   条件筛选 ???  主键 删除   添加条件关键字  where
delete from emp where empno = 1; --  常用操作

delete  from  emp where empno <=1  >=1   = 1   <>
delete  from  emp where empno   <> 5;
--  truncate  清空    效果等同  delete from emp   区别

--  truncate  清空表数据  原先表删除  然后按照原来的表结构 创建一张新表  达到 清空数据作用   效率高
--  delete  没有删除表  直接删除数据
delete from emp;
insert into emp  values (null,'张三5','销售','zs5@itcast.cn');

--  truncate  清空表数据
truncate table emp;
select * from emp;
--  区别 :delete    删除数据  可以恢复         truncate  不可恢复   ( 事务)
start  transaction ;  --  开启事务
-- delete from  emp;
truncate table emp;
select * from emp;
-- 回滚数据操作
rollback;

--  修改 操作   update   修改字段的值  update  emp  set  设值  需不需要条件?
update emp set job = '保洁' ;  --  所有的员工 都是保洁 .....添加条件  where
update  emp  set job = '保洁'  where empno = 2;

-- 修改多个字段
update emp set job='人事' ,email = 'haha@itcast.cn' where empno = 2;

--  查询
drop table if exists exam;
create table if not exists exam(
id int primary key auto_increment,
name varchar(20) not null,
chinese double,
math double,
english double
);
insert into exam values(null,'关羽',85,76,70);
insert into exam values(null,'张飞',70,75,70);
insert into exam values(null,'赵云',90,65,95);
insert into exam values(null,'赵子龙',89,75,85);
insert into exam values(null,'孔子',88,65,55);
insert into exam values(null,'老子',88,65,55);
insert into exam values(null,'刘备',null,55,38);
show tables;
-- 1: 查询表中所有学生的信息。
select * from exam;
-- 2: 查询表中所有学生的姓名和对应的英语成绩。
select  name,english from exam;
-- 3: 过滤表中重复数据 (查询英语成绩，排除完全相同重复数据)  distinct  去重  (重复)
select  distinct(english)  from exam;
--  别名  的使用 别名 代替表达式

-- 1:在所有学生分数上加10分特长分。
select chinese ,math,english from exam;
select  chinese+10,math+10,english+10 from exam;
select  ifnull(chinese,0)+10 as 语文特长分 ,ifnull(math,0)+10 as  数学特长分 ,ifnull(english,0)+10  as 英文特长分 from exam;

--  mysql  提供自带函数  ifnull();  判断字段是否为空   null  --->目标的值替换
/*!
ifnull(english,0)

if(english==null){
english = 0;
}else{
this.english = english;
}

*/

-- 2: 统计每个学生的总分。

select  name , chinese +math+english as score from exam;

-- 3: 使用别名表示学生分数。
select chinese 语文 ,math 数学,english 英文 from exam;

--  ***  在对列起别名时，as可以省略  as  加强可读性

--  语法三: select 列名 from 表名 where条件语句

-- 课堂练习：
-- 查询姓名为关羽的学生成绩
select chinese,math,english,name
from exam
where name='关羽';

-- 查询英语成绩大于90分的同学

select *
from exam
where english > 90;

-- 查询总分大于200分的所有同学   sql  语句解析  3: select  显示   1:   from  解析表   2: where  条件
select *
from exam
where  ( ifnull(chinese,0)+ifnull(math,0)+ifnull(english,0))  >200;

--  查询运算符   算术运算符  + - * / >= <= <>


-- 2) between  ...and... 在两者之间取值 between 70 and 80 等价于 >=70 <=80
--  查询英文成绩 在70--80之间的学员有哪些?
----- 注意前面那个数要比后面那个数要小
select *
from exam
where english between 70 and 80;


-- 3) in(值,值,值) 在指定值中任取一个 in(70,80,90) 值可以是70、80或者90
--  找出  英文成绩  70  95 范围
select *
from exam
where english in(70,95);

-- 4) like '模糊查询，表达式有两个占位符 % 任意字符串 _ 任意单个字符
--  例如： name like '张%' 所有姓张学员
--          name like '张_' 所有姓张名字为两个字学员
--  姓赵的学员有哪些?   含有子的 学员有哪些?
select *
from exam
where name like '赵%'; --  以赵开头

select *
from exam
where name like '%子%';  --  含有子 姓名


--  找出  中间那个字 是子  并且姓名只有三个字  _  任意的单个字符

select *
from exam
where name like '_子_';

-- 5) is null 判断该列值为空  找出学员成绩空值
select *
from  exam
where chinese is null;  -- is  not  null

--  6) and 逻辑与  &&           or 逻辑或  ||           not 逻辑非  !

-- 7) 查询英语分数在 90－100之间的同学。
select *
from exam
where  english >=90  and english  <=100;

-- 8)查询数学分数为65,75,85的同学。

select * from exam where math in (65,75,85);

-- 9)查询所有姓赵的学生成绩
select * from  exam  where name like '赵%';

-- 10)查询英语分>80，语文分>80的同学。   or
select  * from exam where english >80  or chinese >80;

-- 11)查询语文没有成绩学员
select * from exam where chinese is null;

-- 12)查询语文有成绩学员

select * from exam where chinese is not null;

--  查询 之排序  降序 desc   descend  下降      升序  asc  ascend  上升   order  by   按照某一个字段 排序

-- 对数学成绩排序后输出(默认排序   默认升序 )。
select  * from exam  order by math desc;
-- 对总分排序按从高到低（降序）的顺序输出  desend
--   mysql  解析sql 语句顺序  :  from --->  where ----> select ----> order by
select ( ifnull(chinese,0)+ifnull(math,0)+ifnull(english,0)) as score,name
from  exam
order by  score desc;  -- 别名是可以排序的

--  对学生成绩按照英语进行降序排序，英语相同学员按照数学降序
select *
from exam
order by english desc,math desc;

--   组函数   学习    关键字();  count  计数
-- 一)count 统计查询结果记录条数  count(字段)   count(字段 非空)
-- 1) 统计一个班级共有多少学生？
select count(*)
from exam

-- 2) 统计英语成绩大于90的学生有多少个？   (统计英语成绩大于90的学生名字)
select count(*),name
from exam where english >90;

-- 3)统计总分大于220的人数有多少？
select count(*)
from exam
where ( ifnull(chinese,0)+ifnull(math,0)+ifnull(english,0)) >220;

-- 二) sum 统计某一列数据的和  select sum(列名) from 表名;   avg average  平均数     min  最小值        max   最大值
-- 1：统计一个班级数学总成绩？  sum  自动 处理 Null  值
select sum(math)
from exam;

-- 2：统计一个班级语文、英语、数学各科的总成绩
select sum(chinese)
from exam;
select sum(math)
from exam;
select sum(english)
from exam;
-- 3：统计一个班级语文、英语、数学的成绩总和
select sum(ifnull(chinese,0)+ifnull(math,0)+ifnull(english,0))
from exam;
--  dept  部门 10  20   30     emp  员工

-- 语法五：select 分组函数 from 表名 group by 列名; 按照某列进行分组统计   统计   求各个部门  最大薪资是多少?
--  emp   职位   job    sales     manager      operation  运维    按照职位划分 找出 每个职位最大薪资是多少?
--  案例分析  分组
drop table if exists products;
create table if not exists products(
id int primary key,
pname varchar(20),
price double(10,2),
category varchar(20) --  类别
);
insert into products  values(1,'电视',900,'电器');
insert into products  values(2,'洗衣机',100,'电器');
insert into products  values(3,'洗衣粉',90,'日用品');
insert into products  values(5,'洗衣粉',90,'日用品');
insert into products  values(4,'桔子',9,'水果');

-- 商品归类后，显示每一类商品的总价 ---- 需要按照类别名称进行分组   组函数
select  category,sum(price) as totalPrice
from products
group by category;

--  查询购买了几类商品，并且每类总价大于100的商品   分组之后过滤

--  先分组 再过滤
select  category,sum(price) as totalPrice
from products
group by category
having totalPrice >100;

--  先过滤  再分组    (效率高)
select  category,sum(price) as totalPrice
from products
where  price >100
group by category;

where 和 having 条件语句的区别 ？
where 是在分组前进行条件过滤，having 是在分组后进行条件过滤
where 不可以接组函数和别名因为where在select之前解析，having 可以使用别名因为having在select之后解析

小结 select 语句书写的规则 ：
S-F-W-G-H-O 组合 select (distinct)... from ...(join) where ... group by... having... order by ... limit ...;
mysql数据库解析的顺序：不能改变
解析顺序 ： from (join) - where - group by - select (distinct) - having - order by - limit
