my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
"""
попытка сделать азадние без помощи преподавателя
idx = 0

while idx < len(my_list):
    people = my_list.pop()
    print(people)
    list_people = people.split(' ')
    print(list_people)
    name = list_people.pop()
    right_name = name.title()
    print(right_name)

# не понятно как это собрать
"""

for position in my_list:
    print('Привет,', position.split()[-1].title())
