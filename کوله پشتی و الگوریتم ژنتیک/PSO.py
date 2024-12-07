import numpy as np
import random


weights = [10, 20, 30, 40, 50]     # وزن آیتم‌ها
values = [60, 100, 120, 180, 200]  # ارزش آیتم‌ها
max_weight = 100                   # ظرفیت کوله‌پشتی
num_items = len(weights)           # تعداد آیتم‌ها


num_particles = 30  # تعداد ذرات
num_iterations = 100  # تعداد تکرارها
c1 = 1.5  # ضریب شتاب برای بهترین موقعیت فردی (pBest)
c2 = 1.5  # ضریب شتاب برای بهترین موقعیت جمعی (gBest)
w = 0.5   # ضریب اینرسی


def fitness(solution):
    total_weight = np.dot(solution, weights)
    total_value = np.dot(solution, values)
    if total_weight > max_weight:
        return 0  
    return total_value


particles = np.random.randint(2, size=(num_particles, num_items))
velocities = np.random.uniform(-1, 1, (num_particles, num_items))
p_best = particles.copy()
p_best_fitness = np.array([fitness(p) for p in p_best])
g_best = p_best[np.argmax(p_best_fitness)]
g_best_fitness = np.max(p_best_fitness)


for iteration in range(num_iterations):
    for i in range(num_particles):
     
        particle_fitness = fitness(particles[i])
        
      
        if particle_fitness > p_best_fitness[i]:
            p_best[i] = particles[i]
            p_best_fitness[i] = particle_fitness
        
        
        if particle_fitness > g_best_fitness:
            g_best = particles[i]
            g_best_fitness = particle_fitness
        
        
        velocities[i] = (w * velocities[i] +
                         c1 * random.random() * (p_best[i] - particles[i]) +
                         c2 * random.random() * (g_best - particles[i]))
        
       
        sigmoid = 1 / (1 + np.exp(-velocities[i]))
        particles[i] = np.where(np.random.rand(num_items) < sigmoid, 1, 0)

  
    print(f"Iteration {iteration+1}/{num_iterations}, Best Fitness: {g_best_fitness}")

print("\nBest solution found:")
print("Selected items:", g_best)
print("Total value:", g_best_fitness)
print("Total weight:", np.dot(g_best, weights))
