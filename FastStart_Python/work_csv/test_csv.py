import csv

with open('file.csv', 'r') as f:
    reader = csv.reader(f)

    with open('new_test.csv', 'w') as file:
        writer = csv.writer(file, delimiter=';')

        for line in reader:
            writer.writerow(line)