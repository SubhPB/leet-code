class Solution:
    '''
    3941. Password Strength

    You are given a string password.

    The strength of the password is calculated based on the following rules:

    1 point for each distinct lowercase letter ('a' to 'z').
    2 points for each distinct uppercase letter ('A' to 'Z').
    3 points for each distinct digit ('0' to '9').
    5 points for each distinct special character from the set "!@#$".
    Each character contributes at most once, even if it appears multiple times.

    Return an integer denoting the strength of the password.

    Constraints:
    1 <= password.length <= 105
    password consists of lowercase and uppercase English letters, digits, and special characters from "!@#$".
    '''
    def passwordStrength(self, password: str) -> int:
        res=0
        for char in set(password):
            if 'a'<=char<='z': res+=1
            elif 'A'<=char<='Z': res+=2
            elif char in '!@#$': res+=5
            elif 0<=int(char)<=9: res+=3
        return res
