# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:



import pandas as pd
import sqlite3

con1 = sqlite3.connect("Students.db")
tablestud = pd.read_sql("SELECT * FROM Students", con1)
print (tablestud)
con2 = sqlite3.connect("teachers.db")
tablestud.to_sql("Students", con2, index = False)





import sqlite3
def get_stud(student_id):
  con = sqlite3.connect("teachers.db")
  cur = con.cursor()
  query = """SELECT * FROM School Join Students ON School.School_id = Students.School_id WHERE  Students.Student_id = ?"""
  cur.execute(query,(student_id,))
  rec = cur.fetchall()
  print(rec)

get_stud(201)

import sqlite3

def get_school_name(school_id):
  con = sqlite3.connect("Schools.db")
  cur = con.cursor()
  query = "SELECT * FROM School WHERE School_id = ?"
  cur.execute(query,(school_id,))
  rec = cur.fetchone()
  return rec[1]


def get_student(student_id):
  con = sqlite3.connect("Students.db")
  cur = con.cursor()
  query = "SELECT * FROM Students WHERE Student_id = ?"
  cur.execute(query,(student_id,))
  rec = cur.fetchall()
  for raw in rec:
    print("ID Студента:", raw[0])
    print("Имя Студента:", raw[1])
    print("ID Школы:", raw[2])
    print("Название Школы:",get_school_name(raw[2]),"\n")
  con.close()



get_student(201)
get_student(202)
get_student(203)
get_student(204)