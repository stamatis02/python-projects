import numpy as np
#θεωρούμε ως κατάσταση 0 την α και 1 την β
katastaseis = np.array(["a","b"])

#δεδομένα σε λογαριθμική κλίμακα για αποφυγή underflow
P = np.log(np.array([0.5,0.5])) #υποθέτουμε αρχικές πιθανότητες ίσες
metabaseis = np.log(np.array([[0.9,0.1],[0.1,0.9]]))
ekpompes = np.log(np.array([[0.4, 0.2],[0.4, 0.2],[0.1, 0.3],[0.1, 0.3]]))
akolouthia="GGTC"
sequence_length = len(akolouthia)

#άδειο διάγραμμα trellis
probabilities = np.zeros((len(katastaseis),sequence_length))
for s in range(len(katastaseis)): #αρχικοποίηση πιθανοτήτων στη θέση 0
    probabilities[s] = P[s]*ekpompes[s][0]

#αρχικοποίηση πίνακα για την αποθήκευση καλύτερης προηγούμενης κατάστασης
previous_positions = np.zeros((len(katastaseis),sequence_length))

for i in range(1,sequence_length): #γέμισμα διαγράμματος trellis με δυναμικό προγραμματισμό
    for j in range(len(katastaseis)):
        best_ix = np.argmax(probabilities[p,i-1]+metabaseis[p,j]+ekpompes[i,j] for p in range(len(probabilities)))
        previous_positions[j,i] = best_ix
        probabilities[j,i] = probabilities[best_ix,i-1]+metabaseis[best_ix,j]+ekpompes[i,j]
            
#δείκτης στην τελευταία θέση με την ψηλότερη πιθανότητα
curr_ix = np.argmax(probabilities[p,sequence_length-1] for p in range(len(probabilities)))

#αποθήκευση των βημάτων του backtracking
result = ""

#backtracking για να βρούμε την καλύτερη ακολουθία καταστάσεων
for i in range(sequence_length-1, -1, -1):
    result+=katastaseis[int(curr_ix)]
    curr_ix = previous_positions[int(curr_ix),i]

print("Πιο πιθανή ακολουθία καταστάσεων:",result[::-1]) #ανάποδα τα βήματα του  backtracking
