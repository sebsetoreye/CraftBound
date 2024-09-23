

class Weapon:
    def __init__(self, name, range, width, damage):
        self.name = name
        self.range = range  # Number of tiles the weapon can hit
        self.width = width 
        self.damage = damage  # Damage per hit

    def __str__(self):
        return f"{self.name}: Range {self.range}, Damage {self.damage}, Width {self.width}"



def hit_enemy_with_weapon(player, enemies, weapon):
    print(f"Player position: ({player.x}, {player.y}), direction: {player.direction}")
    print(f"Attacking with {weapon}")

    # Set initial target to player's position
    target_x, target_y = player.x, player.y

    # Determine how far to move in each direction
    if player.direction == "up":
        dx, dy = -1, 0  # Move up in the grid
        wx, wy = 0, 1   # Width is horizontal (along y-axis)
    elif player.direction == "down":
        dx, dy = 1, 0   # Move down in the grid
        wx, wy = 0, 1   # Width is horizontal (along y-axis)
    elif player.direction == "left":
        dx, dy = 0, -1  # Move left in the grid
        wx, wy = 1, 0   # Width is vertical (along x-axis)
    elif player.direction == "right":
        dx, dy = 0, 1   # Move right in the grid
        wx, wy = 1, 0   # Width is vertical (along x-axis)

    # Loop through all tiles in the weapon's range
    for step in range(1, weapon.range + 1):  # Weapon range determines how far it can attack
        target_x += dx
        target_y += dy

        # Check width for each step in the range
        for width_offset in range(-(weapon.width // 2), (weapon.width // 2) + 1):
            # Calculate width offset
            width_x = target_x + wx * width_offset
            width_y = target_y + wy * width_offset

            # Check if an enemy is at this position
            for enemy in enemies:

                if enemy.x == width_x and enemy.y == width_y:
                    enemy.health -= weapon.damage  # Apply weapon-specific damage
                    if not enemy.is_alive():
                        print(f"Enemy defeated by {weapon.name}!")
                    else:
                        print(f"Enemy hit by {weapon.name}! Health remaining: {enemy.health}")

    print(f"{weapon.name} attack complete.")

