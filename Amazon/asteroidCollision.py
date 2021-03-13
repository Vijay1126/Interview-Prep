class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for asteroid in asteroids:
            
            while stack and stack[-1]>0>asteroid:
                if abs(asteroid) == stack[-1]:
                    stack.pop()
                    break
                else:
                    if abs(asteroid)>stack[-1]:
                        stack.pop()
                        continue
                break
            else:
                stack.append(asteroid)
            
        return stack
            
                
