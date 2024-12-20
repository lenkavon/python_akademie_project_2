from random import randint, sample


def generate_number(figures=4, repeat_digits=False):
    """Vygeneruje nahodne cislo s danym poctem cifer.
    Args:
        figures (int): Pocet cifer v cislu (3-7), default = 4.
    Returns:
        int: Nahodne vygenerovane cislo.
    Raises:
        ValueError: Pokud je pocet cifer mensi nez 4 nebo vetsi nez 7.
    """
    if figures < 3 or figures > 7:
        raise ValueError("rad musi byt v rozsahu 3-7")

    if repeat_digits:
        start = 10 ** (figures - 1)
        end = 10**figures - 1
        return randint(start, end)
    else:
        return int("".join(sample("0123456789", figures)))
