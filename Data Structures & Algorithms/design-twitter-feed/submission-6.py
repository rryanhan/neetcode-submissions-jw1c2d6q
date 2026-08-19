class Twitter:

    def __init__(self):
        self.followerMap = defaultdict(set)
        self.postMap = defaultdict(list) # uID : post1, post2, post3
        self.counter = 0

        # user : posts
        # 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append([self.counter, tweetId])

        while len(self.postMap[userId]) > 10:
            self.postMap[userId].pop(0)
        self.counter -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        k = 0
        res = []
        heap = []
        self.followerMap[userId].add(userId)
        # minHeap contains followee's posts
            # traverse via indices 

        for userToTrack in self.followerMap[userId]: # users they follow
            tweets = self.postMap[userToTrack]
            if tweets:
                index = len(tweets) - 1
                timeStamp, tweetId = tweets[index]
                # index - 1 is the next one we are looking for
                heapq.heappush(heap, [timeStamp, tweetId, userToTrack, index - 1])
        while len(res) < 10 and heap:
            timeStamp, tweetId, userToTrack, nextIndex = heapq.heappop(heap)
            res.append(tweetId)
            if nextIndex >= 0:
                nextTimeStamp, nextTweetId = self.postMap[userToTrack][nextIndex]
                heapq.heappush(heap, [nextTimeStamp, nextTweetId, userToTrack, nextIndex - 1])
        return res
                

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)


# for posts, we can attach a timestamp as well 