from f2py_jit.finline import inline_source

src = open('interaction.f90').read()
print(src)
a = inline_source(src)
print(a)
