'''
1900. The Earliest and Latest Rounds Where Players Compete

    There is a tournament where n players are participating. The players are standing in a single row and are numbered from 1 to n based on their initial standing position (player 1 is the first player in the row, player 2 is the second player in the row, etc.).

    The tournament consists of multiple rounds (starting from round number 1). In each round, the ith player from the front of the row competes against the ith player from the end of the row, and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances to the next round.

    For example, if the row consists of players 1, 2, 4, 6, 7
    Player 1 competes against player 7.
    Player 2 competes against player 6.
    Player 4 automatically advances to the next round.
    After each round is over, the winners are lined back up in the row based on the original ordering assigned to them initially (ascending order).

    The players numbered firstPlayer and secondPlayer are the best in the tournament. They can win against any other player before they compete against each other. If any two other players compete against each other, either of them might win, and thus you may choose the outcome of this round.

    Given the integers n, firstPlayer, and secondPlayer, return an integer array containing two values, the earliest possible round number and the latest possible round number in which these two players will compete against each other, respectively.

    

    Example 1:

    Input: n = 11, firstPlayer = 2, secondPlayer = 4
    Output: [3,4]
    Explanation:
    One possible scenario which leads to the earliest round number:
    First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    Second round: 2, 3, 4, 5, 6, 11
    Third round: 2, 3, 4
    One possible scenario which leads to the latest round number:
    First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    Second round: 1, 2, 3, 4, 5, 6
    Third round: 1, 2, 4
    Fourth round: 2, 4
    Example 2:

    Input: n = 5, firstPlayer = 1, secondPlayer = 5
    Output: [1,1]
    Explanation: The players numbered 1 and 5 compete in the first round.
    There is no way to make them compete in any other round.

    Constraints:

    2 <= n <= 28
    1 <= firstPlayer < secondPlayer <= n

    python ./src/app/2025/July/1900.py
'''

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:

        def leftShift(k:int, P1:int,P2:int):
            diff = P2-P1
            P1 = k-P2+1
            P2 = P1+diff
            return (P1,P2)

        def nextRound(k:int,P1:int,P2:int):
            if P1 == k-P2+1: return (1,1)

            m = (k+1)//2
            
            if P1>=m or P1>k-P2: 
                # P>=m: means case-i but values exist in right segment, let's symmetrically shift into left half!

                # P1>k-p2 means case-ii one in left and other in right segment but their order is more inclined to right side,
                #  making left-shift to smoothly run 'oppositeSegment'
                P1,P2 = leftShift(k,P1,P2)
            
            if P2<=m: # case-i both players exist in same half
                return sameSegment(k,P1,P2)
            else:
                return oppositeSegment(k,P1,P2)
        
        def sameSegment(k:int,P1:int,P2:int):
            mn, mx = k//2, 0
            for sl in range(P1):
                for sm in range(P2-P1):
                    NP1 = sl+1
                    NP2 = NP1+sm+1
                    tmn, tmx = nextRound((k+1)//2, NP1, NP2)
                    mn, mx = min(mn,tmn), max(mx,tmx)
            return (1+mn,1+mx)
        
        def oppositeSegment(k:int,P1:int,P2:int):
            mn, mx = k//2, 0
            OP2 = k-P2+1 #opponent of P2
            consts = (P2-OP2)//2
            for sl in range(P1):
                for sll in range(OP2-P1):
                    NP1 = sl+1
                    NP2 = NP1+sll+consts+1
                    tmn,tmx = nextRound((k+1)//2, NP1, NP2)
                    mn,mx = min(mn,tmn), max(mx,tmx)

            return (1+mn,1+mx)
        return nextRound(n,firstPlayer,secondPlayer)

if __name__ == "__main__":
    testcases = []
    add = lambda n,firstPlayer,secondPlayer: testcases.append([n,firstPlayer,secondPlayer])
    
    add(n = 11, firstPlayer = 2, secondPlayer = 4)
    add(n = 5, firstPlayer = 1, secondPlayer = 5)
    add(n = 5, firstPlayer = 2, secondPlayer = 5)
    for [n,firstPlayer,secondPlayer] in testcases:
        print(f'n={n} firstPlayer={firstPlayer} secondPlayer={secondPlayer} result={Solution().earliestAndLatest(n,firstPlayer,secondPlayer)}')