class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r) // 2
            totalTime = 0

            # compute the total time needed to eat all the piles
            # at rate k
            for p in piles:
                # for each pile it will take pileSize/eatRate hours to eat it
                # approximate to the higher digit
                totalTime += math.ceil(float(p) / k)
            # if we can reduce the speed, search the left half
            if totalTime <= h:
                res = k
                r = k - 1
            # else if we need to increase the speed search the right half
            else:
                l = k + 1
        return res