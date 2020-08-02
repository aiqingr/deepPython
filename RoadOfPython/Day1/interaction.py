name = input("Name: ")
age = int(input("Age: "))
job = input("Job:")

print(name, age, job, type(age))

info_1 = f'''
-------------info of {name}
Name: {name}
Age: {age}
Job: {job}
'''
print(info_1)

info_2 = '''
----------info of %s--------
Name: %s
Age: %d
Job: %s
''' % (name, name, age, job)
print(info_2)

info_3 = '''
----------info of {_name}-------
Name: {_name}
Age: {_age}
Job: {_job}
''' .format(_name=name, _age=age, _job=job)
print(info_3)

