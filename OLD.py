#импортируем pandas и json
import pandas as pd
import json

#по api github скачиваем файлы
data = pd.read_json('https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/data.json')
replace = pd.read_json('https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/replacement.json')


#Преаращаем dataframe в list
replace = replace.values.tolist()

#cсоздаем словарь, значиение повторяющихся ключей автоматически перезаписывается
#и храниться последнее записанное значение
dict_replace = {}
for i in replace:
  dict_replace[i[0]] = i[1]
dict_replace

#Преаращаем dataframe в list
data = data.values.tolist()

#создадим список ключей
keys = list(dict_replace.keys())

# отсортируем ключи по длине от самого длинного к саммому короткому
# в таком случае сначала будут заменяться более длинные ключи в строке
keys.sort(reverse=True)

new_data = []

# заменяем подстроки в сообщениях на изночальные и добавляем полученное сообщение в список
for i in range(len(data)):
  data_now = data[i][0]
  for j in keys:
    if dict_replace[j] is None:
      data_now = data_now.replace(j, '')
    else:
      data_now = data_now.replace(j, dict_replace[j])
  new_data.append(data_now)

# сохраняем итоговый список строк
with open("result.json", "w") as result:
   json.dump(new_data, result)
