def pao(f):
    def wrapper(recheio):
        print("(fatia superior pao)")
        f(recheio)
        print("(fatias inferior pao)")
    return wrapper

@pao
def lanche(recheio):
    print(f"{recheio}")
    print("queijo")
    print("hamburgue vegano")
    print("molho")

@pao
def opa(a):
    print(f"")


lanche("alface")
print("********************")
opa('')