
GLYPHS = 'rpgbo'
SIDES = 'ABCDEFGHIJKLMNO'

def all_possible_pieces_long_way():
    piece = [0,0,0,0,0,0,0,0]
    while True:
        ret = ''.join([GLYPHS[i] for i in piece])
        yield ret        
        pos = 7
        while True:
            piece[pos] += 1
            if piece[pos] < 5:
                break
            piece[pos] = 0
            pos -= 1
            if pos < 0:
                return
            
def all_unique_pieces_long_way():
    seen = set()
    for piece in all_possible_pieces_long_way():
        a = sorted([piece[0], piece[1]])
        b = sorted([piece[2], piece[3]])
        c = sorted([piece[4], piece[5]])
        d = sorted([piece[6], piece[7]])
        d = [a, b, c, d]
        d = sorted(d)
        ret = ''
        for p in d:
            ret += p[0] + p[1]
        if ret not in seen:
            seen.add(ret)
            yield ret        

def all_possible_pieces():
    piece = [0,0,0,0]
    while True:
        ret = ''.join([SIDES[i] for i in piece])
        yield ret        
        pos = 3
        while True:
            piece[pos] += 1
            if piece[pos] < 15:
                break
            piece[pos] = 0
            pos -= 1
            if pos < 0:
                return 
            
def all_unique_pieces():
    seen = set()
    for piece in all_possible_pieces():
        ret = ''.join(sorted(piece))
        if ret not in seen:
            seen.add(ret)
            yield ret          
            
     

# cp = 0
# for s in all_possible_pieces_sides():
#     cp += 1
# print(cp)

cp = 0
for p in all_unique_pieces_long_way():    
    cp += 1
print(cp)
    
cp = 0
for p in all_unique_pieces():    
    cp += 1
print(cp)
