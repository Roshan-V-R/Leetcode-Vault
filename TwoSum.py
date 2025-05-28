# #Brute Force method
# # def twosums(a,t):
# #     for i in range(len(a)):
# #         for j in range(i+1,len(a)):
# #             if a[i] + a[j] == t:
# #                 return[i,j]
# #
# a = [2,7,9,11]
# t = 9
#
#
# #Hash map method
# def twosums2(a,t):
#     seen = {}
#     for i,b in enumerate(a):
#         comp = t - b
#         if comp in seen:
#             return [seen[comp],i]
#         seen[b] = i
# print(twosums2(
# s = "10"*5
# print(s)
# a = 10
# A = 20
# print(a)

# a = 200
# b = 330
# if b > a:
#   print("b > a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")
c = 0
n = int(input("Number: "))
for i in range(1, n + 1):
    if n % i == 0:
        c += 1

if c == 2:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")



