# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(input().rstrip())

phonebook={}

for i in range(n):
    input_arr=input().split()
    if len(input_arr) == 2:
        phonebook[input_arr[0]]=input_arr[1]

while True:
    try:
        name=input().rstrip()
        if name in phonebook:
            print(f'{name}={phonebook[name]}')
        else:
            print("Not found")
    except:
        break

