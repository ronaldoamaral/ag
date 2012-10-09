import math

class Cromossomo():

  def __init__(self, nbits):
    self.gens = self.gerar_gens(nbits) 
    
  def gerar_gens(self, nbits):
    return '1000101110110101000111'
    
  def valor(self, min, max):
    """ Retorna um valor real correspondente a conversao do binario"""
    nbits = len(self.gens)
    dec = int(self.gens,2)
    real = min+dec*((max-min)/(math.pow(2,nbits)-1))
    return real
  

class AG():

  def __init__(self, precisao, min, max):
    self.min = min
    self.max = max
    self.precisao  = precisao
    self.n_bits = self.nbits()
    self.pop = []
    
  def gerar_populacao(self, tamanho):
    for i in range(tamanho):
      self.pop.append(Cromossomo(self.n_bits))
  
  def nbits(self):
    n = math.log((self.max-self.min) * math.pow(10,self.precisao))
    return int(n)
   

  
def main():
  ag = AG(10, -1, 2)
  ag.gerar_populacao(10)
  print ag.pop[0].valor(-1,2)

if __name__ == "__main__":
  main()  
