immutable_var = ( 'black', 3, False )
print(immutable_var)
# immutable_var[2] = 200
# print(immutable_var)    выдает ошибку при попытке внесения изменений в кортеж!!!!
mutable_list = ['black, red', 'grey', 8, 9]
print(mutable_list)
mutable_list[2] = 62
print(mutable_list)