EILENAME = 'work_with_filers.txt'

file = open(EILENAME, encoding='itf-8')
print(file.readline(), end='')
print(file.readline(), end='')


for line in file:
    print(line, end='')