from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


# Magia negra
fire = Spell("Fire", 10, 10, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Magia blanca

cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Instantiate Objects

potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-potion", "potion", "heals for 100 HP", 100)
superpotion = Item("Super potion", "potion", "Heals  500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party´s HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 5}, {"item": grenade, "quantity": 5}]


# Instancio participantes
player1 = Person("Valos :", 3260, 132, 60, 34, player_spells, player_items)
player2 = Person("Nick  :", 4160, 188, 60, 34, player_spells, player_items)
player3 = Person("Robot :", 3089, 174, 60, 34, player_spells, player_items)
enemy = Person("Drake", 11200, 321, 315, 25, [], [])
players = [player1, player2, player3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("================================")

    print("\n\n")

    print(bcolors.HEADER + " NAME" + bcolors.ENDC + bcolors.OKGREEN + "   HP" + bcolors.ENDC + "                                        " + bcolors.OKBLUE + "MP" + bcolors.ENDC)
    for player in players:
        player.get_stats()

    print("\n")

    for player in players:
        player.choose_action()

        choice = input("   Choose action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_Damage()
            enemy.take_dmg(dmg)
            print("You attacked for:", dmg, "points of damage.")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("   Choose magic:")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + "heals for ", str(magic_dmg), " HP. " + bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_dmg(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue
            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n")

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + "fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_dmg(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)
    enemy_choice = 1


    enemy_dmg = enemy.generate_Damage()
    player1.take_dmg(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)
    print("--------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win !!!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False
