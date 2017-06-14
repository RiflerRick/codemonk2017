def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def main():
    for i in range(1, 12):
        print(gcd(11,i))

if __name__=="__main__":
    main()