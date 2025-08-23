#ДАН СПИСОК ЦЕН НА ТОВАРЫ В ДОЛЛАРАХ И ОТНОШЕНИЕ К КУРСУ ЕВРО
#С ПОМОЩЬЮ ФУНКЦИИ map() ПРЕОБРАЗУЕМ ДАННЫЕ ЦЕНЫ В ВАЛЮТУ ЕВРО
prices_in_usd = [10, 20, 30, 40, 50]
exchange_rate = 0.85

prices_in_euro = list(map(lambda x: round(x * exchange_rate, 2), prices_in_usd))



#ФУНКЦИЯ, КОТОРАЯ С ПОМОЩЬЮ filter() ПРИВОДИТ НОМЕР К ЭДИНОМУ ФОРМАТУ: 1234567890
#С ПОМОЩЬЮ map() СОХРАНЯЕМ РЕЗУЛЬТАТ
phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']

def format_phone_number(number):
   return ''.join(filter(str.isdigit, number))

formatted_numbers = list(map(format_phone_number, phone_numbers))

print(formatted_numbers)
#\['1234567890', '1234567890', '1234567890', '1234567890', '1234567890']



#ФУНКЦИЯ, КОТОРАЯ ПРИНИМАЕТ СПИСОК БАГОВ И ВОЗВРАЩАЕТ СПИСОК БАГОВ ТОЛЬКО С ВЫСОКОЙ СЕРЬЕЗНОСТЬЮ('high')
bugs = [
   {"id": 1, "description": "Баг №1", "severity": "low"},
   {"id": 2, "description": "Баг №2", "severity": "medium"},
   {"id": 3, "description": "Баг №3", "severity": "high"},
   {"id": 4, "description": "Баг №4", "severity": "high"},
]

def filter_high_severity(bugs):
    return list(filter(lambda bug: bug["severity"] == "high", bugs))

print(filter_high_severity(bugs))



#ФУНКЦИЯ, КОТОРАЯ ПРИНИМАЕТ СПИСОК ТЕСТОВЫХ КЕЙСОВ И ВОЗВРАЩАЕТ ТОЛЬКО ТЕСТОВЫЕ КЕЙСЫ ТИПА 'API'
test_cases = [
   {"id": 1, "description": "Тест №1", "type": "UI"},
   {"id": 2, "description": "Тест №2", "type": "API"},
   {"id": 3, "description": "Тест №3", "type": "API"},
   {"id": 4, "description": "Тест №4", "type": "Performance"},
]

def filter_api_tests(test_cases):
    return list(filter(lambda test_case: test_case["type"] == "API", test_cases))

print(filter_api_tests(test_cases))



#ФУНКЦИЯ, КОТОРАЯ ПРИНИМАЕТ ОБА СПИСКА И ВОЗВРАЩАЕТ СПИСОК КОРТЕЖЕЙ, ГДЕ КАЖДЫЙ КОРТЕЖ СОДЕЖРИТЬ ИМЯ ИНЖЕНЕРА И ЕГО ЗАДАЧУ
engineers = ["Анна", "Иван", "Елена", "Олег"]
tasks = ["Тестирование UI", "Тестирование API", "Написание тестовых сценариев"]

def assign_tasks_to_engineers(engineers, tasks):
    return list(zip(engineers, tasks))

print(assign_tasks_to_engineers(engineers, tasks))



#ФУНКЦИЯ, КОТОРАЯ ПРИНИМАЕТ ОБА СПИСКА И ВОЗВРАЩАЕТ СПИСОК БУЛЕВЫХ ЗНАЧЕНИЙ, ПОКАЗЫВАЮЩИЙ, СОВПАДАЕТ ЛИ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ С ФАКТИЧЕСКИМ ДЛЯ КАЖДОГО ТЕСТА
expected_results = ["pass", "fail", "pass", "pass"]
actual_results = ["pass", "pass", "pass", "fail"]

def compare_test_results(expected, actual):
   return [exp == act for exp, act in zip(expected, actual)]

print(compare_test_results(expected_results, actual_results))



#ФУНКЦИЯ ДОЛЖНА ВЕРНУТЬ True, ЕСЛИ ХОТЯ БЫ ОДИН ИЗ ТЕСТОВЫХ КЕЙСОВ ЗАВЕРШИЛСЯ С РЕЗУЛЬТАТОМ 'fail'
#ФУНКЦИЯ ДОЛЖНА ВЕРНУТЬ True, ЕСЛИ ВСЕ ТЕСТОВЫЕ КЕЙСЫ ЗАВЕРШИЛИЬ С РЕЗУЛЬТАТОМ 'pass' или 'skip'
test_results = ["pass", "pass", "skip", "fail", "pass"]

#если хотя бы один завершился с результатом 'fail'
def has_failures(test_results):
    return any(result == "fail" for result in test_results)

print(has_failures(test_results))

#если все кейсы завершились с результатом 'pass' или 'skip'
def all_passed_or_skipped(test_results):
    return all(result in ["pass", "skip"] for result in test_results)

print(all_passed_or_skipped(test_results))