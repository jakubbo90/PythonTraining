from sys import argv

program_name, first_arg, second_arg = argv

zdanie = first_arg
how_many_times = range(int(second_arg))

for element in how_many_times:
    print(zdanie)