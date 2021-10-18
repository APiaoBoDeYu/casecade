# a = ["a", "b", "a", "c", "a", "c", "b", "d", "e", "c", "a", "c"]
# duixiang = set(a)
# d = {}
# for i in duixiang:
#     d[i] = a.count(i)
#
# a = sorted(d.items(), key=lambda x: x[1], reverse=True)
# print(a)

#
import pickle
from collections import Counter
f = open('./bin/test_20210805.pkl','rb')
objects=[]
info = pickle.load(f)
for file in info:
    for dec in file['detections']:
        objects.append(dec[5])

result=Counter(objects)
tag_dir={7:'JJXS_yybw',8:'XCXJ_BY3',9:'XCXJ_BY2',10:'NZXJ_yjh',11:'XCXJ_XS'}
print(result)
for i in result:
    print('%s:'%tag_dir[i]+'%s'%result[i])
print(f)

# def _not_divisible(n):
#     return lambda x: x % n > 0
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列
#
# primes()
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break


# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
# #
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
#
# for i in count():
#     print(i())

# import sys
# print(sys.path)
