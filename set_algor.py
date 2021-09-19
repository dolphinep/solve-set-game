from itertools import combinations
def all_dif(a,b,c):
    return (a != b) and (b != c) and (a != c)

def same(a,b,c):
    return a==b==c

def normal_logic(list):
        if not all_dif(list[0].number, list[1].number, list[2].number) and not same(list[0].number, list[1].number, list[2].number):
            return False
        if not all_dif(list[0].shape, list[1].shape, list[2].shape) and not same(list[0].shape, list[1].shape, list[2].shape):
            return False
        if not all_dif(list[0].color, list[1].color, list[2].color) and not same(list[0].color, list[1].color, list[2].color):
            return False
        if not all_dif(list[0].shading, list[1].shading, list[2].shading) and not same(list[0].shading, list[1].shading, list[2].shading):
            return False
        return True

class combinations_alg:  
    def cal(pieces):
        perms = combinations(pieces, 3)
        for x in perms:
            # for y in x:
            #     print(y.toString())
            # print("----------------------")
            if normal_logic(x):
                return x
