
'''
-----> O módulo fornece uma interface de classe que cria um banco de dados.
'''
class CriaBancoDeDados:

    def __init__(self, nome_banco, host='', user='', passwd=''):
        '''
        ------> O método inicializador cria atributos e faz chamadas de métodos da classe.
        parametro nome_banco: Recebe o nome do banco de dados a ser criado.
        parametro host: Recebe o endereço do MySql na máquina.
        parametro user: Recebe o usuário de acesso.
        parametro passwd: Recebe a senha de acesso ao sistema de gerenciamento.
        '''
        self.__localhost = host
        self.__user = user
        self.__passwd = passwd

        self.__acesso_ao_sistema()
        self.__criando_um_banco(nome_banco)


    def __acesso_ao_sistema(self):
        '''
        ------> O método de instância realiza o acesso ao sistema de gerenciamento de banco de dados.
        retorna: None
        '''
        import mysql.connector

        try:
            self.__sistema = mysql.connector.connect(host=self.__localhost, user=self.__user, passwd=self.__passwd)
            if self.__sistema.is_connected():
                print('A conexão com o sistema foi estabelecida.')
            else:
                print('Não foi possivel se conectar ao sistema de gerenciamento de banco de dados!.')
                exit()
        except:
            print('O banco de dados repassado não foi encontrado!!.')
            exit()


    def __criando_um_banco(self, nome_banco):
        '''
        ------> O método de instância executa uma instrução SQL para criar um banco de dados.
        parametro nome_banco: Recebe o nome do banco de dados a ser criado.
        retorna: None
        '''
        cursor = self.__sistema.cursor()
        try:
            cursor.execute(F'CREATE DATABASE {nome_banco} DEFAULT CHARACTER SET latin1 DEFAULT COLLATE latin1_general_ci;')
            print('O banco de dados foi criado com sucesso!.')
            cursor.close()
            self.__sistema.close()
        except:
            print('Não foi possivel criar um banco de dados com esse nome!.')


