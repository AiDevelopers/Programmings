'''Question:-
We represent scores of batsmen across a sequence of matches in a two level dictionary as follows:

   {'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}
Each match is identified by a string, as is each player. The scores are all integers. The names associated with the matches are not fixed (here they are 'match1','match2','match3'), nor are the names of the players. A player need not have a score recorded in all matches.

Define a Python function orangecap(d) that reads a dictionary d of this form and identifies the player with the highest total score. Your function should return a pair (playername,topscore) where playername is a string, the name of the player with the highest score, and topscore is an integer, the total score of playername.

The input will be such that there are never any ties for highest total score.

For instance:

  >>> orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
('player3', 100)

  >>> orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}})
('Kohli', 120)
Let us consider polynomials in a single variable x with integer coefficients: for instance, 3x4 - 17x2 - 3x + 5. Each term of the polynomial can be represented as a pair of integers (coefficient,exponent). The polynomial itself is then a list of such pairs.

We have the following constraints to guarantee that each polynomial has a unique representation:

Terms are sorted in descending order of exponent
No term has a zero cofficient
No two terms have the same exponent
Exponents are always nonnegative
For example, the polynomial introduced earlier is represented as

  [(3,4),(-17,2),(-3,1),(5,0)]
The zero polynomial, 0, is represented as the empty list [], since it has no terms with nonzero coefficients.

Write Python functions for the following operations:

  
  addpoly(p1,p2)
  multpoly(p1,p2)
that add and multiply two polynomials, respectively.

You may assume that the inputs to these functions follow the representation given above. Correspondingly, the outputs from these functions should also obey the same constraints.

Hint: You are not restricted to writing just the two functions asked for. You can write auxiliary functions to "clean up" polynomials – e.g., remove zero coefficient terms, combine like terms, sort by exponent etc. Build a library of functions that can be combined to achieve the desired format.

You may also want to convert the list representation to a dictionary representation and manipulate the dictionary representation, and then convert back.

Some examples:

  >>> addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
  [(2, 1),(3, 0)]
Explanation: (4x3 + 3) + (-4x3 + 2x) = 2x + 3

  >>> addpoly([(2,1)],[(-2,1)])
  []
Explanation: 2x + (-2x) = 0

  >>> multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
  [(1, 3),(-1, 0)]
Explanation: (x - 1) * (x2 + x + 1) = x3 - 1

Sample Test Cases
Input	Output
Test Case 1	
orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
('player3', 100)
Test Case 2	
orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}})
('Kohli', 120)
Test Case 3	
addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
[(2, 1), (3, 0)]
Test Case 4	
addpoly([(2,1)],[(-2,1)])
[]
Test Case 5	
multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
[(1, 3), (-1, 0)]
Test Case 6	
multpoly([(2,1)],[(-2,1)])
[(-4, 2)]
Test Case 7	
orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
('player3', 100)
Test Case 8	
orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}})
('Kohli', 120)
Test Case 9	
orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91},'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}})
('Kohli', 120)
Test Case 10	
orangecap({'match1':{'player1':57, 'player2':38}})
('player1', 57)
Test Case 11	
addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
[(2, 1), (3, 0)]
Test Case 12	
addpoly([(2,1)],[(-2,1)])
[]
Test Case 13	
addpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
[(1, 2), (2, 1)]
Test Case 14	
multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
[(1, 3), (-1, 0)]
Test Case 15	
multpoly([(2,1)],[(-2,1)])
[(-4, 2)]
Test Case 16	
multpoly([(4,3),(3,0)],[(-4,3),(2,1)])
[(-16, 6), (8, 4), (-12, 3), (6, 1)]

'''

def orangecap(dict1):
    dict2 = {}
    for k1 in dict1:
        for k2 in dict1[k1]:
            dict2[k2] = dict2.get(k2, 0) + dict1[k1][k2]
    player = max(dict2, key=dict2.get)
    return player, dict2[player]
  
from collections import defaultdict
def addpoly(*polynoms):
    result = defaultdict(int)
    for polynom in polynoms:
        for factor, exponent in polynom:
            result[exponent] += factor
    return sorted([(coeff, exponent) for exponent, coeff in result.items() if coeff])

def multiply_terms(term_1, term_2):
    new_c = term_1[0] * term_2[0]
    new_e = term_1[1] + term_2[1]
    return (new_c, new_e)
  
def clearList(list):
  c=0
  for i in list:
    if i[0]==0:
      list.pop(c)
      clearList(list)
    c=c+1
  return list

  
def multpoly(p1, p2):
    
    result_poly = []
    for term_1 in p1:
        for term_2 in p2:
            result_poly.append(multiply_terms(term_1, term_2))
    collected_terms = []
    exps = [term[1] for term in result_poly]
    for e in exps:
        count = 0
        for term in result_poly:
            if term[1] == e:
                count += term[0]
        collected_terms.append((count, e))
    newList= clearList( collected_terms)
    return newList
import ast

def todict(inp):
    inp = ast.literal_eval(inp)
    return (inp)

def topairoflists(inp):
    inp = "["+inp+"]"
    inp = ast.literal_eval(inp)
    return (inp[0],inp[1])

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "orangecap":
   arg = todict(farg)
   print(orangecap(arg))
elif fname == "addpoly":
   (arg1,arg2) = topairoflists(farg)
   print(addpoly(arg1,arg2))
elif fname == "multpoly":
   (arg1,arg2) = topairoflists(farg)
   print(multpoly(arg1,arg2))
else:
   print("Function", fname, "unknown")
