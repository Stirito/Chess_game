import pygame
class Piece():
    def __init__(self,side):
        self.x = None
        self.y = None
        self.pos = (self.x,self.y)
        self.image = None
        self.side = side
        self.is_selected = False
        self.moves = []
        self.isattacked = False
    def show(self,window,tile_size):
        if self.image != None:
            size_of_new_image = (tile_size,tile_size)
            newimage = pygame.transform.scale(self.image, size_of_new_image)
            window.blit(newimage,(self.x*tile_size-2.5,self.y*tile_size-2.5))
    def show_move(self,window):
        for move in self.moves:

            if move[0] != "Ennemy":
                center_x = move[0]*(600//8)+((600//8)//2)
                center_y = move[1] * (600 // 8) + ((600 // 8) // 2)
                pygame.draw.circle(window,(0,125,0),(center_x,center_y),15)
            else:
                center_x = move[1][0] * (600 // 8) + ((600 // 8) // 2)
                center_y = move[1][1] * (600 // 8) + ((600 // 8) // 2)
                pygame.draw.circle(window, (0, 125, 0), (center_x, center_y), 25,5)
 
    def check_moves(self,window,board):
        moves = []

    def is_line(self, line):
        return self.y == line

    def move(self, board, new_x, new_y):
        board[new_y][new_x] = self
        board[self.y][self.x] = "X"
        self.x = new_x
        self.y = new_y
        self.pos = (new_x, new_y)

class Pions(Piece):
    def __init__(self,side):
        super().__init__(side)
        self.starting_pos = True
        if side == "BLANC":
            self.image = pygame.image.load("chess_pieces\pion_blanc.png")
        else:
            self.image = pygame.image.load("chess_pieces\pion_noir.png")
        self.image_rect = self.image.get_rect()



class Cavalier(Piece):
    def __init__(self,side):
        super().__init__(side)
        if side == "BLANC":
            self.image = pygame.image.load("chess_pieces\cavalier_blanc.png")
        else:
            self.image = pygame.image.load("chess_pieces\cavalier_noir.png")
        self.image_rect = self.image.get_rect()

class Fou(Piece):
    def __init__(self,side):
        super().__init__(side)
        if side == "BLANC":
            self.image = pygame.image.load("chess_pieces\fou_blanc.png")
        else:
            self.image = pygame.image.load("chess_pieces\fou_noir.png")
        self.image_rect = self.image.get_rect()

class Reine(Piece):
    def __init__(self,side):
        super().__init__(side)
        if side == "BLANC":
            self.image = pygame.image.load("chess_pieces/reine_blanche.png")
        else:
            self.image = pygame.image.load("chess_pieces/reine_noire.png")
        self.image_rect = self.image.get_rect()

class Roi(Piece):
    def __init__(self,side):
        super().__init__(side)
        if side == "BLANC":
            self.image = pygame.image.load("chess_pieces/roi_blanc.png")
        else:
            self.image = pygame.image.load("chess_pieces/roi_noir.png")
        self.image_rect = self.image.get_rect()


class Tour(Piece):
    def __init__(self,side):
        super().__init__(side)
        if side == "BLANC":
            self.image = pygame.image.load("chess_pieces/tour_blanche.png")
        else:
            self.image = pygame.image.load("chess_pieces/tour_noire.png")
        self.image_rect = self.image.get_rect()

