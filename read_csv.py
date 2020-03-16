import csv

with open('codigos.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # str1 = "Column names are {", ".join(row[0])}"
            line_count += 1
        else:
            str1 = "\tLado: %s, NFC: %s, QR: %s" % (row[0],row[1],row[2])
            print(str1)
            line_count += 1
    print('Processed {line_count} lines.')