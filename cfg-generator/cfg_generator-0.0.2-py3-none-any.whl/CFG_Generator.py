from sys import argv
from random import random, sample
from math import exp, pi, sqrt
from numpy.random import chisquare, normal

__extra_productions = 2
__number_non_terminals = 0
__terminal_ratios = 0.0
__productions_length = 1
__tree_depth = 0

def generate_grammar(number_non_terminals = None,
                extra_productions = None,
                terminal_ratios = None,
                productions_length = None,
                tree_depth = None):
  global __extra_productions
  global __number_non_terminals
  global __terminal_ratios
  global __productions_length
  global __tree_depth

  df = 1 + int(random() * 20)
  
  if number_non_terminals is None:
    number_non_terminals = 2 + int(chisquare(df, 1)[0])
  __number_non_terminals = number_non_terminals

  if extra_productions is None:
    extra_productions = int(chisquare(1 + df // 2, 1)[0])
  __extra_productions = extra_productions

  if terminal_ratios is None:
    terminal_ratios = normal(1, 0.2)
  __terminal_ratios = terminal_ratios

  if productions_length is None:
    productions_length = 1 + int(normal(4, 2))
  __productions_length = productions_length

  if tree_depth is None:
    tree_depth = 1 + int(chisquare(1 + df // 4, 1)[0])
  __tree_depth = tree_depth
  
  s = __number_non_terminals
  t = s / __terminal_ratios

  s = round(s) 
  t = round(t)

  t = t if t > 0 else 1

  prcount = s + __extra_productions

  nts, ts = __gen_terminals(s, t)
  prs = __gen_productions(prcount, nts, ts)

  return nts, ts, prs

'''
Generates the Non-terminals and Terminal symbols to be used in the Grammar

Converts the integer value provided into a base 26 number, and this number is
directly mapped onto the arabic [A-Za-z] alphabet
'''
def __gen_terminals(nt, t):
  nts = []
  ts = []

  def base_10_to_26(base10):
    value = []
    rem = base10
    while True:
      val = rem // 26
      value.insert(0, rem % 26)
      rem = val
      if rem == 0:
        break

    return value

  def recursive_add(depth, max, symbol, base, array):
    if depth == max:
      array.append(symbol)
      return
    for a in range(26):
      recursive_add(depth + 1, max, symbol + chr(base + a), base, array)

  nt_base26 = base_10_to_26(nt)
  for col, val in enumerate(nt_base26):
    for i in range(val):
      recursive_add(col + 1, len(nt_base26), chr(65 + i), 65, nts)
      
  t_base26 = base_10_to_26(t)
  for col, val in enumerate(t_base26):
    for i in range(val):
      recursive_add(col + 1, len(t_base26), chr(97 + i), 97, ts)

  return nts, ts

'''
Generates the productions for the CFG

First generates a graph, that will determine which productions go where in the context free
grammar. This graph has the origin, the start symbol on top, which branches out to all other nodes,
other non-terminal symbols, to create the CFG. This function creates the nodes of the graph and 
assigns them to a certain level in the tree
'''
def __gen_productions(prcount, nts, ts):
  global __tree_depth
  if __tree_depth > len(nts) - 1:
    __tree_depth = len(nts) - 1

  levels = [[] for i in range(__tree_depth + 1)] 
  final_alloc = [[] for i in range(__tree_depth + 1)]
  
  poss = []
  # pr_start = 0
  # nt_no = 0

  intervals = [1 for i in range(__tree_depth + 1)]
  for i in range(__tree_depth + 1, prcount):
    index = int(__get_no(__tree_depth) * __tree_depth) + 1
    intervals[index] = intervals[index] + 1

  x = 0
  for index, count in enumerate(intervals):
    for i in range(x, x + count):
      levels[index].append(i)
      if (len(levels[index]) > 1) and not (index in poss):
        poss.append(index)
    x = x + count

  intervals = [1 for i in range(__tree_depth + 1)]
  for i in range(__tree_depth + 1, len(nts)):
    index = poss[int(__get_no(__tree_depth) * len(poss))]
    intervals[index] = intervals[index] + 1
    if intervals[index] == len(levels[index]):
      poss.remove(index)

  x = 0
  for index, count in enumerate(intervals):
    for i in range(x, x + count):
      final_alloc[index].append(i)
    x = x + count

  return __gen_production_tree(prcount, final_alloc, levels, nts, ts)

'''
Creates the different edges in the graph, or the connections between productions in the CFG 
'''
def __gen_production_tree(prcount, final_alloc, levels, nts, ts):
  adj_matrix = [[] for i in range(prcount)]
  for i in range(prcount):
    for i in range(prcount):
      adj_matrix[i].append(0)

  final_assignments = [-1] * prcount

  for i in range(0, __tree_depth + 1):
    for j in range(len(final_alloc[i])):
      nt = final_alloc[i][j]
      pr = levels[i][j]

      final_assignments[pr] = nt

  for i in range(__tree_depth, 0, -1):
    for to_index, j in enumerate(final_alloc[i]):

      others = int(__get_no(i / 2.0) * len(final_alloc[i - 1]))
      for o in range(others + 1):
        from_index = int(random() * len(final_alloc[i - 1]))

        start = levels[i - 1][from_index]
        end = levels[i][to_index]
        adj_matrix[start][end] = 1

  prs = [ "" for i in range(prcount) ]

  for index in range(prcount):
    a = final_assignments[index]
    row = adj_matrix[index]
    if a == -1:
      continue

    r = __gen_rule_from_tree(nts[a], nts, ts, row, final_assignments)
    prs[index] = r

  indices = []

  for i in range(__tree_depth, 0, -1):
    for start in levels[i]:
      if not final_assignments[start] == -1:
        continue

      indices.append(start)
      index = sample(final_alloc[i], 1)[0]
      final_assignments[start] = index

      others = int((1 - __get_no(__tree_depth * 3)) * __tree_depth) + 1
      for o in range(others):
        end = int(__get_no(__tree_depth) * prcount)
        adj_matrix[start][end] = 1
        
  for index in indices:
    r = __gen_rule_from_tree(nts[final_assignments[index]], nts, ts, 
        adj_matrix[index], final_assignments)
    prs[index] = r

  prs.sort()
  return prs

'''
Uses the adjacency matrix generated for the graph to generate the productions for hte CFG. The productions
for each of the CFG must have a rule relating it to the production corresponding to the adjacent node in the graph
'''
def __gen_rule_from_tree(pr, nts, ts, vertices, nodes):
  non_terminals = []

  indices = [i for i, j in enumerate(vertices) if j == 1]
  [non_terminals.append(nts[nodes[i]]) for i in indices if nts[nodes[i]] not in non_terminals]

  if len(non_terminals) == 0:
    r = random()
    if r < 1.25 - exp(1.6 / nts.index(pr)):
      rule = ['#']
    else:
      df = __get_def(nts.index(pr))
      rule = __gen_t_only(ts, df)
  else:
    r = random()
    if r < 0.6:
      df = __get_def(len(non_terminals) / 2.0)
      rule = __gen_nt_only(pr, non_terminals, df)
    else:
      df = __get_def(len(nts) - nts.index(pr))
      rule = __gen_mixed(pr, non_terminals, ts, df)

  return [pr, rule]

'''
Generate a production consisting of only terminal symbols, given a list of terminal symbols
'''
def __gen_t_only(ts, df):
  n = __get_prob(df)
  if n > 50:
    n = 50

  terminals = []
  for i in range(n):
    terminals.append(ts[int(random() * len(ts))])

  rule = []
  for t in terminals:
    rule = rule + [t]
  return rule

'''
Generate a production consisting of only non-terminal symbols, given a list of non-terminal symbols
'''
def __gen_nt_only(pr, nts, df):
  n = __get_prob(df)
  if n > 50:
    n = 50
  
  nterminals = []

  for i in range(len(nts), n):
    nterminals.append(nts[int(random() * len(nts))])

  rules = []
  for nt in nts:
    rules.append(nt)

  for t in nterminals:
    rules.append(t)

  return rules

'''
Generate a production consisting of a mix of terminal and non-terminal symbols, given a list of terminal and
non-terminal symbols
'''
def __gen_mixed(pr, nts, ts, df):
  
  x1 = __terminal_ratios * 1.0 / (__terminal_ratios + 1)
  x2 = 1

  rules = []
  for nt in nts:
    rules += [nt]
  
  n =  __get_prob(df)
  if n > 50:
    n = 50

  for i in range(len(nts), n):
    r = random()
    if (r < x1):
      r = int(random() * len(nts))
      p = nts[r]
      if n == 1:
        if p == pr:
          p = nts[r - 1]
      rules += [p]
    else:
      rules += sample(ts, 1)

  return rules

def __get_def(i):
  return 1 + i * __productions_length / 4

def __get_no(d):
  h1 = 1.0 / (1 + d)
  h2 = 2 - h1
  m = h2 - h1
  r = random()

  if m == 0:
    x =  r
  else:
    x =  sqrt((2 * r / m) + (h1 / m) ** 2) - h1 / m

  return x

def __get_prob(df):
  x = int(normal(df, df / 5, 1)[0])
  if x < -1:
    x = -1
  return 1 + x

def print_grammar(nts, ts, prs):
  non_terminals = "Non-terminals:"
  for nt in nts:
    non_terminals += " " + nt

  terminals = "Terminals:"
  for t in ts:
    terminals += " " + t

  print(non_terminals)
  print(terminals)
  print("Context Free Grammar:")
  for pr in prs:
    production = ""
    for p in pr[1]:
      if p in nts:
        production += " {}".format(p)
      else:
        production += " '{}'".format(p)
    print("{} ->{}".format(pr[0], production))