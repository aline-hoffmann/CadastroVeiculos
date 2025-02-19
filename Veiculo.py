class Veiculo:
    # __init_ => é o método construtor
    def __init__(self, marca, modelo, placa, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__placa = placa
        self.__ano = ano
    
    #Métodos getters and setters para os atributos privados
    
    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        if marca != "Peugeot":
            self.__marca = marca

    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_placa(self):
        return self.__placa
    def set_placa(self, placa):
        self.__placa = placa

    def get_ano(self):
        return self.__ano
    def set_ano(self, ano):
        self.__ano = ano
    
    def get_marca(self):
        return self.__marca
    def set_marca(self):
        self.__marca = marca

    # Método de instância
    def calcularTempoUso(self):
        return 2024 - self.__ano
    
    # Método STR
    def __str__(self):
        return f'''Marca: {self.__marca}
    - Modelo: {self.__modelo}
    - Placa: {self.__placa}
    - Ano: {self.__ano}'''
    
''' #Criando uma instância da Classe Veículo
uno = Veiculo("Fiat", "Uno", "ABC", 2005)
print(uno)
print(uno.__str__)

# Abaixo estou instanciando um objeto da Classe Veiculo
meuUno = Veiculo("Fiat", "Uno com Escada", "ABC-1234", 2000)
print(meuUno.get_marca())
print(meuUno.calcularTempoUso())
meuUno.__ano = 2010
print(meuUno.calcularTempoUso())  
teuFusca = Veiculo("Volks", "Fusca do Itamar", "DEF-", 1995) '''

'''print(meuUno.calcularTempoUso())
print(teuFusca.calcularTempoUso())

print("")'''