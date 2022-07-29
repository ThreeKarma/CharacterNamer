import random, os, roman
from pathlib import Path
vowels = str("a e i o u a e i o u y").split()
consonants = str("b c d f g h j k l m n p q r s t v w x y z").split()
clusters = str("sk sl sm sn sp st sw br cr dr fr gr pr tr bl cl fl gl pl str spr thr chr phr shr sh ch th wh ph gh qw").split()
endings = str("ct ft ld lp lt mp nd nk nt pt rd rk sk sp st").split()
alphabet = str("a b c d e f g h i j k l m n o p q r s t u v w x y z").split()
def numer():
    return " "+roman.toint(random.randint(2, 16))
def adject():
    dir = Path(os.path.realpath(__file__)).parent
    adjectives = dir / Path('c:/Coding/Python Code/Bots/Character Namer/english-adjectives.txt')
    with adjectives.open() as adjectives_open:
        adjective = " the "+random.choice(adjectives_open.readlines()).title().strip()
    return random.choices([adjective,numer(),""],weights=(49,49,2))[0]
def conso():
    return random.choice(consonants)
def alpha():
    return random.choice(alphabet)
def vowel():
    return random.choice(vowels)
def clust():
    return random.choice(clusters)
def ends():
    return random.choice(endings)