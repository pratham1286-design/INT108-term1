def outer():
  x = "outer"
  def inner():
    nonlocal x
    x = "changed in inner"
  inner()
  print(x)

outer()