# import os
# import pickle
# # from evaluation import eval_fitness
# import matplotlib.pyplot as plt
# import numpy as np
# from pureples.shared.visualize import draw_net_3d
# import glob

# local_dir = os.path.dirname(__file__)

# data_files = [glob.glob(local_dir+f"/genomes_{i}.pkl")[0] for i in range(1,21)]
# genome_data = []
# for file in data_files:
#   with open(file, "rb") as f:
#     genome_data.append(pickle.load(f))

# #find total fitness
# fitness=[]
# for i in range (19):
#     total_fitness=[]
#     for genome in genome_data[i]:
#         genome=genome[:400]
#         gen_fitness=[]
#         for ind,g in genome:
#             gen_fitness.append(g.fitness)

#         gen_fitness.sort()
#         total_fitness.append(gen_fitness)
#     fitness.append(total_fitness)

# #average
# data = np.array(fitness)
# average=np.average(data, axis=0)

# plt.figure()
# plt.plot(np.arange(len(genome_data[5])), [np.mean(i) for i in average], label="Average")
# plt.plot(np.arange(len(genome_data[5])), [np.mean(i) for i in total_fitness], label="Best")
# plt.legend()
# plt.xlabel("Generation")
# plt.ylabel("Fitness")
# # plt.xticks(np.arange(min(x), max(x)+1, 1.0))
# plt.ylim(0, 65)
# plt.savefig('ave_fitness_radar4.svg')
# plt.show()

import os
import pickle
import matplotlib.pyplot as plt
import numpy as np
import glob

local_dir = os.path.dirname(__file__)

data_files = [glob.glob(local_dir + f"/genomes_{i}.pkl")[0] for i in range(0, 12)]
genome_data = []
for file in data_files:
    with open(file, "rb") as f:
        genome_data.append(pickle.load(f))

avg_all=[]
best_all=[]
for i in range(10):
    total_fitness_each=[]
    for genome in genome_data[i]:
        genome=genome[:401]
        gen_fitness=[]
        for ind,g in genome:
            gen_fitness.append(g.fitness)

        gen_fitness.sort()
        total_fitness_each.append(gen_fitness)
    avg_all.append([np.mean(i) for i in total_fitness_each])
    best_all.append([i[-1] for i in total_fitness_each])

avg = [sum(item) / len(item) for item in zip(*avg_all)]

best = [sum(item) / len(item) for item in zip(*best_all)]

plt.figure()
# Iterate over the lists in best_all and plot them
for i, data in enumerate(best_all):
    data=data[:400]
    plt.plot(np.arange(len(genome_data[2])), data, color='lightgray', label="Trials" if i == 0 else '')

# Plot avg and best
plt.plot(np.arange(len(genome_data[2])), avg, label="Average")
plt.plot(np.arange(len(genome_data[2])), best, label="Best")

plt.ylim(0, 65)
plt.legend(fontsize=14)
plt.xlabel("Generation", fontsize=14)
plt.ylabel("Fitness", fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig(os.path.dirname(__file__) + "/avg_fitness2.svg")
plt.show()
