class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join(list(map(lambda x: x[:-1], sorted(s.split(), key = lambda x: x[-1]))))