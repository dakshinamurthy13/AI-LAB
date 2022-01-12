combination = []
variable = {}

def generateCombination(n):
    comb=[]
    boolComb=[]
    booleanValue={"1":True,"0":False}
    for i in range(pow(2,n)):
        num=str(bin(i).replace("0b", ""))
        while len(num) < n:
            num = "0" + num
        comb.append([n for n in num])
    for c in comb:
        boolComb.append([booleanValue[t]for t in c])
    return boolComb

def generateVariable(n):
    v=dict()
    values="pqrstuvw"
    for i in range(n):
        v[values[i]]=i
    return v

kb = ''
q = ''

priority = {'~':3,'v':1,'^':2}

def input_rules():
    global kb,q,combination,variable
    n=int(input("Enter number of variables : "))
    combination=generateCombination(n)
    variable=generateVariable(n)
    print("Available variables")
    print(variable)
    print("Enter the kb according to the variables")
    kb = (input("Enter knowledge base :  "))
    q = (input("enter query :  "))

def _eval(i,val1,val2):
    if i=='^':
        return val2 and val1
    return val2 or val1


def evaluatePostfix(exp,comb):
    stack = []
    for i in exp:
        if isOperand(i):
            stack.append(comb[variable[i]])
        elif i == '~':
            val1 = stack.pop()
            stack.append(not val1)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(_eval(i,val1,val2))

    return stack.pop()

def toPostfix(infix):
    stack=[]
    postfix = ''
    for c in infix:
        if isOperand(c):
            postfix += c
        else:
            if isLeftParanthesis(c):
                stack.append(c)
            elif isRightParanthesis(c):
                operator = stack.pop()
                while not isLeftParanthesis(operator):
                    postfix += operator
                    operator = stack.pop()
            else:
                while (not isEmpty(stack)) and hasLessOrEqualPriority(c,peek(stack)):
                    postfix += stack.pop()
                stack.append(c)
    while (not isEmpty(stack)):
        postfix += stack.pop()
    return postfix


def entailment():
    global kb,q
    print('*'*10 + "Truth Table Reference" + '*'*10)
    print('kb','alpha')
    print('*'*10)
    for comb in combination:
        s = evaluatePostfix(toPostfix(kb),comb)
        f = evaluatePostfix(toPostfix(q),comb)
        print(s,f)
        print('-'*10)
        if s and not f:
            return False
    return True


def isOperand(c):
    return c.isalpha() and c!= 'v'

def isLeftParanthesis(c):
    return c=='('

def isRightParanthesis(c):
    return c==')'

def isEmpty(stack):
    return len(stack)==0

def peek(stack):
    return stack[-1]

def hasLessOrEqualPriority(c1,c2):
    try: return priority[c1]<=priority[c2]
    except KeyError: return False

input_rules()
ans = entailment()
if ans:
    print("Knowledge base entails query")
else:
    print("Knowledge base does not entail query")

# Test case 1
# Enter number of variables : 5
# Available variables
# {'p': 0, 'q': 1, 'r': 2, 's': 3, 't': 4}
# Enter the kb according to the variables 
# Enter knowledge base :  (~pv~qvr)^(~sv~tvq)^s^t^p
# enter query :  r
# **********Truth Table Reference**********
# kb alpha
# **********
# False False
# ----------
# False False
# ----------
# False False
# ----------
# False False
# ----------
# False True
# ----------
# False True
# ----------
# False True
# ----------
# False True
# ----------
# False False
# ----------
# False False
# ----------
# False False
# ----------
# False False
# ----------
# False True
# ----------
# False True
# ----------
# False True
# ----------
# False True
# ----------
# False False
# ----------
# False False
# ----------
# False False
# ----------
# False False
# ----------
# False True
# ----------
# False True
# ----------
# False True
# ----------
# False True
# ----------
# False False
# ----------
# False False
# ----------
# False False
# ----------
# False False
# ----------
# False True
# ----------
# False True
# ----------
# False True
# ----------
# True True
# ----------
# Knowledge base entails query

# Test case 2
# Enter number of variables : 3
# Available variables
# {'p': 0, 'q': 1, 'r': 2}
# Enter the kb according to the variables
# Enter knowledge base :  (~qv~pvr)^(~q^p)^q
# enter query :  r
# **********Truth Table Reference**********
# kb alpha
# **********
# False False
# ----------
# False True
# ----------
# False False
# ----------
# False True
# ----------
# False False
# ----------
# False True
# ----------
# False False
# ----------
# False True
# ----------
# Knowledge base entails query