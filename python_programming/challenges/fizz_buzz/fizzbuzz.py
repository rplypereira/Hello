import datetime

def speed():
    st = datetime.datetime.now()
    n = 1

    while n <= 5000:
        if n % 15 == 0 :
            print(f"{n} fizzbuzz\n")
        else:
            if n % 3 == 0:
                print(f"{n} fizz\n")
            elif n % 5 == 0:
                print(f"{n} buzz\n")
            else:
                print(f"{n}\n")
        n += 1
    et = datetime.datetime.now()
    
    print(et - st)

if __name__ == '__main__':
    speed()
    
