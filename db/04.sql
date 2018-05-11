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
insert into emp values(null,'tomy','BOSS',38000,null,null,'2013-1-20',30);
insert into emp values(null,'kitty','teaching',7000,5,700,'2014-5-20',30);
insert into emp values(null,'kitty','teaching',6000,5,500,'2014-6-20',30);
insert into emp values(null,'green','analyst',15000,6,1000,'2014-2-20',40);
insert into emp values(null,'brown','analyst',12000,9,7000,'2014-4-20',40);
insert into emp values(null,'danis','department',3000,6,800,'2014-3-4',50);
insert into emp values(null,'brown','department',1800,11,600,'2014-4-20',50);
insert into emp values(null,'smith','department',1200,11,500,'2014-5-20',50);

--  dept
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
--  查看 表数据
select  * from emp;
select * from dept;
emp  dept  添加一个外键约束

Dept 字段: deptno  int   primary key   dname  部门名称   dlocation 部门所在地
和emp 多表联查

--1.  找出 30部门在上海工作的所有工作人员
select *
from emp as e,dept as d
where e.deptno = d.deptno and e.deptno = 30;

--2 ．列出薪金比“lily”多的所有员工。
分析：先查询出lily工资
select *
from emp
where salary > (select salary from emp where ename ='lily');

--3． lily 的领导是谁?
select manager.*
from emp as worker,emp as manager
where worker.mgr = manager.empno and worker.ename = 'lily';

--4． 列出受雇日期早于其直接上级的所有员工。
select worker.*
from emp as worker, emp as manager
where worker.mgr = manager.empno and worker.hiredate< manager.hiredate;

-- 5． 找出每个部门薪资最低的人的姓名和部门号
select ename ,deptno from emp where  (salary,deptno) in (select  min(salary) as min_sal,deptno from emp group by deptno);
或者:
select e.ename,e.deptno
from emp as e,(select  min(salary) as min_sal,deptno from emp group by deptno)  as m
where e.deptno = m.deptno and e.salary= m.min_sal ;

--6． 列出所有sales的姓名及其部门名称。
select ename,deptno,job
from emp
where job='sales';

--7．列出最低薪金大于7000的各种工作。
分析：工作的最低薪金 ---- 按工作分组，求最低薪金
大于7000 是一个分组条件 --- having
select min(salary) as min_sal,job
from emp
group  by job
having min_sal>7000;

--8．列出在部门“SALES”（销售部）工作的员工的姓名，假定不知道销售部的部门编号。
分析：员工姓名位于 emp  部门名称 dept
select ename
from emp
where job='sales';

--9．列出薪金高于公司平均薪金的所有员工。
分析：先求公司平均薪金 select avg(sal) from emp;
select *
from emp
where salary>(select avg(salary) from emp );

--10．列出与“SCOTT”从事相同工作的所有员工。
select *
from emp
where job=(select job from emp where ename='scott');

--11．列出薪金等于部门30中员工的薪金的所有员工的姓名和薪金。
select salary from emp where deptno=30;
select ename,salary
from emp
where salary in(select salary from emp where deptno=30);

--12．列出各个部门平均薪资高于10000所有员工的薪金的员工姓名和薪金。
select deptno from emp group by deptno having avg(salary)>10000;
select ename,salary
from emp
where deptno in(select deptno from emp group by deptno having avg(salary)>10000);

--13．列出在每个部门工作的员工数量、平均工资。
 分析：按部门分组
select count(*),avg(salary),deptno
from emp
group by deptno;

--14．列出所有员工的姓名、部门名称和工资。
select ename,deptno,salary
from emp;
select * from emp ;

--15．列出所有部门的详细信息和部门人数。
select d.*,count(*)
from emp as e,dept as d
where e.deptno=d.deptno
group by deptno;

--16．列出各种工作的最低工资。
分析：各个工作 分组 ， 最低工资 min
select min(salary),job
from emp
group by job;

--17．列出各个部门的最低薪金。
select min(salary),deptno
from emp
group by deptno;
分析: 先按照各个部门分组 在找出最低的 显示

--18．列出所有员工的年工资,按年薪从低到高排序。
分析： asc
select (ifnull(salary,0)*12+ifnull(bonus,0)) as totalSalary,ename
from emp
order by totalSalary asc;

--19. 查出emp表中薪水在8000以上（包括8000）的所有员工的员工号、姓名、薪水。
select empno,ename,salary
from emp
where salary>=8000;

--20. 查询出所有薪水在'tom'之上的所有人员信息。
分析：找出tom 的薪水 可以使用子查询
select *
from emp
where salary>(select salary from emp where ename='tom');

--21. 查询出emp表中部门编号为20，薪水在8000以上（不包括8000）的所有员工，显示他  们的员工号，姓名以及薪水，以如下列名显示：员工编号 员工名字 薪水
select empno,ename,salary
from emp
where deptno=20 and  salary>=8000 ;

--22. 查询出emp表中所有的工作种类（无重复）
分析：distinct
select distinct(job)
from emp;

--23. 查询出所有奖金（bonus）字段不为空的人员的所有信息。
分析: null
select *
from emp
where bonus  is  not null;

--24. 查询出薪水在800到2500之间（闭区间）所有员工的信息。（注：使用两种方式实现and以及between and）
select *
from emp
-- where salary>=800 and salary<=2500;
where salary between 800 and 2500;

--25. 查询出员工号为3，5，7的所有员工的信息。（注：使用两种方式实现，or以及in）
select *
from emp
-- where empno in(3,5,7);
where empno=3 or empno=5 or empno=7;

--26. 查询出名字中有“a”字符，并且薪水在10000以上（不包括10000）的所有员工信息。
分析： 模糊查询 like
select *
from emp
where ename like '%a%' and salary >10000;

--27. 查询出名字第三个字母是“m”的所有员工信息。
select *
from emp
where ename like '__m';

--28. 显示公司最高薪资的人的所有信息
select *
from emp
where salary=(select max(salary) from emp);

--29. 员工mary 领导是谁
select manager.ename
from emp as worker,emp as manager
where worker.mgr=manager.empno and worker.ename='mary';

--30. 查询出最早工作的那个人的名字、入职时间和薪水以及工作地点和部门号。
分析：最早工作人 --- hiredate 最小值
select e.ename,e.hiredate,e.salary,d.dlocation,e.deptno
from emp as e,dept as d
where e.deptno=d.deptno and e.hiredate=(select min(hiredate) from emp);

--31. 显示mary下属有哪些
select *
from emp as worker,emp as manager
where worker.mgr=manager.empno and manager.ename ='mary';

--32. 显示出各个部门薪水最低的人的所有信息。
select * from emp where (salary,deptno) in (select  min(salary) as min_sal,deptno from emp group by deptno);

--33. 查出emp表中所有部门的最高薪水和最低薪水，部门编号为10的部门不显示。
select max(salary),min(salary)
from emp
where deptno<>10
group by deptno;
