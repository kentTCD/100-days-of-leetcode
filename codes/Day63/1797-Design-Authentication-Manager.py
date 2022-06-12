class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tk_time = timeToLive
        self.hash = {} # tokenId: expireTime

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.hash[tokenId] = currentTime + self.tk_time

    def renew(self, tokenId: str, currentTime: int) -> None:
        ex_time = self.hash.get(tokenId)
        if ex_time:
            if ex_time > currentTime:
                self.hash[tokenId] = currentTime + self.tk_time

    def countUnexpiredTokens(self, currentTime: int) -> int:
        for tk_id in list(self.hash.keys()):
            if self.hash[tk_id] <= currentTime:
                del self.hash[tk_id]
        return len(self.hash)