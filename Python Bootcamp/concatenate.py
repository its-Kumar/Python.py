def concatenate(L1, L2, connector):
    
    return [word1+connector+word2 for (word1,word2) in zip(L1,L2)]

print(
    concatenate(['a','b','c'],['x','y','z'],'-')
)