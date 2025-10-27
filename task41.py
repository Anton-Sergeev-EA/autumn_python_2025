# todo: Создайте иерархию классов для экспорта данных в разные форматы.
# Требования:
# Абстрактный базовый класс DataExporter:
#
# Методы:
# export(self, data) - абстрактный метод
# get_format_name(self) - возвращает название формата
# validate_data(self, data) - общий метод проверки данных (не пустые ли)
#
# Конкретные реализации:
# JSONExporter:
# Экспортирует данные в JSON-формат
# Добавляет поле "export_timestamp" с текущим временем
#
# CSVExporter:
# Экспортирует данные в CSV (если data - список словарей)
# Автоматически определяет заголовки из ключей первого элемента
#
# XMLExporter:
# Создает XML структуру с корневым элементом <report>
# HTMLExporter (дополнительно):
# Создает красивую HTML-таблицу с CSS-стилями


# Этот код должен работать после реализации:
#sales_data = [
    #{"product": "Laptop", "price": 1000, "quantity": 2},
    #{"product": "Mouse", "price": 50, "quantity": 10}
#]

# exporters = [
#     JSONExporter(),
#     CSVExporter(),
#     XMLExporter()
# ]
#
# for exporter in exporters:
#     print(f"Формат: {exporter.get_format_name()}")
#     exporter.export(sales_data)
#     print("---")

import json
import csv
from abc import ABC, abstractmethod
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom



class DataExporter(ABC):
    """Абстрактный базовый класс для экспорта данных."""

    @abstractmethod
    def export(self, data):
        """Абстрактный метод экспорта данных."""
        pass

    def get_format_name(self):
        """Возвращает название формата."""
        return self.__class__.__name__.replace('Exporter', '')

    def validate_data(self, data):
        """Проверяет, что данные не пустые и итерируемые."""
        if not data:
            raise ValueError("Данные не могут быть пустыми")
        if not hasattr(data, '__iter__'):
            raise ValueError("Данные должны быть итерируемым объектом")
        return True



class JSONExporter(DataExporter):
    """Экспортер данных в формат JSON."""

    def export(self, data):
        """Экспортирует данные в JSON с добавлением timestamp."""
        self.validate_data(data)

        export_data = {
            "data": data,
            "export_timestamp": datetime.now().isoformat()
        }

        json_str = json.dumps(export_data, indent=2, ensure_ascii=False)
        print(json_str)



class CSVExporter(DataExporter):
    """Экспортер данных в формат CSV."""

    def export(self, data):
        """Экспортирует список словарей в CSV-формат."""
        self.validate_data(data)

        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("Для CSV экспорта данные должны быть списком словарей")

        if len(data) == 0:
            print("Нет данных для экспорта")
            return

        fieldnames = data[0].keys()
        import sys
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)



class XMLExporter(DataExporter):
    """Экспортер данных в формат XML."""

    def export(self, data):
        """Создает XML структуру с корневым элементом <report>."""
        self.validate_data(data)

        root = ET.Element("report")
        root.set("export_timestamp", datetime.now().isoformat())

        for i, item in enumerate(data):
            if not isinstance(item, dict):
                raise ValueError("Каждый элемент данных должен быть словарем")

            record = ET.SubElement(root, "record")
            record.set("id", str(i))

            for key, value in item.items():
                field = ET.SubElement(record, key)
                field.text = str(value)

        rough_string = ET.tostring(root, 'unicode')
        reparsed = minidom.parseString(rough_string)
        pretty_xml = reparsed.toprettyxml(indent=" ")

        print(pretty_xml)



class HTMLExporter(DataExporter):
    """Экспортер данных в формат HTML с CSS-стилями."""

    def export(self, data):
        """Создает HTML-таблицу с CSS-стилями."""
        self.validate_data(data)

        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("Для HTML экспорта данные должны быть списком словарей")

        if len(data) == 0:
            print("<p>Нет данных для отображения</p>")
            return

        headers = list(data[0].keys())

        export_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Отчет</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #4CAF50;
            color: white;
        }}
        tr:hover {{
            background-color: #f5f5f5;
        }}
        .timestamp {{
            color: #666;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <h2>Отчет данных</h2>
    <p class="timestamp">Дата экспорта: {export_date}</p>
    <table>
        <thead>
            <tr>"""

        for header in headers:
            html += f"<th>{header}</th>"
        html += "</tr>\n        </thead>\n        <tbody>\n"

        for item in data:
            html += "        <tr>\n"
            for header in headers:
                html += f"            <td>{item.get(header, '')}</td>\n"
            html += "        </tr>\n"

        html += """        </tbody>
    </table>
</body>
</html>"""

        print(html)


if __name__ == "__main__":
    sales_data = [
        {"product": "Laptop", "price": 1000, "quantity": 2},
        {"product": "Mouse", "price": 50, "quantity": 10}
    ]

    exporters = [
        JSONExporter(),
        CSVExporter(),
        XMLExporter(),
        HTMLExporter()
    ]

    for exporter in exporters:
        print(f"Формат: {exporter.get_format_name()}")
        exporter.export(sales_data)
        print("---")
