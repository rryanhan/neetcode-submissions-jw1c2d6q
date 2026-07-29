class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # index
        l = r = 0

        while r < len(nums):
            # remove left val from window
            if q and l > q[0]:
                q.popleft()
            # montonic decreasing deque
                # the front of the deque ALWAYS has the largest number in the window
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            

            # is the window of sufficient size?
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output



        
        