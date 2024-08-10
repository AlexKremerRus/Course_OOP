for i in range(10):
    with open('file.txt', 'a+') as f:
        f.write('Hello World ')
        f.seek(0)
        data = f.read()
        # f.seek(-1)
print(data)