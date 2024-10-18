from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    #could sort and compare, but using 2 counters/maps
    if len(s) != len(t):
        return False
    s_letters = Counter()
    t_letters = Counter()
    for char in range(len(s)):
        s_letters[s[char]] += 1
        t_letters[t[char]] += 1
        #check if we can stop the loop early
        if s[char] not in t or t[char] not in s:
            return False 
            
    if s_letters == t_letters:
        return True
    else:
          return False

s, t = "anagram", "nagaram"

print(isAnagram(s,t))