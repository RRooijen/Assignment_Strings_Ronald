# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
score_goal_first = 'Ruud Gullit'
score_goal_second = 'Marco van Basten'
goal_0 = str(32)
goal_1 = str(54)

scorers = score_goal_first + goal_0, score_goal_second + goal_1

print(scorers)

report = f'{score_goal_first} scored in the {goal_0}nd minute. \n{score_goal_second} scored in the {goal_1}th minute.'

print(report)

#Part 2

player = ("Jan Wouters")

first_name = (player[0:3]); print(player.find("Jan"))

last_name_len = (player.find("Wouters")); (player[4:]); print(len(player[4:]))

name_short = f'{player[:1]}. {player[4:]}'; print(name_short)

chant = f'{first_name}! ' * 3; print(chant.strip(" "))

good_chant = print(" " != chant)