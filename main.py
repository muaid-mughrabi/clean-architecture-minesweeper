from minesweeper.model.game import Game
from minesweeper.view.SimpleBoardViewer import SimpleBoardPresenter

g = Game(10, 10, 2)
p = SimpleBoardPresenter(g.board)

print(p.generate_view())

while not g.game_over:
    x = int(input("Enter x coordinates: "))
    y = int(input("Enter y coordinates: "))
    g.reveal(x, y)
    print(p.generate_view())

print(f"Game endstate is: {g.detect_state()}")
