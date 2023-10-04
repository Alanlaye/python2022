#使用函数：
def print_models(un_m,co_m):
    while un_m:
        cu_m = un_m.pop()
        print("Printing model: "+cu_m)
        co_m.append(cu_m)
def show(co_m):
    print("\nThe following models have been printed:")
    for co in co_m:
        print(co)
un_m = ['iphone case', 'robot pendant', 'dodecahedron']
co_m = []
print_models(un_m,co_m)
show(co_m)
