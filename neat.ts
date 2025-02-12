interface Individual {
    genes: number[];
    fitness: number;
}

class GeneticAlgorithm<T extends Individual> {
    private populationSize: number;
    private mutationRate: number;
    private crossoverRate: number;
    private elitismCount: number;
    private population: T[];

    constructor(populationSize: number, mutationRate: number, crossoverRate: number, elitismCount: number) {
        this.populationSize = populationSize;
        this.mutationRate = mutationRate;
        this.crossoverRate = crossoverRate;
        this.elitismCount = elitismCount;
        this.population = [];
    }

    // Initialize the population with random individuals
    initializePopulation(createIndividual: () => T) {
        this.population = [];
        for (let i = 0; i < this.populationSize; i++) {
            this.population.push(createIndividual());
        }
    }

    // Calculate the fitness of each individual in the population
    calculateFitness(fitnessFunction: (individual: T) => number) {
        for (const individual of this.population) {
            individual.fitness = fitnessFunction(individual);
        }
    }

    // Select parents for crossover based on fitness (e.g., tournament selection)
    selectParents(tournamentSize: number): T[] {
        const parents: T[] = [];
        for (let i = 0; i < this.populationSize; i++) {
            let bestIndividual: T | null = null;
            for (let j = 0; j < tournamentSize; j++) {
                const randomIndex = Math.floor(Math.random() * this.populationSize);
                const randomIndividual = this.population[randomIndex];
                if (bestIndividual === null || randomIndividual.fitness > bestIndividual.fitness) {
                    bestIndividual = randomIndividual;
                }
            }
            parents.push(bestIndividual!);
        }
        return parents;
    }

    // Perform crossover between two parents to create offspring
    crossover(parent1: T, parent2: T, crossoverFunction: (parent1: T, parent2: T) => T): T {
        return crossoverFunction(parent1, parent2);
    }

    // Mutate an individual
    mutate(individual: T, mutationFunction: (individual: T, mutationRate: number) => T): T {
        return mutationFunction(individual, this.mutationRate);
    }

    // Create the next generation
    createNextGeneration(crossoverFunction: (parent1: T, parent2: T) => T, mutationFunction: (individual: T, mutationRate: number) => T) {
        const nextGeneration: T[] = [];

        // Elitism: Copy the best individuals to the next generation
        const sortedPopulation = [...this.population].sort((a, b) => b.fitness - a.fitness);
        for (let i = 0; i < this.elitismCount; i++) {
            nextGeneration.push(sortedPopulation[i]);
        }

        // Create new individuals through crossover and mutation
        while (nextGeneration.length < this.populationSize) {
            const parent1 = this.selectParents(5)[Math.floor(Math.random() * this.populationSize)];
            const parent2 = this.selectParents(5)[Math.floor(Math.random() * this.populationSize)];
            let offspring = this.crossover(parent1, parent2, crossoverFunction);
            offspring = this.mutate(offspring, mutationFunction);
            nextGeneration.push(offspring);
        }

        this.population = nextGeneration;
    }

    // Get the best individual from the current population
    getBestIndividual(): T {
        let bestIndividual = this.population[0];
        for (const individual of this.population) {
            if (individual.fitness > bestIndividual.fitness) {
                bestIndividual = individual;
            }
        }
        return bestIndividual;
    }

    getPopulation(): T[] {
        return this.population;
    }
}

// Example usage (replace with your specific implementation)
function createRandomIndividual(): Individual {
    // Create a random individual based on your problem domain
    return {
        genes: [Math.random(), Math.random()],
        fitness: 0,
    };
}

function calculateIndividualFitness(individual: Individual) {
    // Calculate the fitness of an individual based on your problem domain
    const x = individual.genes[0];
    const y = individual.genes[1];
    return -(x * x + y * y); // Example: Minimize the function -(x^2 + y^2)
}

function performCrossover(parent1: Individual, parent2: Individual): Individual {
    // Perform crossover between two parents to create offspring
    const offspringGenes = [...parent1.genes];
    for (let i = 0; i < offspringGenes.length; i++) {
        if (Math.random() < 0.5) {
            offspringGenes[i] = parent2.genes[i];
        }
    }
    return {
        genes: offspringGenes,
        fitness: 0,
    };
}

function performMutation(individual: Individual, mutationRate: number): Individual {
    // Mutate an individual
    const mutatedGenes = [...individual.genes];
    for (let i = 0; i < mutatedGenes.length; i++) {
        if (Math.random() < mutationRate) {
            mutatedGenes[i] += (Math.random() - 0.5) * 0.1; // Add a small random value
        }
    }
    return {
        genes: mutatedGenes,
        fitness: 0,
    };
}

// Main execution
const populationSize = 100;
const mutationRate = 0.01;
const crossoverRate = 0.9;
const elitismCount = 5;
const tournamentSize = 5;
const geneticAlgorithm = new GeneticAlgorithm<Individual>(populationSize, mutationRate, crossoverRate, elitismCount);

geneticAlgorithm.initializePopulation(createRandomIndividual);

const numberOfGenerations = 100;
for (let i = 0; i < numberOfGenerations; i++) {
    geneticAlgorithm.calculateFitness(calculateIndividualFitness);
    geneticAlgorithm.createNextGeneration(performCrossover, performMutation);
    const bestIndividual = geneticAlgorithm.getBestIndividual();
    console.log(`Generation ${i + 1}: Best Fitness = ${bestIndividual.fitness}`);
}

const bestIndividual = geneticAlgorithm.getBestIndividual();
console.log("Best Individual:", bestIndividual);