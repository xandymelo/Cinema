import os
os.chdir(r"C:\Users\xandy\Desktop\cinema")
class ControladorAssentos():
  maior_numero_da_matriz = 0
  quant_de_zeros_para_numeracao_do_assento = 0
  def __init__(self,qtd_ass_ocup = 0,qtd_devo = 0,caixa = 0):
    self.caixa = caixa
    self.qtd_devo = qtd_devo
    self.qtd_ass_ocup = qtd_ass_ocup
  def retornar_assentos(self,list_assentos,matriz):#pega a lista com os numeros, retorna uma lista com os assentos dos respectivos numeros#
    list = []
    for d in list_assentos: 
      for i in matriz:
        for j in i:
          if str(j.numero).zfill(ControladorAssentos.quant_de_zeros_para_numeracao_do_assento) == d:
            list.append(j)
    return list
  def comprar_assentos(self,list_assentos,matriz):#ajeitar isso##achar o objeto a partir do obj.numero dela#
    list = self.retornar_assentos(list_assentos,matriz)
    avaliador = True
    soma = 0
    for c in list:
      if c.disponivel == False:
        print("Escolha um assento disponível")
        avaliador = False
        return 0
    if avaliador == True:
      for c in list:
        c.set_disponivel(False)
        soma += c.preco
        self.caixa += c.preco
        self.qtd_ass_ocup += 1
      print("Seus assentos foram comprados por sucesso, você pagou R${:.2f}".format(soma))
      return 1
    
  def devolver_assentos(self,list_assentos,matriz):
    list = self.retornar_assentos(list_assentos,matriz)
    soma = 0
    avaliador = True
    for c in list:
      if c.disponivel == True:
        print("Escolha um assento não disponível")
        avaliador = False
        return 0
    if avaliador == True:
      for c in list:
        c.set_disponivel(True)
        soma += c.preco * 0.9
        self.caixa -= c.preco * 0.9
        self.qtd_ass_ocup -= 1
        self.qtd_devo += 1
    print("Seus ingressos foram devolvidos com sucesso, você ganhou R${:.2f} de volta.".format(soma))
    return 1

  def emitir_resumo(self):
    print("Saldo: R${:.2f}".format(self.caixa))
    print("Quantidade de Assentos ocupados: {:.2f}".format(self.qtd_ass_ocup))
    print("Quantidade de devoluções: {:.2f}".format(self.qtd_devo))
  def salvar_arquivo(self,arq):
    arq.close()
  def carregar_arquivo(self):
    arq = open("load.txt","r+")
    return arq
  def carregar_arquivo_apagando(self):
    arq = open("load.txt","w")
    return arq
  def ler_linhas_arquivo(self,arq):
    linhas = arq.readlines()
    return linhas
  def escrever_arquivo(self,texto,arq):
    arq.write(texto)
