# while True:
#     reply = input('Enter text:')
#     if reply == 'stop':
#         break
#     else:
#         try:
#             num = int(reply)
#             print(int(reply)**2)
#         except:
#             print('Bad!'*8)
# print('bye')
# while True:
#     reply = input("Enter text:")
#     print(reply)
#     if reply == 'stop':
#         break
#     elif not reply.isdigit():
#         print('Bad!'*8)
#     else:
#         num = int(reply)
#         if num < 20:
#             print('low')
#         else:
#             print(num**2)
# print('Bye')  
[a,b,c] = (1,2,3)
print(a,c)
(a,b,c) = "ABC"
print(a,c)    
a = 1
print(a)  
for(a,b,c) in [(1,2,3),(4,5,6)] :
    print(a,b,c)
for((a,b),c) in [((1,2),3),((4,5),6)]:
    print(a,b,c)
#斐波那契数列
fibs = [0,1]
for i in range(8):
    fibs.append(fibs[-2]+fibs[-1])
print(fibs)
# fibs = [0,1]
# num = input('how many fibnacci numbers do you want?')
# for i in range(num):
#     fibs.append(fib[-2]-fib[-1])
# print(fibs)
# X = 'Spam'
# def func() :
#     X = 'NI!'
#     print(X)
# print(X)

# X = 'Spam'
# def func() :
#     X = 'NI'
#     print(X)
# func()
# print(X)

# X = 'Spam'
# def func() :
#     global X
#     X = 'NI'
# func()
# print(X)

