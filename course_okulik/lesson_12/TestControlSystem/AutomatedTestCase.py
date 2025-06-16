from course_okulik.lesson_12.TestControlSystem.MyTestCase import MyTestCase


class AutomatedTestCase(MyTestCase):
    def __init__(self, title, priority, script_name):
        super().__init__(title, priority)
        self._script_name = script_name


    def run_test(self):
        super().run_test()
        print(f'Запуск автоматизированного скрипта: {self._script_name}')


    def __str__(self):
        parent_info = super().__str__()
        return f'{parent_info}\nСкрипт: {self.script_name}'


    @property
    def script_name(self):
        return self._script_name

