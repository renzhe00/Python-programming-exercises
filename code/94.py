def solve(heads, legs):
    s = 'No Solvtions'
    for rabbits in range(heads+1):
        chickens = heads-rabbits
        if rabbits*4+chickens*2 == legs:
            return {'rabbits': rabbits, 
                    'chickens': chickens}
    return s

solutions = solve(35, 94)
print(solutions)