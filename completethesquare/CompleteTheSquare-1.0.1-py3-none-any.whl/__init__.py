from math import sqrt

class CompleteTheSquare:

  def __init__(self, equation):
    self._equation = equation

  @property
  def equation(self):
    return f"{self._equation}"
  
  @equation.setter
  def equation(self, equation):
    self._equation = equation
  
  def _split(self):
    eq = [each if each != " " else "" for each in self._equation]
    r = eq.index("x")
    one = eq[:r]
    t = eq.index("x", (len(one) + 1))
    
    r += 3
    two = eq[r:t]

    t += 1
    three = eq[t:]

    one = "".join(one) if "".join(one) != "" else 1
    two = "".join(two) if "".join(two) != "" else 1
    three = "".join(three) if "".join(three) != "" else 1
    return float(one), float(two), float(three)
  
  def _complete(self, a, b, c, mode="One"):
    fe = "(x" if mode == "One" else f"{a}(x"
    if b % 2 == 0:
      t = b // 2
      if t > 0:
        fe += f"+{t})²"
      else:
        fe += f"{t}"
    else:
      t = b / 2
      if t > 0:
        fe += f"+{t})²"
      else:
        fe += f"{t}"
    r = -t ** 2
    y = eval(f"{r}+{c}")
    if mode != "One":
      y *= a
    if y > 0:
      fe += f"+{y}"
    else:
      fe += f"{y}"
        
    return fe

  def _solve(self, eq):
    os = 0
    eq = [each if each != " " else "" for each in eq]
    t = eq.index("²")
    t += 1
    d = float("".join(eq[t:]))
    if d < 0:
      os += -d
    else:
      os -= d
    r = eq.index("(")
    try:
      rer = float("".join(eq[:r]))
      os /= rer
    except:
      pass
    os = sqrt(os)
    i = eq.index("x")
    i += 2
    o = eq.index(")")
    uh = float("".join(eq[i:o]))
    fo = -uh + os
    ft = uh + os
    return fo, ft

  def cts(self):
    a, b, c = CompleteTheSquare._split(self)
    
    if a == 1:
      fe = CompleteTheSquare._complete(self, a, b, c)
      return fe
    else:
      fe = "(x"
      if b % a == 0:
        bb = b // a
      else:
        bb = b / a
      if c % a == 0:
        cc = c // a
      else:
        cc = b / a
      fe = CompleteTheSquare._complete(self, a, bb, cc, "MOne")
      return fe
    
  def solve(self):
    fe = CompleteTheSquare.cts(self)
    sol, sol2 = CompleteTheSquare._solve(self, fe)
    return [sol, sol2]