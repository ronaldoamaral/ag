import math

class Cromossomo():
  """ """
  def __init__(self, nbits, min, max):
    self.min = min
    self.max = max
    self.gens = self.gerar_gens(nbits) 
    
  def gerar_gens(self, nbits):
    return '1000101110110101000111'
    
  def valor(self):
    """ Retorna um valor real correspondente a conversao do binario"""
    nbits = len(self.gens)
    dec = int(self.gens,2)
    real = self.min+dec*((self.max-self.min)/(math.pow(2,nbits)-1))
    return real
  

class AG():
  """ """
  def __init__(self, precisao, min, max):
    self.min = min
    self.max = max
    self.precisao  = precisao
    self.n_bits = self.nbits()
    self.pop = []
    
  def nbits(self):
    n = math.log((self.max-self.min) * math.pow(10,self.precisao))
    return int(n)

  def gerar_populacao(self, tamanho):
    for i in range(tamanho):
      self.pop.append(Cromossomo(self.n_bits, self.min, self.max))   

  
def main():
  ag = AG(10, -1, 2)
  ag.gerar_populacao(10)
  for i in ag.pop:
    print i.gens + " = " + str(i.valor())

if __name__ == "__main__":
  main()  
