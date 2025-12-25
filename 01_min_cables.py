import heapq
import random


def gen_cable(n: int) -> List[int]:
    random.seed(4)
    return [random.randint(1, 30) for _ in range(n)]

def min_cost_cables(cables: List[int]):
    heap = cables[:]          # копіюємо лист щоб не змінити
    heapq.heapify(heap)

    total_cost = 0
    merges = []               # додаємо як (a, b, cost)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap) # зʼєднуємо що разу два найкоротших
        cost = a + b
        total_cost += cost
        heapq.heappush(heap, cost)
        merges.append((a, b, cost))

    return total_cost, merges

if __name__ == "__main__":
    cables = gen_cable(100)
    #cables = [8, 4, 6, 12] #test
    print(f"ННаявні кабелі {cables}")

    total, merges = min_cost_cables(cables)
    print("Мінімальні витрати:", total)
    print("Порядок об'єднання:")
    for a, b, cost in merges:
        print(f"{a} + {b} -> {cost}")
