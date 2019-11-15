class Assentos():
  def __init__(self,num,preco,disponivel):
    self.numero = num
    self.preco = preco
    self.disponivel = disponivel
  def get_numero(self):
    return self.numero
  def set_numero(self,novo_numero):
    self.numero = novo_numero
  def get_preco(self):
    return self.preco
  def set_preco(self,novo_preco):
    self.preco = novo_preco
  def get_disponivel(self):
    return self.disponivel
  def set_disponivel(self,novo_boolean):
    self.disponivel = novo_boolean

  def __eq__(self,assento):
    return self.numero == assento.numero