import random

print("Hello Human!")
player_hp = 16

print("You have spawned into a desolate world where the law exists only in ROCK PAPER SCISSORS")
print("Defeat every enemy to win!")

monsters = [("verity", 3), ("mewity", 4), ("the great verity ultra hypersonic very cool fireproof bulletproof blah blah blah blah dragon", 6)]
fight_number = 1

for name, enemy_hp in monsters:
    print("\n--- Fight", fight_number, "of", len(monsters), "---")
    print("A " + name + " appears in front of you!")

    while player_hp > 0 and enemy_hp > 0:
        print("\nYour HP:", player_hp, "|", name, "HP:", enemy_hp)
        choice = input("Pick Rock, Paper, or Scissors\n").lower().strip()

        if choice == "shoot":
            print("404 3rr0r! y0u w3r3n'7 5upp053d 70 d0 7h15!")
            player_hp = 0
            break
        elif choice not in ["rock", "paper", "scissors"]:
            print("That's not a valid move!")
            continue

        enemy = random.choice(["rock", "paper", "scissors"])
        print("ROCK PAPER SCISSOR SHOOT!")
        print("Enemy picked", enemy)

        if choice == enemy:
            print("Tie!")
        elif choice == "rock" and enemy == "scissors":
            print("You win!")
            enemy_hp = enemy_hp - 1
        elif choice == "paper" and enemy == "rock":
            print("You win!")
            enemy_hp = enemy_hp - 1
        elif choice == "scissors" and enemy == "paper":
            print("You win!")
            enemy_hp = enemy_hp - 1
        else:
            print("You lose!")
            player_hp = player_hp - 1

    if player_hp <= 0:
        print("Game over!")
        break

    print("You defeated the " + name + "!")
    fight_number = fight_number + 1

if player_hp > 0:
    print("\nGreat job! You survived and won every fight!")




