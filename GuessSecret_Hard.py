import collections
import random
from typing import List
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def checkBadChars(word) -> bool:
            return not any(word[i] in bad[i] for i in range(0, 6))

        def scoreMatch(word) -> bool:
            return all(match(word, word2) == score for word2, score in possibleWords.items())

        def match(word1, word2) -> int:
            return sum(word1[i] == word2[i] for i in range(6))

        possibleWords = {}
        bad = collections.defaultdict(set)
        for _ in range(10):
            # build the word list
            wordList = [word for word in wordlist if checkBadChars(word) and scoreMatch(word)]
            word1 = wordlist.pop(random.randint(0, len(wordlist) - 1))
            score = master.guess(word1)
            if score == 0:
                for i in range(len(word1)):
                    bad[i].add(word1[i])
            elif score < 6:
                possibleWords[word1] = score
            else:
                return None

obj = Solution()
obj.findSecretWord(['cat','dog','rat','bat','mat'])