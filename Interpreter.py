def PRINT(data,state,flag,end,count,n):
    if data[1]=="(" and data[-1]==")":
        if n==4:
            if data[2][0]=="\"" and data[2][-1]=="\"":
                print(data[2][1:-1])
            elif data[2] in sandy:
                print(sandy[data[2]])
            else:
                print(eval(data[2:-1]))
            return 11,state,end,flag,count
        else:
            c=""
            #print("ok")
            for i in range(2,n):
                if data[i][0]=="\"" and data[i][-1]=="\"":
                    print(data[i][1:-1])
                    continue
                elif data[i] in sandy:
                    c+=str(sandy[data[i]])
                elif data[i]!="," and data[i]!=")":
                    c+=data[i]
                    continue
                elif data[i]=="," or data[i]==")":
                    if c!="":
                        print(eval(c))
                        c=""
                        continue
                    else:
                        continue
            return 11,state,end,flag,count
    else:
        #print("Syntax error")
        return False,state,end,flag,count

def DECLARATION(data,state,flag,end,count,n):
    if data[1:]==[]:
        return False,state,end,flag,count
    elif data[1] in sandy:
        print(data[1]," already declared")
        return True,state,end,flag,count
    else:
        c=""
        for i in range(1,n):
            if data[i]=="=":
                c=""
            elif data[i] in sandy and i!=1:
                if data[i].isnumeric():
                    c+=str(sandy[data[i]])
                else:
                    c+='"'+sandy[data[i]]+'"'
            else:
                c+=data[i]
        sandy[data[1]]=str(eval(c))
        if data[0]=="var":
            variables[data[1]]=str(eval(c))
        elif data[0]=="let":
            constants[data[1]]=str(eval(c))
        return 11,state,end,flag,count

def IF(data,state,flag,end,count,n):
    c=""
    for i in range(1,n):
        if data[i] in sandy:
            c+=str(sandy[data[i]])
        elif data[i]=="{":
            count+=1
            flag=1
        elif data[i]=="}":
            count-=1
            flag=0
        elif data[i]=="&&":
            c+=" and "
        elif data[i]=="||":
            c+=" or "
        elif data[i]=="(" or data[i]==")":
            continue
        else:
            c+=data[i]
    try:
        if eval(c):
            state=1
            end=1
        else:
            state=0
            end=0
        return 11,state,end,flag,count
    except:
        print("variable not declared")
        return True,state,end,flag,count

def ELSEIF(data,state,flag,end,count,n):
    c=""
    for i in range(2,n):
        if data[i] in sandy:
            c+=str(sandy[data[i]])
        elif data[i]=="{":
            count+=1
            flag=1
        elif data[i]=="}":
            count-=1
            flag=0
        elif data[i]=="&&":
            c+=" and "
        elif data[i]=="||":
            c+=" or "
        elif data[i]=="(" or data[i]==")":
            continue
        else:
            c+=data[i]
    try:
        if eval(c):
            state=1
        else:
            state=0
        if end==1:
            return 11,0,end,flag,count
        else:
            if state==1:
                end=1
            return 11,state,end,flag,count
    except:
        print("variable not declared")
        return True,state,end,flag,count

def ELSE(data,state,flag,end,count,n):
    if n==1:
        if end==1:
            return 11,0,end,0,count
        else:
            return 11,1,1,0,count
    else:
        if data[1]=="{":
            count+=1
            flag=1
        if end==1:
            return 11,0,end,flag,count
        else:
            return 11,1,1,1,count

def LEFTCURLY(data,state,flag,end,count,n):
    flag=1
    count+=1
    return 11,state,end,flag,count

def RIGHTCURLY(data,state,flag,end,count,n):
    flag=0
    count-=1
    return 11,state,end,flag,count

def ASSIGN(data,state,flag,end,count,n):
    if data[0] in variables:
        c=""
        for i in range(0,n):
            if data[i]=="=":
                c=""
            elif data[i] in sandy and i!=0:
                if data[i].isnumeric():
                    c+=str(sandy[data[i]])
                else:
                    c+='"'+sandy[data[i]]+'"'
            else:
                c+=data[i]
        sandy[data[0]]=eval(c)
        return 11,state,end,flag,count
    elif data[0] in constants:
        print(data[0]," is immutable value")
        return 10,state,end,flag,count
    else:
        print(data[0]," not declared")
        return 10,count,end,flag,count

sandy={}
variables={}
forvar={}
constants={}
data1={}
