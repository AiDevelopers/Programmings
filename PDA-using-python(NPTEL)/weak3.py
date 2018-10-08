'''Question:-
Define a Python function descending(l) that returns True if each element in its input list is at most as big as the one before it. For instance:

  >>> descending([])
  True

  >>> descending([4,4,3])
  True

  >>> descending([19,17,18,7])
  False
A list of integers is said to be a valley if it consists of a sequence of strictly decreasing values followed by a sequence of strictly increasing values. The decreasing and increasing sequences must be of length at least 2. The last value of the decreasing sequence is the first value of the increasing sequence.

Write a Python function valley(l) that takes a list of integers and returns True if l is a valley and False otherwise.

Here are some examples to show how your function should work.

  >>> valley([3,2,1,2,3])
  True

  >>> valley([3,2,1])
  False

  >>> valley([3,3,2,1,2])
  False
A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix

  1  2  3
  4  5  6 
would be represented as [[1, 2, 3], [4, 5, 6]].

The transpose of a matrix makes each row into a column. For instance, the transpose of the matrix above is

  1  4  
  2  5
  3  6
Write a Python function transpose(m) that takes as input a two dimensional matrix using this row-wise representation and returns the transpose of the matrix using the same representation.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

  >>> transpose([[1,4,9]])
  [[1], [4], [9]]

  >>> transpose([[1,3,5],[2,4,6]])
  [[1, 2], [3, 4], [5, 6]]

  >>> transpose([[1,1,1],[2,2,2],[3,3,3]])
  [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
Sample Test Cases
Input	Output
Test Case 1	
descending([])
True
Test Case 2	
descending([4,4,3])
True
Test Case 3	
descending([19,17,18,7])
False
Test Case 4	
valley([2])
False
Test Case 5	
valley([13,12,14,14])
False
Test Case 6	
valley([5,4,3,2,1,2])
True
Test Case 7	
valley([17,1,2,3,4,5])
True
Test Case 8	
transpose([[19,14]])
[[19], [14]]
Test Case 9	
transpose([[21,33,11],[42,64,16]])
[[21, 42], [33, 64], [11, 16]]
Test Case 10	
transpose([[16,31,42],[26,82,73],[84,53,38]])
[[16, 26, 84], [31, 82, 53], [42, 73, 38]]
Test Case 11	
descending([4,4,4,4])
True
Test Case 12	
descending([4,3,2,1,2])
False
Test Case 13	
descending([3])
True
Test Case 14	
valley([5,4,3,2,1,2,3,4,5,4,3,2,1])
False
Test Case 15	
valley([5,5,3,2,3,4,5])
False
Test Case 16	
valley([5,4,3,2,1,1,2,3,4,5])
False
Test Case 17	
valley([2,1,2])
True
Test Case 18	
transpose([[1,2,3,4,5]])
[[1], [2], [3], [4], [5]]
Test Case 19	
transpose([[17,23,4,44],[11,12,17,18],[19,27,12,88]])
[[17, 11, 19], [23, 12, 27], [4, 17, 12], [44, 18, 88]]
Test Case 20	
transpose([[1],[2],[3],[4]])
[[1, 2, 3, 4]]


'''


def transpose(m):
  l=m
  c=l[0]
  lenght=len(c)
  x=0
  temp=[]
  new=[]
  for i in range(lenght):
  	
      for d in l:
          temp.append(d[i])
      
      new.append(temp)
      temp=[]
  return(new)

#next one
def descending(list):
    flag=0
    if(len(list)is 0):
        return True
    else:
        for i in range(0,len(list)):
            if(i>0 and list[i]<=list[i-1]):
                flag=flag+1
            
    if(flag is (len(list)-1)):
        return True
    else:
        return False



def valley(list):
    n=len(list)
    loc=list.index(min(list))
    
    if(n<5):
        return False
    elif(n is 0):
        return True
    flag=0
    flag1=0
    
    for i in range(0,n-1):
            if(list[i+1]<list[i] and i<loc):
                flag=flag+1
               

            elif(list[i]>list[i-1] and i>loc):
                flag1=flag1+1
            elif(list[i] is list[i+1]):
                return False
            
            else:
                flag1=flag1+1
                flag=flag+1
                
    if(list[n-1]>list[n-2] and list[n-1]>list[loc]):
        flag1=flag1+1
    elif(list[n-1]>list[n-2] and list[n-1]<=list[loc]):
        flag=flag+1
        
    if(flag>=2 and flag1>=2):
        return True
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "descending":
  arg = parse(farg)
  print(descending(arg))

if fname == "valley":
  arg = parse(farg)
  print(valley(arg))

if fname == "transpose":
  arg = parse(farg)
  print(transpose(arg))
