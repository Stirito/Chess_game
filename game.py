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
    def check_queen(self):
        for line in self.board:
            for tile in line:
                if issubclass(tile.__class__,Piece):
                    pion = tile
                    if pion.is_line(0) and pion.side == "BLANC":

                        self.board[pion.y][pion.x] = Reine("BLANC")
                        self.define_x_y()
                    elif pion.is_line(7) and pion.side == "NOIR":
                        self.board[pion.y][pion.x] = Reine("NOIR")
                        self.define_x_y()

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

            for line in self.board:
                for case in line:
                    if issubclass(case.__class__, Piece):
                        pion = case
                        pion.check_moves(self.window,self.board)

            for line in self.board:
                for case in line:
                    if issubclass(case.__class__, Piece):
                        pion = case
                        if pion.is_selected:
                            pion.show_move(self.window)
            self.check_queen()



            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:


                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for line in self.board:
                            for case in line:
                                if issubclass(case.__class__, Piece):
                                    pion = case
                                    if self.is_on_piece(pion) and pion.is_selected == False:
                                        pion.is_selected = True

                                    else:
                                        if pion.is_selected:
                                            mouse_pos = pygame.mouse.get_pos()
                                            tile_clicked_pos = (tile_clicked_x,tile_clicked_y) = (mouse_pos[0]//self.TILE_SIZE,mouse_pos[1]//self.TILE_SIZE)
                                            tile_clicked = self.board[tile_clicked_y][tile_clicked_x]
                                            if tile_clicked_pos in pion.moves and self.is_tile_is_empty(tile_clicked_x,tile_clicked_y):
                                                pion.move(self.board,tile_clicked_x,tile_clicked_y)
                                            elif not self.is_tile_is_empty(tile_clicked_x,tile_clicked_y) and not pion.pos == (tile_clicked_x,tile_clicked_y):

                                                if issubclass(tile_clicked.__class__, Piece):
                                                    pion_clicked = tile_clicked
                                                    pion_clicked_x = tile_clicked_x
                                                    pion_clicked_y = tile_clicked_y
                                                    if pion_clicked.side != pion.side:
                                                        self.delete_piece_in_tile(pion_clicked_x,pion_clicked_y)
                                                        pion.move(self.board,tile_clicked_x,tile_clicked_y)



                                        else:

                                            pion.is_selected = False
                                        pion.is_selected = False

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