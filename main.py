# One Organism 
import random
import string

def fitness(enter, target):
	fit = 0
	for i in range(0, len(enter)):
		fit += abs(ord(target[i]) - ord(enter[i]))
	return(fit)

def mutate(enter):
    index = random.randint(0, len(enter) - 1)
    parts = list(enter)
    parts[index] = chr(ord(parts[index]) + random.randint(-1, 1))
    return(''.join(parts))

def genesis(spec):
    to = ''
    for i in range(spec):
        to += random.choice(string.ascii_letters) 
    return(to)


def init(target):
    state = genesis(len(target))
    fit = fitness(state, target)
    i = 0
    while True:
        i += 1
        m = mutate(state)
        _fit = fitness(m, target)
        if _fit < fit:
            fit = _fit
            state = m
            print("Generation: {i}\nFitness: {f}\nValue: {s}".format(i=i, f=fit, s=state)) 
        if fit == 0:
            break
    print("Evolution complete!")

init('Hello World!')