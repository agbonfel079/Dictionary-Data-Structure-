# Dict items  are key  value pairs  enclosed in curly brackets
# Dict is ordered as of python 3.7
# Dict  is mutable
# Dict keys are unique , cannont  have duplicates 
# Elements can  be of different  data types

'''
Dict Attributes
'''

# print(dir(dict))
# print(help(dict.pop))

'''
Creating Python Dictionary 
'''

# dict_example = {}
# dict_example = {'name': 'Felix', 'age': 45}
# dict_example = dict([(1,'car'), (2, 'bicycle')])
# print(dict_example)

'''
Access Dictionary Values  
'''

# student = {'name': 'Felix', 'age': 45}
# print(student['age'])
# print(student.get('age'))
# print(student.keys())
# print(student.values())


# students = [{'name': 'Felix', 'age': 45},  {'name': 'Mary', 'age': 35}]
# # print(students[1]['name'])
# for i in range (len(students)):
#   print(students[i] ['name'])
#   print(students[i] ['age'])

'''
  Changing Dictionary  elements
  '''

# student = {'name': 'Felix', 'age': 45}
# student ['age'] = 35
# print(student)

#==================

# student = {'name': 'Felix', 'age': 45}
# student.update({'name': 'Jennifer', 'age': 25})
# print(student)

# #==================

# student = {'name': 'Felix', 'age': 45}
# student.setdefault('name','John')
# student.setdefault('subject','Python')
# student.setdefault('subject','English')
# print(student)

'''
  Remove Element From  Dictionary 
  '''
# student = {'name': 'Felix', 'age': 45}
# # student.pop('name')
# student.popitem()
# print(student)


# #==================


# student = {'name': 'Felix', 'age': 45}
# # student.pop('name')
# student.clear()
# print(student)

# #==================

# student = {'name': 'Felix', 'age': 45}
# # student.pop('name')
# del student
# print(student)


'''
  Dictionary Membership  Test
  '''

student = {'name': 'Felix', 'age': 45}

print('age' not in student)
