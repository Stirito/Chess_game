import pygame
import sys
from chess_pieces.piece import Cavalier,Roi,Reine,Fou,Tour,Pions,Piece
class Game:
    def __init__(self):

        self.widht = 600
        self.height = 600
        self.window = pygame.display.set_mode(size=(self.widht, self.height))
        self.running = True
        self.starting = False
        self.is_selecting_mode = False
        self.TILE_SIZE = self.widht//8
        self.board = [[Pions("NOIR"),"X","X","X","X","X","X","X"],
                      ["X",Pions("NOIR"),"X","X","X","X","X","X"],
                      ["X","X","X","X","X","X","X","X"],
                      ["X","X","X","X","X","X","X","X"],
                      ["X","X","X","X","X","X","X","X"],
                      ["X",Pions("NOIR"),"X","X","X","X","X","X"],
                      [Pions("BLANC"),"X","X","X","X","X","X","X"],
                      ["X","X","X","X","X","X","X","X"]]
    def define_x_y(self):
        for line in self.board:
            for case in line:
                if issubclass(case.__class__, Piece):
                    pion = case
                    pion.pos = (pion.x,pion.y) = (line.index(pion),self.board.index(line))

    def delete_piece_in_tile(self,x,y):
        self.board[y][x] = "X"
    def is_tile_is_empty(self,x,y):
        return self.board[y][x] == "X"
   

    def debug_board(self):
        for line in self.board:
            print(f"{line}\n")
    def run(self):
        while self.running:
            if self.starting == False:
                self.define_x_y()
                self.starting = True



            self.draw_board()
            self.draw_pieces()

       
    



            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:


                        sys.exit()
                

                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
            pygame.display.flip()


    def draw_board(self):
        for x in range(8):
            for y in range(8):
                tile = pygame.Rect((x*self.TILE_SIZE,y*self.TILE_SIZE),(self.TILE_SIZE,self.TILE_SIZE))
                if y%2 == 0 and x%2 == 0:
                    color = (125,0,0)
                elif y%2 != 0 and  x%2 == 0:
                    color = (255,255,255)
                elif y%2 == 0 and x%2 != 0:
                    color = (255,255,255)
                elif y%2 != 0 and x%2 != 0:
                    color = (125,0,0)


                pygame.draw.rect(self.window,color,tile)

    def is_on_piece(self,pion):
        return pion.x == pygame.mouse.get_pos()[0] // self.TILE_SIZE and pion.y == pygame.mouse.get_pos()[1] // self.TILE_SIZE
    def draw_pieces(self):
        for line in self.board :
            for case in line:
                if isinstance(case,Piece):
                    pion = case
                    pion.show(self.window,self.TILE_SIZE)