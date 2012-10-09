import math

def nbits(p, min, max):
  n = math.log((max-min) * math.pow(10,p))
  return int(n)
  
def bin2real(bin, min, max):
  nbits = len(bin)
  dec = int(bin,2)
  real = min+dec*((max-min)/(math.pow(2,nbits)-1))
  return real
  
  
def main():
  n = nbits(22, -1,2)
  print bin2real('1000101110110101000111', -1, 2)


if __name__ == "__main__":
  main()  
