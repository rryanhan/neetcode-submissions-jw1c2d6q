# need to keep track of time for all posts
# need to know the order of posts a user makes

class Twitter:

    def __init__(self):
        self.time = 0 # decrement so its a maxHeap, most recently used
        self.followerMap = defaultdict(set) # uId -> (uIds)
        self.postMap = defaultdict(list) # uId -> [time, tweetId]
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append([self.time, tweetId])
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []
        self.followerMap[userId].add(userId)
        for followeeId in self.followerMap[userId]:
            if followeeId in self.postMap:
                index = len(self.postMap[followeeId]) - 1
                time, tweetId = self.postMap[followeeId][index]
                minHeap.append([time, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.postMap[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
        
