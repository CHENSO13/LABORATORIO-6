
print("Diferencia simetrica de dos conjuntos")
conjunto1 = {'gata', 'perro', 'oso', 'lobo', 'tigre'}
conjunto2 = {'gata', 'tornillo', 'alicate','martillo'}

print("primer conjunto:     ", conjunto1)
print("segundo conjunto:    ", conjunto2)
print("")
print("Diferencia Simetrica entre el primer y segundo conjunto:     ")
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diferencia_simetrica)
