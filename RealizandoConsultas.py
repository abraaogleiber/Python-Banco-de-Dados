

class BancoDeDados:

    def __init__(self, host, user, database, passwd):
        '''
        ------> Realiza uma busca dentro de um banco de dados.
        parametro host: Recebe o endereço do serviço MySql de sua máquina.
        parametro user: Recebe o usuário com para acesso do sistema.
        parametro database: Recebe o banco de dados para acesso.
        parametro passwd: Recebe a senha para validação de entrada.
        '''
        self.host = host
        self.user = user
        self.database = database
        self.passwd = passwd


    def realizar_conexao(self):
        '''
        ------> Faz a conexão com o SGBD local.
        retorna: None
        '''
        import mysql.connector
        from mysql.connector import Error
        global conexao

        try:
            conexao = mysql.connector.connect(host=self.host, user=self.user, database=self.database, passwd=self.passwd)
            print('Conexão estabelecida com sucesso!.\n')
        except Error:
            exit('Erro ao tentar se conectar ao serviço SGBD local.')


    def consulta_ao_banco(self):
        '''
        ------> Realiza a consulta ao dados armazenados no banco.
        retorna: None
        '''
        if conexao.is_connected():
            cursor = conexao.cursor()

            instrucao_sql = F"SELECT * FROM alunos"

            try:
                cursor.execute(instrucao_sql)
                retorno = cursor.fetchall()
            except Exception:
                exit('Você inseriu um dos valores de forma errada!. Tente novamente.')
        else:
            print('O programa não tem acesso ao servidor local.')
            exit()


        for regis in retorno:
            media = (regis[1] + regis[2] + regis[3] + regis[4]) / 4
            print(
                  'Nome' + 'N1'.rjust(15) + 'N2'.rjust(15) + 'N3'.rjust(15) + 'N4'.rjust(15) + 'Media'.rjust(15) + '\n'
                  f'{regis[0]}' + f'{regis[1]}'.rjust(13) + f'{regis[2]}'.rjust(15) + f'{regis[3]}'.rjust(15) + f'{regis[4]}'.rjust(15) + f'{media:.1f}\n'.rjust(15)
                 )



if __name__ == '__main__':
    teste = BancoDeDados('localhost', 'root', 'alunos', 'abraao2020') #---passo---(1)
    teste.realizar_conexao() #---passo---(2)
    teste.consulta_ao_banco() #---passo---(3)