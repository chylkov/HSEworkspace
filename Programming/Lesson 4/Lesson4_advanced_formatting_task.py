input_line = '(print (array 0 (mult 1000 500)) (file "out.txt" "and.txt" "about.bin"))'

space = '    '
count = 0
last_symbol = '('
last_position = 0
bracket_stack = []
for i in range(len(input_line)):
    if input_line[i] == '(':
        bracket_stack.append(('(', i))
    if input_line[i] == ')':
        bracket_stack.append((')', i))
print(bracket_stack)

for i in range(len(bracket_stack) - 1):
    if bracket_stack[i][0] == '(' and  bracket_stack[i+1][0]:
        print('\n' + space * count, end='')
        print(input_line[bracket_stack[i][1]:bracket_stack[i+1][1]], end='')
        count += 1
    if bracket_stack[i][0] == ')':
        print(')', end='')
        count -= 1