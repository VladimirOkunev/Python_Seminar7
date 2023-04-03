# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу 
# с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке


string = list(input('Введите текст: ').split())

def volwe_check(phrase):
    vowel_list = 'аиеёоуыэюя'
    count = 0
    for char in phrase:
        if char in vowel_list:
            count +=1
    return count

new_list = list(map(lambda x: volwe_check(x), string))

if new_list.count(new_list[0]) == len(new_list):
    print('Парам пам-пам')
else:
    print('Пам парам') 


