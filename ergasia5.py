print("δωσε τις διαστασεις ορθωγωνιου")
l=int(input("πλατος:"))
p=int(input("μήκος:"))
arr=[]
m=(p*l)
k=0
z=0
sam=0
while z<=100:
 for i in range(l):
  col=[]
  arr.append(col)
  for j in range(p):
   if m%2==0:
    if k<(m//2):
     col.append("s")
     k+=1
    else:
     col.append("o")
   else:
     if k<((m//2)+1):
      col.append("s")
      k+=1
     else:
      col.append("o")
 #print(arr) 
 neo=[]
 for i in range(l):
    for j in range (p):
     neo.append(arr[i][j])
 #print(neo)
 import random
 random.shuffle(neo)
 #print(neo)
 tel=[]#φταιχνω καινουργιο λιστα εμφωλευμενη  στην οποια βαζω την neo 
 po=0
 for i in range(l): 
   mi=[]
   tel.append(mi)
   for j in range(p): 
    mi.append(neo[po])
    po+=1
   #print(mi,"\n")#kathe grammh gia elegxo
 fores1=0 
 fores2=0 
 for i in range(l):#ελεγχω τα orizontia  κουτακια αν και ποσα σοσ υπαρχουν
  for j in range(p):
   if j<=p-3:
    if tel[i][j]=="s" and tel[i][j+1]=="o" and tel[i][j+2]=="s":
      fores1+=1
 for j in range(p): #ελεγχω  ta katheta κουτακια αν και ποσα σοσ υπαρχουν
  for i in range(l):
   if i<=l-3:
     if tel[i][j]=="s" and tel[i+1][j]=="o" and tel[i+2][j]=="s":  
      fores2+=1
 dia=0 
 dia2=0    
 for i in range(l):
  for j in range(p):
   if i<=l-3 and j<=p-3:
    if tel[i][j]=="s" and tel[i+1][j+1]=="o" and tel[i+2][j+2]=="s":
      dia2+=1
    if i<=l-3 and j>=p-3: 
      if tel[i][j]=="s" and tel[i+1][j-1]=="o" and tel[i+2][j-2]=="s":   
       dia+=1
 #print("ta katheta:",fores2)  
 ##print("ta orizontia",fores1)
 #print(" diagonios:",dia)   
 #print(" diagonios:",dia2)
 sam+=(fores1+fores2+dia2+dia)
 z+=1
print("o mesos oros einai:",round(sam/100))