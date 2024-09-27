my_dict = {'Elena' :1978, 'Mariya' :1985, 'Evgeniy' :1991}
print(my_dict)
print(my_dict.get('Elena'))
print(my_dict.get('Ilona'))
my_dict.update({'Mark' :1652, 'Matvey' :1988})
del my_dict['Elena']
print(my_dict)

my_set = {5, 8, 8, 'red', (5, 14, 13)}
print(my_set)
my_set.add(33)
my_set.add(True)
my_set.discard(8)
print(my_set)
