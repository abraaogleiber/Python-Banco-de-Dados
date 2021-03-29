
from abc import ABC, abstractmethod


class BancoDadosModelo(ABC):

    def __init__(self, host, user):
        '''
        ------> Classe abstrata, somente para fins de estudo. Implementa um modelo de conexão a banco de dados.
        parametro host: Recebe o endereço do SGBD.
        parametro user: Recebe o usuário para acesso.
        '''
        self._host = host
        self._user = user

    @property
    def GetHost(self):
        return self._host

    @property
    def GetUser(self):
        return self._user


    @abstractmethod
    def conectar_ao_sistema():
        '''
        ------> Toda classe que herda deste modelo deverá implementa esse método, para efetuar a conexão com o banco.
        retorna: None
        '''
        pass


class BancoDeDados(BancoDadosModelo):

    def __init__(self, host, user, banco_dados, passwd):
        '''
        ------> Classe que implementa método para a inserção de dados em uma tabela.
        parametro host: Recebe o endereço do SGBD.
        parametro user: Recebe o usuário para acesso.
        parametro banco_dados: Recebe o nome do banco de dados para acesso.
        parametro passwd: Recebe a senha para acessar o sistema interno.
        '''
        super().__init__(host=host, user=user)
        self._banco_dados = banco_dados
        self._passwd = passwd

        self.conectar_ao_sistema()

    @property
    def GetBancoDados(self):
        return self._banco_dados

    @property
    def GetPasswd(self):
        return self._passwd


    def conectar_ao_sistema(self):
        '''
        ------> Método responsável por se conectar ao sistema SGBD.
        retorna: None
        '''
        import mysql.connector
        from mysql.connector import Error
        import time

        try:
            self._sistema_interno = mysql.connector.connect(host=self.GetHost, user=self.GetUser, database=self.GetBancoDados, passwd=self.GetPasswd)

            time.sleep(2)  # O fluxo do programa altera para esperar a resposta do sistema(SGBD).
            if self._sistema_interno.is_connected():
                print('Conexão estabelecida com o sistema SGBD de sua máquina!.')
            else:
                raise Error
        except Error as problema:
            print('Não foi possivel se conectar com ao gerenciador(SGBD) de sua máquina!!.')
            exit('Descrição do problema: {}'.format(problema))


    def desconectar_do_sistema(self):
        '''
        ------> Método responsável por desconectar o programa do sistema SGBD.
        retorna: None
        '''
        if self._sistema_interno.is_connected():
            self._sistema_interno.close()
        else:
            print('O banco de dados já foi desconectado!.')


    def adicionar_conteudo(self, tabela):
        '''
        ------> Método responsável por adicionar conteúdos à tabela.
        parametro tabela: Recebe o nome da tabela.
        retorna: None
        '''
        cursor = self._sistema_interno.cursor()

        try:
            if tabela == 'alunos':
                nome = str(input('Nome: ')).strip().title()
                n1 = float(input('1º Nota: '))
                n2 = float(input('2º Nota: '))
                n3 = float(input('3º Nota: '))
                n4 = float(input('4º Nota: '))
                cursor.execute(f"INSERT INTO {tabela} VALUES (DEFAULT, '{nome}', '{n1}', '{n2}', '{n3}', '{n4}');")
            elif tabela == 'disciplinas':
                m1 = str(input('1º Materia: ')).strip().capitalize()
                m2 = str(input('2º Materia: ')).strip().capitalize()
                m3 = str(input('3º Materia: ')).strip().capitalize()
                m4 = str(input('4º Materia: ')).strip().capitalize()
                cursor.execute(f"INSERT INTO {tabela} VALUES (DEFAULT, '{m1}', '{m2}', '{m3}', '{m4}');")
            else:
                exit('A tabela não foi encontrada, talves não exista.')
        except:
            exit('Não foi possivel adicionar os valores no banco!.')
        finally:
            self._sistema_interno.commit()
            cursor.close()
            self.desconectar_do_sistema()
