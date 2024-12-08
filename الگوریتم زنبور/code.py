import random
import numpy as np


NUM_WORKER_BEES = 20
NUM_SCOUT_BEES = 10
ITERATIONS = 100


def calculate_collisions(board):
    collisions = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                collisions += 1
    return collisions

def generate_random_solution(n):
    return [random.randint(0, n - 1) for _ in range(n)]

# جستجوی محلی توسط زنبورهای کارگر
def local_search(board):
    n = len(board)
    best_board = board[:]
    best_collisions = calculate_collisions(best_board)

    for i in range(n):
        original_row = board[i]
        for new_row in range(n):
            if new_row != original_row:
                board[i] = new_row
                current_collisions = calculate_collisions(board)
                if current_collisions < best_collisions:
                    best_board = board[:]
                    best_collisions = current_collisions
        board[i] = original_row

    return best_board

# جستجوی جهانی توسط زنبورهای دیده‌بان
def global_search(n):
    return generate_random_solution(n)

# الگوریتم زنبور برای حل مسئله هشت وزیر
def bee_algorithm(n):
    # مقداردهی اولیه
    solutions = [generate_random_solution(n) for _ in range(NUM_WORKER_BEES + NUM_SCOUT_BEES)]

    for _ in range(ITERATIONS):
        # محاسبه برخوردها برای تمام راه‌حل‌ها
        solutions = sorted(solutions, key=calculate_collisions)

        # انتخاب بهترین راه‌حل‌ها
        elite_solutions = solutions[:NUM_WORKER_BEES]

        # جستجوی محلی توسط زنبورهای کارگر
        worker_solutions = [local_search(solution) for solution in elite_solutions]

        # جستجوی جهانی توسط زنبورهای دیده‌بان
        scout_solutions = [global_search(n) for _ in range(NUM_SCOUT_BEES)]

        # ترکیب نتایج
        solutions = worker_solutions + scout_solutions

        # اگر راه‌حل بدون برخورد پیدا شد، خروج از حلقه
        for solution in solutions:
            if calculate_collisions(solution) == 0:
                return solution

    return None


n = 8
solution = bee_algorithm(n)
if solution:
    print("راه‌حل پیدا شد:", solution)
    print("تعداد برخوردها:", calculate_collisions(solution))
else:
    print("راه‌حلی یافت نشد.")
