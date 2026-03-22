import random


class Game:
    def __init__(self):
        self.board=[[0 for col in range(3)] for row in range(3)]
        self.moveCount=0
    def playMove(self,pos):
        if self.moveCount%2==0:
            self.board[pos[0]][pos[1]]=1
        else:
            self.board[pos[0]][pos[1]]=-1
        self.moveCount+=1
    def gameOver(self,board=None,moveCount=None):
        if board is None:
            board=self.board
        if moveCount is None:
            moveCount=self.moveCount
        if self.moveCount%2==1:
            check=1
        else:
            check=-1
        if board[0][0]==board[0][1]==board[0][2]==check or\
            board[1][0]==board[1][1]==board[1][2]==check or\
            board[2][0]==board[2][1]==board[2][2]==check or\
            board[0][0]==board[1][0]==board[2][0]==check or\
            board[0][1]==board[1][1]==board[2][1]==check or\
            board[0][2]==board[1][2]==board[2][2]==check or\
            board[0][0]==board[1][1]==board[2][2]==check or\
            board[0][2]==board[1][1]==board[2][0]==check:
            if check==1:
                return 'Player X won'
            else:
                return 'Player O won'
        elif moveCount==9:
            return 'Draw'
    def display(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col]==1:
                    print('X',end=' ')
                elif self.board[row][col]==-1:
                    print('O',end=' ')
                else:
                    print(' ',end=' ')
            print()


class DeterministicPlayer:
    def __init__(self,playsAs):
        self.playsAs=playsAs
    def play(self,board):
        opponent=-self.playsAs
        if board[0][0]==board[0][1]==opponent or board[1][2]==board[2][2]==opponent or board[1][1]==board[2][0]==opponent:
            if board[0][2]==0:
                return (0,2)
        elif board[0][0]==board[0][2]==opponent or board[1][1]==board[2][1]==opponent:
            if board[0][1]==0:
                return (0,1)
        elif board[0][1]==board[0][2]==opponent or board[1][0]==board[2][0]==opponent or board[1][1]==board[2][2]==opponent:
            if board[0][0]==0:
                return (0,0)
        elif board[1][0]==board[1][1]==opponent or board[0][2]==board[2][2]==opponent:
            if board[1][2]==0:
                return (1,2)
        elif board[1][0]==board[1][2]==opponent or board[0][1]==board[2][1]==opponent or board[0][0]==board[2][2]==opponent or board[0][2]==board[2][0]==opponent:
            if board[1][1]==0:
                return (1,1)
        elif board[1][1]==board[1][2]==opponent or board[0][0]==board[2][0]==opponent:
            if board[1][0]==0:
                return (1,0)
        elif board[2][0]==board[2][1]==opponent or board[0][2]==board[1][2]==opponent or board[0][0]==board[1][1]==opponent:
            if board[2][2]==0:
                return (2,2)
        elif board[2][0]==board[2][2]==opponent or board[0][1]==board[1][1]==opponent:
            if board[2][1]==0:
                return (2,1)
        elif board[2][1]==board[2][2]==opponent or board[0][0]==board[1][0]==opponent or board[0][2]==board[1][1]==opponent:
            if board[2][0]==0:
                return (2,0)
        if board[1][1]==0:
            return (1,1)
        else:
            emptyPos=[]
            for row in range(3):
                for col in range(3):
                    if board[row][col]==0:
                        emptyPos.append((row,col))
            return random.choice(emptyPos)


class RandomPlayer:
    def __init__(self,playsAs):
        self.playsAs=playsAs
    def play(self,board):
        emptyPos=[]
        for row in range(3):
            for col in range(3):
                if board[row][col]==0:
                    emptyPos.append((row,col))
        return random.choice(emptyPos)


class Agent:
    def __init__(self):
        self.epsilon=0.1
        self.lookUp={}
        self.experiences={}
        def Q(state,action):
            if (state,action) not in self.lookUp:
                self.lookUp[(state,action)]=0
            return self.lookUp[(state,action)]
        self.Q=Q
        def updateQ(state,action,reward):
            if (state,action) not in self.experiences:
                self.experiences[(state,action)]=1
            else:
                self.experiences[(state,action)]=self.experiences[(state,action)]+1
            self.lookUp[(state,action)]=self.lookUp[(state,action)]+(reward-self.lookUp[(state,action)])/self.experiences[(state,action)]
        self.updateQ=updateQ
        def policy(state,actions):
            Qs=[]
            for action in actions:
                Qs.append(self.Q(state,action))
            bestQ=Qs[0]
            bestActions=[actions[0]]
            for _ in range(1,len(Qs)):
                if Qs[_]==bestQ:
                    bestActions.append(actions[_])
                elif Qs[_]>bestQ:
                    bestActions.clear()
                    bestActions.append(actions[_])
            if random.uniform(0,1)>self.epsilon:
                return random.choice(bestActions)
            return random.choice(actions)
        self.policy=policy


