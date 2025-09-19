from course_okulik.lesson_12.TestControlSystem.MyTestCase import MyTestCase


class TestSuite:
    def __init__(self, name):
        self._name = name
        self._test_cases = []

    def add_test_case(self, test_case: MyTestCase):
        if isinstance(test_case, MyTestCase):
            self._test_cases.append(test_case)
        else:
            print(f'Ошибка: В тест-набор "{self._name}" можно добавлять только экземпляры TestCase.')

    def run_suite(self):
        print(f"Запуск тест-набора: {self._name}")
        for test in self._test_cases:
            MyTestCase.run_test()
