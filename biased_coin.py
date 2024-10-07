import random

def flip_biased_coin(p):    
    number = random.randint(0,9)
    if number < p * 10:
        return "win"
    else: return "fail"

# Otestování funkce
print(flip_biased_coin(0.7))  # Simulace hodu s 70% šancí na výhru
