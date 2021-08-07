from itertools import product
from itertools import permutations
from itertools import combinations

# =============================================================================================================

# 1. 순열(permutatiions)
# from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 2))

print(result)
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# =============================================================================================================

# 2. 중복순열(product)
# from itertools import product
data = ['A', 'B', 'C']

result = list(product(data, repeat=2))

print(result)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# =============================================================================================================

# 3. 조합(combinations)
# from itertools import combinations
data = ['A', 'B', 'C']

result = list(combinations(data, 2))

print(result)
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# =============================================================================================================
