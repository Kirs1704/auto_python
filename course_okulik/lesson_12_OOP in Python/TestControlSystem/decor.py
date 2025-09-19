import functools

def log_test_execution(some_method):
    @functools.wraps(some_method)
    def wrapper(self, *args, **kwargs):
        method_name = some_method.__name__
        print(f"LOG: Начало выполнения '{method_name}' для {self.test_id}")
        result = some_method(self, *args, **kwargs)
        print(f"LOG: Завершение выполнения '{method_name}' для {self.test_id}")
        return result

    return wrapper