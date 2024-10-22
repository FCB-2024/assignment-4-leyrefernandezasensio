## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main() :
	i = 1
r = 0
x = int(input("Enter one value: "))

while i <= x:
    if x % i == 0:
        r = r + i
    i = i + 1
l = x - 1
s = 0
while l >= 1 and s < r:
    a = 1
    s = 0
    while a <= l:
        if l % a == 0:
            s = s + a
        a = a + 1
    l = l - 1
if s > r:
    print("not antiprime")
else:
    print("antiprime")

	return("anti-prime")

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main())
