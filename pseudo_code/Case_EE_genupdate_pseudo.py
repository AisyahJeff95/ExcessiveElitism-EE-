from your_module import create  # Import the function to create the creatures
import neat
from pureples.shared.substrate import Substrate
from pureples.shared.genome import CppnGenome
from pureples.hyperneat import create_phenotype_network
import pybullet as p
import pybullet_data
import numpy as np
import os
import pickle
import copy
import glob
from your_module import visualize  # Import your visualization module
import random

# Define your configuration path
config_path = os.path.dirname(__file__) + '/config_EE'

# Define parameters for the simulation
sphereRadius = 0.3
defaultPatrsNum = 1
maxPartsNum = 10
growRate = 50
growInterval = 20
EventNum = 4
pop_radius = 60
Total_Step = 20000
save_interval = 1

# Number of elite genomes to carry over
M = 82
Genomes = []

# Function to evaluate fitness for the first generation
def eval_fitness(genomes, config=None, mode="GUI", camera=None):
    # ... (Your existing eval_fitness code here)

# Function to evaluate fitness for subsequent generations
def eval_fitness2(genomes, config=None, mode="GUI", camera=None):
    # ... (Your existing eval_fitness2 code here)

# Function to run the evolutionary algorithm for a specified number of generations
def run(gens):
    # Create the initial population for the first generation
    if gens == 400:
        pop = neat.population.Population(config)
        stats = neat.statistics.StatisticsReporter()
        pop.add_reporter(stats)
        pop.add_reporter(neat.reporting.StdOutReporter(True))
        pop.run(eval_fitness, gens)
        
        # Carry the first M genomes to the new_genomes list
        new_genomes = [copy.deepcopy(pop.population[i]) for i in range(M)]

        # Save the new_genomes to file or wherever you want

    else:
        # Create a new population with the remaining genomes
        pop = neat.population.Population(config)
        
        # Generate new genomes for the remaining population
        remaining_genomes = pop.config.pop_size - M
        for _ in range(remaining_genomes):
            genome = pop.create_genome(-1)
            genome.initialize()
            new_genomes.append(genome)

        pop.population = new_genomes
        stats = neat.statistics.StatisticsReporter()
        pop.add_reporter(stats)
        pop.add_reporter(neat.reporting.StdOutReporter(True))
        pop.run(eval_fitness2, gens)

        # Save the new_genomes to file or wherever you want

    # Save speciation data
    stats.save_species_count(delimiter='|', filename='/path/to/speciation_EE.csv')

if __name__ == '__main__':
    run(400)  # Run for 400 generations
