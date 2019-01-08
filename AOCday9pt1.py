#%%

def marbleGame(noElves, noMarbles):
    marbleCircle = [0,2,1]
    scores = {}
    currpos = 1
    j=3
    
    for i in range(3,noMarbles):

        lenCircle = len(marbleCircle)
        
        if i%23 == 0:
                                    
            if j in scores:         
                scores[j]+=i
            else:
                scores[j]=i
                                
            if currpos >=7:
                currpos-=7
            else:
                currpos = lenCircle - 7 + currpos
            
            scoreincr = marbleCircle.pop(currpos)
            scores[j]+=scoreincr
                        
        else:
            currpos += 2
            
            if currpos > lenCircle:
                currpos -= lenCircle
                
            marbleCircle.insert(currpos, i)

        if j ==noElves:
            j=1
            print(j, i)
        else:
            j+=1

    
    print(max(zip(scores.values(), scores.keys())))
            
        
        
marbleGame(410, 72059)