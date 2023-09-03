# 0x0F. Python - Object-relational mapping

```sql
███ ███ █   █     ███ █ █ ███ █ █ ███ █   █     █   █ █ █ ███ ███ █
█ █ █ █ ██ ██     █ █ █ █  █  █ █ █ █ ██  █     ██ ██ █ █ █   █ █ █
█ █ ██  █ █ █     ███  █   █  ███ █ █ █ █ █     █ █ █  █   █  █ █ █
█ █ █ █ █   █     █    █   █  █ █ █ █ █  ██     █   █  █    █ ███ █
███ █ █ █   █     █    █   █  █ █ ███ █   █     █   █  █  ███ ███ ███
                                                                █
```

## Learning Objectives

### General

* Why Python programming is awesome
* How to connect to a MySQL database from a Python script
* How to ```SELECT``` rows in a MySQL table from a Python script
* How to ```INSERT``` rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table

## Environment

<div>
<!-- Ubuntu --> <a href="https://ubuntu.com/" target="_blank"><img height="24px" src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/ubuntu-icon.svg" alt="Ubuntu"> </a> <!-- GNU Bash --> <a href="https://www.vim.org/" target="_blank"><img height="24px" src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/gnu-bash-logo.svg" alt="GNU Bash"> <!-- Vim --> <a href="https://www.vim.org/" target="_blank"><img height="24px" src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/Vimlogo.svg" alt="Vim text editor"> </a> <!-- MySQL --> <a href="" target="_blank"><img height="24px" src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/mysql.svg" alt="MySQL" > </a>
</div>

* OS: Ubuntu 20.04 LTS
* Terminal: Bash 5.0.17
* Editor: VIM 7.4.52
* Language: SQL
* Language: Python 3.8.8
* MySQL 8.0.27
* modules
  * ```MySQLdb``` 2.0.x
  * ```SQLAlchemy```1.4.x

>MySQL installation:

```bash
sudo apt update
sudo apt install mysql-server
```

> Connect to MySQL:

```bash
sudo mysql
```

> Container on demand:

```bash
service mysql start
```

> MYSQLdb installation:

```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)
```

> SQLAlchemy install:

```bash
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22
```

The following messege must be ignored:

```bash
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")
  cursor.execute(statement, parameters)
```

## With or without ORM examples

> Without ORM

```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

> With ORM

```python
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

## Execute files

all files include the following shebang:

```bash
#!/usr/bin/python3
```

```bash
$ cat 0-select_states.sql | mysql -uroot -p
Enter password:
$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```

```bash
$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
```

```bash
$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

> SQL injection
  > Delete all the records in the table

```bash
./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
```

```bash
$ ./0-select_states.py root root hbtn_0e_0_usa
$
```

> SQL injection safe

```bash
$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

> Cities by state

```bash
cat 4-cities_by_state.sql | mysql -uroot -p
```

```bash
$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
```

```bash
./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
```

```bash
$ cat 6-model_state.sql | mysql -uroot -p
Enter password:
```

```bash
$ ./6-model_state.py root root hbtn_0e_6_usa
$ cat 6-model_state.sql | mysql -uroot -p
Enter password:
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

---

## ORM

```bash
cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
```

```bash
$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
```

```bash
$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
```

```bash
$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
```

```bash
$ ./11-model_state_insert.py root root hbtn_0e_6_usa
6
```

```bash
$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa
$
```

```bash
$ ./13-model_state_delete_a.py root root hbtn_0e_6_usa
$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
2: New Mexico
4: New York
$
```

```bash
$ cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
Enter password:
$ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
$
```

```bash
$ cat 100-relationship_states_cities.sql | mysql -uroot -p
Enter password:
```

```bash
$ ./100-relationship_states_cities.py root root hbtn_0e_100_usa
$ cat 100-relationship_states_cities.sql | mysql -uroot -p
Enter password:
id  name
1   California
id  name    state_id
1   San Francisco   1
```

```bash
$ cat 101-relationship_states_cities_list.sql | mysql -uroot -p
$ ./101-relationship_states_cities_list.py root root hbtn_0e_101_usa
1: California
    1: San Francisco
    2: San Jose
    3: Los Angeles
    4: Fremont
    5: Livermore
2: Arizona
    6: Page
    7: Phoenix
3: Texas
    8: Dallas
    9: Houston
    10: Austin
4: New York
    11: New York
5: Nevada
    12: Las Vegas
    13: Reno
    14: Henderson
    15: Carson City
$
```

```bash
$ ./102-relationship_cities_states_list.py root root hbtn_0e_101_usa
1: San Francisco -> California
2: San Jose -> California
3: Los Angeles -> California
4: Fremont -> California
5: Livermore -> California
6: Page -> Arizona
7: Phoenix -> Arizona
8: Dallas -> Texas
9: Houston -> Texas
10: Austin -> Texas
11: New York -> New York
12: Las Vegas -> Nevada
13: Reno -> Nevada
14: Henderson -> Nevada
15: Carson City -> Nevada
$
```

## Autor

>```Ronald Rivero```

## Connect

<br>
<div>
<!-- Twitter -->
<a href="https://twitter.com/ralex_uy" target="_blank"> <img align="left" alt="Ronald Rivero | Twitter" src="https://img.shields.io/twitter/follow/ralex_uy?style=social"/> </a>
<!-- Linkedin -->
<a href="https://www.linkedin.com/in/ronald-rivero/" target="_blank"> <img align="left" alt="Ronald Rivero | LinkedIn" src="https://img.shields.io/badge/LinkedIn-Follow-blue?style=social&logo=linkedin"/> </a>
<!-- Github -->
<a href="https://github.com/ralexrivero/" target="_blank"> <img align="left" src="https://img.shields.io/github/followers/ralexrivero?style=social" alt="Ralex | Github"> </a>
</br>
</div>
