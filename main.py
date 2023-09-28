#импортируем pandas и json
import pandas as pd
import json

class DataRecovery:
    def __init__(self, data_file,replacement_file,output_file):
        self.data_file = data_file
        self.replacement_file = replacement_file
        self.output_file = output_file

    def __load_data(self, file_path):
        # по api github скачиваем файлы
        data = pd.read_json(file_path)
        # Преаращаем dataframe в list
        data = data.values.tolist()
        return data

    def __save_data(self,new_data):
        # сохраняем итоговый список строк
        with open(self.output_file, "w") as result:
            json.dump(new_data, result)

    def __search_for_replacements(self,replace):
        # cсоздаем словарь, значиение повторяющихся ключей автоматически перезаписывается
        # и храниться последнее записанное значение
        dict_replace = {}
        for i in replace:
            dict_replace[i[0]] = i[1]
        return dict_replace

    def __keys_replacements(self, dict_replace):
        # создадим список ключей
        keys = list(dict_replace.keys())
        # отсортируем ключи по длине от самого длинного к саммому короткому
        # в таком случае сначала будут заменяться более длинные ключи в строке
        keys.sort(reverse=True)
        return keys

    def __replace_data(self, data, replacements):
        dict_replace = self.__search_for_replacements(replacements)
        keys = self.__keys_replacements(dict_replace)
        new_data = []
        # заменяем подстроки в сообщениях на изночальные и добавляем полученное сообщение в список
        for i in range(len(data)):
            data_now = data[i][0]
            for j in keys:
                if dict_replace[j] is None:
                    data_now = data_now.replace(j, '')
                else:
                    data_now = data_now.replace(j, dict_replace[j])
            if data_now != '':
                new_data.append(data_now)
        return new_data

    def recover(self):
        #загружаем файлы по указанным путям github
        data = self.__load_data(self.data_file)
        replacements = self.__load_data(self.replacement_file)
        #восстанавливаем данные
        new_data = self.__replace_data(data, replacements)
        #сохраняем востановленные данные
        self.__save_data(new_data)


def program_start():
    data_file = 'https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/data.json'

    replacement_file = 'https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/replacement.json'

    output_file = "result.json"

    processor = DataRecovery(data_file, replacement_file, output_file)

    processor.recover()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    program_start()


