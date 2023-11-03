terra = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
power = 1

def game(terra, power):
    # total_power = power
    for i in terra:
        for k in i:
            if k <= power:
                power += k
            else:
                continue
    return power

print(game(terra, power))