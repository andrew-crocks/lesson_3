
input_str = input("Введите ваше имя, дату рождения и дату смерти, разделенные звездочкой: ")

name, birth_date, death_date = input_str.split("*")

birth_year = birth_date.split("-")[0]
death_year = death_date.split("-")[0]

age = int(death_year) - int(birth_year)

print(f"Name: {name}")
print(f"Age: {age} years")