from generate_number import generate_number
from guess_result import guess_result

def cows_and_bulls():
    """
    Hlavni funkce pro spusteni hry Cows and Bulls.
    pravidla: https://en.wikipedia.org/wiki/Bulls
    
    Args: N/A
    Returns: N/A
    """
    
    print("Vitejte ve hre Cows and Bulls!")
    print("Chcete hrat zakladni verzi (4 cisla) y/n?")

    choice = input()
    if choice == "y":
        figures = 4
        repeat_digits = False
    else:
      figures = int(input("Zadejte pocet cifer (3-7):"))
      input("Chcete povolit opakovani cifer y/n?")
      repeat_digits = True if input() == "y" else False

    number = generate_number(figures=figures, repeat_digits=repeat_digits)

    guess_result(number, figures, 10)

if __name__ == "__main__":
  cows_and_bulls()
        








