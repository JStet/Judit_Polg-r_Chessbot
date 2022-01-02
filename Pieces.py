import pygame
import weakref


class Piece:
    _instances = set()

    def __init__(self, icon_path):
        self._instances.add(weakref.ref(self))

        img = pygame.image.load(icon_path)
        self.icon = pygame.transform.scale(img, (90, 90))
        self.position = None
    
    @classmethod
    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead


Q_B_Rook = Piece(icon_path="media/black_pieces/black_3.png")
Q_B_Knight = Piece(icon_path="media/black_pieces/black_5.png")
#Q_B_Bishop = Piece(icon_path="media/black_pieces/black_4.png")
#B_Queen = Piece(icon_path="media/black_pieces/black_2.png")
#B_King = Piece(icon_path="media/black_pieces/black_1.png")

