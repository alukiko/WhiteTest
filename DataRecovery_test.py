from unittest import TestCase, main
from main import DataRecovery


class DataRecoveryTest(TestCase):
    def test_recover(self):
        data_file = 'https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/data.json'

        replacement_file = 'https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/replacement.json'

        output_file = "result.json"

        processor = DataRecovery(data_file, replacement_file, output_file)

        new_data = processor.recover()

        correct_result = processor._load_data('correct_result.json')
        for i in range(len(correct_result)):
            correct_result[i] = correct_result[i][0]

        self.assertEqual(new_data, correct_result)

if __name__ == "__main__":
    main()