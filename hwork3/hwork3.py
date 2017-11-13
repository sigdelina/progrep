word = str(input('введите слово: ')) #Можно использовать и str для получения нужного результата
for i in range(1, len(word)+1):
    print(word[:i])
