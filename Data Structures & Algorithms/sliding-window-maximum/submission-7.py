class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        q = deque()
        res = []

        while r < len(nums):
            # there is an element in queue, and it is out of bounds now
            if q and q[0] < l:
                q.popleft()

            # we only care about largest element, pop until current nums is 
            # sorted within the q
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            q.append(r)

            if (r - l + 1) == k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res
        


# monotonic queue
#   - keep track of the largest element in that queue with its index
#   - USE INDEX, as that way we know if the element is in bounds or not

# main condition -> r <= len(nums)

# we might have just shrank the window, so we want to see if the largest value is 
# still within bounds; if not, pop it out

# is the new nums[i] greater than q[-1]?
    # if so, pop q[-1]
    # then, append index

# condition -> is r - 1 + 1 == k?
    # if so, append q[0] to the array
    # then we can start shrinking the left pointer


