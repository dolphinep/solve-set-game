from set_algor import permutation_alg
from piece_class import Piece

def rule():
    print(">>> number = number of item (1, 2, 3)")
    print(">>> shape = 1:ovals  2:sprouts  3:diamonds")
    print(">>> color = 1:green  2:yellow/red  3:pink/purple")
    print(">>> shading = 1:striped  2:outlined  3:filled")
    
    print("<<< Please input number on the following pattern  number:shape:color:shading ex. 1 2 1 3 >>>")

#MAIN GAME
print("<<< WELCOME TO SET GAME >>>")
while True:
    try:
        pieces_num = int(input("Input number of pieces :: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break
print("There are ", pieces_num, " pieces this turn")

rule()
pieces = []
for i in range(pieces_num):
    text_str = ">>> Piece "+ str(i+1) + " :: "
    while True:
        try:
            input_int_arr = [ int(x) for x in input(text_str).split() if(0 < int(x) <= 3)]
            if len(input_int_arr) !=4:
                print("please input number in length 4 ex. 1 2 3 2")
                continue
        except ValueError:
            print("please input number ex. 1 2 3 2")
            continue
        else:
            break
    piece = Piece(i+1, input_int_arr[0], input_int_arr[1], input_int_arr[2], input_int_arr[3])
    pieces.append(piece)

print(">>> YOUR BOARD CONTAIN")
for x in pieces: print(x.toString())
result_list = permutation_alg.cal(pieces) 
if len(result_list) != 0:
    print("SOLUTION SET")
    for y in result_list: print(">>>>", y.toString())
else:
    print("SOLUTION NOT FOUND!!")