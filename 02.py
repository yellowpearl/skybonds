"""
ВАЖНО: при кол-ве лотов > 1000 возникнет ошибка RecursionError
Алгоритмическая сложность: O(n*W), n - кол-во лотов, W - сумма средств
Сложность по памяти: O(n)
Сложность - 7/10, затраченное время 4ч
"""

def knapsack(W, wt, val, n):
    """
    Функция для решения задачи о рюкзаке, которая возвращает выбранные элементы.

    :param W: Сумма средств
    :param wt: Массив цен на лоты
    :param val: Массив доходностей лотов
    :param n: Кол-во лотов
    :return: (v, p), где v - максимальная доходность, p - список названий лотов
    """
    # Base Case
    if n == 0 or W == 0:
        return 0, []

    if (wt[n - 1] > W):
        return knapsack(W, wt, val, n - 1)

    v1, p1 = knapsack(W - wt[n - 1], wt, val, n - 1)
    v1 += val[n - 1]
    p1 = [names[n - 1]] + p1

    v2, p2 = knapsack(W, wt, val, n - 1)

    return (v1, p1) if v1 >= v2 else (v2, p2)


if __name__ == "__main__":
    days_amount, _, amount_of_funds = [int(_) for _ in input().split()]

    profits = []
    costs = []
    names = []

    while True:
        b = input().split()
        if b:
            day, name, price, amount = (int(b[0]), b[1], float(b[2]), int(b[3]))
            bond_cost = round((1000 - price / 100 * 1000), 1)
            bond_income = days_amount - day + 30
            profits.append((bond_cost+bond_income)*amount)  # Доход лота
            names.append(" ".join(b))  # Название лота
            costs.append(round(price / 100 * 1000 * amount, 1))  # Стоимость лота
        else:
            break

    val, path = knapsack(
        W=amount_of_funds,
        wt=costs,
        val=profits,
        n=len(names),
    )
    print(int(val))
    for p in reversed(path):
        print(p)
    print()
