

from abc import ABC, abstractmethod


class ModeloBancoDeDados(ABC):
    '''
    -----> Modelo de banco de dados
    '''

    @abstractmethod
    def conectar_ao_SGBD(self):
        pass



class BancoDeDadosAlunos(ModeloBancoDeDados):

    __host = 'localhost'
    __user = 'root'
    __database = 'alunos'

    def __init__(self, passwd):
        '''
        ------> Define um atributo, e invoca um método.
        parametro passwd: Recebe a senha para acesso.
        '''
        self._passwd = passwd
        self.conectar_ao_SGBD()  #---passo---> (2)

    @property
    def GetHost(self):
        return BancoDeDadosAlunos.__host
    @GetHost.setter
    def SetHost(self, novo_host):
        BancoDeDadosAlunos.__host = novo_host

    @property
    def GetUser(self):
        return BancoDeDadosAlunos.__user        # Área de Getters e Setters
    @GetUser.setter
    def SetUser(self, novo_user):
        BancoDeDadosAlunos._user = novo_user

    @property
    def GetDatabase(self):
        return BancoDeDadosAlunos.__database

    @property
    def GetPasswd(self):
        return self._passwd


    def conectar_ao_SGBD(self):
        '''
        -------> Faz a conexão com o SGBDe chama um método.
        retorna: None
        '''
        import time
        import mysql.connector
        from mysql.connector import Error

        try:
            self._conection = mysql.connector.connect(host=self.GetHost, user=self.GetUser, database=self.GetDatabase, passwd=self.GetPasswd)
            if self._conection.is_connected():
                print('Conexão estabelecida com o serviço MySql local.\n')
                self.adicionar_dados_na_tabela() #---passo---> (3)
            else:
                exit('Não foi possivel se conectar ao SGBD de sua máquina!.')
        except Error as problema_identificado:
            exit(f'Não foi possivel se conectar ao SGBD de sua máquina!. Erro: {problema_identificado}')


    def encerrar_conexao(self):
        '''
        -------> Encerra a conexão com o SGBD.
        retorna: None
        '''
        if self._conection.is_connected():
            self._conection.commit()
            self._conection.close()
        else:
            print('O programa já foi desconectado do serviço!.')


    def adicionar_dados_na_tabela(self):
        '''
        -------> Adiciona dados na tabela definida na instrução SQL e chama dois métodos.
        retorna: None
        '''
        cursor = self._conection.cursor()

        inf = self.coleta_de_dados_aluno() #---passo---> (4)
        cursor.execute(f"INSERT INTO alunos VALUES ('{inf[0]}', '{inf[1]}', '{inf[2]}', '{inf[3]}', '{inf[4]}');")
        self.encerrar_conexao()  #---passo---> (5)


    def coleta_de_dados_aluno(self):
        '''
        -------> Faz a coleta dos dados de um aluno
        retorna: Uma lista com as informações de um aluno.
        '''
        aluno_infor = []

        nome = str(input('Nome: ')).strip().title()
        if not nome.isalpha():
            exit('O nome deve ser alfabético!.. Tente novamente.')

        aluno_infor.append(nome)
        for iter in range(1, 5):
            try:
                aluno_infor.append(float(input(f'{iter}º Nota: ')))
            except ValueError:
                exit('As notas devem ser numericas!. Tente novamente.')
        return aluno_infor



if __name__ == '__main__':
    teste = BancoDeDadosAlunos('abraao2020')  #---passo---> (1)
