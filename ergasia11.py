userinput=input("Δώσε το όνομα του αρχείου που θέλεις...!")
myfile=open(userinput)
info=myfile.readlines()
print(info)
while info:
 for x in info:
  print(x)
  if x is dict:#an einai lejiko elegxo kleidia kai values 
   for r in x.keys:
    x.append(r)
   for z in x.values:
    info=z  
  else:
   x=( ", ".join( repr(e) for e in x ) )
  for r in x.keys:
   x.append(r)
   for z in x.values:
    info=z 