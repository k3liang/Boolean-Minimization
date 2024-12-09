import random

def gen_random_bitstring(length):
    return ''.join(random.choice('01') for i in range(length))

def gen_file(name, line_count, length):
    gen_minterms = set()

    with open(name, 'w') as file:
        while len(gen_minterms) < line_count:
            minterm = gen_random_bitstring(length)
            if minterm not in gen_minterms:
                gen_minterms.add(minterm)
                file.write(minterm + '\n')

if __name__ == "__main__":
    filename = input("Enter file name: ")
    line_count = input("Enter number of generated minterms: ")
    length = input("Enter number of variables: ")

    line_count = int(line_count)
    length = int(length)

    gen_file("tests/"+ filename, line_count, length)