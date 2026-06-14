import random

POP_SIZE = 20
GENERATIONS = 200
MUTATION_RATE = 0.1

teachers = [0,1,2,3,4]
courses = [0,1,2,3,4]

def create_chromosome():
    chromosome = []
    for course in courses:
        for _ in range(3):
            teacher = random.choice(teachers)
            day = random.randint(0, 4)
            slot = random.randint(0, 4)
            chromosome.append((teacher, course, day, slot))
    return chromosome

def fitness(chromosome):
    penalty = 0

    schedule = {}
    for t, c, d, s in chromosome:
        if (t, d, s) in schedule:
            penalty += 5
        schedule[(t, d, s)] = True

    course_count = {}
    for _, c, _, _ in chromosome:
        course_count[c] = course_count.get(c, 0) + 1

    for c in courses:
        if course_count.get(c, 0) != 3:
            penalty += 5

    for t in teachers:
        teacher_slots = [(d, s) for (tt, _, d, s) in chromosome if tt == t]
        teacher_slots.sort()

        count = 1
        for i in range(1, len(teacher_slots)):
            if teacher_slots[i][0] == teacher_slots[i - 1][0] and \
               teacher_slots[i][1] == teacher_slots[i - 1][1] + 1:
                count += 1
                if count > 3:
                    penalty += 5
            else:
                count = 1

    return -penalty

def selection(population):
    population.sort(key=fitness, reverse=True)
    return population[:10]

def crossover(p1, p2):
    point = random.randint(1, len(p1) - 1)
    return p1[:point] + p2[point:]

def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        i = random.randint(0, len(chromosome) - 1)
        chromosome[i] = (
            random.choice(teachers),
            random.choice(courses),
            random.randint(0, 4),
            random.randint(0, 4)
        )
    return chromosome

def genetic_algorithm():
    population = [create_chromosome() for _ in range(POP_SIZE)]

    for gen in range(GENERATIONS):
        population = selection(population)

        new_population = population[:]

        while len(new_population) < POP_SIZE:
            p1, p2 = random.sample(population, 2)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

        best = max(population, key=fitness)
        print("Generation", gen + 1, "Fitness:", fitness(best))

    print("Best Timetable Found:")
    print(best)


genetic_algorithm()