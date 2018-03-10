-- 重点掌握 :表设计的原则原理 和 sql语句的编写

-- 当天小结:  重点       一对多  多对多 表设计原则 和sql 编写
--                多表链接 笛卡尔积过滤
--                外链接 (左 右 链接  掌握)   自链接 (自己和自己链接)
--                子查询 优化sql 语句
show databases;
drop database if exists mydb2;
create database if not exists mydb2;
use mydb2;
--   员工表   部门表
drop table if exists emp;
create table if not exists emp(
empno int primary key auto_increment,  --  员工号  number
ename varchar(10) not null, -- 员工姓名  -- varchar2
job varchar(20), -- 职位
salary double(8,2), -- 薪资   3500.20     (8,2)  8 表示该字段 总长度 8位     2 : 小数点后面2位    最大值 :  999999.99     number(8,2)
mgr int(10),  --  该员工上级领导的 员工号  empno
bonus double(6,2),  --  奖金  (6,2)
hiredate date,   --  入职日期   默认 年月日
deptno int(10)   --  部门号
);
--  插入数据
insert into emp values(null,'mary','sales',7000,6,1000,'2014-1-1',10);
insert into emp values(null,'lily','sales',6000,1,800,'2014-5-1',10);
insert into emp values(null,'tom','sales',5000,1,4000,'2014-3-1',10);
insert into emp values(null,'james','account',8000,6,null,'2014-2-1',20);
insert into emp values(null,'scott','teaching',8000,6,3000,'2014-1-20',30);
insert into emp values(null,'tom','BOSS',38000,null,null,'2013-1-20',30);
insert into emp values(null,'kitty','teaching',7000,5,700,'2014-5-20',30);
insert into emp values(null,'kitty','teaching',6000,5,500,'2014-6-20',30);
insert into emp values(null,'green','analyst',15000,6,1000,'2014-2-20',40);
insert into emp values(null,'brown','analyst',12000,9,7000,'2014-4-20',40);
insert into emp values(null,'danis','department',3000,6,800,'2014-3-4',50);
insert into emp values(null,'brown','department',1800,11,600,'2014-4-20',50);
insert into emp values(null,'smith','department',1200,11,500,'2014-5-20',50);
insert into emp values(null,'qb','department',8000,11,2000,'2013-5-20',null);

--  dept  部门表说明   dept   department  部门  系  English Department
drop table if exists dept;
create table if not exists dept(
deptno int primary key,  --  部门号
dname varchar(30),  --  部门名称
dlocation varchar(255)  -- 部门所在地
);
insert into dept values(10,'teaching','北京');
insert into dept values(20,'analyst','武汉');
insert into dept values(30,'department','上海');
insert into dept values(40,'sales','郑州');
insert into dept values(50,'account','广州');
insert into dept values(60,'it','山西');

--  查看 表数据
select  * from emp;
select * from dept;

--  多表查询之  子查询
-- 1.1例：查询工资比编号为3雇员工资高的雇员信息。 5000
--  1:  找到编号 3  员工薪资   5000
select salary from emp where  empno=3;
-- 2:   select * from emp where salary >5000;  (第一条sql语句结果)  条件 where 子查询   诞生
select * from emp where salary >(select salary from emp where  empno=3);

--  显示和雇员scott同部门的雇员姓名、工资和部门编号
-- 1:  找出scott 部门号
select deptno from emp where ename = 'scott';
-- 2: 显示同部门所有员工
select ename,salary,deptno from emp where deptno = (select deptno from emp where ename = 'scott');

-- 3: 显示工资最低的雇员姓名、职位和工资。
-- select job,ename, min(salary) from emp;  --  错误的
-- 1: 所有员工最低薪资  作为条件筛选  1200
select min(salary)  from emp;
-- 2: 显示最低薪资的员工信息
select * from emp where salary = (select min(salary)  from emp);

-- 4: 显示部门内最低工资 比 20部门最低工资  要高的部门的编号及部门内最低工资。

select min(salary) from emp where deptno = 20;  -- 8000
--  先分组   部门号分组
select  min(salary)  from emp  group by deptno;

