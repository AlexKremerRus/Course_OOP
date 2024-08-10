import os

print(os.getcwd()) # текущая директория
os.chdir('work_csv') # переход в папку work_csv
print(os.getcwd())

os.mkdir('new_dir_test') # создание директории

os.chdir(os.getcwd() + os.sep + 'new_dir_test') # переход в папку new_dir_test os.sep - разделитель для разных операционных систем

print(os.listdir(os.getcwd())) # список файлов в текущей директории

os.makedirs('mk/dirs/test')

os.removedirs('mk/dirs/test') # удаление директории и если директория выше пустая то удаляет и ее

os.rename('test.txt', 'test_2.txt') # переименование файла или директории

os.remove('test_2.txt') # удаление файла

# обход по директориям
for path, dirs, files in os.walk(os.getcwd()):
    print('path: ', path)
    print('dirs: ', dirs)
    print('files: ', files)
    print('-----------------------------------')

print(os.path.exists('work_csv'))  # проверка существования файла/директории
