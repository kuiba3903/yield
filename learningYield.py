def add(n):
    i = 0
    while i < n:
        k = yield i
        i += 1
        print(k,i)


a = add(100)
print(a)
a.send(None)
print(next(a))
print(a.send("hello world!"))
print(next(a))
print(a.send("hello2world"))
a.close()
print(a)

