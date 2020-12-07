'''
	Intro to modules
'''
def getPrime():
    __name__
my_primes = []
number= int(input("Enter Number To Prime Number: "))
for num in range(number, number+100):
    isPrime = True
    for i in range(2, num):
          if num % i == 0:
              isPrime = False
    if isPrime:
        my_primes.append(num)
print(my_primes)

if __name__ == '__main__':
    getPrime()
    

    
    
   