--  emp
drop table if exists emp;
create table if not exists emp(
empno int primary key auto_increment,
ename varchar(10) not null,
job varchar(20),
salary double(8,2),
mgr int(10),
bonus double(6,2),
hiredate date,
deptno int(10)
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
select * from emp;
--  dept  明天待用
drop table if exists dept;
create table if not exists dept(
deptno int primary key,
dname varchar(30),
dlocation varchar(255)
);
insert into dept values(10,'teaching','北京');
insert into dept values(20,'analyst','武汉');
insert into dept values(30,'department','上海');
insert into dept values(40,'sales','郑州');
insert into dept values(50,'account','广州');
select * from dept;

-- 课后练习题

-- 1. 查询EMP表的全部职工的EMPNO、ENAME和JOB。
select empno,ename,job
from emp

-- 2. 将题1的查询结果按salary升序次序排列。
select empno,ename,job,salary
from emp
order by salary asc;

-- 3. 查询EMP表的全部列，列的次序为：JOB，SAL，ENAME，EMPNO，MGR，HIREDATE，
BONUS，DEPTNO，查询结果按年薪列升序。
select job,salary,ename,empno,mgr,hiredate,bonus,deptno,(ifnull(salary,0) *12+ ifnull(bonus,0)) as totalSalary
from emp
order by totalSalary asc;

-- 4. 列出EMP表中的不同的JOB，去掉重复值。
select distinct(job) from emp;

-- 5. 查询在部门10中工作，其工资高于7000的职工信息。
select *
from emp
where deptno=10 and salary >=7000;

-- 6. 列出其JOB为MANAGER或ANALYST的职工名及职工号。
select ename,empno
from emp
where job in('manager','analyst');

-- 7. 列出工资在5500至20000之间的职工名字、职工号。
select ename,empno,salary
from emp
where salary between 5500 and 20000;

-- 8. 查出工资为6k的工资所在的部门。
select salary,deptno
from emp
where salary=6000;

-- 9. 查出以W开头或以S结尾，或有4个字符长的职工名的职工信息。
select *
from emp
where ename like 'w%' or ename like '%s' or ename like '____';

-- 10. 列出没有奖金的职工信息。
select *
from emp
where bonus is null;

-- 11. 查出佣金比他自己的5％的工资高的职工名字、工资、佣金、以及佣金与工资之比，并按佣金与工资比的降序排列结果。
select ename,salary,bonus,(ifnull(bonus,0)/ifnull(salary,0)) as ratio
from emp
where bonus > (salary * 0.05)
order by ratio desc;

-- 12. 列出每种职业(JOB)的平均工资。
select job,avg(salary)
from emp
group by job;

-- 13. 按部门计算各部门的工资总额、平均工资和职工人数并略去平均工资低于8000的部门。
select sum(salary),avg(salary),count(*),deptno
from emp
group by deptno
having avg(salary) >= 8000;

-- 14. 查询各部门中各种职业(JOB)的人数、平均工资、最高工资和最低工资，查询结果以DEPTNO、JOB升序排序。
select deptno,job,count(*), avg(salary),max(salary),min(salary)
from emp
group by deptno,job
order by deptno asc,job asc;

-- 15．列出至少有一个员工的所有部门。
分析：每个部门有多少员工  ------ 根据部门编号进行分组
select deptno,count(*)
from emp
group by deptno
having count(*)>=1;

-- 16．列出在每个部门工作的员工数量、平均工资。
分析：按部门分组
select deptno,count(*),avg(salary)
from emp
group by deptno;

-- 17．列出各种工作的最低工资。
分析：各个工作 分组 ， 最低工资 min
select job,min(salary)
from emp
group by job;

-- 18．列出各个部门的最低薪金。
分析: 先按照各个部门分组 在找出最低的 显示
select deptno,min(salary)
from emp
group by deptno;

-- 19．列出所有员工的年工资,按年薪从低到高排序。
分析： asc
select ename,(ifnull(salary,0)*12+ifnull(bonus,0)) as totalSalary
from emp
order by totalSalary asc;

-- 20 .查出emp表中薪水在8000以上（包括8000）的所有员工的员工号、姓名、薪水。
select empno,ename,salary
from emp
where salary>=8000;

-- 21.查询出emp表中部门编号为20，薪水在8000以上（不包括8000）的所有员工，显示他们的员工号，姓名以及薪水，以如下列名显示：员工编号 员工名字 薪水
select empno,ename,salary,deptno
from emp
where deptno=20 and salary>=8000
group by deptno;

-- 22.查询出emp表中所有的工作种类（无重复）
分析：distinct
select distinct(job)
from emp;

-- 23.查询出所有奖金（bonus）字段不为空的人员的所有信息。
分析: null
select *
from emp
where bonus is not null;

-- 24.查询出薪水在6000到25000之间（闭区间）所有员工的信息。（注：使用两种方式实现and以及between and）
select *
from emp
-- where salary between 6000 and 25000;
where salary>=6000 and salary<=25000;

-- 25.查询出员工号为10，30，50的所有员工的信息。（注：使用两种方式实现，or以及in）
select *
from emp
-- where empno in(10,30,50);
where empno=10 or empno=30 or empno=50;

-- 26.查询出名字中有“a”字符，并且薪水在10000以上（不包括10000）的所有员工信息。
分析： 模糊查询 like
select *
from emp
where ename like '%a%'and salary>10000 ;

-- 27.查询出名字第三个字母是“m”的所有员工信息。
select *
from emp
where ename like '__m';

-- 28.各个部门中薪资超过7000的有多少人?
select deptno,count(*)
from emp
where salary>7000
group by deptno;

-- 29 从事销售人员的平均薪资
select avg(salary)
from emp
where job='sales';
