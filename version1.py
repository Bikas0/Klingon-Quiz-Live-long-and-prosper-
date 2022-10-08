with open("klingon-english.txt") as f:
    contents = f.read()
    
x = contents.split("\n")
data = [i.split('|') for i in x]
klin_w = []
eng_w = []
for i in range (len(data)-1):
    klin_w.append(data[i][0])
    eng_w.append(data[i][1])
    
user_input = input("Take input into the computer :  ")

if user_input in eng_w:
    index = -1
    for i in range(len(eng_w)):
        if user_input == eng_w[i]:
            index = i 
            user_input = klin_w[index]

if user_input in klin_w:
    print("Correct!")
    
else:
    output = "impossible cause initial letter doesn't match"
    for i in range(len(klin_w)):
        if (user_input[0].lower() == klin_w[i][0]) or (user_input[0].upper() == klin_w[i][0]): 
            output = klin_w[i]        
    print(f"Sorry, you're wrong!\nThe correct answer is {output}") 