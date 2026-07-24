from numpy import asarray,arange
from numpy.random import rand
from matplotlib import pyplot as plt

def gradient_descent(bounds,num_iterations,step_size):
    solutions,score= [],[]
    solution = bounds[:,0] + rand(len(bounds)) * (bounds[:,1] - bounds[:,0])

    for i in range(num_iterations):

        solutions.append(solution - step_size * (solution*2))
        score.append(solution**2)

    return {'Solutions' : solutions,'Scores' : score}

ss = gradient_descent(asarray([[-1,1]]),30,0.1)

plt.plot((arange(asarray([[-1,1]])[0,0],asarray([[-1,1]])[0,1]+0.1,0.1)),((arange(asarray([[-1,1]])[0,0],asarray([[-1,1]])[0,1]+0.1,0.1))**2))
plt.plot(ss['Solutions'],ss['Scores'],'.-',color='red')
plt.show()