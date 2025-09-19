import uuid

from decor import log_test_execution


class MyTestCase:
    ID_prefix = 'ТС -'

    def __init__(self, title, priority):
        self._title = title
        self._priority = priority
        self._status = 'Not started'
        self._test_id = MyTestCase.ID_prefix + str(uuid.uuid4())


    def __str__(self):
        return f'[{self.test_id}] - {self.title} -\nПриоритет: {self.priority}\nСтатус: {self.status}'

    # Блок с геттерами

    @property
    def test_id(self):
        return self._test_id

    @property
    def title(self):
        return self._title

    @property
    def priority(self):
        return self._priority

    @property
    def status(self):
        return self._status

    # Блок с сеттерами

    @priority.setter
    def priority(self, new_priority_value):
        valid_values = ("High", "Medium", "Low")
        if new_priority_value in valid_values:
             self._priority = new_priority_value
             print("Приоритет успешно изменен!")
        else:
            print(f'Недопустимое значение для поля "Priority". Используйте одно из предложенных: {valid_values}')

    @status.setter
    def status(self, new_status_value):
        valid_values = ("Not Started", "In Progress", "Passed", "Failed", "Blocked")
        if new_status_value in valid_values:
            self._status = new_status_value
            print("Статус успешно изменен!")
        else:
            print(f'Недопустимое значение для поля "Status". Используйте одно из предложенных: {valid_values}')


    # Публичные методы

    @log_test_execution
    def run_test(self):
        print(f"Запуск тест-кейса {self.test_id}: {self.title}")
        self.status = 'In Progress'

    @log_test_execution
    def complete_test(self, result: bool):
        if result:
            self.status = 'Passed'
            print(f'Тест-кейс {self.test_id} завершен со статусом: {self.status}')
        else:
            self.status = 'Failed'
            print(f'Тест-кейс {self.test_id} завершен со статусом: {self.status}')










