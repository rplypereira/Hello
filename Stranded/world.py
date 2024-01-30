import random

#create some constants so that we can iterate over them!
GRASS = "🟩"
WATER = "🟦"
TREES = "🌴"
SEED = random.seed(1)
PLAYER = "🤖"
# Setting the size of the grid IE.-10x10
GRID_SIZE = 10

# Function to generate the jungle
def gen_jungle(grid_size):
    jungle = []
    return [
        [
            GRASS if random.random() < 0.7
            else TREES if random.random() < 0.9
            else WATER
            for _ in range(grid_size)
        ]
        for _ in range(grid_size)
    ]

def display_jungle(jungle):
    for row in jungle:
        print("".join(row))

def main():
    my_jungle = gen_jungle(GRID_SIZE)
    display_jungle(my_jungle)
    
if __name__ == "__main__":
    main()
            