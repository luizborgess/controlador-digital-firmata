import numpy as np

## O sample time deve ser o mesmo a ser utilizado durante o programa, a utilizaçao de diferentes
##sample times pode ocasionar no crash do software.

inicio = 0
final = 20
#limite max 20

sample_time = 0.1
offset=1
y = np.array([])

x = np.arange(inicio, final, sample_time)

limite_inferior = 4 * np.pi
limite_superior = 5 * np.pi
ganho = 0.4

# plot para seno entre 2pi e 3pi
for tempo in x:
    if limite_inferior < tempo < limite_superior:
        y = np.append(y, (ganho * np.sin(tempo))+offset)
    else:
        y = np.append(y, offset)


w = np.column_stack((x, y))
w = np.append(w, np.zeros([np.size(y),1]), axis = 1)
w[0,2]=limite_inferior
w[1,2]=limite_superior
w[2,2]=offset
w[3,2]=sample_time*1000
print(w)
print(np.shape(w))


np.savetxt('input_disturbance.csv', w, delimiter=",")


