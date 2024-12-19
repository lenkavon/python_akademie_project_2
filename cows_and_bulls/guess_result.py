from validate_guess import validate_guess

def guess_result(number, figures, round):
    """
    Funkce pro hadani cisla.
    Args:
        number (int): Hadane cislo.
        figures (int): Pocet cifer v hadanem cislu.
        round (int): Pocet pokusu.
    Returns: 
        N/A
    """
    
    if round == 0:
        print("Bohuzel jste neuhodli cislo.")
        print(f"Spravne cislo bylo: {number}")
        return
    
    guess = input("Zadejte hadane cislo: ")
    while not validate_guess(guess, figures):
        guess = input("Zadejte hadane cislo: ")
    
    guess_int = int(guess)

    cows = 0
    bulls = 0
    for i in range(figures):
        if str(guess_int)[i] == str(number)[i]:
            bulls += 1
        elif str(guess_int)[i] in str(number):
            cows += 1

    print(f"Tip: {guess_int} -> Cows: {cows} Bulls: {bulls}, Zbyva pokusu: {round - 1}")
    if bulls == figures:
        print("Gratulujeme, uhodli jste cislo!")
        return
    else:
        return guess_result(number, figures, round - 1)
    

if __name__ == "__main__":
    guess_result(1234, 4, 10)