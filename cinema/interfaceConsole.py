from Assentos import Assentos
from ControladorAssentos import ControladorAssentos
class interfaceConsole():
  
  def __init__(self,qtd_ass_ocup = 0,qtd_devo = 0,caixa = 0):
    self.__controlador = ControladorAssentos()    
    self.maior_numero_da_matriz = 0
    self.quant_de_zeros_para_numeracao_do_assento = 0
  def main(self):#ajeitar isso#
    controlador = self.get_controlador()
    arq = controlador.carregar_arquivo()
    linhas = controlador.ler_linhas_arquivo(arq)
    
    if linhas == []:
        tamanho_da_sala = self.escolher_tamanho_da_sala()
        quant_de_linhas = int(tamanho_da_sala[0])
        quant_de_colunas = int(tamanho_da_sala[1])
        matriz = self.montar_matriz(quant_de_linhas,quant_de_colunas)
    else:
      esc = self.perguntar_sobre_load()
      if int(esc) == 1:
        linhas_colunas = linhas[0].split(" ")
        quant_de_linhas = int(linhas_colunas[0])
        quant_de_colunas = int(linhas_colunas[1])
        matriz = self.montar_matriz(quant_de_linhas,quant_de_colunas)
        linhas.remove(linhas[0])
        self.carregar_caixa_e_dev(linhas)
        linhas.remove(linhas[0])
        self.carregar_assentos_ocupados(linhas,matriz)
      elif int(esc) == 0:
        tamanho_da_sala = self.escolher_tamanho_da_sala()
        quant_de_linhas = int(tamanho_da_sala[0])
        quant_de_colunas = int(tamanho_da_sala[1])
        matriz = self.montar_matriz(quant_de_linhas,quant_de_colunas)
    controlador.salvar_arquivo(arq)
    self.maior_numero_da_matriz += int((quant_de_linhas * quant_de_colunas)) - 1
    self.quant_de_zeros_para_numeracao_do_assento += int(len(str(self.maior_numero_da_matriz)))
    self.loop_principal(quant_de_linhas,quant_de_colunas,matriz)
  def loop_principal(self,quant_de_linhas,quant_de_colunas,matriz):
    controlador = self.get_controlador()
    loop_menu = True
    while loop_menu:
      self.imprimir_sala(quant_de_linhas,quant_de_colunas,matriz)
      escolha_menu = self.exibir_menu()
      while int(escolha_menu) > 4 or int(escolha_menu) < 1:
          print("Escolha uma opção válida (número inteiro 1-4)")
          escolha_menu = self.exibir_menu()
      if int(escolha_menu) == 1:
        self.imprimir_sala_com_os_lugares_ocupados(quant_de_linhas,quant_de_colunas,matriz)
        cadeiras_escolhidas = self.cadeiras_escolhidas(quant_de_linhas,quant_de_colunas)
        av = True
        while av:
          v = controlador.comprar_assentos(cadeiras_escolhidas,matriz)
          if v == 0:
            av = True
          if v == 1:
            av = False
            break
          cadeiras_escolhidas = self.cadeiras_escolhidas(quant_de_linhas,quant_de_colunas)
      if int(escolha_menu) == 2:
        self.imprimir_sala_com_os_lugares_ocupados(quant_de_linhas,quant_de_colunas,matriz)
        cadeiras_escolhidas = self.cadeiras_escolhidas(quant_de_linhas,quant_de_colunas)
        av = True
        while av:
          v = controlador.devolver_assentos(cadeiras_escolhidas,matriz)
          if v == 0:
            av = True
          if v == 1:
            av = False
            break
          cadeiras_escolhidas = self.cadeiras_escolhidas(quant_de_linhas,quant_de_colunas)
      if int(escolha_menu) == 3:
        controlador.emitir_resumo()
      if int(escolha_menu) == 4:
        loop_menu = False
        arq = controlador.carregar_arquivo_apagando()
        self.salvar_matriz_e_caixa(quant_de_linhas,quant_de_colunas,arq)
        self.salvar_assentos_ocupados(arq,matriz)
  
  
  def perguntar_sobre_load(self):
    esc = input("Existe um arquivo que podemos carregar, quer carregar ?1 - SIM, 0 - NÃO  ")
    ava = True
    while ava:
      if (esc.isdigit()):
        if int(esc) == 1 or int(esc) == 0:
          ava = False
          break
      esc = input("Existe um arquivo que podemos carregar, quer carregar ?1 - SIM, 0 - NÃO  ")
    return esc
  
  
  def carregar_assentos_ocupados(self,linhas,matriz):
    controlador = self.get_controlador()
    for c in range(len(linhas)):
      linhas[c] = linhas[c].replace("\n","")
    assentos_ocupados = controlador.retornar_assentos(linhas,matriz)
    for c in assentos_ocupados:
      c.set_disponivel(False)
      controlador.qtd_ass_ocup += 1
          
  
  
  
  def carregar_caixa_e_dev(self,linhas):
    controlador = self.get_controlador()
    caixa_dev = linhas[0].split(" ")
    caixa = float(caixa_dev[0])
    quant_de_dev = float(caixa_dev[1])
    controlador.caixa += caixa
    controlador.qtd_devo += quant_de_dev
  
  def salvar_matriz_e_caixa(self,quant_de_linhas,quant_de_colunas,arq):
    controlador = self.get_controlador()
    texto1 = "{} {}\n".format(quant_de_linhas,quant_de_colunas)
    controlador.escrever_arquivo(texto1,arq)
    texto = "{} {}\n".format(controlador.caixa,controlador.qtd_devo)
    controlador.escrever_arquivo(texto,arq)
  
  
  def salvar_assentos_ocupados(self,arq,matriz):
    controlador = self.get_controlador()
    for i in matriz:
      for j in i:
        if j.disponivel == False:
          texto = "{}\n".format(j.numero)
          controlador.escrever_arquivo(texto,arq)
    controlador.salvar_arquivo(arq)
  def get_controlador(self):
    return self.__controlador
  def escolher_tamanho_da_sala(self):
    num_de_linhas = (input ("Informe o número de linhas: "))
    while not num_de_linhas.isdigit ():
        print ("Escreva um número inteiro!")
        num_de_linhas = (input ("Informe o número de linhas: "))
    num_de_colunas = (input ("Informe o número de colunas: "))
    while not num_de_colunas.isdigit ():
        print ("Escreva um número inteiro!")
        num_de_colunas = (input ("Informe o número de colunas: "))
    num_de_linhas = int (num_de_linhas)
    num_de_colunas = int (num_de_colunas)
    return [num_de_linhas,num_de_colunas]
  def montar_matriz(self,num_de_linhas,num_de_colunas):
    matriz = []
    contador = 0
    maior_numero_da_matriz = (num_de_linhas * num_de_colunas) - 1
    quant_de_zeros_para_numeracao_do_assento = int(len(str(maior_numero_da_matriz)))
    for c in range (0, num_de_linhas):
        matriz.append ([None] * num_de_colunas)
        for i in range (0, num_de_colunas):
          matriz[c][i] = Assentos(str(contador).zfill(quant_de_zeros_para_numeracao_do_assento),20 - c,True)
          contador += 1
    return matriz
  def imprimir_sala(self,num_de_linhas,num_de_colunas,matriz): 
    linha_matriz = ""
    for c in range (0, num_de_linhas):
        linha_matriz = ""
        for i in range (0, num_de_colunas):
            linha_matriz += " {}".format (matriz[c][i].numero)
        print(linha_matriz)
  def imprimir_sala_com_os_lugares_ocupados(self,num_de_linhas,num_de_colunas,matriz):
    linha_matriz = ""
    for c in range (0, num_de_linhas):
        linha_matriz = ""
        for i in range (0, num_de_colunas):
            if matriz[c][i].disponivel == True:
              linha_matriz += " {}".format (matriz[c][i].numero)
            else:
              linha_matriz += " xx"
        print(linha_matriz)
  def exibir_menu(self):
    escolha_da_operacao = input("""Bem vindo ao sistema de ingressos.
    Escolha a operação:
    1 - Comprar ingressos
    2 - Devolver ingressos
    3 - Resumo das vendas
    4 - Sair
    Digite sua escolha: """)
    while not escolha_da_operacao.isdigit():
        print ("Escreva um número inteiro!")
        escolha_da_operacao = input("""Bem vindo ao sistema de venda de ingressos.
        Escolha a operação:
        1 - Comprar ingressos
        2 - Devolver ingressos
        3 - Resumo das vendas
        4 - Sair
        Digite sua escolha: """)

    return escolha_da_operacao
  def cadeiras_escolhidas(self,num_de_linhas,num_de_colunas):#ajeitar remove_repetidos#
    avaliador2 = True
    while avaliador2:
      escolha_do_assento = input ("Escolha dos assentos: ").split (",")
      quant_de_assentos_requeridos_para_comprar = len (escolha_do_assento)
      for c in range(0,quant_de_assentos_requeridos_para_comprar):
        if escolha_do_assento[c].isdigit():
            avaliador2 = False
        else:
            print("Escolha um assento válido!")
            avaliador2 = True
            break
        if int(escolha_do_assento[c]) > (num_de_colunas * num_de_linhas) - 1:
            print("Escolha os assentos entre 0 e {}".format((num_de_colunas * num_de_linhas) - 1))
            avaliador2 = True
            break
        if len(escolha_do_assento[c]) < self.quant_de_zeros_para_numeracao_do_assento:
          escolha_do_assento[c] = "{}".format(str(escolha_do_assento[c]).zfill(self.quant_de_zeros_para_numeracao_do_assento))
      escolha_do_assento = self.remove_repetidos(escolha_do_assento)
    return escolha_do_assento
  def procurar (self,lista, valor): # função que procura um elemento em uma matriz(lista dentro de lista)#
    return [(lista.index(x), x.index(valor)) for x in lista if valor in x]
  def remove_repetidos(self,lista):
      l = []
      for i in lista:
          if i not in l:
              l.append(i)
      l.sort()
      return l