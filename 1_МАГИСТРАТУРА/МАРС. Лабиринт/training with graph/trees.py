'''
Деревья могут быть представлены в виде:

----------ПРИМЕР С ОДНОЙ ВЕТКОЙ-------------

#Словари
trees = {'Хвойное дерево': 'Сосна', 'Лиственный': 'Берёза', 'Хвойные': 'Ель', 'Лиственные': 'Осина'}
for type, example in trees.items():
    print(f'{example} это {type}')
#Списки
money = ['dollars', 'euros', 'bitcoins', 'roubles']
for id, value in enumerate(money):
    print(f'{id + 2} {value}')


#----------ПРИМЕР С НЕСКОЛЬКИМИ ВЕТКАМИ-------------
#Словари
robots = {'flying':['4-bladed copters','2-bladed copters'], 'wheeled':['mecanum','differential', 'omni'], 'underwater': ['sea','river']}
for type, example in robots.items():

    print(f'{type} robots are divided on:')
    print(f"{' and '.join([str(example) for example in [*example]])}\n")  # разделяет 'каким-то текстом' выводимые элементы списка example
    #оператор *_name_ выводит все элементы спсика
    #print(*example)

#Списки
rating = [['Ze', 'Ukr', 'Free'],
          ['Nav', 'Rus', 'Fut'],
          ['Pu', 'Bye', 'Forever']]
for rat, codes in enumerate(rating):
    print(f'Место {rat+1} в нашем рейтинге занимает...\t')
    print(f"{' с '.join([str(codes) for codes in [*codes]])}\n") # разделяет 'каким-то текстом' выводимые элементы списка codes
'''
#----------ТЕОРИЯ ДЕРЕВЬЕВ------- https://en.wikipedia.org/wiki/Tree_(data_structure)#Terminology


# -------------СЛОВАРЬ ДЕРЕВА С ПОДДЕРЕВЬЯМИ-----------------
families = {'Peter':
                {'Johan': {'Carrot', 'Dildo'},
                 'Mike': {'Sparrow'}},
            'Nombert':
                {'Lilu': {'Stitch', 'Box'},
                 'Luke': {'Sweets', 'Turtle'}},
            'Harry':
                {'Albus Severus': {'Hedwig'}}
            }
'''
for parent, children in families.items():
    print(f"{parent} has {len(children)} kid(-s-):")
    print(f"    {' and '.join(str(kid) for kid in [*children])}")
    for child, property in children.items():
        print(f"    {child} has {len(property)} property(-ies-):")
        print(f"        {' and '.join(str(item) for item in [*property])}")

                              #-------------ИЗМЕНЕНИЕ(УДАЛЕНИЕ ЭЛЕМЕНТА) ДЕРЕВА ВНУТРИ ЦИКЛА-----------------
for parent, children in families.items():
    for kid, property in children.items():
        for object in property:
            if object == 'Sparrow':
                families[parent][kid] = {} # СПОСОБ 1



                            # -------------ИЗМЕНЕНИЕ(ЗАМЕНА ЭЛЕМЕНТА) ДЕРЕВА ВНУТРИ ЦИКЛА-----------------
for parent, children in families.items():
    for kid, property in children.items():
        for object in property:
            if object == 'Sparrow': families[parent][kid] = {'OWL'}

               #-------------ИЗМЕНЕНИЕ(УДАЛЕНИЕ ЭЛЕМЕНТА) ДЕРЕВА (ПРЯМОЕ ОБНОВЛЕНИЕ, ТО ЕСТЬ УКАЗАНИЕ КОНКРЕТНЫХ ID СЛОВАРЯ)-----------------
#families['Nombert']['Lilu'] = {'Stitch', 'Box'}
#del families['Peter'] -- УДАЛЕНИЕ ВОЗМОЖНО ТОЛЬКО ВНЕ ЦИКЛА'''

for parent, children in families.items():
    print(f"{parent} has {len(children)} kid(-s-):")
    print(f"    {' and '.join(str(kid) for kid in [*children])}")
    for child, property in children.items():
        print(f"    {child} has {len(property)} property(-ies-):")
        print(f"        {' and '.join(str(item) for item in [*property])}")

