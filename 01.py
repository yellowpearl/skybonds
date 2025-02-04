"""
Алгоритмическая сложность: O(n)
Сложность по памяти: O(1)
Сложность - 1/10, затраченное время 10м
"""

if __name__ == "__main__":
    _sum = 0
    fractions = []
    n = int(input())

    while n > 0:
        i = float(input())
        fractions.append(i)
        _sum += i
        n -= 1

    for i in fractions:
        print(round(i/_sum, 3))
