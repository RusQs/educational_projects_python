simbol_list = list('.,;:/?!#@$%^&*()-=+')
alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text_list = ('vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip')
# text_list = input('Введите зашифрованный текст: ').split('/')
new_text_list = []
group_text_list = []
decoder_text_list = []
step = 25
start = 0
new_row = ''

for i in text_list:
	if i in alphabet_lower:
		new_row += alphabet_lower[(alphabet_lower.index(i) + step) % 26]
	elif i in alphabet_upper:
		new_row += alphabet_upper[(alphabet_upper.index(i) + step) % 26]
	elif i in simbol_list or i == ' ':
		new_row += i
new_word_list = new_row.split()

for word in new_word_list:
	if '/' not in word:
		group_text_list.append(word)
	else:
		group_text_list.append(word)
		new_text_list.append(group_text_list)
		group_text_list = []

for i in reversed(new_word_list[0]):
	start += 1
	if i in alphabet_upper:
		break

for row in new_text_list:
	for word in row:
<<<<<<< HEAD
		decoder_text_list.append(word[len(word) - (start % len(word)):] + word[:len(word) - (start % len(word))])
	start += 1

decoder_text = '\n'.join(' '.join(decoder_text_list).split('/'))
print(decoder_text)
=======
		for i in word:
			if i in alphabet_upper:
				# TODO В шифре используется сдвиг в обратную сторону
				#  То есть в слове utifulBea сдвиг не 6, а 3 (в обратную сторону)
				#  Получить его можно, взяв индекс у перевернутого слова и прибавив к нему 1:
				#  word[::-1].index(i) + 1
				step = word.index(i)
		new_word = list(word)
		for _ in range(step):
			# TODO Поскольку сдвиг в обратную сторону, нужно не первый элемент перемещать в конец,
			#  а последний элемент перемещать в начало
			#  Вставить в начало последний элемент можно так:
			#  new_word.insert(0, new_word[-1])
			new_word.append(new_word[0])
			# TODO т.к. remove удаляет первое вхождение символа, он удалит тот символ,
			#  которые мы только что переместили в начало
			#  Нам нужно удалить последний, поэтому будем использовать pop():
			#  new_word.pop(-1)
			new_word.remove(new_word[0])

		# TODO Шаг должен меняться с каждой строкой, а не с каждым словом
		#  Сдвиг в строке у вас находится автоматически, поэтому просто удалите строчку ниже
		step += 1
		qwerty.append(''.join(new_word))
	print(' '.join(qwerty))
>>>>>>> c9aa6f5d321f2141c1cdfbecef02e37a9d3d12a8







