name = input("Введите имя: ").lower()
surname = input("Введите фамилию: ").lower()

print("Ваши данные:")
print(f"Имя: [{name}]")
print(f"Фамилия: [{surname}]")
print(f"Email (полный): [{name + "." + surname + "@school.ru"}]")
print(f"Email (короткий): [{name[:1] + "." + surname + "@school.ru"}]")
