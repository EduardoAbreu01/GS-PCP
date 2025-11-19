class Curso:
    def __init__(self,nome,categoria,carga):
        self.nome = nome
        self.categoria = categoria
        self.carga = carga

# Cria o toString
    def exibir(self):
        print("Curso: " + self.nome  + " Categoria: " + self.categoria + " Carga: " + self.carga)




