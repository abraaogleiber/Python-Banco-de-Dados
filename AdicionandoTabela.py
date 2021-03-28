

class BancoDeDados:
    '''
    ----> A classe nos disponibiliza um meio complicado para a implementação de tabelas em um banco de dados
          deve se usada somente para fins de estudo e pesquisa.
    '''
    def __init__(self, host, user, database, passwd):
        '''
        ------> O método inicializador recebe informações e repassa direto ao método que fará conexão.
        parametro host: Recebe o host(endereço) do sistema de bancos de dados.
        parametro user: Recebe o usuário utilizado para logar-se no sistema de bancos de dados.
        parametro database: Recebe o nome do banco residente do sistema de bancos de dados.
        parametro passwd: Recebe a senha de acesso ao sistema de banco de dados.
        '''
        self.conectar_com_sistema(host, user, database, passwd)


    @classmethod
    def conectar_com_sistema(cls, host, user, database, passwd):
        '''
        ------>
        parametro host: Recebe o host(endereço) do sistema de bancos de dados.
        parametro user: Recebe o usuário utilizado para logar-se no sistema de bancos de dados.
        parametro database: Recebe o nome do banco residente do sistema de bancos de dados.
        parametro passwd: Recebe a senha de acesso ao sistema de banco de dados.
        retorna: None
        '''
        import mysql.connector

        cls.sistemaSGBD = mysql.connector.connect(host=host, user=user, database=database, passwd=passwd)
        if cls.sistemaSGBD.is_connected():
            print('Conexão estabelecida com o sistema interno(SGBD).')
        else:
            exit('Não foi possivel se conectar ao sistema local(SGBD).')


    def criar_tabela_no_banco_de_dados(self, nome_tabela):
        '''
        ------> O método criar uma tabela no banco escolhido.
        parametro nome_tabela: Recebe nome da tabela que será criada.
        retorna: None
        '''
        import mysql.connector
        
        try:
            cursor = self.sistemaSGBD.cursor()
            cursor.execute(f'CREATE TABLE {nome_tabela}('
                            'id TINYINT AUTO_INCREMENT, '
                            'nome VARCHAR(30), '
                            'email VARCHAR(40) UNIQUE, '
                            'PRIMARY KEY(id)'
                            ');DEFAULT CHARSET = latin1')
            print(f'A tabela "{nome_tabela}" foi criada com sucesso!.')
        except mysql.connector.Error as erro:
            print(f'Não é possivel criar uma tabela com o nome "{nome_tabela}", talvez já exista!.')
            print(erro)
        finally:
            if self.sistemaSGBD.is_connected():
                cursor.close()
                self.sistemaSGBD.close()
                print('Conexão encerrada com o sistema de interno(SGBD).')
