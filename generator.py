def csv_reader(file_name):
    with open(file_name, "r") as file:
        for row in file:
            yield row


def fibo():
    n1 = 0
    n2 = 1

    yield n1

    yield n2

    while True:
        buff = n1+n2
        n1 = n2
        n2 = buff
        yield n2


csv_gen = (row for row in open("generator_text.txt"))

print(type(csv_gen))

csv_gen2 = csv_reader("generator_text.txt")

print(type(csv_gen2))

print("GENERATOR 1\n\n")

for line in csv_gen:
    print(line)

print("GENERATOR 2\n\n")

for line in csv_gen2:
    print(line)

gen = fibo()
print(type(gen))
for i in range(10):
    print(next(gen))
