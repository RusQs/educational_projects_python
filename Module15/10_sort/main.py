first_list = [1, 4, -3, 0, 10]
second_list = []

print('Изначальный список: ', first_list)

for i in range(len(first_list)):
	second_list.append(min(first_list))
	first_list.remove(min(first_list))

print('Отсортированный список:', second_list)

#Не совсем понял что значило в задании то что нельзя использовать дополнительный список. Нужно было изменить
# начальный, а не создавать сортировку в новом?

# TODO Нужно было изменить начальный - именно так
#  В процессе сортировки нужно было работать только с одним списком.
#  Вы как раз использовали для сортировки дополнительный список.