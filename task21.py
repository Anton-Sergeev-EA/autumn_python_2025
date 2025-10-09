#todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# нужно сопоставить данные для подстановки. В итоге вместо "?" должны
# подставиться значения и получиться файл config.txt:

config_template = 'config_default.txt'
output_file = 'config.txt'

config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug': True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}


# Функция для форматирования значений
def format_value(value):
    if isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, bool):
        return str(value).capitalize()
    else:
        return str(value)


# Чтение шаблона и генерация нового файла
with open(config_template, 'r', encoding='utf-8') as infile, \
        open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        line = line.strip()
        
        # Пропускаем пустые строки и заголовки
        if not line or line.startswith('Конфигурация') or line.startswith(
                'Настройки'):
            outfile.write(f"{line}\n")
            continue
        
        # Разбиваем строку на ключ и значение
        if '=' in line:
            key, _ = line.split('=')
            key = key.strip()
            
            # Проверяем наличие ключа в словаре
            if key in config_values:
                formatted_value = format_value(config_values[key])
                outfile.write(f"{key:<15} =  {formatted_value}\n")
