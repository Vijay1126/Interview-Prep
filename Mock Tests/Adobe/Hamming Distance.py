class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        length = max(len(bin(x)), len(bin(y)))
        x = bin(x)[2:].zfill(length)
        y = bin(y)[2:].zfill(length)
        print(x,y)
        count = 0
        for a,b in zip((x), (y)):
            count+=a!=b
        return count
