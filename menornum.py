# Achar o menor número de uma sequência.

def find_smallest_int(arr):
    arr.sort()
    return arr[0]

print(find_smallest_int([34, 15, 88, 2]))

# ou:
def find_smallest_int(arr):
    return min(arr)

print(find_smallest_int([34, 15, 88, 2]))

