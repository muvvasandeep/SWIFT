def LEXER(swift):
    keywords=["associatedtype","class","deinit","enum","extension","fileprivate","func","import","init","inout","internal","let","open","operator","private","protocol","public","static","struct","subscript","typealias","var","break","case","continue","default","defer","do","else","fallthrough","for","guard","if","in","repeat","return","switch","where"," while","as","Any","catch","false","is","nil","rethrows","super","self","Self","throw","throws","true","try","_","#available","#colorLiteral","#column","#else","#elseif","#endif","#file","#fileLiteral","#function","#if","#imageLiteral","#line","#selector"," #sourceLocation","associativity","convenience","dynamic","didSet","final","get","infix","indirect","lazy","left","mutating","none","nonmutating","optional","override","postfix","precedence","prefix","Protocol","required","right","set","Type","unowned","weak","willSet"]
    operators=["+","-","/","%","<",">","*",".","!",":","&","(",")","{","}","[","]","-","?","#","=",'"',"'"]
    op=["(",")","{","}","[","]","'",'"']
    separators=[",",";"]
    special_operators=["++","--","+=","-=","*=","/=","==","<=",">=","!=","..<","...","&&","||"]
    special=["\n","\t","\0"]
    comments=["//"]
    tokens=[]
    methods=["print"]
    keywords_list=[]
    operators_list=[]
    separators_list=[]
    special_list=[]
    methods_list=[]

    for i in swift:
        if i in comments:
            #print(i)
            break
        elif i in keywords:
            tokens.append(i)
            keywords_list.append(i)
            #print(i,"->keyword")
        elif i in operators:
            tokens.append(i)
            operators_list.append(i)
            #print(i,"->operator")
        elif i in separators:
            tokens.append(i)
            separators_list.append(i)
            #print(i,"->separator")
        elif i in methods:
            #print(i,"->methods")
            methods_list.append(i)
            tokens.append(i)
        elif i in special:
            tokens.append(i)
            special_list.append(i)
            #print(i,"->special")
        else:
            num=len(i)
            swift=i
            j=0
            while j<num:
                variable=''
                if swift[j].isdigit() or swift[j].isalpha() or swift[j]=="_" or swift[j]=='"' or swift[j]=="'" or swift[j]==".":
                    while swift[j].isdigit() or swift[j].isalpha() or swift[j]=="_" or swift[j]=='"' or swift[j]=="'" or swift[j]==".":
                        variable+=swift[j]
                        j+=1
                        if j==num:
                            break
                    if variable in keywords:
                        tokens.append(variable)
                        keywords_list.append(variable)
                        #print(variable,"->keyword")
                        continue
                    elif variable in methods:
                        #print(variable,"->methods")
                        methods_list.append(variable)
                        tokens.append(variable)
                        continue
                    else:
                        tokens.append(variable)
                        keywords_list.append(variable)
                        #print(variable,"->identifier")
                        continue
                elif swift[j] in separators:
                    tokens.append(swift[j])
                    separators_list.append(swift[j])
                    #print(swift[j],"->separator")
                    j+=1
                    continue
                elif swift[j] in operators:
                    operator=''
                    if swift[j] in op:
                        tokens.append(swift[j])
                        operators_list.append(swift[j])
                        #print(swift[j],"->operator")
                        j+=1
                        continue
                    while swift[j] in operators:
                        operator+=swift[j]
                        j+=1
                        if j==num:
                            break
                    if operator in special_operators or operator in operators:
                        tokens.append(operator)
                        operators_list.append(operator)
                        #print(operator,"->operator")
                    elif operator in comments:
                        tokens.append(operator)
                    else:
                        tokens.append(operator[0])
                        j-=1
                        #print(operator[0],"->operator")
                else:
                    #print("error")
                    #break
                    j+=1
                    continue
    #print(tokens)
    #print(keywords_list)
    #print(operators_list)
    #print(separators_list)
    return tokens
