x =int(input("δωσε μου την διασταση του τετραγωνου"))
tim=[]
for lok in range(0,99):
 tim.append(0)
er=0
sam=0 
tet=0
print("Οι θέσεις είναι:",x*x)
for fores in range(0,99):#apo 0 mexri 99 einai 100 fores
 m=(x*x)
 arr=[]
 rows, cols = (x,x)
 k=0 #μετρητης για να γεμισω τις μισες με μοναδες η τις μισες και μια 
 for i in range(cols): #φτιαχνω εμφψλευμενη λιστα με εμφωλευμενο λοοπ
  col=[]
  arr.append(col)
  for j in range(rows):
     if m%2==0:# ελεγχω αν ειναι μονος η ζυγος 
      if k<(m//2):#ελεγχω αν ειμαστε στα μισα η οχι 
       col.append(1)
       k+=1
      else:
       col.append(0)
     if m%2==1:
      if k<((m//2)+1):
       col.append(1)
       k+=1
      else:
       col.append(0)
 #print(arr)      
 neo=[]#φτιαχνω νεα λιστα ετσι ωστε να την γεμισω με τα μηδενικα και τις μοναδες 
 for i in range(cols):
   for j in range (rows):
    neo.append(arr[i][j]) 
 #print(neo)
 import random
 random.shuffle(neo)#ανακατευω τυχαια
 #print(neo)
 tel=[]#φταιχνω καινουργιο λιστα εμφωλευμενη  στην οποια βαζω την neo 
 po=0
 for i in range(rows): #φτιαχνω την εμφωλευμενη λιστα ακατεμενη τυχαια
  mi=[]
  tel.append(mi)
  for j in range(cols): 
   mi.append(neo[po])
   po+=1
   
 for i in range(rows):#για τα καθετα
  k=0
  for j in range(cols):
   if tel[i][j]==1:
     k+=1
     if k==4:
      tet+=1
   else:
     k=0
 for j in range(rows):#για τα οριζοντια
  k=0
  for i in range(cols):
   if tel[i][j]==1:
     k+=1
     if k==4:
      tet+=1
   else:
      k=0
 for i in range(rows):#αυτο ειναι για τους δυο διαγωνιους 
  k=0
  for j in range(cols):
   if i<=x-4 and j<=x-4:
     if tel[i][j] ==tel[i+1][j+1] and tel[i][j] ==tel[i+2][j+2] and tel[i][j] ==tel[i+3][j+3]  and tel[i][j] ==1: 
      tet+=1
   if i<=x-4 and j >=x-4:
     if tel[i][j] ==tel[i-1][j-1] and tel[i][j] ==tel[i-2][j-2] and tel[i][j] ==tel[i-3][j-3]and tel[i][j] ==1:
       tet+=1     
mo=(tet/100)
print("Ο Μέσος όρος τετράδων ειναι:",round(mo))



  

