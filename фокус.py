import random
import os
zap = []
Big_S=list('ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЪЭЮЯ')
Low_S=list('abcdefghijklmnopqrstuvwxyzабвгдежзийклмнопрстуфхцчшщыьъэюя')
Num_SS=list('1234567890!@#$%^&*():;')
x = int (input(' x = : '))
svod=[]
pas=[]
while x==0:
 id = input('login : ')
 svod.append(id)
 

 bb=2
 lb=2
 nu=2
 
 p=""
 Pass=""
 Passa=""
 def serch():
     for i in range(len(svod)):
        if id == svod[i]:
           return True       
 def Big():
    for i in range(bb):
        global Pass
        n=random.randrange(len(Big_S))
        Pass=Pass+Big_S[n]
    return Pass

 def Low():
    for i in range(lb):
        global Pass
        n=random.randrange(len(Low_S))
        Pass=Pass+Low_S[n]
    return Pass

 def Num():
    for i in range(nu):
        global Pass
        n=random.randrange(len(Num_SS))
        Pass=Pass+Num_SS[n]
    return Pass

 def All():
    global Passa
    if bb>0:
        Passa=Big()
    if lb>0:
        Passa=Low()
    if nu>0:
        Passa=Num()
    Passr=list(Passa)
    random.shuffle(Passr)
    Passend=""
    for i in range(len(Passr)):
        Passend=Passend+Passr[i]
    return Passend
 q=All()
 pas.append(q)
 x=1
 print(svod)
 print(pas)
 print ('hello, ',id, 'your password is: ',q)
 x = int(input('чтобы продолжить нажми 0 '))
 

