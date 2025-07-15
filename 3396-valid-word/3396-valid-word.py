class Solution:
    def isValid(self, word: str) -> bool:
        pattern = r"^(?=[a-zA-Z0-9]{3,}$)(?=.*[aeiouAEIOU])(?=.*[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])"
        return bool(re.match(pattern, word))
        