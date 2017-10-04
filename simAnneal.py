import ga_eval as ge
import random
import numpy as np

STEP = 0.1
T0 = 100

def parabola(x):
    return x[0] * x[0] + x[1] * x[1]

def neighbor(start):
    val = random.random()
    if val > 0.75:
        return [start[0] - STEP, start[1] - STEP]
    elif val > 0.5:
        return [start[0] + STEP, start[1] - STEP]
    elif val > 0.25:
        return [start[0] - STEP, start[1] + STEP]
    else:
        return [start[0] + STEP, start[1] + STEP]

def sch1(t):
    return T0/(np.log(t + 1))


def simAnnealing(cost):
    cur = np.array([random.random() * 10, random.random() *10])

    # cost is the fuction value trying to minimize
    for t in range(1, 1000):
        # print(t)
        #print(cost(cur))
        costCur = cost(cur)
        nxt = np.array(neighbor(cur))
        costNext = cost(nxt)
        costDif = costCur - costNext
        #print(costDif, costCur, costNext)
        if costDif > 0:
           cur = nxt
        else:
            T = sch1(t)
            prob = np.e**(costDif/T) # As the number of iterations increase the prob of jumping elseware is lower
            i = random.random()
            print(1 - prob, 1 - i)
            if 1 - prob > 1 - i: # Could be wrong
                print("WOW")
                cur = nxt
    return cur


if __name__ == "__main__":
    #ge._plot_f(parabola, *ge._mesh(-10, 10, -10, 10), title="The Parabola Function")
    min = simAnnealing(ge.bump)
    print("The Min of the para is", min)
    #print("Hello World")