f= open("ergasia.txt","r",encoding="utf8")
x=f.read()
import re
x2=re.sub('[^a-zA-Z]+', ' ', x)#χρησιμοποιω τηνν συναρτηση re για να αφησω το ascii αρχειο μονο με γραμματα
l=""
let=[]
for letter in x2:
 if letter==" ":#οποτε αλλαζει η λεξη την βαζω σε λιστα
  let.append(l)
  l=""
 else:
  l+=letter#προσθετω καθε γραμμα ετσι ωστε να δημιουργηθει η λεξη 
#print(let) #για ελεγχο! 
let2=[]
l=0
k=""
for i in range(len(let)):
 if len(let)-i>2:
  let2.append(let[i]+" "+let[i+1]+" "+let[i+2])#φτιαχνω τις τριαδες 
 
#print(let2)
import random
o=(random.choice(let2))#επιλεγω τυχαια τριαδα
#print(o)
destroy=0
lej=0
keim=""
while lej<200 or destroy==0:#loop mexri na dimioyrghso 200 λεξεις η μεχρι να μην μπορω να συνεζισω αλλο το κειμενο
 dd=0
 le=""   
 for t in o:
  if dd==1:
   le+=t
  if t==" ":
   dd=1
 q=0
 le1=""
 le2=""
 #print(le)#αυτeς ειναι οι 2 τελευεταιες λεξεις της τυχαις τριαδας
 con="false"#δεικτης ετσι ωστε οταν βρεθει η επομενη λεξη που θα βαλω στο κειμενο να μην γινονται οι εντολες απο τις 2 επαναληψεις ετσι ωστε να συνεχιζουμε για την καινουργια τριαδα που θα δημιουργηθει 
 for z in let2:#ψαχνω στην λιστα των τριαδων
  if con=="false":#αν βρεθηκε η επομενη λεξη δεν θα γινονται οι εντολες
   q=0
   le1=""
   le2=""
   le3=""
   for i in z:#ψαχνω μεσα στις 3 λεξεις και βρισκω τις 2 πρωτες να δω αν ειναι ισες με τις 2τελευταιεςι απο την τυχαι τριαδα
    if i==" ":
     q+=1
    if q==1:
     le2+=i
    if q==0:
     le1+=i
    if q==2:
     le3+=i
   first=le1+le2 
   from sys import intern
   if (intern(le)==intern(first)):#elegxo an einai iso 
       keim= keim + le3  
       lej+=1
       o= le + le3
       con="true"
   else:
    destroy=1 
print(keim)#to tixaio keimeno
print(lej)#oi lejeis 
