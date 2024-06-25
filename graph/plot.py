import matplotlib.pyplot as plt

""" Grafico Linear"""
x = [i for i in range(100)]
y = [(i * 2) + 1 for i in x]
plt.plot(x, y, marker='*')
plt.title("Titulo do grafico")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()

""" Grafico polinomial """
x = [i for i in range(-100, 100, 1)]
y = [pow(i, 2) + i + 4 for i in x]
plt.plot(x, y, marker='o', color='red')
plt.title("Titulo do grafico")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.show()
