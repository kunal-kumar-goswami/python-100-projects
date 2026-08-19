def read_numbers_from_file(file_name):
    with open(file_name, 'r') as file:
        return [int(line.strip()) for line in file]

file1_content = read_numbers_from_file('/python/100 Days of Code/DAY 26/file1.txt')
file2_content = read_numbers_from_file('/python/100 Days of Code/DAY 26/file2.txt')

result = [num for num in file1_content if num in file2_content]

print(result)