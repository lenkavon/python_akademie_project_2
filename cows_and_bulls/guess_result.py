from .validate_guess import validate_guess

def guess_result(number, figures, attempts, repeat_digits):
    """
    Funkce pro hadani cisla.
    Args:
        number (int): Hadane cislo.
        figures (int): Pocet cifer v hadanem cislu.
        attempts (int): Pocet pokusu.
    Returns:
        N/A
    """

    if attempts == 0:
        print("Bohuzel jste neuhodli cislo.")
        print(f"Spravne cislo bylo: {number}")
        return

    guess = input("Zadejte hadane cislo: ")
    while not validate_guess(guess, figures, repeat_digits):
        guess = input("Zadejte hadane cislo: ")

    guess_int = int(guess)

    cows = 0
    bulls = 0
    for i in range(figures):
        if str(guess_int)[i] == str(number)[i]:
            bulls += 1
        elif str(guess_int)[i] in str(number):
            cows += 1

    print(
        f"Tip: {guess_int} -> {'Cow' if cows == 1 else 'Cows'}: {cows} {'Bull' if bulls == 1 else 'Bulls' }: {bulls}, Zbyva pokusu: {attempts - 1}"
    )
    if bulls == figures:
        print(f"Gratulujeme, uhodli jste cislo! v {10 - attempts}. pokusu")
        return 10 - attempts
    else:
        return guess_result(number, figures, attempts - 1, repeat_digits)


if __name__ == "__main__":
    guess_result(1234, 4, 10, False)
