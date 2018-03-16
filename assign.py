'''
Grammar for assigning statement
S->n=E
E->TB
B->+TB|-TB|epsilon
T->FC
C->*FC|/FC|epsilon
F->(E)|n
'''
symbols=["%","<",">",".","!",":","&","(",")","{","}","[","]","?","#",'"',"'",","]
#parsing the assignment statement
from Lexer import *
arb=[]
class parser():
    tk={}
    parsetable=[["S->n=E","","","","","","S->n=E"],["E->TB","","","E->TB","","",""],["","B->+TB","","","B->epsilon","B->epsilon",""],["T->FC","","","T->FC","","",""],["","C->epsilon","C->*FC","","C->epsilon","C->epsilon",""],["F->n","","","F->(E)","","",""]]
    terminal={}
    nonterminal={}
    def _init_(self):
        parser.terminal['n']=0
        parser.terminal['+']=1
        parser.terminal['*']=2
        parser.terminal['(']=3
        parser.terminal[')']=4
        parser.terminal['$']=5
        parser.terminal['=']=6
        parser.nonterminal['S']=0
        parser.nonterminal['E']=1
        parser.nonterminal['B']=2
        parser.nonterminal['C']=3
        parser.nonterminal['F']=4
        parser.nonterminal['T']=5
    def map1(self,tok):
        n=len(tok)
        parser.tk['+']='+'
        parser.tk['*']='*'
        parser.tk['(']='('
        parser.tk[')']=')'
        parser.tk[')']='='
        for i in tok:
            if i!='+' or i!='*' or i!='(' or i!=')' or i!='=' or i!='-' or i!='/':
                if i in symbols:
                    parser.tk[i]='n'
                else:
                    return False
    def check(self,tok):
        if tok[1]!='=':
            return False
    def parse(self,tok):
        try:
            st=[]
            index=0
            st.insert(0,"$")
            st.insert(0,'S')
            a=parser.tk[tok[0]]
            x=st[0]
        except:
            return False
        while x!="$":
            if a=="@":
                print("Variable can't start with @")
                return False
            elif x==a:
                index+=1
                st.pop()
                if index==len(a):
                    return True
                a=tok[index]
            elif 65<=ord(a)<=91:
                print("error")
                return False
            elif parser.parsetable[parser.nonterminal[x]][parser.terminal[a]]=="":
                print("parsing error")
                return False
            else:
                string=parser.parsetable[parser.nonterminal[x]][parser.terminal[a]][3:]
                for k in string[::-1]:
                    st.insert(0,k)
            x=st[0]
        print("no match")
        return False
a=input().strip().split(' ')
arb=arb+LEXER(a)
#if a[0]=="if" or a[0]=="for":
while 1:
    a=input().strip().split(' ')
    if a[0]=="end":
        break
    arb=arb+LEXER(a)
f=parser()
f.map2(arb)
print(f.parse(arb))
#parser.py

                
                
        
        
