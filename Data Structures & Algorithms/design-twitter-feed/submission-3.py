from collections import deque, defaultdict
class Twitter:

    def __init__(self):
        self.followerMap = defaultdict(set)
        self.posts = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = deque([(tweetId, self.time)])
        else:
            self.posts[userId].append((tweetId, self.time))
        self.time -= 1
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        feed = []
        heapq.heapify(heap)
        self.followerMap[userId].add(userId)
        # get the most recent tweet for each followee
        for fid in self.followerMap[userId]:
            if fid in self.posts:
                index = len(self.posts[fid]) - 1
                tweetId, time = self.posts[fid][index]
                # we're going to use a maxHeap (times are negative) to store the newest tweets
                heapq.heappush(heap, (time, tweetId, fid, index-1))
        while heap and len(feed) < 10:
            # we get the most recent tweet and if there are more for this followee we add the next one to the heap
            time, tweetId, fid, index = heapq.heappop(heap)
            feed.append(tweetId)
            if index >= 0:
                tweetId, time = self.posts[fid][index]
                heapq.heappush(heap, (time, tweetId, fid, index-1))
        
        return feed



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
        return
        