-- 显示   部门号   部门最低薪资
select  min(salary) as min_sal ,deptno
from emp
group by deptno
having  min_sal>( select min(salary) from emp where deptno = 20);

--  多表联查    emp   部门dept
--  多表联查的sql 语句
-- 显示  marry 工作地点?
-- 第一步 找出两张表笛卡尔积   (笛卡尔积   结果是集合  冗余的数据 )
select *
from emp ,dept
where emp.deptno = dept.deptno;
--  从笛卡尔积 筛选有效的数据 条件    emp.deptno = dept.deptno
-- 第二步  找出有效数据  进行 再次筛选
select *
from emp ,dept
where emp.deptno = dept.deptno and emp.ename='mary';
--  *  表示两张表的所有字段显示

select dept.dlocation
from emp ,dept
where emp.deptno = dept.deptno and emp.ename='mary';


--  优化  表的别名形式
select d.dlocation
from emp as  e ,dept as  d
where e.deptno = d.deptno and e.ename='mary';

--  两张表的链接类型:   1:   外连接

--  2:  内连接    emp  表自己和自己链接
--  题目: 找出 mary 领导是谁?
--  1:  子查询     : 分析 :  找出mary mgr    select  mgr  from emp where ename = 'mary';
--  2:  select * from emp where empno = mgr;
select * from emp where empno = (select  mgr  from emp where ename = 'mary');

-- 3: 多表联查   内连接 (自链接)  必须要用表别名区分
select  manager.*
from  emp as worker ,emp as manager
where  worker.mgr = manager.empno and worker.ename='mary';

-- 4:  内连接  例子 :   mary 下属有哪些?
select worker.*
from emp as worker , emp as manager
where  worker.mgr = manager.empno and manager.ename = 'mary';

--  5:  外链接的例子   emp  dept  找薪资最低员工所在的部门地点?
select * from dept;
--  等值链接
select d.dlocation
from  emp as e ,dept as d
where e.deptno = d.deptno and  e.salary=(select min(salary)  from emp);

--  拓展   左外链接   右外链接
select * from emp;
select  * from dept

select *
from  emp as e ,dept as d
where e.deptno = d.deptno;

--  找出所有部门 的员工信息 要求 部门信息要全部显示
--  左外  或者  右外   join  on
--  left  join   表示  左边的表  驱动表  基表  该表所有信息 都会显示出来
select *
from  emp as e    right join   dept as d
on e.deptno = d.deptno;
--  dept  基表  里面所有的数据 都会显示出来
--  from   emp as e    left join     dept as d   左边表作为 基表  该表所有数据都会出现

--  表的设计原则 :    所有关系型表 中 存在三种关系  京东   登录  用户表    商品  订单   销售榜单   查看订单   订单 商品信息

--  1: 1    1: n   或者  n:1      多对多
--    商品 n  <---------->  n  订单


--    用户表   1   <-- >  n   订单

--    老公 1: <---->   1    老婆        工作室     负责人


--  emp  n   ------>  1  dept


--  多表设计之  一对多   user  --->order
-- 用户和订单表分析 京东  商城

create  table if not exists user(
	id int auto_increment,
	name varchar(20),
	salary double(10,2),
	 primary key(id)
);

create  table if not exists orders(
	id int primary key auto_increment,
	info varchar(20),
	money double(10,2),
	uid int   --  外键
);

--  添加关系映射  一对多   多方添加外键约束  alter    约束 系统名称  唯一  给约束起一个名字
alter table orders add constraint user_orders_fk foreign key(uid)  references user(id);

desc  orders;
--  更新数据  先插入 关联表 一方

insert into user values(null,'张柏芝',8000);
insert into user values(null,'陈冠希',9000);
insert into user values(null,'黄海波',5000);

insert into orders values(null,'上海是闵行区三路公路3279号205',1000,1);
insert into orders values(null,'张柏芝',700,1);


--  问题 :  找出 张柏芝的所有订单信息  ....   多表联查
/*!
dao   db  -->数据库 -->对象  List<Order>   orders   ....servlet
request.setAttibute("orders",orders);
request.getRequestDispatcher("/listOrders.jsp").forward(request,response);
listOrders.jsp    el+jstl  --->table  <c:foreach  var="order"  items="${orders}">
*/
select o.*
from user as  u  , orders  as  o
where u.id = o.uid  and  u.name='张柏芝';

