# read file
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method

f=open('file1.txt')
# # print(f.read())
# # f.close()
# print(f'cursor position - {f.tell()}')

# print(f.read())
# print(f.readline())
# print(f.readline(),end='')
# print(f'cursor position - {f.tell()}')
# print('before seek method')
# f.seek(0)
# print('after seek method')
# print(f.read())
# lines=f.readlines
# print(len(lines))
# for line in lines:
#     print(line,end='')
# f=open(r"G:\new_folder\file1.txt")
for line in f.readlines()[:2]:
    print(line,end='')
print(f.closed)
f.close()
print(f.closed)
