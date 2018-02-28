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
            return DECLARATION(data,state,flag,end,count,n)
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
                #print(data,11)
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
