import re

list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']


def verify_data(test_text, list_keys):
    # Проверка наличия открывающих и закрывающих скобок
    if test_text.count('{') != test_text.count('}'):
        raise ValueError('Ошибка: неверное количество открывающих и закрывающих скобок')

    # Извлекаем ключи из текста
    extracted_keys = re.findall(r'{([^}]+)}', test_text)

    # Проверка соответствия извлеченных ключей значениям из list_keys
    for key in extracted_keys:
        if key not in list_keys:
            raise ValueError(f'Ошибка: ключ "{key}" не соответствует значениям из list_keys')

    # Если все проверки пройдены, возвращаем текст
    return test_text


# Пример использования
Test_text = '''{name}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью '''

try:
    result = verify_data(Test_text, list_keys)
    print(result)
except ValueError as e:
    print(e)
