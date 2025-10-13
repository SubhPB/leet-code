class Solution:
    '''
    You are given a string s consisting only of the characters 'a', 'b', and 'c'.
    A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
    Return the length of the longest balanced substring of s.

    Example 1:
    Input: s = "abbac"
    Output: 4

    Explanation:
    The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

    Example 2:
    Input: s = "aabcc"
    Output: 3
    Explanation:
    The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

    Example 3:
    Input: s = "aba"
    Output: 2
    Explanation:
    One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

    Constraints:

    1 <= s.length <= 10^5
    s contains only the characters 'a', 'b', and 'c'
    '''
    def longestBalanced(self, s: str) -> int:

        def longestZeroSum(c1:str,c2:str):
            longest=0;freq={0:-1} #basecase
            cnt=0
            for i,c in enumerate(s):
                if c == c1: cnt+=1
                elif c == c2: cnt-=1
                else: cnt=0; freq={0:i}
                if cnt in freq:
                    longest=max(longest,i-freq[cnt])
                else: freq[cnt]=i
            return longest
        
        res=0
        for ci in range(3): 
            
            cnt=0#C1
            for c in s:
                if c=="abc"[ci]: cnt+=1
                else: cnt=0
                res=max(res,cnt)

            for cj in range(ci+1,3):
                longest=longestZeroSum("abc"[ci],"abc"[cj])
                res=max(res,longest) #C2

        #Triplet algorthim needs to be researched to grab the core intuition!
        def longestTriplet(): #C3
            longest=0;freq={(0,0):-1} # need 2D imagination
            a=0;b=0;c=0
            for i,ch in enumerate(s):
                if ch=='a': a+=1
                elif ch=='b': b+=1
                else: c+=1
                x=a-b;y=a-c
                if (x,y) in freq:
                    longest=max(longest,i-freq[(x,y)])
                else: freq[(x,y)]=i
            return longest
        res=max(res,longestTriplet())
        return res

        
            