import random

def family_shuffle():
    nuclear = ['Gabe', 'Abby', 'Nick', 'Andrew', 'Margie', 'Chris']
    extended = ['Craig', 'Kim', 'Michael', 'Jessica', 'Bethany']
    chosen = []
    pairings = []
    random.shuffle(nuclear)
    random.shuffle(extended)
    pairings.append((extended[0], nuclear[0]))
    chosen.append(nuclear[0])
    for giver in extended[1:] + [nuclear[0]]:
        receiver = random.choice(nuclear)
        while receiver in chosen or receiver == giver:
            receiver = random.choice(nuclear)
        pairings.append((giver, receiver))
        chosen.append(receiver)
    for giver in nuclear[1:]:
        receiver = random.choice(extended)
        while receiver in chosen or receiver == giver:
            receiver = random.choice(extended)
        pairings.append((giver, receiver))
        chosen.append(receiver)
    pairings = sorted(pairings)
    for g, r in pairings:
        print(f"{g}\t->\t{r}")

if __name__ == "__main__":
    family_shuffle()
