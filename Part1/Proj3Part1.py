s_emp = (
       ('ID','LAST_NAME','FIRST_NAME','USERID','START_DATE','COMMENTS','TITLE','SALARY','COMMISSION','DEPT_ID','MANAGER_ID'),
       (10,'Jackson','Marta','jacksomt','27-Feb-91','null','Warehouse Manager',1507,'null',45,2),
       (11,'Henderson','Colin','hendercs','14-May-90','null','Sales Representative',1400,10,31,3),
       (12,'Gilson','Sam','gilsonsj','18-Jan-92','null','Sales Representative',1490,12.5,32,3),
       (13,'Sanders','Jason','sanderjk','18-Feb-91','null','Sales Representative',1515,10,33,3),
       (14,'Dameron','Andre','dameroap','9-Oct-91','null','Sales Representative',1450,17.5,35,3),
       (15,'Hardwick','Elaine','hardwiem','7-Feb-92','null','Stock Clerk',1400,'null',41,6),
       (16,'Brown','George','browngw','8-Mar-90','null','Stock Clerk',940,'null',41,6),
       (17,'Washington','Thomas','washintl','9-Feb-91','null','Stock Clerk',1200,'null',42,7),
       (18,'Patterson','Donald','patterdv','6-Aug-91','null','Stock Clerk',795,'null',42,7),
       (19,'Bell','Alexander','bellag','26-May-91','null','Stock Clerk',850,'null',43,8),
       (2,'Smith','Doris','smithdj','8-Mar-90','null','VP Operations',2450,'null',41,1),
       (20,'Gantos','Eddie','gantosej','30-Nov-90','null','Stock Clerk',800,'null',44,9),
       (21,'Stephenson','Blaine','stephebs','17-Mar-91','null','Stock Clerk',860,'null',45,10),
       (22,'Chester','Eddie','chesteek','30-Nov-90','null','Stock Clerk',800,'null',44,9),
       (23,'Pearl','Roger','pearlrg','17-Oct-90','null','Stock Clerk',795,'null',34,9),
       (24,'Dancer','Bonnie','dancerbw','17-Mar-91','null','Stock Clerk',860,'null',45,7),
       (25,'Schmitt','Sandra','schmitss','9-May-91','null','Stock Clerk',1100,'null',45,8),
       (3,'Norton','Michael','nortonma','17-Jun-91','null','VP Sales',2400,'null',31,1),
       (4,'Quentin','Mark','quentiml','7-Apr-90','null','VP Finance',2450,'null',10,1),
       (5,'Roper','Joseph','roperjm','4-Mar-90','null','VP Administration',2550,'null',50,1),
       (6,'Brown','Molly','brownmr','18-Jan-91','null','Warehouse Manager',1600,'null',41,2),
       (7,'Hawkins','Roberta','hawkinrt','14-May-90','null','Warehouse Manager',1650,'null',42,2),
       (8,'Burns','Ben','burnsba','7-Apr-90','null','Warehouse Manager',1500,'null',43,2))

s_dept = (
       ('ID','NAME','REGION_ID'),
       (10,'Finance',1),
       (31,'Sales',1),
       (32,'Sales',2),
       (33,'Sales',3),
       (34,'Sales',4),
       (35,'Sales',5),
       (41,'Operations',1),
       (42,'Operations',2),
       (43,'Operations',3),
       (44,'Operations',4),
       (45,'Operations',5),
       (50,'Administration',1))

#select * from s_dept;
print "\nSelect * from s_dept \n", \
       [[i[0], i[1], i[2]] for i in s_dept[1::]]

#select last_name, first_name, title, salary from s_emp;
print "\nSelect last_name, first_name, title, salary from s_emp \n", \
       [[i[1], i[2], i[5], i[6] ] for i in s_emp[1::]]

#select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40;
print "\nSelect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 \n", \
       [[i[1], i[2], i[5], i[6] ] for i in s_emp[1::] if (i[5] > 1500) and (i[9] > 40)]

#select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by last_name;
print "\nSelect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by last_name \n", \
       sorted([[i[1], i[2], i[6], i[7]] for i in s_emp[1::] if (i[5] > 1500) and (i[9] > 40)], key=lambda x: str(x[0]))

#select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by salary desc;
print "\nSelect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by salary desc \n", \
       sorted([[i[1], i[2], i[6], i[7]] for i in s_emp[1::] if (i[5] > 1500) and (i[9] > 40)], key=lambda x: int(x[3]), reverse=True)

#select last_name, first_name, title, salary, name from s_emp e join s_dept d on(e.dept_id = d.id);
print "\nSelect last_name, first_name, title, salary, name from s_emp e join s_dept d on(e.dept_id = d.id) \n", \
       [[i[1], i[2], i[5], i[6], j[1] ] for i in s_emp[1::] for j in s_dept[1::] if (i[9]==j[0]) ]

#select dept_id, avg(salary) from s_emp group by dept_id order by dept_id;
print "\nSelect dept_id, avg(salary) from s_emp group by dept_id order by dept_id"
for department in sorted({d[9] for d in s_emp[1::] }):
       print (department, (lambda l: round(sum(l) / len(l), 2))(map(int,[ e[7] for e in s_emp[1::] if e[9] == department ])))

#select dept_id, avg(salary) from s_emp group by dept_id having avg(salary) < 1500;
print "\nSelect dept_id, avg(salary) from s_emp group by dept_id order by dept_id"
for department in sorted({d[9] for d in s_emp[1::] }):
       print (lambda deptno, avgSal: (deptno, avgSal) if avgSal < 1500 else '')(department, (lambda l: round(sum(l) / len(l), 2))(map(int,[ e[7] for e in s_emp[1::] if e[9] == department ])))
