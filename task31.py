# todo: Извлеките IP-адреса всех запросов, которые завершились с ошибкой (
#  коды ответа 4xx или 5xx).

log_entries = [
    "192.168.1.1 - GET /home 200 1.2s",
    "192.168.1.2 - POST /login 404 0.8s",
    "192.168.1.3 - GET /profile 500 2.1s",
    "192.168.1.4 - GET /about 200 0.5s",
    "192.168.1.5 - POST /submit 403 1.5s"
]
def extract_error_ips(logs):
    error_ips = []
    for entry in logs:
        parts = entry.split()
        if len(parts) < 4:
            continue
        ip = parts[0]
        try:
            status_code = int(parts[-2])
        except ValueError:
            continue
        if 400 <= status_code <= 599:
            error_ips.append(ip)
    return error_ips

result = extract_error_ips(log_entries)
print(result)