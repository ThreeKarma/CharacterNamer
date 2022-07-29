import random, letter as lg
def choice():
    current = 1
    length=random.randint(2, 4)
    name=""
    if random.randint(1, 20) == 20:
        name=lg.alpha()
    else:
        while current<=length:
            if length == 1:
                name = random.choices([random.choice([(lg.conso()+lg.vowel()),(lg.vowel()+lg.conso()),(lg.clust()+lg.vowel())]), ""], weights=(95,5))[0]
            elif current == length:
                name+= random.choices([lg.ends(), lg.alpha(),""], weights=(50,35,15))[0]
            else:
                name += random.choice([lg.alpha(), lg.clust()])
                if name[-1] == "q":
                    name += "u"
                elif name[-1] in lg.vowels:
                    name+=random.choices([(random.choice([lg.conso(),lg.clust()])+lg.vowel()), lg.vowel()], weights=(85,15))[0]
                else:
                    name += lg.vowel()
            current+=1
    name = name.title()
    return name + lg.adject()
def getRandomName():
    out = ""
    names = ["You just had to be difficult"]
    current = 1
    while current<10:
        newname = choice()
        out += " "+str(current)+". "+newname+"\n"
        names.append(newname)
        current+=1
    newname = choice()
    out += " 10. "+newname
    names.append(newname)
    print(out)
    keeps = input("What names would you like to keep?").split()
    for i in keeps:
        with open('c:/Coding/Python Code/Bots/Character Namer/FavoriteNames.txt', 'a') as f:
            f.writelines('\n'+(names[int(i)]))