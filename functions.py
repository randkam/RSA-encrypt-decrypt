def checkPrivateKey( d, e, p, q ):
    return (d * e) % ((p-1)*(q-1)) == 1

  
def extendedEuclid(a, b):
  if a == 0:
      return [b, 0, 1]
  else:
      [gcd, x, y] = extendedEuclid(b % a, a)
      return [gcd, y - (b // a) * x, x]

def modInverse(a, m):
  simplifiedGcd = extendedEuclid(a, m)
  gcd = simplifiedGcd[0]
  x = simplifiedGcd[1]
  if gcd ==1:
    return x % m

def genPrivateKey(e, p, q):
  key = (p - 1) * (q - 1)
  d = modInverse(e, key)

  return d


def reduceModulo(m, e, n):
  reducedNum = 1
  while e > 0:
    if e % 2 == 1:
      reducedNum = (reducedNum * m) 
      reducedNum = reducedNum % n

    m = (m * m) 
    m = m % n
    e  = e // 2

  return reducedNum
  
def encryptRSA( message, e, n ):
  encryptedList = []
  for i in range(len(message)):
    encryptedList.append(reduceModulo(message[i], e, n))   
  return encryptedList


def decryptRSA( ciphertext, d, q, p):
  decryptedList = []
  for i in range(len(ciphertext)):
    decryptedList.append(reduceModulo(ciphertext[i], d, q*p))
  return decryptedList


