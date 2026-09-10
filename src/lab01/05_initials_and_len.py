FIO = input("ФИО: ")

lenth = sum([len(i) for i in FIO.split()]) + 2
initials = [i[0] for i in FIO.split()]

print(f"Инициалы: {"".join(initials)}")
print(f"Длина (символов): {lenth}")