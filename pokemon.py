import math
import random

LEVEL_UP_CONST = 1.01
NATURE_CONST = 1

NATURES = {
  "jolly": ("speed", "sp_atk"),
  "timid": ("speed", "atk"),
  "adamant": ("atk", "sp_atk")
}

MOVES = {
  "thunder": ("thunder", 1.0, 0.5, "special"),
  "tackle": ("normal", 0.5, 0.95, "physical")
}

EFFECTIVENESS = {
  "thunder": (("water", "flying"), ("grass", "thunder"), ("ground")),
  "normal": ((), ("steel", "rock"), ("ghost")),
  "water": (("fire", "ground", "rock"), ("water", "grass"), ())
}

class Stats:
  def __init__(self, atk, defense, sp_def, sp_atk, speed, health, nature):
    self.atk = atk
    self.defense = defense
    self.sp_def = sp_def
    self.sp_atk = sp_atk
    self.speed = speed
    self.health = health
    self.nature = nature

  def raise_stats(self):
    boost, decrease = NATURES[self.nature]
    if boost == "speed":
      self.speed = self.speed + NATURE_CONST
    elif boost == "atk":
      self.atk = self.atk + NATURE_CONST
    
    if decrease == "sp_atk":
      self.sp_atk = self.sp_atk - NATURE_CONST
    elif decrease == "atk":
      self.atk = self.atk - NATURE_CONST

    self.atk += 1
    self.defense += 1
    self.sp_def += 1
    self.sp_atk += 1
    self.speed += 1
    self.health += 1
  
  def __repr__(self):
    return f"Health: {int(self.health)}\nAttack: {int(self.atk)}\nDefense: {int(self.defense)}\nSp Attack: {int(self.sp_atk)}\nSp Defense: {int(self.sp_def)}\nSpeed: {int(self.speed)}\nNature: {self.nature}"

class Pokemon:
  def __init__(self, stats, elem_type, lvl, exp, next_lvl, poke_name, move_list, ours):
    self.elem_type = elem_type
    self.lvl = lvl
    self.exp = exp
    self.next_lvl = next_lvl
    self.poke_name = poke_namegam
    self.moves = move_list
    self.stats = stats
    self.alive = True
    self.ours = ours

  def add_exp(self, gained_exp):
    total_exp = gained_exp + self.exp
    if total_exp >= self.next_lvl:
      self.lvl = self.lvl + 1
      self.exp = total_exp - self.next_lvl
      self.next_lvl = math.ceil(self.next_lvl * LEVEL_UP_CONST)
      self.stats.raise_stats()
    else:
      self.exp = total_exp

  def __repr__(self):
    return f"Name: {self.poke_name}\nLevel: {str(self.lvl)}\nExp: {self.exp}\nRequired Exp to next level: {str(self.next_lvl)}\nStats:\n{str(self.stats)}"

  def attack_damage_map(self, enemy_type, ls):
    tmp = {}
    for move in ls:
      if move is not None:
        move_type, hit_points, _, _ = MOVES[move]ss
        super_effective, not_very_effective, no_effect = EFFECTIVENESS[move_type]
        stab = 1.5 if self.elem_type == move_type else 1

        if enemy_type in super_effective:
          tmp[move] = hit_points * 2 * stab
        elif enemy_type in not_very_effective:
          tmp[move] = hit_points * 0.5 * stab
        elif enemy_type in no_effect:
          tmp[move] = 0
        else:
          tmp[move] = hit_points * stab
    return tmp

  def determine_move(self, move_dict):
    max_dmg = (None, 0)
    for move, damage in move_dict.items():
      if damage > max_dmg[1]:
        max_dmg = (move, damage)

    return max_dmg
    
  def attack(self, poke, move, hitpoints):
    print(self.poke_name + " used " + move + "!")
    e_type, dmg, acc, ph_spec = MOVES[move]
    if random.random() > acc:
      print("But it missed!")
      return False
    my_atk, their_def = (self.stats.sp_atk, poke.stats.sp_def) if ph_spec == "special" else (self.stats.atk, poke.stats.defense)
    total_attack = (my_atk * hitpoints) - their_def
    total_attack = 1 if total_attack <= 0 else total_attack
    poke.stats.health = poke.stats.health - total_attack
    print("Enemy " + poke.poke_name + " took " + str(total_attack) + " damage!")
    if poke.stats.health < 0:
      poke.stats.health = 0
      poke.alive = False

  @staticmethod
  def who_faster(poke1, poke2):
    if poke1.stats.speed > poke2.stats.speed:
      return (poke1, poke2)
    elif poke1.stats.speed == poke2.stats.speed:
      if random.randint(0, 1):
        return (poke1, poke2)
      else:
        return (poke2, poke1)
    else:
      return (poke2, poke1)

  @staticmethod
  def turn(our_pokemon, enemy_pokemon, our_move):
    enemy_poke_move_map = enemy_pokemon.attack_damage_map(our_pokemon.elem_type, enemy_pokemon.moves)
    enemy_move, enemy_hitpoints = enemy_pokemon.determine_move(enemy_poke_move_map)

    our_move_map = our_pokemon.attack_damage_map(enemy_pokemon.elem_type, [our_move])

    poke_first, poke_second = Pokemon.who_faster(our_pokemon, enemy_pokemon)

    print(poke_first.poke_name + " attacks!")
    
    if poke_first.ours:
      poke_first.attack(poke_second, our_move, our_move_map[our_move])
    else:
      poke_first.attack(poke_second, enemy_move, enemy_hitpoints)

    if poke_second.alive:
      if poke_second.ours:
        poke_second.attack(poke_first, our_move, our_move_map[our_move])
      else:
        poke_second.attack(poke_first, enemy_move, enemy_hitpoints)

    if not poke_second.alive:
      print(poke_second.poke_name + " fainted!")
    if not poke_first.alive:
      print(poke_first.poke_name + " fainted!")

def format_move(move):
  ty, damage, acc, ph_spec = MOVES[move]
  return f"{move.capitalize()}\nType: {ty.capitalize()}\tAttack power: {str(int(damage * 100))}\tAccuracy: {str(int(100 * acc))}%\tPhysical/Special: {ph_spec}"

pika = Pokemon(Stats(10, 6, 8, 13, 18, 30, "timid"), "thunder", 5, 300, 700, "pikachu", ["thunder", "tackle", None, None], True)
squirtle = Pokemon(Stats(8, 6, 1, 13, 15, 10, "adamant"), "water", 3, 300, 500, "squirtle", ["tackle", None, None, None], False)

print("Enemey trainer approaches!")
print("Go! " + squirtle.poke_name)
print("Go! " + pika.poke_name + " I know you can do it!")
while pika.alive and squirtle.alive:
  prompt = "\n".join(["\n" + format_move(move) for move in pika.moves if move is not None])
  move_selection = input("Which move do you wanna use?\n" + prompt + "\n")
  Pokemon.turn(pika, squirtle, move_selection)