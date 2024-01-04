import datetime
import itertools as its

def speed():
    st = datetime.datetime.now()
    #insert code here
    
    fizzes = its.cycle([""] * 2 + ["Fizz"])
    buzzes = its.cycle([""] * 4 + ["Buzz"])
    fizz_buzz = (fizz + buzz for fizz, buzz in zip(fizzes,buzzes))
    result = (word or n for word, n in zip(fizz_buzz, its.count(1)))
    
    for i in its.islice(result, 5000):
        print(i)
    
    et = datetime.datetime.now()
    print(et - st)


if __name__ == '__main__':
    speed()