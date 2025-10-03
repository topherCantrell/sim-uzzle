
GLYPHS = 'rpgbo'
SIDES = 'ABCDEFGHIJKLMNO'
SIDE_DEFINITION = {
    'A': 'rr',
    'B': 'rp',
    'C': 'rg',
    'D': 'rb',
    'E': 'ro',
    'F': 'pp',
    'G': 'pg',
    'H': 'pb',
    'I': 'po',
    'J': 'gg',
    'K': 'gb',
    'L': 'go',
    'M': 'bb',
    'N': 'bo',
    'O': 'oo',    
}

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

def report_all_unique_pieces():
    cp = 0
    for _ in all_unique_pieces_long_way():    
        cp += 1
    print('Using the "long way:',cp)
    cp = 0
    for _ in all_unique_pieces():    
        cp += 1
    print('Using the domino sides:', cp)

def report_all_allowed_pieces():
    cp = 0
    for p in get_allowed_pieces():    
        cp += 1        
    print('Count of allowed pieces:', cp)

def get_allowed_pieces():
    for p in all_unique_pieces():
        doubles = 0
        counts = {g:0 for g in GLYPHS}
        for s in p:
            g1, g2 = SIDE_DEFINITION[s]
            if g1 == g2:
                doubles += 1
            counts[g1] += 1
            counts[g2] += 1
        # TODO make sure each piece has 1 or 2 of each glyph
        if all(1 <= counts[g] <= 2 for g in GLYPHS) and doubles == 1:
            yield p

if __name__ == '__main__':
    # report_all_unique_pieces()
    report_all_allowed_pieces()
