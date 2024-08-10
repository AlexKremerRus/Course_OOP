
# Открываем файл
file = open("file", mode='w+')
file.write("Hello World!")
file.seek(0)
# # Читаем содержимое файла
print(file.read())
# # Закрываем файл
file.close()

# work in image file
file_copy = open("copy.png", mode='wb+')
file_logo = open("test.png", mode='rb+')
# print(file_logo.read())
file_copy.write(file_logo.read())
file_logo.close()
file_copy.close()
