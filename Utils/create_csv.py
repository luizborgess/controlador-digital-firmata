import numpy as np

## O sample time deve ser o mesmo a ser utilizado durante o programa, a utilizaçao de diferentes
##sample times pode ocasionar no crash do software.

inicio = 0
final = 10
sample_time = 0.1
y = np.array([])

x = np.arange(inicio, final, sample_time)

limite_inferior = 2 * np.pi
limite_superior = 3 * np.pi
ganho = 1

# plot para seno entre 2pi e 3pi
for tempo in x:
    if limite_inferior < tempo < limite_superior:
        y = np.append(y, ganho * np.sin(tempo))
    else:
        y = np.append(y, 0)

w = np.column_stack((x, y))
np.savetxt('input_disturbance.csv', w, delimiter=",")


