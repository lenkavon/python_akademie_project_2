def validate_guess(guess, figures, repeat_digits=False):
    """
    Funkce pro validaci hadaneho cisla.
    Args:
        guess (str): Hadane cislo.
        figures (int): Pocet cifer v hadanem cislu.
    Returns:
        bool: True, pokud je hadane cislo validni, jinak False.
    """
    if not repeat_digits and len(set(guess)) != figures:
        print("Hadane cislo nesmi obsahovat opakovane cislice.")
        return False
    if not guess.isdigit():
        print("Hadane cislo musi byt cele cislo.")
        return False
    if len(guess) != figures:
        print(f"Hadane cislo musi mit {figures} cifer.")
        return False
    return True


if __name__ == "__main__":
    test_guess = input("Zadejte hadane cislo: ")
    guess_valid = validate_guess(test_guess, 4)
    print(f"hadane cislo je {'validni' if guess_valid else 'nevalidni'}")
