class Shomaresh:
    def __init__(self, v: int=0 , i: int=1 ) -> None:
        self.val = v
        self.incr = i 
         
    def afzayesh(self) -> None:
        self.val += self.incr
        
    def __repr__(self) -> str:
        return str(self.val)
        
K = Shomaresh(i=900,v=25)
K.afzayesh()
print(K.val , K.incr, K)
