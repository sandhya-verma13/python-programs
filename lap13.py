def anagram(w1,w2):
    w1=w1.lower()
    w2=w2.lower()
    len(w1)==len(w2)
    return sorted(w1)==sorted(w2)
w1=input( )
w2=input( )
print(anagram(w1,w2))
