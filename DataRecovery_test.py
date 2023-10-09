from unittest import TestCase, main
from main import DataRecovery


class DataRecoveryTest(TestCase):
    def test_recover(self):
        data_file = 'https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/data.json'

        replacement_file = 'https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/replacement.json'

        processor = DataRecovery(data_file, replacement_file)

        new_data = processor.recover()

        correct_result = processor._load_data('correct_result.json')

        self.assertEqual(new_data, correct_result)

if __name__ == "__main__":
    main()