## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys
    
def main(n) :
    d = 0
    i = 1
    while i <= n:
        if n % i == 0:
            d += 1
        i += 1
    return d
    
def ap(n):
    num_divisores = main(n)
    i = 1
    while i < n:
        if main(i) >= num_divisores:
            return "not anti-prime"
        i += 1
    return "anti-prime"  
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python antiprime.py <entero-positivo>")
    else:
        num = int(sys.argv[1])
        res = ap(num)
        print(res)

