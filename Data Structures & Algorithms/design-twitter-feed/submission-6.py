class Twitter:

    def __init__(self):
        self.usertoposts = {} # userid:list of [time, postid]
        self.usertofollowee = {} #userid:set of followee user_ids -> since we want O(1) add and remove
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        if userId in self.usertoposts:
            self.usertoposts[userId].append([self.time, tweetId])
        else:
            self.usertoposts[userId] = [[self.time,tweetId]]

    def getNewsFeed(self, userId: int) -> List[int]:
        curr = []
        if userId in self.usertoposts:
            curr = self.usertoposts[userId]
        listoftimetweetIds = []
        if curr:
            for i in curr:
                listoftimetweetIds.append(i)
        if userId in self.usertofollowee:
            following = self.usertofollowee[userId]
            for followee in following:
                if followee != userId and followee in self.usertoposts:
                    for post in self.usertoposts[followee]:
                        listoftimetweetIds.append(post)
        
        heapq.heapify_max(listoftimetweetIds)
        res = []
        for i in range(10):
            if listoftimetweetIds:
                res.append(heapq.heappop_max(listoftimetweetIds)[1])
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.usertofollowee:
            self.usertofollowee[followerId].add(followeeId)
        else:
            self.usertofollowee[followerId] = set()
            self.usertofollowee[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.usertofollowee and followeeId in self.usertofollowee[followerId]:
            self.usertofollowee[followerId].remove(followeeId)
        
