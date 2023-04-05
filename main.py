from game import Game

def main():
    game = Game()

    while True:
        game.handle_events()
        game.update()
        game.draw()

if __name__ == "__main__":
    main()
