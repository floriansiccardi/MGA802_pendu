import random


def read(filename):
    """Retourne le contenue du fichier texte filename """
    with open(filename, 'r') as f:
        return f.read().split('\n')


def select_word():
    return random.choice(words)


def ask_letter():
    ltr = input(' - Veuillez entrer une lettre à jouer :   ').lower()
    while ltr in played_letters:
        ltr = input(' - Cette lettre a déjà été jouée.\nVeuillez entrer une autre lettre :   ').lower()
    return ltr


def play_letter(ltr):
    global chance, displayed_word
    new_displayed_word = ''
    win = False
    for i, lt in enumerate(word):
        if lt == ltr:
            new_displayed_word += ltr
            win = True
        else:
            new_displayed_word += displayed_word[i]
    displayed_word = new_displayed_word
    played_letters.append(ltr)
    if not win:
        chance -= 1
        print(f'   Cette lettre n\'est pas présente dans le mot.\n   Il vous reste maintenant {chance} vies')
    return new_displayed_word


words = read(filename='mots_pendu.txt')
word = select_word()

displayed_word = '_' * len(word)
played_letters = []
chance = 6

running = True
while running:
    print(f'\n > Mot actuel :   {displayed_word}')
    letter = ask_letter()
    play_letter(letter)
    if chance == 0:
        print(f'\n > Vous avez perdu ...\n   Le mot était {word}')
        break
    if word == displayed_word:
        print(f' > Félicitaion, vous avez gagné !\n   Il vous restait {chance} vies.')
        break
