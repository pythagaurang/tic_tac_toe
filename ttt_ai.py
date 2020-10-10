class ttt_ai:
    file=open("depth.txt",mode="w")
    def evaluate(self,grid):
        # check horizontal vectors
        for i in range(0, 9, 3):
            if grid[i] == grid[i+1] == grid[i+2] != -1:
                if grid[i]:
                    return +10
                else:
                    return -10
        # check vertical vectors
        for i in range(3):
            if grid[i] == grid[i+3] == grid[i+6] != -1:
                if grid[i]:
                    return +10
                else:
                    return -10
        # check diagonal vectors
        if grid[0] == grid[4] == grid[8] != -1:
            if grid[0]:
                return +10
            else:
                return -10
        if grid[2] == grid[4] == grid[6] != -1:
            if grid[2]:
                return +10
            else:
                return -10
        return 0

    def minimax(self,grid, isMax):
        score = self.evaluate(grid)
        #if game over return score
        if score :
            return score
        if -1 not in grid:
            return 0
        scores=[]
        for i in range(9):
            if grid[i]==-1:
                grid[i]=int(isMax)
                scores.append(self.minimax(grid, not isMax))
                grid[i]=-1
        return max(scores)if isMax else min(scores)

    def __call__(self,grid):
        bestScore = -1000
        bestMove = None
        if sum(grid)==-9:
            return 0
        for i in range(9):
            if grid[i]==-1:
                grid[i]=1
                moveScore = self.minimax(grid, False)
                grid[i]=-1
                if moveScore>bestScore:
                    bestMove=i
                    bestScore=moveScore
        print(f"Best Move: row:{bestMove//3} col:{bestMove%3}, Value: {bestScore}")
        return bestMove

ai_player=ttt_ai()