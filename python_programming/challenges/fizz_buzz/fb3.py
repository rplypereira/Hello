import datetime

def speed():
    st = datetime.datetime.now()
    #insert code here
    print(*map(lambda i: 'Fizz'*(not i%3) + 'Buzz'*(not i%5) or i, range(1,5000)),sep = '\n')
    et = datetime.datetime.now()
    print(et - st)


if __name__ == '__main__':
    speed()