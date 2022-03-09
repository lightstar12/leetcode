class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == 'type':
            key = 0
        elif ruleKey == 'color':
            key = 1
        elif ruleKey == 'name':
            key = 2
        cnt = 0
        for i in range(len(items)):
            if items[i][key] == ruleValue:
                cnt = cnt + 1
        return cnt