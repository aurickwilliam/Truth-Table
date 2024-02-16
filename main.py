
# Printing the truth table
no_variables = int(input('Enter number of variables: '))

all_list = []
header_list = ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if no_variables > len(header_list):
    print('Too much Variable')
    quit()

# Formula: 2^n / 2
for col in range(no_variables):
    var = []
    value = 0
    for row in range(2 ** (col + 1)):
        no_val = (2 ** no_variables) // (2 ** (col + 1))
        for x in range(no_val):
            var.append(value)
        if value == 0:
            value = 1
        elif value == 1:
            value = 0
    all_list.append(var)

for header in range(no_variables):
    print('  ' + header_list[header] + '\t', end='')
print()
index = 0
for c in range(2 ** no_variables):
    print('  ', end='')
    for lst in all_list:
        print(str(lst[index]) + "\t  ", end='')
    print()
    index += 1
