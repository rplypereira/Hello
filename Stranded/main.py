import world
import os
import platform


player_pos = [0,0]
MAP = world.gen_jungle(10)
MAP_SIZE = 10
world.display_jungle(MAP)

def clear_screen():
    # Clear the terminal screen
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
        
def move_player(direction, player_pos, map_size):
    # Calculate new position based on direction
    new_x, new_y = player_pos
    if direction == "w":  # up
        new_y -= 1
    elif direction == "s":  # down
        new_y += 1
    elif direction == "a":  # left
        new_x -= 1
    elif direction == "d":  # right
        new_x += 1
    
    # Check boundaries
    new_x = max(0, min(new_x, map_size - 1))
    new_y = max(0, min(new_y, map_size - 1))
    
    return [new_x, new_y]

def display_map(map, player_position):
    # Clear the screen before redrawing
    clear_screen()
    
    for y, row in enumerate(map):
        for x, col in enumerate(row):
            if [x, y] == player_position:
                print(world.PLAYER, end=' ')
            else:
                print(col, end=' ')
        print()  # Newline for the next row
        
def main():
    while True:
        # Draw the map with the player in it
        display_map(MAP, player_pos)
        
        # Get player input for movement
        move = input("Move (WASD): ").lower()
        if move in ["w", "a", "s", "d"]:
            # Update the player's position
            player_pos[:] = move_player(move, player_pos, MAP_SIZE)

        # Do something if the player wants to quit
        if move == "q":
            break

# Check if the script is directly run
if __name__ == "__main__":
    main()