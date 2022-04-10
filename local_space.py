
a=1

def foo(): 
    print("w funkcji - przestrzen lokalna: ")
    print(globals())
    print(locals())

print("na poziomie modułu - przestrzeń globalna")
print(globals())
print(locals())

print()
foo()
