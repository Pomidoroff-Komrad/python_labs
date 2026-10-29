import csv
import json
from pathlib import Path


def read_csv(csv_path: str) -> list[list[str]]:
    """Читает CSV и проверяет заголовок и длину строк."""
    p = Path(csv_path)
    if p.suffix.lower() != '.csv':
        raise ValueError('Нужен CSV файл')

    with p.open(encoding='utf-8', newline='') as f:
        try:
            rows = list(csv.reader(f, strict=True))
        except csv.Error:
            raise ValueError('Неверный формат CSV') from None

    if not rows or not rows[0] or not any(rows[0]):
        raise ValueError('Пустой CSV или нет заголовка')
    header = rows[0]
    if any(not name.strip() for name in header) or len(set(header)) != len(header):
        raise ValueError('Заголовки должны быть непустыми и разными')
    for row in rows[1:]:
        if len(row) != len(header):
            raise ValueError('Все строки должны иметь одинаковую длину')
    if len(rows) < 2:
        raise ValueError('CSV-файл не содержит данных')
    return rows


def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразует список словарей из JSON в CSV."""
    p = Path(json_path)
    out = Path(csv_path)
    if p.suffix.lower() != '.json' or out.suffix.lower() != '.csv':
        raise ValueError('Нужны файлы JSON и CSV')

    with p.open(encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError('Неверный или пустой JSON') from None

    if not isinstance(data, list) or not data:
        raise ValueError('Пустой JSON или неподдерживаемая структура')

    header = []
    for row in data:
        if not isinstance(row, dict):
            raise ValueError('JSON должен содержать список словарей')
        for key, value in row.items():
            if not key.strip():
                raise ValueError('Название поля не должно быть пустым')
            if isinstance(value, (dict, list)):
                raise ValueError('Вложенные объекты и списки не поддерживаются')
            if key not in header:
                header.append(key)
    if not header:
        raise ValueError('В JSON нет полей')

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """Сохраняет строки CSV как список словарей в JSON."""
    out = Path(json_path)
    if out.suffix.lower() != '.json':
        raise ValueError('Нужен выходной файл JSON')
    rows = read_csv(csv_path)
    data = []
    for row in rows[1:]:
        data.append(dict(zip(rows[0], row)))

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    json_to_csv('data/samples/people.json', 'data/out/people_from_json.csv')
    csv_to_json('data/samples/people.csv', 'data/out/people_from_csv.json')