--  删除表   顺序
--  先删除  多方数据  再删除一方
drop table orders;
drop  table  user;

--  建立一对多表设计  建表同时创建关联
create  table if not exists user(
	id int auto_increment,
	name varchar(20),
	salary double(10,2),
	 primary key(id)
);

create  table if not exists orders(
	id int primary key auto_increment,
	info varchar(20),
	money double(10,2),
	uid int ,  --  外键
	constraint user_orders_fk foreign key(uid)  references user(id)
);

-- 多表设计之 多对多原则  orders  products
--  订单表已经创建好了 ....
create  table if not exists products(
id int primary key auto_increment,
name varchar(20),
price double(10,2),
category varchar(100)
);

--  创建 中间表

create  table if not exists orders_products(
oid int ,  --  订单主键
pid int, --  商品主键
buynum int, --  一张订单 商品购买数量
primary key(oid,pid) --  联合主键
);

--  添加关系
alter table orders_products add constraint orders_products_orders_fk  foreign key (oid) references orders(id);
alter table orders_products add constraint orders_products_products_fk  foreign key(pid) references products(id);

desc  orders_products;

--  更新数据  先更新 "父表"    再更新中间表数据

insert  into products values(null,'剃须刀',999,'日用品');
insert  into products values(null,'牙膏',19,'日用品');
insert  into products values(null,'牙刷',9,'日用品');
insert  into products values(null,'洗衣液',99,'日用品');
insert  into products values(null,'苹果手机',4999,'数码');
insert  into products values(null,'mac 电脑',17988,'数码');
insert  into products values(null,'火龙果',88,'水果');
insert  into products values(null,'榴莲',48,'水果');
insert  into products values(null,'苹果',18,'水果');

insert into orders  values(null,'上海传智播客205',2000,1);
insert into orders  values(null,'上海传智播客210',1000,1);

select * from orders;
select * from products;
select * from orders_products;

--  更新中间表数据   中间表的数据 -->  订单里商品数据   3号订单  4号订单  存在对应商品数据
-- 1号订单购买的商品信息
insert  into orders_products values(1,5,2);
insert  into orders_products values(1,6,1);
-- 3号订单 购买的商品信息
insert  into orders_products values(3,1,20);
insert  into orders_products values(3,2,10);
insert  into orders_products values(3,3,5);

-- 4号订单购买的商品信息
insert  into orders_products values(4,7,5);
insert  into orders_products values(4,8,10);
insert  into orders_products values(4,9,15);


--  1: 查询 订单号3  所有的商品  显示商品的所有信息以及购买数量!   orders   / products
select  p.*,op.buynum
from  orders as o , products as p , orders_products as op
where o.id = op.oid and p.id = op.pid  and o.id = 3;
--  备用
select  p.*,op.buynum
from  products as p , orders_products as op
where  p.id = op.pid  and op.oid = 3;

select * from user;
--  2: 查询张柏芝 的所有订单  以及订单的商品信息  products   orders    orders_products
select p.*,o.*
from  orders  as o ,products as p ,orders_products as op ,user as u
where  o.id = op.oid and p.id = op.pid and u.id = o.uid and u.id=1;

-- 3: 查询水果卖了多少?  buynum    中间表  products
select  sum(op.buynum)
from  products as p ,orders_products as op
where p.id = op.pid and p.category='水果';


-- 4: 查询商品销售榜单 显示给用户看的   ?  buynum   products   orders_products
select p.*,sum(op.buynum)  as totalSales
from   products as p , orders_products as op
where p.id = op.pid
group by p.id
order by totalSales desc;


--  小结 : 1:  根据需求  判断 几张表    找关系  过滤器 笛卡尔积   得到有效数据
--           2:  得到有效的数据  根据条件  筛选

--  多对多表设计原则 :
--  1:  引入第三张表 作为中间表
--  2:  联合主键 以及  外键约束   (sql 语句的编写)





