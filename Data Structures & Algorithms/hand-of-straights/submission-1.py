class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        minH = list(count.keys()) # put card values (not counts) in min heap
        heapq.heapify(minH)

        while minH:
            first = minH[0] # get minimum card

            for i in range(first, first + groupSize): # create a group
                if i not in count:
                    return False
                
                count[i] -= 1
                if count[i] == 0: # need to pop from min heap
                    if i != minH[0]: # card is not smallest
                        return False
                    
                    heapq.heappop(minH)

        
        return True
