import numpy as np
import matplotlib.pyplot as plt

a_i1 = np.array([0.911, 0.95, 0.911])
S_i1 = np.array([0.442, 0.442, 0.442])

a_i2 = np.array([0.911])
S_i2 = np.array([1.69])

A1 = np.dot(a_i1, S_i1)

a_m1 = A1/np.sum(S_i1)

A2 = np.dot(a_i2, S_i2)

a_m2 = A2/np.sum(S_i2)


#Wall reduction Index:

Ls = 50 #[dB]
Lr = np.linspace(35, 1, 100) #[dB]

R1 = Ls - Lr + 10*np.log10(a_m1)
R2 = Ls - Lr + 10*np.log10(a_m2)

print(f'{np.log10(a_m1)}, {np.log10(a_m2)}')

plt.figure()

plt.title("R vs Lr")

plt.ylabel("R (Índice de reducción del panel) [dB]")
plt.xlabel("Lr [dB]")

plt.grid()

plt.plot(Lr, R1, color='red', ls='-.')
plt.plot(Lr, R2, color='black', ls='-.')

plt.legend(['Panel Michael', 'Panel Edgar'])

plt.show()

