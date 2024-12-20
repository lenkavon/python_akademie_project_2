from cows_and_bulls.main import cows_and_bulls

def game():
    result = cows_and_bulls()
    if result:
        print("Victory!")
    else:
        print("Game over!")

    input("Chcete hrat znovu? y/n")
    if input() == "y":
        return game()
    else:
        print("Dekujeme za hru!")
    

if __name__ == "__main__":
    cows_and_bulls()