snake_case = input("Введіть рядок у форматі snake_case: ")

words = snake_case.split("_")

capitalized_words = [word.capitalize() for word in words]

camel_case = "".join(capitalized_words)

print(f"Рядок у форматі capitalized camelCase: {camel_case}")