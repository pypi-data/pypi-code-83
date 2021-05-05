import ast
code = """
#x = y[3]
#y = [0] * 4
#z = x * y
#print("hello")
#if z < 5:
#   a = z[0:1]
#for i in range(0,5):
#    a = 0b10
def test():
    x = 'hello'
    print (5)
x.eq(5)
"""
code = """
if x: 5
else:
    if y: foo
"""

code = """
#x()[5:3] = 4
#x(fred=foo)
#x = [0] * 4
#GPR[5] = 0
x = GPR[r][32:63]
"""

xcode = """
if x in [5]:
    print(3)
"""

code = """
range(7,-1,-1)
"""

code = """
CR[5] = CR[5:3]
"""

tree = ast.parse(code)
print (ast.dump(tree))
print(tree)
import astor
print (astor.dump_tree(tree))
#print (astor.dump_tree(tree.body[0].body[1]))
#print (tree.body[0].value)
#print (tree.body[0].value.n)
x = ast.Constant(5)
print (dir(x))
