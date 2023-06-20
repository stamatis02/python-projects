from Bio.Seq import Seq
from Bio import SeqIO



#Φορτώνουμε τις 2 αλληλουχιες 
for sequence1 in SeqIO.parse("1.fasta", "fasta"): 
	seq1 = sequence1.seq	
for sequence2 in SeqIO.parse("2.fasta", "fasta"):
	seq2 = sequence2.seq
seq1 = len(sequence1) #Βρίσκουμε το μέγεθος της πρώτης αλληλουχιάς
seq2 = len(sequence2) #Βρίσκουμε το μέγεθος της δεύτερης αλληλουχιάς


player = 1 
print(seq1)
print(seq2)




#Εδώ ελέγχουμε αν κέρδισε καποιος παίχτης
def check():
      a = False
      if(seq1==0 or seq2==0 or (seq1<2 and seq2<2)):
            print("Νικητής ειναι ο παίχτης ",player)
            a = True
      return a 

def changeplayer():
      if(player==1): #Αλλαγη παιχτων
            player=2 #Αν επαιζε ο παιχτης 1 τωρα εχει σειρα ο παιχτης 2
      elif(player==2): #Αλλαγη παιχτων
            player=1 #Αν επαιζε ο παιχτης 2 τωρα εχει σειρα ο παιχτης 1

#x=int(input( "γραψε 1 η 2 \n"))
while(True): 
      print("σειρα του παιχτη:" , player , " \n απο ποια αλληλουχια θέλεις να αφερεσεις 2 νουκλεοτιδια?")
      x=int(input( "γραψε 1 η 2 \n")) 
      changeplayer()
      if x==1:
            if seq1<2:
                  print("den mporeis na afaireseis apo auto")
                  seq1-=1
                  seq2-=2
            else: 
                  seq1-=2
                  seq2-=1           
      elif x==2:                  
            if seq2<2:
                  print("den mporeis na afaireseis apo auto")
                  seq1-=2
                  seq2-=1
            else:
                  seq1-=1
                  seq2-=2
      print("kanoyrgio mikos",seq1," \n 2o:",seq2) 
      if(check()):
            break     
  
 
   
       
  


