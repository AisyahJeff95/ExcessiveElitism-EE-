import os
import pickle
from evaluation import eval_fitness
import matplotlib.pyplot as plt
import numpy as np
from pureples.shared.visualize import draw_net_3d
import glob
import creature.plot2 as plot
import pybullet as p

local_dir = os.path.dirname(__file__)
file_path=glob.glob(local_dir+"/*.pkl")[0]
with open(file_path, "rb") as f:
    Genomes = pickle.load(f)
genomes = Genomes[999]

# Find the best individual across all generations
best_overall = max((g.fitness, ind, gen) for gen, genomes in enumerate(Genomes) for ind, g in genomes)

# Unpack the tuple
best_fitness, best_ind, best_gen = best_overall

# Load the best generation for further analysis if needed
best_generation = Genomes[best_gen]

# Evaluate fitness if needed
eval_fitness(best_generation, mode="DIRECT")

# Plot trajectory, partsNum, and fitness
plot.trajectory(60, best_generation)
plot.partsNum(Genomes)
plot.fitness(Genomes)
plt.show()

# best_ind=sorted([(g.fitness,ind) for ind,g in genomes])[-1][1]

# eval_fitness(genomes,mode="DIRECT")

# plot.trajectory(60,genomes)
# # plot.trajectory_2(100,genomes)
# plot.partsNum(Genomes)
# plot.fitness(Genomes)
# plt.show()