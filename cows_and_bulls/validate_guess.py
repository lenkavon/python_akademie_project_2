def validate_guess(guess, figures):
    """
    Funkce pro validaci hadaneho cisla.
    Args:
        guess (str): Hadane cislo.
        figures (int): Pocet cifer v hadanem cislu.
    Returns:
        bool: True, pokud je hadane cislo validni, jinak False.
    """
    
    if not guess.isdigit():
        print("Hadane cislo musi byt cele cislo.")
        return False
    if len(guess) != figures:
        print("Hadane cislo musi mit", figures, "cifer.")
        return False
    return True

if __name__ == "__main__":
    guess = input("Zadejte hadane cislo: ")
    res = validate_guess(guess, 4)
    print(f"hadane cislo je {'validni' if res else 'nevalidni'}")