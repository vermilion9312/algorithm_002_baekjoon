# https://www.acmicpc.net/problem/2309

n = 9
arr = [int(input()) for _ in range(n)]
arr.sort()

for i in range(n):
    for j in range(i + 1, n):
        for k in range(n):
            print(i, j, k)




# import sys

# n = 9
# a = [int(input()) for _ in range(n)]
# a.sort()
# for i in range(0, n):
#     for j in range(i + 1, n):
#         total = 0
#         for k in range(0, n):
#             if i == k or j == k:
#                 continue
#             total += a[k]
#         if total == 100:
#             for k in range(0, n):
#                 if i == k or j == k:
#                     continue
#                 print(a[k])
#             sys.exit(0)


# print("오답230418-2-1823")
# total = 0
# arr = []
# while True:
#     try:
#         height = int(input())
#         total += height
#         arr.append(height)
#     except:
#         break

# total -= 100
# arr2 = []

# for i in range(len(arr)):
#     total -= arr[i]

#     for j in range(len(arr)):
#         if i != j:
#             total -= arr[j]
#             if total == 0:
#                 arr2.append(arr[i])
#                 arr2.append(arr[j])
#                 break
#             else:
#                 total += arr[j]

#     if total == 0:
#         break
#     else:
#         total += arr[i]

# arr3 = []

# for v in arr:
#     if v not in arr2:
#         arr3.append(v)

# arr3.sort()

# for v in arr3:
#     print(v)
