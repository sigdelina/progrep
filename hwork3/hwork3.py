word = str(input('введите слово: ')) #Можно использовать str для получения нужного результата (выводится символ строки), так как в задании четко не сказано, что необходимо использовать list(тогда нужно будет извлекать элементы из list)
for i in range(1, len(word)+1):
    print(word[:i])