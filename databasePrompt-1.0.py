import  sqlite3
import os
DBName=input('Nome do Banco de Dados (Se houver ".db", inclua): ')
conex=sqlite3.connect(DBName)
c = conex.cursor()
def cls():
    os.system('cls')
def TabelaChoose():
    c.execute("SELECT rowid, name from sqlite_master WHERE type='table';")
    listaIndices=[]
    listaNomeTable=[]
    for i in c.fetchall():
        print('{}: {}'.format(i[0], i[1]))
        listaIndices.append(i[0])
        listaNomeTable.append(i[1])
    print('-')
    a=input('Escolha o número da TABELA a ser editada (CRIAR para criar uma nova/DELETAR para deletar) (''CLOSE'' para fechar): ')
    TabelaEscolhida=''
    if a.upper()=='CLOSE':
        print('Programa fechando...')
        fechar+=1
    if a.upper()!='CLOSE' and a.isdigit()==True:
        if int(a) in listaIndices:
            cls()#
            L1=listaIndices.index(int(a))
            L2=listaNomeTable[L1]
            tabEscolhida=str(L2)
            c.execute("SELECT rowid, * from "+tabEscolhida+"")
            fetchada=c.fetchall()
            voidchecker=0
            if fetchada!=[]:
                #
                NumeroElementos=len(fetchada[0])
                #
                NumLeft=NumeroElementos
                print('Tabela: ')
                for i in fetchada:
                    #
                    listaPrint=[]
                    #
                    NumUp=0
                    atual=''
                    for e in i:
                        NumUp+=1
                        if len(listaPrint)<NumeroElementos:
                            listaPrint.append(str(e))
                        if len(listaPrint)>=NumeroElementos:
                            c.execute("SELECT rowid, * FROM "+tabEscolhida+"")
                            for index, item in enumerate(listaPrint, start=1):
                                print(item, end='--' if index % NumeroElementos else '\n')
                            for l in listaPrint:
                                listaPrint.remove(l)
            print('---')
            c.execute("SELECT * from "+tabEscolhida+"")
            namesColunas = list(map(lambda x: x[0], c.description))
            print('Nomes das colunas:')
            print(namesColunas)
            print('---')
            if fetchada!=[]:
                print('Digite "CRIAR" para criar uma linha')
                print('Digite "DELETAR" para deletar uma linha')
                print('Digite "EDITAR" para modificar uma linha')
                print('("Close" para voltar)')
            if fetchada==[]:
                voidchecker+=1
                print('')
                print('[TABELA VAZIA]')
                print('Digite "CRIAR" para criar uma linha')
                print('("Close" para voltar)')
                print('---')
            comando=input('Comando: ')
            ###############################################################MODULO DE CRIAÇÃO##################
            if comando.upper()=='CRIAR' and voidchecker==0:
                #
                novaLinha=[]
                #
                contadorCRIAR=0
                nomeColunaAtual=''
                while len(novaLinha)<NumeroElementos-1:
                    nomeColunaAtual=namesColunas[contadorCRIAR]
                    contadorCRIAR+=1   
                    inputCRIAR=input('{}: '.format(nomeColunaAtual))
                    novaLinha.append(inputCRIAR)
                acaboLoop45=0
                while acaboLoop45==0:
                    escolhaCRIAR=input('Deseja realmente criar a linha: {} ? [S(Sim)/N(Não)]'.format(novaLinha))
                    if escolhaCRIAR.upper()=='S':
                        print('criar')
                        Aaaddd=str(novaLinha)
                        AdNovo=Aaaddd.replace('[', '(')
                        AdDefinitivo=AdNovo.replace(']', ')')
                        print(Aaaddd)
                        c.execute("""INSERT INTO """+tabEscolhida+"""  VALUES """+AdDefinitivo+"""""")
                        conex.commit()
                        acaboLoop45+=1
                    if escolhaCRIAR.upper()=='N':
                        print('cancelo')
                        acaboLoop45+=1
                    if escolhaCRIAR.upper()!='S' and escolhaCRIAR.upper()!='N':
                        print('não compreendi')
            ##################################################################################################
            if comando.upper()=='CRIAR' and voidchecker==1:
                c.execute("SELECT * FROM "+tabEscolhida+"")
                namesColunas = list(map(lambda x: x[0], c.description))
                print('Nomes das colunas:')
                print(namesColunas)
                #
                novaLinha=[]
                #
                contadorCRIAR=0
                nomeColunaAtual=''
                while len(novaLinha)<len(namesColunas):
                    nomeColunaAtual=namesColunas[contadorCRIAR]
                    contadorCRIAR+=1   
                    inputCRIAR=input('{}: '.format(nomeColunaAtual))
                    novaLinha.append(inputCRIAR)
                acaboLoop45=0
                while acaboLoop45==0:
                    escolhaCRIAR=input('Deseja realmente criar a linha: {} ? [S(Sim)/N(Não)]'.format(novaLinha))
                    if escolhaCRIAR.upper()=='S':
                        print('criar')
                        Aaaddd=str(novaLinha)
                        AdNovo=Aaaddd.replace('[', '(')
                        AdDefinitivo=AdNovo.replace(']', ')')
                        print(Aaaddd)
                        c.execute("""INSERT INTO """+tabEscolhida+"""  VALUES """+AdDefinitivo+"""""")
                        conex.commit()
                        acaboLoop45+=1
                    if escolhaCRIAR.upper()=='N':
                        print('cancelo')
                        acaboLoop45+=1
                    if escolhaCRIAR.upper()!='S' and escolhaCRIAR.upper()!='N':
                        print('cancelo')
                        acaboLoop45+=1
                    if escolhaCRIAR.upper()!='S' and escolhaCRIAR.upper()!='N':
                        print('não compreendi')                        
            ###############################################################MODULO DE DELEÇÃO##################            
            if comando.upper()=='DELETAR':
                delEscolha=input('Escolha o número da linha a ser deletada: ')
                acaboLoop46=0
                while acaboLoop46==0:
                    escolhaDEL=input('Deseja realmente deletar a linha: {} ? [S(Sim)/N(Não)]'.format(delEscolha))
                    if escolhaDEL.upper()=='S':
                        print('deletar')
                        c.execute("""DELETE from """+tabEscolhida+""" where rowid = """+delEscolha+"""""")
                        acaboLoop46+=1
                        conex.commit()
                    if escolhaDEL.upper()=='N':
                        print('cancelo')
                        acaboLoop46+=1
                    if escolhaDEL.upper()!='S' and escolhaCRIAR.upper()!='N':
                        print('não compreendi')
            ###############################################################MODULO DE EDIÇÃO####################
            if comando.upper()=='EDITAR':
                namesColunas2=[]
                c.execute("SELECT rowid, * from "+tabEscolhida+"")
                for i in namesColunas:
                    namesColunas2.append(i.upper())
                editEscolha=input('Escolha o número da linha a ser editada: ')
                editColuna=str(input('Qual o nome da coluna a ser editada?: '))
                if editColuna.upper() in namesColunas2:
                    qualsera=namesColunas2.index(editColuna.upper())
                    qualsera2=str(namesColunas[qualsera])
                    newValorEdit=str(input('Novo valor para {}: '.format(qualsera2)))
                    c.execute('UPDATE '+tabEscolhida+' SET '+qualsera2+' = "'+newValorEdit+'" WHERE rowid = '+editEscolha+'')
                    conex.commit()
                if editColuna.upper() not in namesColunas2:
                    print('Essa é uma resposta inválida. Tente novamente.')
            ##################################################################################################
            cls()#
                    
    if a.isdigit()==True and a.upper()!='CRIAR' and int(a) not in listaIndices and a.upper()!='DELETAR':
        print('Índice de tabela não existente. Tente novamente.')
    if a.upper()!='CLOSE' and a.isdigit()==False and a.upper()!='CRIAR' and a.upper()!='DELETAR':
        print('Digite apenas os comandos indicados ou números de tabelas.')
    if a.upper()=='CRIAR':
        novoNomeTabela=input('Nome da nova tabela: ')
        while True:
            numeroRowsTabela=input('Número de colunas da tabela (MIN=2/MAX=10): ')
            if numeroRowsTabela.isdigit()==True and int(numeroRowsTabela)<11:#
                rowsESCRITOS=''
                rowsCOUNTER=1
                while rowsCOUNTER<=int(numeroRowsTabela):
                    porhora=input('Nome da coluna {}: '.format(str(rowsCOUNTER)))
                    if rowsCOUNTER==1:
                        rowsESCRITOS+=('({},'.format(porhora))
                    if rowsCOUNTER>1 and rowsCOUNTER<int(numeroRowsTabela):
                        rowsESCRITOS+=(' {},'.format(porhora))
                    if rowsCOUNTER==int(numeroRowsTabela):
                        rowsESCRITOS+=('{})'.format(porhora))
                    rowsCOUNTER+=1
                novoargumento= """ CREATE TABLE """+novoNomeTabela+""" """+rowsESCRITOS+""""""
                c.execute(novoargumento)
                conex.commit()
                break
            else:
                print('digita direito ladrão plmds')
    #
    if a.upper()=='DELETAR':
        NumTabelaDel=input('Número da tabela a ser deletada ("CLOSE" para cancelar): ')
        if NumTabelaDel.isdigit()==True:
            NumTD=int(NumTabelaDel)
            if NumTD<1:
                print('ERRO: Insira um índice número existente')
            if NumTD>=1 and NumTD>=len(listaIndices):
                NameToDelete=listaNomeTable[NumTD-1]
                c.execute("""DROP TABLE """+NameToDelete+"""""")
            if NumTD>len(listaIndices):
                print('ERRO: Insira um índice número existente')
        if NumTabelaDel.isdigit()!=True:
            print('ERRO: Insira um índice número existente')
    conex.commit()
    cls()
#-.-. .- .. --- .-. ... ...-
fechar=0
while fechar==0:
    print('--------')
    TabelaChoose()
conex.commit()
conex.close()
