import hashlib
import pandas as pd

class GerenciadorSenha:
    def __init__(self):
        self.senhas = pd.DataFrame(columns=['ID', 'IP', 'Senha'])

    def adicionar_senha(self, id, ip, senha):
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        nova_senha = pd.DataFrame([[id, ip, senha_hash]], columns=['ID', 'IP', 'Senha'])
        self.senhas = pd.concat([self.senhas, nova_senha], ignore_index=True)

    def consultar_senha(self, id):
        resultados = self.senhas.loc[self.senhas['ID'] == id, 'Senha']
        return resultados.tolist()

def main():
    gerenciador = GerenciadorSenha()

    gerenciador.adicionar_senha(18007511, '192.168.1.1', 'minhasenha')
    gerenciador.adicionar_senha(18007512, '192.168.1.2', 'outrasenha')

    id_usuario = 18007511
    resultado_consulta = gerenciador.consultar_senha(id_usuario)
    print(resultado_consulta)

if __name__ == "__main__":
    main()


