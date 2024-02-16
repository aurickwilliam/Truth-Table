
# Printing the truth table
no_variables = int(input('Enter number of variables: '))

all_list = []
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

for lst in all_list:
    for truth in lst:
        print(truth)
    print()
