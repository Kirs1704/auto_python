from course_okulik.lesson_12.TestControlSystem.MyTestCase import MyTestCase

class ManualTestCase(MyTestCase):
    def __init__ (self, title, priority, estimated_time_min):
        super().__init__(title, priority)
        self._estimated_time_min = estimated_time_min

    @property
    def estimated_time_min(self):
        return self._estimated_time_min


    def run_test(self):
        super().run_test()
        print(f"Начните ручное выполнение. Ожидаемое время: {self.estimated_time_min} мин.")


    def __str__(self):
        parent_info = super().__str__()
        return f'{parent_info}\nВремя: {self.estimated_time_min} мин'


