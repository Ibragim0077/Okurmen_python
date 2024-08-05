# def func_show(func):
#     def wrapper(*args, **kwargs):
#         resurit = func(+args, **kwargs)
#         print(f"площвль прямогугольника: {resurit}")

#     return wrapper

# @func_show
# def get_sq(width, night):
#     return width * hight


# b, m = map(int, input().split())
# text = [i for i in input().split]
# grt_sq(n, m)



def show_menu (func) :
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(len( result)):
            print(f" {(i + 1)}. {result [i]}")
    return wrapper
@show_menu
def get_menu (menus) :
    return menus. split()

text = input ("Введите меню через пробел: ")
get_menu (text)

































