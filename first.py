def outer():
  x = "outer"
  def inner():
    nonlocal x
    x = "changed in inner"
  inner()
  print(x)

outer()
num=int(input("Enter a number: "))
a=10
b=10
print(id(a))
print(id(b))