class RLPlayer:
    def __init__(self,playsAs):
        self.playsAs=playsAs
        self.encode={1:'X',0:'_',-1:'O'}
        self.agent=Agent()
    def play(self,board):
        key=''.join(self.encode[x] for x in board[0]+board[1]+board[2])
        emptyPos=[]
        for row in range(3):
            for col in range(3):
                if board[row][col]==0:
                    emptyPos.append((row,col))
        pos=self.agent.policy(key,emptyPos)
        return key,pos
    def collect(self,key,pos,reward):
        self.agent.updateQ(key,pos,reward)


playerX=RLPlayer(1)
playerO=RLPlayer(-1)
randomPlayerX=RandomPlayer(1)
randomPlayerO=RandomPlayer(-1)
gamesWonAsX=0
gamesWonAsO=0
gamesDrawnAsX=0
gamesDrawnAsO=0
gamesLostAsX=0
gamesLostAsO=0
for _ in range(500000):
    game=Game()
    if random.choice([1,-1])==1:
        while True:
            key,pos=playerX.play(game.board)
            game.playMove(pos)
            gameOver=game.gameOver()
            if gameOver is not None:
                if gameOver=='Draw':
                    playerX.collect(key,pos,0)
                    gamesDrawnAsX+=1
                else:
                    playerX.collect(key,pos,1)
                    gamesWonAsX+=1
                break
            game.playMove(randomPlayerO.play(game.board))
            gameOver=game.gameOver()
            if gameOver is not None:
                if gameOver=='Draw':
                    playerX.collect(key,pos,0)
                    gamesDrawnAsX+=1
                else:
                    playerX.collect(key,pos,-1)
                    gamesLostAsX+=1
                break
            playerX.collect(key,pos,-0.01)
    else:
        game.playMove(randomPlayerX.play(game.board))
        while True:
            key,pos=playerO.play(game.board)
            game.playMove(pos)
            gameOver=game.gameOver()
            if gameOver is not None:
                if gameOver=='Draw':
                    playerO.collect(key,pos,0)
                    gamesDrawnAsO+=1
                else:
                    playerO.collect(key,pos,1)
                    gamesWonAsO+=1
                break
            game.playMove(randomPlayerX.play(game.board))
            gameOver=game.gameOver()
            if gameOver is not None:
                if gameOver=='Draw':
                    playerO.collect(key,pos,0)
                    gamesDrawnAsO+=1
                else:
                    playerO.collect(key,pos,-1)
                    gamesLostAsO+=1
                break
            playerO.collect(key,pos,-0.01)
print(f'Games won as X : {gamesWonAsX} \t\t Games won as O : {gamesWonAsO}')
print(f'Games drawn as X : {gamesDrawnAsX} \t Games drawn as O : {gamesDrawnAsO}')
print(f'Games lost as X : {gamesLostAsX} \t\t Games lost as O : {gamesLostAsO}')


print('--------------------------------------------------------------------')


gamesWonAsX=0
gamesWonAsO=0
gamesDrawn=0
playerX.agent.epsilon=0.1
playerO.agent.epsilon=0.1
for _ in range(10000):
    game=Game()
    while True:
        game.playMove(playerX.play(game.board)[1])
        gameOver=game.gameOver()
        if gameOver is not None:
            if gameOver=='Draw':
                gamesDrawn+=1
            else:
                gamesWonAsX+=1
            break
        game.playMove(playerO.play(game.board)[1])
        gameOver=game.gameOver()
        if gameOver is not None:
            if gameOver=='Draw':
                gamesDrawn+=1
            else:
                gamesWonAsO+=1
            break
print('Games won as X :',gamesWonAsX)
print('Games won as O :',gamesWonAsO)
print('Games drawn :',gamesDrawn)


print('------------------------------------')


game=Game()
while True:
    game.playMove(playerX.play(game.board)[1])
    game.display()
    gameOver=game.gameOver()
    if gameOver is not None:
        print(gameOver)
        break
    game.playMove(eval(input('Your move:')))
    game.display()
    gameOver=game.gameOver()
    if gameOver is not None:
        print(gameOver)
        break