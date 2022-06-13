w = "wizard"
e = "elf"
h = "human"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50

my_hp = 0
my_damage = 0
my_character = ""


while True:
    print("Your options are,\n1.", w, "\n2.", e, "\n3.", h)
    character = input("Choose ypur caharacter:")
    if character == "1":
        my_character = w
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2":
        my_character = e
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3":
        my_character = h
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character")


print("You chose:", my_character)
print("Health:", my_hp)
print("Damage", my_damage)

while True:
    dragon_hp = dragon_hp - my_damage
    print("Your", my_character, "damaged the Dragon")
    print("The dragon's hitpoints are now:", dragon_hp)
    if dragon_hp <= 0:
        print("The dragon has lost the battle!")
        break
    my_hp = my_hp - dragon_damage
    print("The dragon strikes backs at", my_character)
    print("The", my_character, "hitpoints are now", my_hp)
    if my_hp <= 0:
        print("the", my_character, "has lost the battle!")
        break
