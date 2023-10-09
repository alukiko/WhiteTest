from unittest import TestCase, main
from main import DataRecovery


class DataRecoveryTest(TestCase):

    def setUp(self):

        self.data_file = 'https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/data.json'

        self.replacement_file = 'https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/replacement.json'

        self.processor = DataRecovery(self.data_file, self.replacement_file)

    def test_search_for_replacements(self):

        replace = [[2,3],[2,4],[5,6],[6,5],[5,8]]

        dict_replace = self.processor._search_for_replacements(replace)

        correct_dict_replace = {2:4,5:8,6:5}

        self.assertEqual(dict_replace, correct_dict_replace)


    def test_keys_replacements(self):

        dict_replace = {"vdv":4,"cc":8,"scscssc":5}

        keys = self.processor._keys_replacements(dict_replace)
        correct_keys = ['scscssc','vdv','cc']

        self.assertEqual(keys, correct_keys)


    def test_recover(self):


        new_data = self.processor.recover()

        correct_result = self.processor._load_data('correct_result.json')

        self.assertEqual(new_data, correct_result)

if __name__ == "__main__":
    main()