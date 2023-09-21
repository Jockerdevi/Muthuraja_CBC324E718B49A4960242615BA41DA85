
def myFunc(e):
  return e['CGPA']
def sort_students(list):
    list.sort(key=myFunc,reverse=True)
    print(list)

    
students = [
  {'name': 'X', 'rollNo':'001','CGPA': 86.9},
  {'name': 'Y','roolNo':'002', 'CGPA': 55.6},
  {'name': 'Z', 'rollNo':'003','CGPA': 90.01},
  {'name': 'A', 'rollNo':'004', 'CGPA': 60.78}
]
students.append({'name':'B','rollNo':'005','CGPA':76.43})


sort_students(students)


