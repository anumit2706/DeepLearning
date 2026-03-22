import random


class ChessBoard:
    class WhiteKing:
        def __init__(self,parent,id='K',pos=(0,4),shortCastleRights=True,longCastleRights=True):
            self.parent=parent
            self.id=id
            self.pos=pos
            self.shortCastleRights=shortCastleRights
            self.longCastleRights=longCastleRights
        def LegalMoves(self,justChecking):
            legalMoves=[]
            if not justChecking:
                if self.parent.IsValid(self.pos[0]+1,self.pos[1]) and (self.parent.IsClear(self.pos[0]+1,self.pos[1]) or self.parent.IsBlack(self.pos[0]+1,self.pos[1])):
                    self.pos=(self.pos[0]+1,self.pos[1])
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0]-1,self.pos[1]),self.pos))
                    self.pos=(self.pos[0]-1,self.pos[1])
                if self.parent.IsValid(self.pos[0]+1,self.pos[1]+1) and (self.parent.IsClear(self.pos[0]+1,self.pos[1]+1) or self.parent.IsBlack(self.pos[0]+1,self.pos[1]+1)):
                    self.pos=(self.pos[0]+1,self.pos[1]+1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0]-1,self.pos[1]-1),self.pos))
                    self.pos=(self.pos[0]-1,self.pos[1]-1)
                if self.parent.IsValid(self.pos[0],self.pos[1]+1) and (self.parent.IsClear(self.pos[0],self.pos[1]+1) or self.parent.IsBlack(self.pos[0],self.pos[1]+1)):
                    self.pos=(self.pos[0],self.pos[1]+1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0],self.pos[1]-1),self.pos))
                    self.pos=(self.pos[0],self.pos[1]-1)
                if self.parent.IsValid(self.pos[0]-1,self.pos[1]+1) and (self.parent.IsClear(self.pos[0]-1,self.pos[1]+1) or self.parent.IsBlack(self.pos[0]-1,self.pos[1]+1)):
                    self.pos=(self.pos[0]-1,self.pos[1]+1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0]+1,self.pos[1]-1),self.pos))
                    self.pos=(self.pos[0]+1,self.pos[1]-1)
                if self.parent.IsValid(self.pos[0]-1,self.pos[1]) and (self.parent.IsClear(self.pos[0]-1,self.pos[1]) or self.parent.IsBlack(self.pos[0]-1,self.pos[1])):
                    self.pos=(self.pos[0]-1,self.pos[1])
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0]+1,self.pos[1]),self.pos))
                    self.pos=(self.pos[0]+1,self.pos[1])
                if self.parent.IsValid(self.pos[0]-1,self.pos[1]-1) and (self.parent.IsClear(self.pos[0]-1,self.pos[1]-1) or self.parent.IsBlack(self.pos[0]-1,self.pos[1]-1)):
                    self.pos=(self.pos[0]-1,self.pos[1]-1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0]+1,self.pos[1]+1),self.pos))
                    self.pos=(self.pos[0]+1,self.pos[1]+1)
                if self.parent.IsValid(self.pos[0],self.pos[1]-1) and (self.parent.IsClear(self.pos[0],self.pos[1]-1) or self.parent.IsBlack(self.pos[0],self.pos[1]-1)):
                    self.pos=(self.pos[0],self.pos[1]-1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0],self.pos[1]+1),self.pos))
                    self.pos=(self.pos[0],self.pos[1]+1)
                if self.parent.IsValid(self.pos[0]+1,self.pos[1]-1) and (self.parent.IsClear(self.pos[0]+1,self.pos[1]-1) or self.parent.IsBlack(self.pos[0]+1,self.pos[1]-1)):
                    self.pos=(self.pos[0]+1,self.pos[1]-1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0]-1,self.pos[1]+1),self.pos))
                    self.pos=(self.pos[0]-1,self.pos[1]+1)
                if self.shortCastleRights and not self.parent.IsInCheck(self.pos[0],self.pos[1]) and self.parent.IsClear(self.pos[0],self.pos[1]+1) and self.parent.IsClear(self.pos[0],self.pos[1]+2):
                    self.pos=(self.pos[0],self.pos[1]+1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        self.pos=(self.pos[0],self.pos[1]+1)
                        if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                            legalMoves.append(((self.pos[0],self.pos[1]-2),self.pos,'short'))
                        self.pos=(self.pos[0],self.pos[1]-1)
                    self.pos=(self.pos[0],self.pos[1]-1)
                if self.longCastleRights and not self.parent.IsInCheck(self.pos[0],self.pos[1]) and self.parent.IsClear(self.pos[0],self.pos[1]-1) and self.parent.IsClear(self.pos[0],self.pos[1]-2):
                    self.pos=(self.pos[0],self.pos[1]-1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        self.pos=(self.pos[0],self.pos[1]-1)
                        if not self.parent.IsInCheck(self.pos[0],self.pos[1]-1):
                            legalMoves.append(((self.pos[0],self.pos[1]-2),self.pos,'short'))
                        self.pos=(self.pos[0],self.pos[1]+1)
                    self.pos=(self.pos[0],self.pos[1]+1)
            else:
                legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1])))
                legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]+1)))
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]+1)))
                legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]+1)))
                legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1])))
                legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]-1)))
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]-1)))
                legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]-1)))
            return legalMoves
    class BlackKing:
        def __init__(self,parent,id='k',pos=(7,4),shortCastleRights=True,longCastleRights=True):
            self.parent=parent
            self.id=id
            self.pos=pos
            self.shortCastleRights=shortCastleRights
            self.longCastleRights=longCastleRights
        def LegalMoves(self,justChecking):
            legalMoves=[]
            if not justChecking:
                if self.parent.IsValid(self.pos[0]+1,self.pos[1]) and (self.parent.IsClear(self.pos[0]+1,self.pos[1]) or self.parent.IsWhite(self.pos[0]+1,self.pos[1])):
                    self.pos=(self.pos[0]+1,self.pos[1])
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0]-1,self.pos[1]),self.pos))
                    self.pos=(self.pos[0]-1,self.pos[1])
                if self.parent.IsValid(self.pos[0]+1,self.pos[1]+1) and (self.parent.IsClear(self.pos[0]+1,self.pos[1]+1) or self.parent.IsWhite(self.pos[0]+1,self.pos[1]+1)):
                    self.pos=(self.pos[0]+1,self.pos[1]+1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0]-1,self.pos[1]-1),self.pos))
                    self.pos=(self.pos[0]-1,self.pos[1]-1)
                if self.parent.IsValid(self.pos[0],self.pos[1]+1) and (self.parent.IsClear(self.pos[0],self.pos[1]+1) or self.parent.IsWhite(self.pos[0],self.pos[1]+1)):
                    self.pos=(self.pos[0],self.pos[1]+1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0],self.pos[1]-1),self.pos))
                    self.pos=(self.pos[0],self.pos[1]-1)
                if self.parent.IsValid(self.pos[0]-1,self.pos[1]+1) and (self.parent.IsClear(self.pos[0]-1,self.pos[1]+1) or self.parent.IsWhite(self.pos[0]-1,self.pos[1]+1)):
                    self.pos=(self.pos[0]-1,self.pos[1]+1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0]+1,self.pos[1]-1),self.pos))
                    self.pos=(self.pos[0]+1,self.pos[1]-1)
                if self.parent.IsValid(self.pos[0]-1,self.pos[1]) and (self.parent.IsClear(self.pos[0]-1,self.pos[1]) or self.parent.IsWhite(self.pos[0]-1,self.pos[1])):
                    self.pos=(self.pos[0]-1,self.pos[1])
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0]+1,self.pos[1]),self.pos))
                    self.pos=(self.pos[0]+1,self.pos[1])
                if self.parent.IsValid(self.pos[0]-1,self.pos[1]-1) and (self.parent.IsClear(self.pos[0]-1,self.pos[1]-1) or self.parent.IsWhite(self.pos[0]-1,self.pos[1]-1)):
                    self.pos=(self.pos[0]-1,self.pos[1]-1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0]+1,self.pos[1]+1),self.pos))
                    self.pos=(self.pos[0]+1,self.pos[1]+1)
                if self.parent.IsValid(self.pos[0],self.pos[1]-1) and (self.parent.IsClear(self.pos[0],self.pos[1]-1) or self.parent.IsWhite(self.pos[0],self.pos[1]-1)):
                    self.pos=(self.pos[0],self.pos[1]-1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0],self.pos[1]+1),self.pos))
                    self.pos=(self.pos[0],self.pos[1]+1)
                if self.parent.IsValid(self.pos[0]+1,self.pos[1]-1) and (self.parent.IsClear(self.pos[0]+1,self.pos[1]-1) or self.parent.IsWhite(self.pos[0]+1,self.pos[1]-1)):
                    self.pos=(self.pos[0]+1,self.pos[1]-1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        legalMoves.append(((self.pos[0]-1,self.pos[1]+1),self.pos))
                    self.pos=(self.pos[0]-1,self.pos[1]+1)
                if self.shortCastleRights and not self.parent.IsInCheck(self.pos[0],self.pos[1]) and self.parent.IsClear(self.pos[0],self.pos[1]+1) and self.parent.IsClear(self.pos[0],self.pos[1]+2):
                    self.pos=(self.pos[0],self.pos[1]+1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        self.pos=(self.pos[0],self.pos[1]+1)
                        if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                            legalMoves.append(((self.pos[0],self.pos[1]-2),self.pos,'short'))
                        self.pos=(self.pos[0],self.pos[1]-1)
                    self.pos=(self.pos[0],self.pos[1]-1)
                if self.longCastleRights and not self.parent.IsInCheck(self.pos[0],self.pos[1]) and self.parent.IsClear(self.pos[0],self.pos[1]-1) and self.parent.IsClear(self.pos[0],self.pos[1]-2):
                    self.pos=(self.pos[0],self.pos[1]-1)
                    if not self.parent.IsInCheck(self.pos[0],self.pos[1]):
                        self.pos=(self.pos[0],self.pos[1]-1)
                        if not self.parent.IsInCheck(self.pos[0],self.pos[1]-1):
                            legalMoves.append(((self.pos[0],self.pos[1]-2),self.pos,'short'))
                        self.pos=(self.pos[0],self.pos[1]+1)
                    self.pos=(self.pos[0],self.pos[1]+1)
            else:
                legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1])))
                legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]+1)))
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]+1)))
                legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]+1)))
                legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1])))
                legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]-1)))
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]-1)))
                legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]-1)))
            return legalMoves
    class WhiteQueen:
        def __init__(self,parent,id='Q',pos=(0,3)):
            self.parent=parent
            self.id=id
            self.pos=pos
        def LegalMoves(self):
            legalMoves=[]
            n=1
            while self.parent.IsValid(self.pos[0]+n,self.pos[1]) and self.parent.IsClear(self.pos[0]+n,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]+n,self.pos[1])))
                n+=1
            if self.parent.IsValid(self.pos[0]+n,self.pos[1]) and self.parent.IsBlack(self.pos[0]+n,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]+n,self.pos[1])))
            w=1
            while self.parent.IsValid(self.pos[0],self.pos[1]+w) and self.parent.IsClear(self.pos[0],self.pos[1]+w):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]+w)))
                w+=1
            if self.parent.IsValid(self.pos[0],self.pos[1]+w) and self.parent.IsBlack(self.pos[0],self.pos[1]+w):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]+w)))
            s=1
            while self.parent.IsValid(self.pos[0]-s,self.pos[1]) and self.parent.IsClear(self.pos[0]-s,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]-s,self.pos[1])))
                s+=1
            if self.parent.IsValid(self.pos[0]-s,self.pos[1]) and self.parent.IsBlack(self.pos[0]-s,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]-s,self.pos[1])))
            e=1
            while self.parent.IsValid(self.pos[0],self.pos[1]-e) and self.parent.IsClear(self.pos[0],self.pos[1]-e):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]-e)))
                e+=1
            if self.parent.IsValid(self.pos[0],self.pos[1]-e) and self.parent.IsBlack(self.pos[0],self.pos[1]-e):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]-e)))
            nw=1
            while self.parent.IsValid(self.pos[0]+nw,self.pos[1]+nw) and self.parent.IsClear(self.pos[0]+nw,self.pos[1]+nw):
                legalMoves.append((self.pos,(self.pos[0]+nw,self.pos[1]+nw)))
                nw+=1
            if self.parent.IsValid(self.pos[0]+nw,self.pos[1]+nw) and self.parent.IsBlack(self.pos[0]+nw,self.pos[1]+nw):
                legalMoves.append((self.pos,(self.pos[0]+nw,self.pos[1]+nw)))
            sw=1
            while self.parent.IsValid(self.pos[0]-sw,self.pos[1]+sw) and self.parent.IsClear(self.pos[0]-sw,self.pos[1]+sw):
                legalMoves.append((self.pos,(self.pos[0]-sw,self.pos[1]+sw)))
                sw+=1
            if self.parent.IsValid(self.pos[0]-sw,self.pos[1]+sw) and self.parent.IsBlack(self.pos[0]-sw,self.pos[1]+sw):
                legalMoves.append((self.pos,(self.pos[0]-sw,self.pos[1]+sw)))
            se=1
            while self.parent.IsValid(self.pos[0]-se,self.pos[1]-se) and self.parent.IsClear(self.pos[0]-se,self.pos[1]-se):
                legalMoves.append((self.pos,(self.pos[0]-se,self.pos[1]-se)))
                se+=1
            if self.parent.IsValid(self.pos[0]-se,self.pos[1]-se) and self.parent.IsBlack(self.pos[0]-se,self.pos[1]-se):
                legalMoves.append((self.pos,(self.pos[0]-se,self.pos[1]-se)))
            ne=1
            while self.parent.IsValid(self.pos[0]+ne,self.pos[1]-ne) and self.parent.IsClear(self.pos[0]+ne,self.pos[1]-ne):
                legalMoves.append((self.pos,(self.pos[0]+ne,self.pos[1]-ne)))
                ne+=1
            if self.parent.IsValid(self.pos[0]+ne,self.pos[1]-ne) and self.parent.IsBlack(self.pos[0]+ne,self.pos[1]-ne):
                legalMoves.append((self.pos,(self.pos[0]+ne,self.pos[1]-ne)))
            return legalMoves
    class BlackQueen:
        def __init__(self,parent,id='q',pos=(7,3)):
            self.parent=parent
            self.id=id
            self.pos=pos
        def LegalMoves(self):
            legalMoves=[]
            n=1
            while self.parent.IsValid(self.pos[0]+n,self.pos[1]) and self.parent.IsClear(self.pos[0]+n,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]+n,self.pos[1])))
                n+=1
            if self.parent.IsValid(self.pos[0]+n,self.pos[1]) and self.parent.IsWhite(self.pos[0]+n,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]+n,self.pos[1])))
            w=1
            while self.parent.IsValid(self.pos[0],self.pos[1]+w) and self.parent.IsClear(self.pos[0],self.pos[1]+w):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]+w)))
                w+=1
            if self.parent.IsValid(self.pos[0],self.pos[1]+w) and self.parent.IsWhite(self.pos[0],self.pos[1]+w):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]+w)))
            s=1
            while self.parent.IsValid(self.pos[0]-s,self.pos[1]) and self.parent.IsClear(self.pos[0]-s,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]-s,self.pos[1])))
                s+=1
            if self.parent.IsValid(self.pos[0]-s,self.pos[1]) and self.parent.IsWhite(self.pos[0]-s,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]-s,self.pos[1])))
            e=1
            while self.parent.IsValid(self.pos[0],self.pos[1]-e) and self.parent.IsClear(self.pos[0],self.pos[1]-e):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]-e)))
                e+=1
            if self.parent.IsValid(self.pos[0],self.pos[1]-e) and self.parent.IsWhite(self.pos[0],self.pos[1]-e):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]-e)))
            nw=1
            while self.parent.IsValid(self.pos[0]+nw,self.pos[1]+nw) and self.parent.IsClear(self.pos[0]+nw,self.pos[1]+nw):
                legalMoves.append((self.pos,(self.pos[0]+nw,self.pos[1]+nw)))
                nw+=1
            if self.parent.IsValid(self.pos[0]+nw,self.pos[1]+nw) and self.parent.IsWhite(self.pos[0]+nw,self.pos[1]+nw):
                legalMoves.append((self.pos,(self.pos[0]+nw,self.pos[1]+nw)))
            sw=1
            while self.parent.IsValid(self.pos[0]-sw,self.pos[1]+sw) and self.parent.IsClear(self.pos[0]-sw,self.pos[1]+sw):
                legalMoves.append((self.pos,(self.pos[0]-sw,self.pos[1]+sw)))
                sw+=1
            if self.parent.IsValid(self.pos[0]-sw,self.pos[1]+sw) and self.parent.IsWhite(self.pos[0]-sw,self.pos[1]+sw):
                legalMoves.append((self.pos,(self.pos[0]-sw,self.pos[1]+sw)))
            se=1
            while self.parent.IsValid(self.pos[0]-se,self.pos[1]-se) and self.parent.IsClear(self.pos[0]-se,self.pos[1]-se):
                legalMoves.append((self.pos,(self.pos[0]-se,self.pos[1]-se)))
                se+=1
            if self.parent.IsValid(self.pos[0]-se,self.pos[1]-se) and self.parent.IsWhite(self.pos[0]-se,self.pos[1]-se):
                legalMoves.append((self.pos,(self.pos[0]-se,self.pos[1]-se)))
            ne=1
            while self.parent.IsValid(self.pos[0]+ne,self.pos[1]-ne) and self.parent.IsClear(self.pos[0]+ne,self.pos[1]-ne):
                legalMoves.append((self.pos,(self.pos[0]+ne,self.pos[1]-ne)))
                ne+=1
            if self.parent.IsValid(self.pos[0]+ne,self.pos[1]-ne) and self.parent.IsWhite(self.pos[0]+ne,self.pos[1]-ne):
                legalMoves.append((self.pos,(self.pos[0]+ne,self.pos[1]-ne)))
            return legalMoves
    class WhiteBishop:
        def __init__(self,parent,id='B1',pos=(0,2)):
            self.parent=parent
            self.id=id
            self.pos=pos
        def LegalMoves(self):
            legalMoves=[]
            nw=1
            while self.parent.IsValid(self.pos[0]+nw,self.pos[1]+nw) and self.parent.IsClear(self.pos[0]+nw,self.pos[1]+nw):
                legalMoves.append((self.pos,(self.pos[0]+nw,self.pos[1]+nw)))
                nw+=1
            if self.parent.IsValid(self.pos[0]+nw,self.pos[1]+nw) and self.parent.IsBlack(self.pos[0]+nw,self.pos[1]+nw):
                legalMoves.append((self.pos,(self.pos[0]+nw,self.pos[1]+nw)))
            sw=1
            while self.parent.IsValid(self.pos[0]-sw,self.pos[1]+sw) and self.parent.IsClear(self.pos[0]-sw,self.pos[1]+sw):
                legalMoves.append((self.pos,(self.pos[0]-sw,self.pos[1]+sw)))
                sw+=1
            if self.parent.IsValid(self.pos[0]-sw,self.pos[1]+sw) and self.parent.IsBlack(self.pos[0]-sw,self.pos[1]+sw):
                legalMoves.append((self.pos,(self.pos[0]-sw,self.pos[1]+sw)))
            se=1
            while self.parent.IsValid(self.pos[0]-se,self.pos[1]-se) and self.parent.IsClear(self.pos[0]-se,self.pos[1]-se):
                legalMoves.append((self.pos,(self.pos[0]-se,self.pos[1]-se)))
                se+=1
            if self.parent.IsValid(self.pos[0]-se,self.pos[1]-se) and self.parent.IsBlack(self.pos[0]-se,self.pos[1]-se):
                legalMoves.append((self.pos,(self.pos[0]-se,self.pos[1]-se)))
            ne=1
            while self.parent.IsValid(self.pos[0]+ne,self.pos[1]-ne) and self.parent.IsClear(self.pos[0]+ne,self.pos[1]-ne):
                legalMoves.append((self.pos,(self.pos[0]+ne,self.pos[1]-ne)))
                ne+=1
            if self.parent.IsValid(self.pos[0]+ne,self.pos[1]-ne) and self.parent.IsBlack(self.pos[0]+ne,self.pos[1]-ne):
                legalMoves.append((self.pos,(self.pos[0]+ne,self.pos[1]-ne)))
            return legalMoves
    class BlackBishop:
        def __init__(self,parent,id='b1',pos=(7,2)):
            self.parent=parent
            self.id=id
            self.pos=pos
        def LegalMoves(self):
            legalMoves=[]
            nw=1
            while self.parent.IsValid(self.pos[0]+nw,self.pos[1]+nw) and self.parent.IsClear(self.pos[0]+nw,self.pos[1]+nw):
                legalMoves.append((self.pos,(self.pos[0]+nw,self.pos[1]+nw)))
                nw+=1
            if self.parent.IsValid(self.pos[0]+nw,self.pos[1]+nw) and self.parent.IsWhite(self.pos[0]+nw,self.pos[1]+nw):
                legalMoves.append((self.pos,(self.pos[0]+nw,self.pos[1]+nw)))
            sw=1
            while self.parent.IsValid(self.pos[0]-sw,self.pos[1]+sw) and self.parent.IsClear(self.pos[0]-sw,self.pos[1]+sw):
                legalMoves.append((self.pos,(self.pos[0]-sw,self.pos[1]+sw)))
                sw+=1
            if self.parent.IsValid(self.pos[0]-sw,self.pos[1]+sw) and self.parent.IsWhite(self.pos[0]-sw,self.pos[1]+sw):
                legalMoves.append((self.pos,(self.pos[0]-sw,self.pos[1]+sw)))
            se=1
            while self.parent.IsValid(self.pos[0]-se,self.pos[1]-se) and self.parent.IsClear(self.pos[0]-se,self.pos[1]-se):
                legalMoves.append((self.pos,(self.pos[0]-se,self.pos[1]-se)))
                se+=1
            if self.parent.IsValid(self.pos[0]-se,self.pos[1]-se) and self.parent.IsWhite(self.pos[0]-se,self.pos[1]-se):
                legalMoves.append((self.pos,(self.pos[0]-se,self.pos[1]-se)))
            ne=1
            while self.parent.IsValid(self.pos[0]+ne,self.pos[1]-ne) and self.parent.IsClear(self.pos[0]+ne,self.pos[1]-ne):
                legalMoves.append((self.pos,(self.pos[0]+ne,self.pos[1]-ne)))
                ne+=1
            if self.parent.IsValid(self.pos[0]+ne,self.pos[1]-ne) and self.parent.IsWhite(self.pos[0]+ne,self.pos[1]-ne):
                legalMoves.append((self.pos,(self.pos[0]+ne,self.pos[1]-ne)))
            return legalMoves
    class WhiteKnight:
        def __init__(self,parent,id='N1',pos=(0,1)):
            self.parent=parent
            self.id=id
            self.pos=pos
        def LegalMoves(self):
            legalMoves=[]
            i,j=self.pos[0]+2,self.pos[1]+1
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsBlack(i,j)):
                legalMoves.append((self.pos,(i,j)))
            i,j=self.pos[0]+1,self.pos[1]+2
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsBlack(i,j)):
                legalMoves.append((self.pos,(i,j)))
            i,j=self.pos[0]-1,self.pos[1]+2
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsBlack(i,j)):
                legalMoves.append((self.pos,(i,j)))
            i,j=self.pos[0]-2,self.pos[1]+1
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsBlack(i,j)):
                legalMoves.append((self.pos,(i,j)))
            i,j=self.pos[0]-2,self.pos[1]-1
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsBlack(i,j)):
                legalMoves.append((self.pos,(i,j)))
            i,j=self.pos[0]-1,self.pos[1]-2
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsBlack(i,j)):
                legalMoves.append((self.pos,(i,j)))
            i,j=self.pos[0]+1,self.pos[1]-2
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsBlack(i,j)):
                legalMoves.append((self.pos,(i,j)))
            i,j=self.pos[0]+2,self.pos[1]-1
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsBlack(i,j)):
                legalMoves.append((self.pos,(i,j)))
            return legalMoves
    class BlackKnight:
        def __init__(self,parent,id='n1',pos=(7,1)):
            self.parent=parent
            self.id=id
            self.pos=pos
        def LegalMoves(self):
            legalMoves=[]
            i,j=self.pos[0]+2,self.pos[1]+1
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsWhite(i,j)):
                legalMoves.append((self.pos,(i,j)))
            i,j=self.pos[0]+1,self.pos[1]+2
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsWhite(i,j)):
                legalMoves.append((self.pos,(i,j)))
            i,j=self.pos[0]-1,self.pos[1]+2
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsWhite(i,j)):
                legalMoves.append((self.pos,(i,j)))
            i,j=self.pos[0]-2,self.pos[1]+1
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsWhite(i,j)):
                legalMoves.append((self.pos,(i,j)))
            i,j=self.pos[0]-2,self.pos[1]-1
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsWhite(i,j)):
                legalMoves.append((self.pos,(i,j)))
            i,j=self.pos[0]-1,self.pos[1]-2
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsWhite(i,j)):
                legalMoves.append((self.pos,(i,j)))
            i,j=self.pos[0]+1,self.pos[1]-2
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsWhite(i,j)):
                legalMoves.append((self.pos,(i,j)))
            i,j=self.pos[0]+2,self.pos[1]-1
            if self.parent.IsValid(i,j) and (self.parent.IsClear(i,j) or self.parent.IsWhite(i,j)):
                legalMoves.append((self.pos,(i,j)))
            return legalMoves
    class WhiteRook:
        def __init__(self,parent,id='R1',pos=(0,0)):
            self.parent=parent
            self.id=id
            self.pos=pos
        def LegalMoves(self):
            legalMoves=[]
            n=1
            while self.parent.IsValid(self.pos[0]+n,self.pos[1]) and self.parent.IsClear(self.pos[0]+n,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]+n,self.pos[1])))
                n+=1
            if self.parent.IsValid(self.pos[0]+n,self.pos[1]) and self.parent.IsBlack(self.pos[0]+n,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]+n,self.pos[1])))
            w=1
            while self.parent.IsValid(self.pos[0],self.pos[1]+w) and self.parent.IsClear(self.pos[0],self.pos[1]+w):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]+w)))
                w+=1
            if self.parent.IsValid(self.pos[0],self.pos[1]+w) and self.parent.IsBlack(self.pos[0],self.pos[1]+w):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]+w)))
            s=1
            while self.parent.IsValid(self.pos[0]-s,self.pos[1]) and self.parent.IsClear(self.pos[0]-s,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]-s,self.pos[1])))
                s+=1
            if self.parent.IsValid(self.pos[0]-s,self.pos[1]) and self.parent.IsBlack(self.pos[0]-s,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]-s,self.pos[1])))
            e=1
            while self.parent.IsValid(self.pos[0],self.pos[1]-e) and self.parent.IsClear(self.pos[0],self.pos[1]-e):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]-e)))
                e+=1
            if self.parent.IsValid(self.pos[0],self.pos[1]-e) and self.parent.IsBlack(self.pos[0],self.pos[1]-e):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]-e)))
            return legalMoves
    class BlackRook:
        def __init__(self,parent,id='r1',pos=(7,0)):
            self.parent=parent
            self.id=id
            self.pos=pos
        def LegalMoves(self):
            legalMoves=[]
            n=1
            while self.parent.IsValid(self.pos[0]+n,self.pos[1]) and self.parent.IsClear(self.pos[0]+n,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]+n,self.pos[1])))
                n+=1
            if self.parent.IsValid(self.pos[0]+n,self.pos[1]) and self.parent.IsWhite(self.pos[0]+n,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]+n,self.pos[1])))
            w=1
            while self.parent.IsValid(self.pos[0],self.pos[1]+w) and self.parent.IsClear(self.pos[0],self.pos[1]+w):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]+w)))
                w+=1
            if self.parent.IsValid(self.pos[0],self.pos[1]+w) and self.parent.IsWhite(self.pos[0],self.pos[1]+w):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]+w)))
            s=1
            while self.parent.IsValid(self.pos[0]-s,self.pos[1]) and self.parent.IsClear(self.pos[0]-s,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]-s,self.pos[1])))
                s+=1
            if self.parent.IsValid(self.pos[0]-s,self.pos[1]) and self.parent.IsWhite(self.pos[0]-s,self.pos[1]):
                legalMoves.append((self.pos,(self.pos[0]-s,self.pos[1])))
            e=1
            while self.parent.IsValid(self.pos[0],self.pos[1]-e) and self.parent.IsClear(self.pos[0],self.pos[1]-e):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]-e)))
                e+=1
            if self.parent.IsValid(self.pos[0],self.pos[1]-e) and self.parent.IsWhite(self.pos[0],self.pos[1]-e):
                legalMoves.append((self.pos,(self.pos[0],self.pos[1]-e)))
            return legalMoves
    class WhitePawn:
        def __init__(self,parent,id='P1',pos=(1,0)):
            self.parent=parent
            self.id=id
            self.pos=pos
        def LegalMoves(self):
            legalMoves=[]
            if self.pos[0]==1:
                for piece in self.parent.pieces:
                    if piece!=self and piece.pos[1]==self.pos[1] and piece.pos[0]==self.pos[0]+1:
                        break
                else:
                    legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1])))
                    for piece in self.parent.pieces:
                        if piece!=self and piece.pos[1]==self.pos[1] and piece.pos[0]==self.pos[0]+2:
                            break
                    else:
                        legalMoves.append((self.pos,(self.pos[0]+2,self.pos[1])))
                for piece in self.parent.pieces:
                    if piece!=self and piece.pos[0]==self.pos[0]+1 and piece.id.islower():
                        if piece.pos[1]+1==self.pos[1]:
                            legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]-1)))
                        if piece.pos[1]-1==self.pos[1]:
                            legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]+1)))
            elif 1<self.pos[0]<6:
                for piece in self.parent.pieces:
                    if piece!=self and piece.pos[1]==self.pos[1] and piece.pos[0]==self.pos[0]+1:
                        break
                else:
                    legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1])))
                for piece in self.parent.pieces:
                    if piece!=self and piece.pos[0]==self.pos[0]+1 and piece.id.islower():
                        if piece.pos[1]+1==self.pos[1]:
                            legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]-1)))
                        if piece.pos[1]-1==self.pos[1]:
                            legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]+1)))
            elif self.pos[0]==6:
                for piece in self.parent.pieces:
                    if piece!=self and piece.pos[1]==self.pos[1] and piece.pos[0]==self.pos[0]+1:
                        break
                else:
                    legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]),'Q'))
                    legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]),'R'))
                    legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]),'B'))
                    legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]),'N'))
                for piece in self.parent.pieces:
                    if piece!=self and piece.pos[0]==self.pos[0]+1 and piece.id.islower():
                        if piece.pos[1]+1==self.pos[1]:
                            legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]-1),'Q'))
                            legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]-1),'R'))
                            legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]-1),'B'))
                            legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]-1),'N'))
                        if piece.pos[1]-1==self.pos[1]:
                            legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]+1),'Q'))
                            legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]+1),'R'))
                            legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]+1),'B'))
                            legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]+1),'N'))
            if self.pos[0]==4:
                for piece in self.parent.pieces:
                    if piece.id[0]=='p' and piece.pos[0]==self.pos[0]:
                        if self.parent.moves[-1][0]==(self.pos[0]+2,self.pos[1]+1) and self.parent.moves[-1][1]==(self.pos[0],self.pos[1]+1):
                            legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]+1),'en'))
                        if self.parent.moves[-1][0]==(self.pos[0]+2,self.pos[1]-1) and self.parent.moves[-1][1]==(self.pos[0],self.pos[1]-1):
                            legalMoves.append((self.pos,(self.pos[0]+1,self.pos[1]-1),'en'))
            return legalMoves
    class BlackPawn:
        def __init__(self,parent,id='p1',pos=(6,0)):
            self.parent=parent
            self.id=id
            self.pos=pos
        def LegalMoves(self):
            legalMoves=[]
            if self.pos[0]==6:
                for piece in self.parent.pieces:
                    if piece!=self and piece.pos[1]==self.pos[1] and piece.pos[0]==self.pos[0]-1:
                        break
                else:
                    legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1])))
                    for piece in self.parent.pieces:
                        if piece!=self and piece.pos[1]==self.pos[1] and piece.pos[0]==self.pos[0]-2:
                            break
                    else:
                        legalMoves.append((self.pos,(self.pos[0]-2,self.pos[1])))
                for piece in self.parent.pieces:
                    if piece!=self and piece.pos[0]==self.pos[0]-1 and piece.id.isupper():
                        if piece.pos[1]+1==self.pos[1]:
                            legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]-1)))
                        if piece.pos[1]-1==self.pos[1]:
                            legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]+1)))
            elif 1<self.pos[0]<6:
                for piece in self.parent.pieces:
                    if piece!=self and piece.pos[1]==self.pos[1] and piece.pos[0]==self.pos[0]-1:
                        break
                else:
                    legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1])))
                for piece in self.parent.pieces:
                    if piece!=self and piece.pos[0]==self.pos[0]-1 and piece.id.isupper():
                        if piece.pos[1]+1==self.pos[1]:
                            legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]-1)))
                        if piece.pos[1]-1==self.pos[1]:
                            legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]+1)))
            elif self.pos[0]==1:
                for piece in self.parent.pieces:
                    if piece!=self and piece.pos[1]==self.pos[1] and piece.pos[0]==self.pos[0]+1:
                        break
                else:
                    legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]),'Q'))
                    legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]),'R'))
                    legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]),'B'))
                    legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]),'N'))
                for piece in self.parent.pieces:
                    if piece!=self and piece.pos[0]==self.pos[0]-1 and piece.id.isupper():
                        if piece.pos[1]+1==self.pos[1]:
                            legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]-1),'Q'))
                            legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]-1),'R'))
                            legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]-1),'B'))
                            legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]-1),'N'))
                        if piece.pos[1]-1==self.pos[1]:
                            legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]+1),'Q'))
                            legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]+1),'R'))
                            legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]+1),'B'))
                            legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]+1),'N'))
            if self.pos[0]==3:
                for piece in self.parent.pieces:
                    if piece.id[0]=='P' and piece.pos[0]==self.pos[0]:
                        if self.parent.moves[-1][0]==(self.pos[0]-2,self.pos[1]+1) and self.parent.moves[-1][1]==(self.pos[0],self.pos[1]+1):
                            legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]+1),'en'))
                        if self.parent.moves[-1][0]==(self.pos[0]+2,self.pos[1]-1) and self.parent.moves[-1][1]==(self.pos[0],self.pos[1]-1):
                            legalMoves.append((self.pos,(self.pos[0]-1,self.pos[1]-1),'en'))
            return legalMoves
    def IsValid(self,i,j):
        return 0<=i<=7 and 0<=j<=7
    def IsClear(self,i,j):
        for piece in self.pieces:
            if piece.pos==(i,j):
                return False
        return True
    def IsWhite(self,i,j):
        for piece in self.whitePieces:
            if piece.pos==(i,j):
                return True
        return False
    def IsBlack(self,i,j):
        for piece in self.blackPieces:
            if piece.pos==(i,j):
                return True
        return False
    def IsInCheck(self,i,j):
        if self.moveCount%2==1:
            for piece in self.blackPieces:
                if piece==self.k:
                    moves=piece.LegalMoves(True)
                else:
                    moves=piece.LegalMoves()
                for move in moves:
                    if move[1]==(i,j):
                        return True
            return False
        else:
            for piece in self.whitePieces:
                if piece==self.K:
                    moves=piece.LegalMoves(True)
                else:
                    moves=piece.LegalMoves()
                for move in moves:
                    if move[1]==(i,j):
                        return True
            return False
    def __init__(self):
        self.K=self.WhiteKing(self)
        self.k=self.BlackKing(self)
        self.Q=self.WhiteQueen(self)
        self.q=self.BlackQueen(self)
        self.B1=self.WhiteBishop(self)
        self.B2=self.WhiteBishop(self,'B2',(0,5))
        self.b1=self.BlackBishop(self)
        self.b2=self.BlackBishop(self,'b2',(7,5))
        self.N1=self.WhiteKnight(self)
        self.N2=self.WhiteKnight(self,'N2',(0,6))
        self.n1=self.BlackKnight(self)
        self.n2=self.BlackKnight(self,'n2',(7,6))
        self.R1=self.WhiteRook(self)
        self.R2=self.WhiteRook(self,'R2',(0,7))
        self.r1=self.BlackRook(self)
        self.r2=self.BlackRook(self,'r2',(7,7))
        self.P1=self.WhitePawn(self)
        self.P2=self.WhitePawn(self,'P2',(1,1))
        self.P3=self.WhitePawn(self,'P3',(1,2))
        self.P4=self.WhitePawn(self,'P4',(1,3))
        self.P5=self.WhitePawn(self,'P5',(1,4))
        self.P6=self.WhitePawn(self,'P6',(1,5))
        self.P7=self.WhitePawn(self,'P7',(1,6))
        self.P8=self.WhitePawn(self,'P8',(1,7))
        self.p1=self.BlackPawn(self)
        self.p2=self.BlackPawn(self,'p2',(6,1))
        self.p3=self.BlackPawn(self,'p3',(6,2))
        self.p4=self.BlackPawn(self,'p4',(6,3))
        self.p5=self.BlackPawn(self,'p5',(6,4))
        self.p6=self.BlackPawn(self,'p6',(6,5))
        self.p7=self.BlackPawn(self,'p7',(6,6))
        self.p8=self.BlackPawn(self,'p8',(6,7))
        self.pieces=[self.K,self.k,self.Q,self.q,self.B1,self.B2,self.b1,self.b2,self.N1,self.N2,self.n1,self.n2,
                    self.R1,self.R2,self.r1,self.r2,self.P1,self.P2,self.P3,self.P4,self.P5,self.P6,self.P7,self.P8,
                    self.p1,self.p2,self.p3,self.p4,self.p5,self.p6,self.p7,self.p8]
        self.whitePieces=[piece for piece in self.pieces if piece.id[0].isupper()]
        self.blackPieces=[piece for piece in self.pieces if piece.id[0].islower()]
        self.moveCount=1
        self.moves=[]
    def PieceAt(self,i,j):
        for piece in self.pieces:
            if piece.pos==(i,j):
                return piece
    def LegalMoves(self):
        legalMoves=[]
        illegalMoves=[]
        if self.moveCount%2==1:
            for piece in self.whitePieces:
                if piece==self.K:
                    legalMoves=legalMoves+piece.LegalMoves(False)
                else:
                    legalMoves=legalMoves+piece.LegalMoves()
        else:
            for piece in self.blackPieces:
                if piece==self.k:
                    legalMoves=legalMoves+piece.LegalMoves(False)
                else:
                    legalMoves=legalMoves+piece.LegalMoves()
        for move in legalMoves:
            if self.moveCount%2==1:
                if self.IsClear(move[1][0],move[1][1]):
                    self.PieceAt(move[0][0],move[0][1]).pos=(move[1][0],move[1][1])
                    if self.IsInCheck(self.K.pos[0],self.K.pos[1]):
                        illegalMoves.append(move)
                    self.PieceAt(move[1][0],move[1][1]).pos=(move[0][0],move[0][1])
                else:
                    piece=self.PieceAt(move[1][0],move[1][1])
                    self.pieces.remove(piece)
                    self.blackPieces.remove(piece)
                    self.PieceAt(move[0][0],move[0][1]).pos=(move[1][0],move[1][1])
                    if self.IsInCheck(self.K.pos[0],self.K.pos[1]):
                        illegalMoves.append(move)
                    self.PieceAt(move[1][0],move[1][1]).pos=(move[0][0],move[0][1])
                    self.pieces.append(piece)
                    self.blackPieces.append(piece)
            else:
                if self.IsClear(move[1][0],move[1][1]):
                    self.PieceAt(move[0][0],move[0][1]).pos=(move[1][0],move[1][1])
                    if self.IsInCheck(self.k.pos[0],self.k.pos[1]):
                        illegalMoves.append(move)
                    self.PieceAt(move[1][0],move[1][1]).pos=(move[0][0],move[0][1])
                else:
                    piece=self.PieceAt(move[1][0],move[1][1])
                    self.pieces.remove(piece)
                    self.whitePieces.remove(piece)
                    self.PieceAt(move[0][0],move[0][1]).pos=(move[1][0],move[1][1])
                    if self.IsInCheck(self.k.pos[0],self.k.pos[1]):
                        illegalMoves.append(move)
                    self.PieceAt(move[1][0],move[1][1]).pos=(move[0][0],move[0][1])
                    self.pieces.append(piece)
                    self.whitePieces.append(piece)
        return [move for move in legalMoves if move not in illegalMoves]
    def PlayMove(self,move):
        if len(move)==2:
            if self.IsClear(move[1][0],move[1][1]):
                self.PieceAt(move[0][0],move[0][1]).pos=(move[1][0],move[1][1])
            else:
                piece=self.PieceAt(move[1][0],move[1][1])
                self.pieces.remove(piece)
                if self.moveCount%2==1:
                    self.blackPieces.remove(piece)
                else:
                    self.whitePieces.remove(piece)
                self.PieceAt(move[0][0],move[0][1]).pos=(move[1][0],move[1][1])
            if self.moveCount%2==1:
                if self.K.shortCastleRights:
                    if self.PieceAt(move[1][0],move[1][1])==self.K or self.PieceAt(move[1][0],move[1][1])==self.R2:
                        self.K.shortCastleRights=False
                if self.K.longCastleRights:
                    if self.PieceAt(move[1][0],move[1][1])==self.K or self.PieceAt(move[1][0],move[1][1])==self.R1:
                        self.K.longCastleRights=False
            else:
                if self.k.shortCastleRights:
                    if self.PieceAt(move[1][0],move[1][1])==self.k or self.PieceAt(move[1][0],move[1][1])==self.r2:
                        self.k.shortCastleRights=False
                if self.k.longCastleRights:
                    if self.PieceAt(move[1][0],move[1][1])==self.k or self.PieceAt(move[1][0],move[1][1])==self.r1:
                        self.k.longCastleRights=False
            if self.moveCount%2==1:
                if self.k.shortCastleRights:
                    if self.PieceAt(move[1][0],move[1][1])==self.r2:
                        self.k.shortCastleRights=False
                if self.k.longCastleRights:
                    if self.PieceAt(move[1][0],move[1][1])==self.r1:
                        self.k.longCastleRights=False
            else:
                if self.K.shortCastleRights:
                    if self.PieceAt(move[1][0],move[1][1])==self.R2:
                        self.K.shortCastleRights=False
                if self.K.longCastleRights:
                    if self.PieceAt(move[1][0],move[1][1])==self.R1:
                        self.K.longCastleRights=False
        else:
            if move[2]=='short':
                if self.moveCount%2==1:
                    self.K.pos=(move[1][0],move[1][1])
                    self.R2.pos=(move[1][0],move[1][1]-1)
                    self.K.shortCastleRights=False
                    self.K.longCastleRights=False
                else:
                    self.k.pos=(move[1][0],move[1][1])
                    self.r2.pos=(move[1][0],move[1][1]-1)
                    self.k.shortCastleRights=False
                    self.k.longCastleRights=False
            elif move[2]=='long':
                if self.moveCount%2==1:
                    self.K.pos=(move[1][0],move[1][1])
                    self.R1.pos=(move[1][0],move[1][1]+1)
                    self.K.longCastleRights=False
                    self.K.shortCastleRights=False
                else:
                    self.k.pos=(move[1][0],move[1][1])
                    self.r1.pos=(move[1][0],move[1][1]+1)
                    self.k.longCastleRights=False
                    self.k.shortCastleRights=False
            elif move[2]=='en':
                if self.moveCount%2==1:
                    piece=self.PieceAt(move[1][0]-1,move[1][1])
                    self.pieces.remove(piece)
                    self.blackPieces.remove(piece)
                else:
                    piece=self.PieceAt(move[1][0]+1,move[1][1])
                    self.pieces.remove(piece)
                    self.whitePieces.remove(piece)
            elif move[2]=='Q':
                if self.moveCount%2==1:
                    queen=self.WhiteQueen(self,'Q*',move[1])
                    piece=self.PieceAt(move[0][0],move[0][1])
                    self.pieces.remove(piece)
                    self.whitePieces.remove(piece)
                    if not self.IsClear(move[1][0],move[1][1]):
                        piece=self.PieceAt(move[1][0],move[1][1])
                        self.pieces.remove(piece)
                        self.blackPieces.remove(piece)
                    self.pieces.append(queen)
                    self.whitePieces.append(queen)
                else:
                    queen=self.BlackQueen(self,'q*',move[1])
                    piece=self.PieceAt(move[0][0],move[0][1])
                    self.pieces.remove(piece)
                    self.blackPieces.remove(piece)
                    if not self.IsClear(move[1][0],move[1][1]):
                        piece=self.PieceAt(move[1][0],move[1][1])
                        self.pieces.remove(piece)
                        self.whitePieces.remove(piece)
                    self.pieces.append(queen)
                    self.blackPieces.append(queen)
            elif move[2]=='R':
                if self.moveCount%2==1:
                    rook=self.WhiteRook(self,'R*',move[1])
                    piece=self.PieceAt(move[0][0],move[0][1])
                    self.pieces.remove(piece)
                    self.whitePieces.remove(piece)
                    if not self.IsClear(move[1][0],move[1][1]):
                        piece=self.PieceAt(move[1][0],move[1][1])
                        self.pieces.remove(piece)
                        self.blackPieces.remove(piece)
                    self.pieces.append(rook)
                    self.whitePieces.append(rook)
                else:
                    rook=self.BlackRook(self,'r*',move[1])
                    piece=self.PieceAt(move[0][0],move[0][1])
                    self.pieces.remove(piece)
                    self.blackPieces.remove(piece)
                    if not self.IsClear(move[1][0],move[1][1]):
                        piece=self.PieceAt(move[1][0],move[1][1])
                        self.pieces.remove(piece)
                        self.whitePieces.remove(piece)
                    self.pieces.append(rook)
                    self.blackPieces.append(rook)
            elif move[2]=='B':
                if self.moveCount%2==1:
                    bishop=self.WhiteBishop(self,'B*',move[1])
                    piece=self.PieceAt(move[0][0],move[0][1])
                    self.pieces.remove(piece)
                    self.whitePieces.remove(piece)
                    if not self.IsClear(move[1][0],move[1][1]):
                        piece=self.PieceAt(move[1][0],move[1][1])
                        self.pieces.remove(piece)
                        self.blackPieces.remove(piece)
                    self.pieces.append(bishop)
                    self.whitePieces.append(bishop)
                else:
                    bishop=self.BlackBishop(self,'b*',move[1])
                    piece=self.PieceAt(move[0][0],move[0][1])
                    self.pieces.remove(piece)
                    self.blackPieces.remove(piece)
                    if not self.IsClear(move[1][0],move[1][1]):
                        piece=self.PieceAt(move[1][0],move[1][1])
                        self.pieces.remove(piece)
                        self.whitePieces.remove(piece)
                    self.pieces.append(bishop)
                    self.blackPieces.append(bishop)
            elif move[2]=='N':
                if self.moveCount%2==1:
                    knight=self.WhiteKnight(self,'N*',move[1])
                    piece=self.PieceAt(move[0][0],move[0][1])
                    self.pieces.remove(piece)
                    self.whitePieces.remove(piece)
                    if not self.IsClear(move[1][0],move[1][1]):
                        piece=self.PieceAt(move[1][0],move[1][1])
                        self.pieces.remove(piece)
                        self.blackPieces.remove(piece)
                    self.pieces.append(knight)
                    self.whitePieces.append(knight)
                else:
                    knight=self.BlackKnight(self,'n*',move[1])
                    piece=self.PieceAt(move[0][0],move[0][1])
                    self.pieces.remove(piece)
                    self.blackPieces.remove(piece)
                    if not self.IsClear(move[1][0],move[1][1]):
                        piece=self.PieceAt(move[1][0],move[1][1])
                        self.pieces.remove(piece)
                        self.whitePieces.remove(piece)
                    self.pieces.append(knight)
                    self.blackPieces.append(knight)
        self.moveCount+=1
        self.moves.append(move)
    def SelectMove(self,depth=3,levelUp=None):
        gameOver=self.GameOver()
        if gameOver=='Checkmate':
            if self.moveCount%2==1:
                return -10000,None
            else:
                return 10000,None
        elif gameOver=='Stalemate':
            return 0,None
        elif depth==0:
            legalMoves=self.LegalMoves()
            numMoves=len(legalMoves)
            moveEvals=[]
            for legalMove in legalMoves:
                pseudoBoard=ChessBoard()
                for move in self.moves:
                    pseudoBoard.PlayMove(move)
                pseudoBoard.PlayMove(legalMove)
                moveEvals.append(pseudoBoard.Evaluate())
                if self.moveCount%2==1:
                    if levelUp is not None and moveEvals[-1]>levelUp:
                        return moveEvals[-1],legalMove
                else:
                    if levelUp is not None and moveEvals[-1]<levelUp:
                        return moveEvals[-1],legalMove
            bestNum=0
            for num in range(1,numMoves):
                if self.moveCount%2==1:
                    if moveEvals[num]>moveEvals[bestNum]:
                        bestNum=num
            return moveEvals[bestNum],legalMoves[bestNum]
        else:
            legalMoves=self.LegalMoves()
            numMoves=len(legalMoves)
            moveEvals=[]
            bestEvalSoFar=None
            bestNum=None
            for legalMove in legalMoves:
                pseudoBoard=ChessBoard()
                for move in self.moves:
                    pseudoBoard.PlayMove(move)
                pseudoBoard.PlayMove(legalMove)
                if bestEvalSoFar is None:
                    moveEvals.append(pseudoBoard.SelectMove(depth-1)[0])
                    bestEvalSoFar=moveEvals[-1]
                    bestNum=0
                else:
                    moveEvals.append(pseudoBoard.SelectMove(depth-1,bestEvalSoFar)[0])
                    if self.moveCount%2==1:
                        if moveEvals[-1]>bestEvalSoFar:
                            bestEvalSoFar=moveEvals[-1]
                            bestNum=len(moveEvals)-1
                    else:
                        if moveEvals[-1]<bestEvalSoFar:
                            bestEvalSoFar=moveEvals[-1]
                            bestNum=len(moveEvals)-1
                if levelUp is not None:
                    if self.moveCount%2==1:
                        if levelUp<moveEvals[-1]:
                            return moveEvals[-1],legalMove
                    else:
                        if levelUp>moveEvals[-1]:
                            return moveEvals[-1],legalMove
            return moveEvals[bestNum],legalMoves[bestNum]
    def GameOver(self):
        if not self.LegalMoves():
            if self.moveCount%2==1:
                if self.IsInCheck(self.K.pos[0],self.K.pos[1]):
                    return 'Checkmate'
                return 'Stalemate'
            else:
                if self.IsInCheck(self.k.pos[0],self.k.pos[1]):
                    return 'Checkmate'
                return 'Stalemate'
    def Evaluate(self):
        if self.GameOver()=='Checkmate':
            if self.moveCount%2==1:
                return 10000,None
            else:
                return -10000,None
        elif self.GameOver()=='Stalemate':
            return 0,None
        eval=0
        for piece in self.whitePieces:
            if piece.id[0]=='P':
                eval+=1
            elif piece.id[0]=='B' or piece.id[0]=='N':
                eval+=3
            elif piece.id[0]=='R':
                eval+=5
            elif piece.id[0]=='Q':
                eval+=9
        for piece in self.blackPieces:
            if piece.id[0]=='p':
                eval-=1
            elif piece.id[0]=='b' or piece.id[0]=='n':
                eval-=3
            elif piece.id[0]=='r':
                eval-=5
            elif piece.id[0]=='q':
                eval-=9
        for piece in self.whitePieces:
            if piece.id[0]=='P':
                if self.moveCount<=10:
                    if piece.pos[0]>1:
                        if 2<=piece.pos[1]<=5:
                            eval+=1
                        else:
                            eval-=1
            elif piece.id[0]=='N':
                if 2<=piece.pos[0]<=4 and 2<=piece.pos[1]<=5:
                    eval+=3
                else:
                    eval-=1
            elif piece.id[0]=='B':
                if piece.pos==(0,0) or piece.pos==(0,7):
                    eval-=1
            elif piece.id[0]=='R':
                if piece.id=='R1':
                    if 2<self.K.pos[1]<6 and not self.K.longCastleRights:
                        eval-=5
                elif piece.id=='R2':
                    if 2<self.K.pos[1]<6 and not self.K.shortCastleRights:
                        eval-=5
            elif piece.id[0]=='Q':
                continue
            else:
                if 2<piece.pos[0]<6 and not piece.shortCastleRights and not piece.longCastleRights:
                    eval-=5
        for piece in self.blackPieces:
            if piece.id[0]=='p':
                if self.moveCount<=10:
                    if piece.pos[0]<6:
                        if 2<=piece.pos[1]<=5:
                            eval-=1
                        else:
                            eval+=1
            elif piece.id[0]=='n':
                if 5<=piece.pos[0]<=3 and 2<=piece.pos[1]<=5:
                    eval-=3
                else:
                    eval+=1
            elif piece.id[0]=='b':
                if piece.pos==(7,0) or piece.pos==(7,7):
                    eval+=1
            elif piece.id[0]=='r':
                if piece.id=='r1':
                    if 2<self.k.pos[1]<6 and not self.k.longCastleRights:
                        eval+=5
                elif piece.id=='r2':
                    if 2<self.k.pos[1]<6 and not self.k.shortCastleRights:
                        eval+=5
            elif piece.id[0]=='q':
                continue
            else:
                if 2<piece.pos[0]<6 and not piece.shortCastleRights and not piece.longCastleRights:
                    eval+=5
        return eval
    def DisplayBoard(self):
        virtualBoard=[['__' for _ in range(8)] for _ in range(8)]
        for piece in self.pieces:
            virtualBoard[piece.pos[0]][piece.pos[1]]=piece.id
        for row in range(7,-1,-1):
            print(virtualBoard[row])


board=ChessBoard()
board.DisplayBoard()
if random.randint(0,1)==0:
    print('You play White')
    move=input('Your move:')
    board.PlayMove(move)
    board.DisplayBoard()
else:
    print('I play White')
while True:
    if board.GameOver()=='Checkmate':
        print('You win by Checkmate')
        break
    elif board.GameOver()=='Stalemate':
        print('Stalemate')
    print('My move:')
    board.PlayMove(board.SelectMove()[1])
    board.DisplayBoard()
    if board.GameOver()=='Checkmate':
        print('I win by Checkmate')
        break
    elif board.GameOver()=='Stalemate':
        print('Stalemate')
    move=eval(input('Your move:'))
    board.PlayMove(move)
    board.DisplayBoard()