from Lexer import *
from Interpreter import *
################################################################################
def PARSER(data,state,flag,end,count):
    n=len(data)
    if data!=[]:
        if (data[0]=="print" and flag==1 and state==1 and end==1) or(data[0]=="print" and count==0):
            return PRINT(data,state,flag,end,count,n)
        elif data[0]=="print":
            return 11,state,end,flag,count
        elif data[0]=="var" or data[0]=="let":
            #syntax=declaration(data)
            #if syntax:
            return DECLARATION(data,state,flag,end,count,n)
            #else:
               # return syntax,state,end,flag,count
        elif data[0]=="if":
            return IF(data,state,flag,end,count,n)
        elif data[0]=="else" and data[1]=="if":
            return ELSEIF(data,state,flag,end,count,n)
        elif data[0]=="else":
            return ELSE(data,state,flag,end,count,n)
        elif data[0]=="{":
            return LEFTCURLY(data,state,flag,end,count,n)
        elif data[0]=="}":
            return RIGHTCURLY(data,state,flag,end,count,n)
        elif data[1]=="=":
            return ASSIGN(data,state,flag,end,count,n)
        elif data[0]=="//":
            return 11,state,end,flag,count
    else:
        return 11,state,end,flag,count

################################################################################
'''
Grammar for declaration:
declaration->constant_declaration|variable_declaration
constant_declaration->var p1
variable_declaratioon->let p1
p1-> p1 EQUAL p2|DEC|DEC,p1
p2-> DEC|NUM
'''
def declaration(tokens):
    length=len(tokens)
    tokenslist={}
    tokenslist[tokens[0]]="KEYWORD"
    if tokens[0]=="let" or tokens[0]=="var":
        for i in range(1,length):
            if tokens[i]=="=":
                tokenslist[tokens[i]]="EQUAL"
            elif tokens[i].isnumeric() or type(tokens[i]) is float:
                tokenslist[tokens[i]]="NUM"
            elif tokens[i]==",":
                tokenslist[tokens[i]]="COMMA"
            else:
                tokenslist[tokens[i]]="DEC"
    if tokenslist[tokens[1]]=="," or tokenslist[tokens[length-1]]==",":
        return False
    for i in range(1,length):
        if tokenslist[tokens[i]]=="EQUAL":
            if tokenslist[tokens[i-1]]=="COMMA" or tokenslist[tokens[i+1]]=="COMMA":
                return False
            else:
                break
        elif tokenslist[tokens[i]]=="NUM":
            return False
        elif tokenslist[tokens[i]]=="DEC":
            if tokenslist[tokens[i+1]]=="DEC":
                return False
        elif tokenslist[tokens[i]]==",":
            if tokenslist[tokens[i+1]]==",":
                return False
    n=i-1
    for j in range(i+1,length):
        if tokenslist[tokens[i]]=="DEC" or tokenslist[tokens[i]]=="NUM":
            if tokenslist[tokens[i]]=="DEC" or tokenslist[tokens[i]]=="NUM":
                return False
        elif tokenslist[tokens[i]]==",":
            if tokenslist[tokens[i+1]]==",":
                return False
    m=length-(i+1)
    #print(tokenslist)
    '''if n==m:
        return True
    else:
        return False'''
                



################################################################################
def main():
    with open("Swift.swift","r") as fp: #takes input from Swift.swift file
        i=0
        check=11
        state=0
        flag=0
        end=1
        bracecount=0
        ifcount=elsecount=elifcount=count=0
        for line in fp:
            if(check==11):
                i+=1
                string=line.strip().split(' ')
                data=LEXER(string)
                #syntax=declaration(data)
                print(data)
                check,state,end,flag,count=PARSER(data,state,flag,end,count)
            elif check==False:
                print("Syntax error in line number ",i)
                break
            elif check==True:
                #print("in line ",i)
                break
            elif check==10:
                break

################################################################################
main()
################################################################################
