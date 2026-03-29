class Twitter:

    def __init__(self):
        self.count = 0
        self.usertofollowee = {} #userid:setoffolloweeids
        self.usertoposts = {} #userid:list of postids
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        if userId in self.usertoposts:
            self.usertoposts[userId].append([self.count, tweetId])    
        else:
            self.usertoposts[userId] = [[self.count, tweetId]]


    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.usertoposts[userId].copy() if userId in self.usertoposts else []
        if userId in self.usertofollowee:
            for followee in self.usertofollowee[userId]:
                if followee == userId:
                    continue
                if followee in self.usertoposts:
                    feed.extend(self.usertoposts[followee])
        


        heapq.heapify_max(feed)
        res = []
        for i in range(min(10,len(feed))):
            res.append(heapq.heappop_max(feed)[1])
        return res
                
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.usertofollowee:
            self.usertofollowee[followerId].add(followeeId)
        else:
            self.usertofollowee[followerId] = set()
            self.usertofollowee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.usertofollowee:
            if followeeId in self.usertofollowee[followerId]:
                self.usertofollowee[followerId].remove(followeeId)

        
