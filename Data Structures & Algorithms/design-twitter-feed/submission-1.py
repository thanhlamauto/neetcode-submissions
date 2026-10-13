from collections import defaultdict
class Twitter:
    
    def __init__(self):
        self.tweets = []
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        result = []

        following = self.follows[userId].copy()
        following.add(userId)
        

        for tweetId, user in reversed(self.tweets):
            if user in following:
                result.append(tweetId)
                if len(result) == 10:
                    break
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
