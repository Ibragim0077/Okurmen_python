# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1

#     return fib(n-1) + fib(n-2)

# print(fib(70))


# (x)def res(x):
#     if (x < 4):
#         print(x)
#         pec(x + 1)
#         print

# def palindrom(s) :
#     return palindrom(s [1:-1])

# print(palindrom("котяток"))
# s = "котятос"
# print(s == s[::-1])


# a = [1, 2, "Naryn", lambda a, b: print(a+b), 'Bro', True]
# print (a)
# print (a [3])
# print(a[3](2, 3))

# def say_name (name) :
#     print (f"Don't say ne goodbay, {name}!") 

#     def say_hello():
#         print("it Hello, name")
#     say_goodbay( )
#     say_hello()
# #say_name("Arsen")


# def say_name (name):
#     def say_900dbay():
#         print(f"Don't say me goodbay, (name)!")
#     return say_goodbay

# say = input ()
# a - say_name (say)
# a( )


# def say_name (name) :
#     return say_goodbay
# a = say_name ("Arsen")
# a ()


# def get_book (name) :
#     def get_author (author):
#         print (f"The book {name} - author {author}")

#     return get_author

# a = get_book("Harry Potter")
# a ("J.K. Rowling")

# def make_counter(n = 0):
#     def next():
#         nonlocal n
#         n += 1
#         return n
#     return next

# t_1 = make_counter ()
# t_2 = make_counter (10)
# print(t_1(), t_2())
# print(t_1(), t_2())
# print(t_1(), t_2())


def limited_calls(func, n):
def limit():
nonlocal n n -= 1
if n < 0:
print ("Limit reached")
else:
func ()
return limit
def func():
print ("Function was called")
a = Limited_calls(func=func, n=5)
a ()
a ()
a ()
a ()
























































