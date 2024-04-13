class Aluno:
    def __init__(self, nome, nota1 , nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0
        
    def _calcular_media(self):
        media = (self.nota1 + self.nota2) / 2
        return media
    
    def mostra_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Nota 1: {self.nota1}')
        print(f'Nota 2: {self.nota2}')
        if self._calcular_media() >= 6:
            print("Aprovado")
        else:
            print("Reprovado")
        
        
if __name__ == '__main__':
    aluno1 = Aluno('Mathias', 9, 1)
    aluno2 = Aluno('Leticia', 10, 9)
    
    aluno1.mostra_dados()
    aluno2.mostra_dados()

