import numpy as np
from tqdm import tqdm
from numba import float64, vectorize, njit,jit

@jit(nopython=True,cache=True)
def crossover_and_mutation(pop,pop_size,dna_size,mutation_rate, CROSSOVER_RATE = 0.8):
    new_pop = []
    for fIdx in range(len(pop)):        #遍历种群中的每一个个体，将该个体作为父亲
        child = pop[fIdx]        #孩子先得到父亲的全部基因（这里我把一串二进制串的那些0，1称为基因）
        if np.random.rand() < CROSSOVER_RATE:            #产生子代时不是必然发生交叉，而是以一定的概率发生交叉
            mother = pop[np.random.randint(pop_size)]    #再种群中选择另一个个体，并将该个体作为母亲
            cross_points = np.random.randint(low=0, high=dna_size*2)    #随机产生交叉的点
            child[cross_points:] = mother[cross_points:]        #孩子得到位于交叉点后的母亲的基因
        mutation(child,dna_size,mutation_rate)    #每个后代有一定的机率发生变异
        new_pop.append(child)

    return new_pop

@jit(nopython=True,cache=True)
def mutation(child,dna_size, MUTATION_RATE=0.003):
    if np.random.rand() < MUTATION_RATE:                 #以MUTATION_RATE的概率进行变异
        mutate_point = np.random.randint(0, dna_size*2)    #随机产生一个
        child[mutate_point] = child[mutate_point]^1
		
class GA(object):
    
    def __init__(self,fun,lbound,ubound,pop_size=200,dna_size=24,crossover_rate=0.8,mutation_rate=0.003,n_iter=300):
        self.func = fun
        self.lbound=lbound
        self.ubound=ubound
        self.pop_size=pop_size
        self.dna_size=dna_size
        self.crossover_rate=crossover_rate
        self.mutation_rate=mutation_rate
        self.n_iter=n_iter
        self.args_len=len(lbound)
        self.pop = np.random.randint(2, size=(pop_size, dna_size*2))
        
    def translateDNA(self,pop):
        result = []
        for i in range(self.args_len):
            tmp = pop[:,i::2]
            bound = (self.lbound[i],self.ubound[i])
            result.append(self.translate(tmp,bound))
        return result
    
    def translate(self,pop,bound):
        pop1 = pop.dot(2**np.arange(self.dna_size)[::-1]) # 2**n次方向量转向
        pop2 = pop1/float(2**self.dna_size-1) # 归一化
        return pop2 * (bound[1]-bound[0])+bound[0]
    
    def get_fitness(self,pop): 
        result = self.translateDNA(pop)
        pred = self.func(*result)
        return (pred - np.min(pred)) + 1e-3 #减去最小的适应度是为了防止适应度出现负数，通过这一步fitness的范围为[0, np.max(pred)-np.min(pred)],最后在加上一个很小的数防止出现为0的适应度

    def select(self, pop, fitness):    # nature selection wrt pop's fitness
        idx = np.random.choice(np.arange(self.pop_size), size=self.pop_size, replace=True,
                               p=(fitness)/(fitness.sum()) )
        return pop[idx]
    
    def cal_result(self,pop):
        fitness = self.get_fitness(pop)
        max_fitness_index = np.argmax(fitness)
        result = self.translateDNA(pop)
        return [x[max_fitness_index] for x in result]
    
    def run(self):
        for _ in tqdm(range(self.n_iter)):#迭代N代
            self.pop = np.array(crossover_and_mutation(self.pop,self.pop_size,self.dna_size, self.mutation_rate,self.crossover_rate))
            fitness = self.get_fitness(self.pop)
            self.pop = self.select(self.pop, fitness) #选择生成新的种群
        return self.cal_result(self.pop)