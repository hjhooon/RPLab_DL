from itertools import combinations

def subsequences(a,n):
    a = list(a)
    new_a = []
    t1 = ()
    for i in a:
        new_a += str(i)

    b = list(combinations(new_a,n))
    for j in b:
        c=""
        for k in range(n):
            c = c + j[k]
        t2 = (c,)
        t1 += t2
    return t1

sub = subsequences ( 'ABCD', 2 )
print ( sub )

sub = subsequences ( range(4), 3 )
print ( sub )