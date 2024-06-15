print('Словари')
my_dict = {'Yurii': 1992, 'Lana': 1980, 'Vlasta': 2009}
print(my_dict.get('Yurii'))
print(my_dict.get('Stepan'))
my_dict.update({'Bro' : 1992 , 'Mama' : 1966})
print(my_dict)
my_dict.pop('Yurii')
print(my_dict)
print('Множества')

my_set = {15, True, 15, 'Yurii', 'Mama', 15, 'Mama'}
print(my_set)
my_set.add(10)
my_set.add(False)
my_set.remove(15)
print(my_set)