#  assignment 2
#  task 1
n = int(input('enter highest number of stars: '))
for i in range(n):
    print('*'*(i+1))
for i in range(n-1):
    print('*'*(n-i-1))

# task 2

word = input("Enter your word: ")
print(word)
print(word[::-1])