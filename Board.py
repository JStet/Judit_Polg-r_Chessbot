from Pieces import *

# Defining Colours
black = pygame.Color(102, 176, 50)
white = pygame.Color(235, 247, 227)
background = pygame.Color(27, 52, 9)

# Generating list of square names
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
numbers = range(1, 9)
squares = []
for number in numbers:
    for letter in letters:
        squares.append(letter+str(number))

# This class will be used later to draw the board

class Rectangle:
    def __init__(self, pos, color, size):
        self.pos = pos
        self.color = color
        self.size = size

    def draw(self):
        pygame.draw.rect(Board.surface, self.color, pygame.Rect(self.pos, self.size))


#generating coordinates for squares and using them to create a list, which will be used later to draw board
rectangles = []
square_coordinates = {}
y = 0
count = 1
square_count = 0
offset = 5
for o in range(1, 9):
    x = 0
    for i in range(1, 9):
        if count % 2 != 0:
            rectangles.append(Rectangle((x, y), white, (100, 100)))
            square_coordinates[squares[square_count]] = [x + offset , y + offset]
            x += 100
            count += 1
            square_count += 1
        else:
            rectangles.append(Rectangle((x, y), black, (100, 100)))
            square_coordinates[squares[square_count]] = [x + offset, y + offset]
            x += 100
            count += 1
            square_count += 1
    count += 1
    y += 100


class Board:
    def __init__(self):
        self.surface = pygame.Surface((800, 800))
        self.positions = {
            "Q_B_Rook": "a1", "Q_B_Knight": "b1"#, "Q_B_Bishop": "c8", "B_Queen": "d8", "B_King": "e8", "K_B_Bishop": "a8"
        }
        update_board(self.positions)


def update_board(positions):
    Q_B_Rook.position = square_coordinates[positions["Q_B_Rook"]]
    Q_B_Knight.position = square_coordinates[positions["Q_B_Knight"]]
    #Q_B_Bishop.position = positions["Q_B_Bishop"]
    #B_Queen.position = positions["B_Queen"]
    #B_King.position = positions["B_King"]


Board = Board()









