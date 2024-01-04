import datetime
import itertools as its

"""exercise preview

write a program that shows via console the numbers between 1,n
both numbers included, with a breakline between each number
substituting the following
    -multiples of three for the word fizz
    -multiples of 5 for the word buzz
    -multiples of both for the word fizzbuzz
    -time it    
"""
def speed():
    
    """speed
    calculates time at the beginning of the script
    calculates time at the end of the script
    prints end time - start time
    """
    st = datetime.datetime.now()
    
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