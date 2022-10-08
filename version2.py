    
with open("klingon-english.txt") as f:
    contents = f.read()
    
x = contents.split("\n")
data = [i.split('|') for i in x]
klin_w = []
eng_w = []

for i in range (len(data)-1):
    klin_w.append(data[i][0])
    eng_w.append(data[i][1])
    

def remove_dup(a):
    i = 0
    while i < len(a):
        j = i+1
        
        while j<len(a):
            if (a[i][0] == a[j]):
                del a[j]
            else:
                j += 1
        i += 1        

vowel = ["a","e","i","o","u"]
consonant = []

i = 0
while i < (len(klin_w)):
    letter = klin_w[i][0]
    if (letter not in vowel and klin_w[i][1] == "h"):
        consonant.append(klin_w[i][0:2])    
    if(letter not in vowel):
         consonant.append(klin_w[i][0])
            
    i += 1
  
    
remove_dup(consonant)  
         


user_input = input()
if (user_input in consonant):
    chosen_word = input("Find a Klingon word that starts with the chosen consonant : ")
while (user_input not in consonant):
    print("Please enter a valid klingon constant")
    user_input = input()
    if (user_input in consonant):
        chosen_word = input("Find a Klingon word that starts with the chosen consonant : ")
        break

j = 0       
while j < (len(klin_w)):
    if chosen_word in klin_w:
        print("Correct!")
        break
    
    else:
        output = "impossible cause initial letter doesn't match"
        k = 0
        while k < len(klin_w):
            if (chosen_word[0] == klin_w[k][0]): 
                output = klin_w[k] 
                break
            k += 1    
        print(f"Sorry, you're wrong!\nThe correct answer is {output}")   
        break

    j += 1

    