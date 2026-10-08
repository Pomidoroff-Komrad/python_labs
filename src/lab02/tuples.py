StudentRecord = tuple[str, str, float]

def format_record(rec: StudentRecord) -> str:
    if type(rec) != tuple:
        raise TypeError('Запись rec должна быть кортежем')
    if len(rec) != 3:
        raise ValueError('Запись rec должна содержать ровно 3 элемента')
    if type(rec[0]) != str or type(rec[1]) != str or type(rec[2]) != float:
        raise TypeError('ФИО и группа должны быть строками, а GPA — числом типа float')
    if rec[0].strip() == '':
        raise ValueError('ФИО не должно быть пустым')
    if rec[1].strip() == '':
        raise ValueError('Группа не должна быть пустой')
    if not 0.0 <= rec[2] <= 5.0:
        raise ValueError('GPA должен быть в диапазоне от 0 до 5')

    fio_parts = rec[0].split()
    if len(fio_parts) < 2 or len(fio_parts) > 3:
        raise ValueError('ФИО должно состоять из 2 или 3 слов')
    group = " ".join(rec[1].split())
    gpa = rec[2]

    surname = fio_parts[0][0].upper() + fio_parts[0][1:]
    initials = "".join(part[0].upper() + "." for part in fio_parts[1:])
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"


test_array_1 = [
    ("Иванов Иван Иванович", "BIVT-25", 4.6),
    ("Петров Пётр", "IKBO-12", 5.0),
    ("Петров Пётр Петрович", "IKBO-12", 5.0),
    ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
]
for record in test_array_1:
    print(format_record(record))
