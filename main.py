# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
score_goal_first = 'Ruud Gullit '
score_goal_second = 'Marco van Basten '
goal_0 = 32
goal_1 = 54

scorers = score_goal_first + str(goal_0) + ', ' + score_goal_second + str(goal_1)

report = f'{score_goal_first}scored in the {str(goal_0)}nd minute\n{score_goal_second}scored in the {str(goal_1)}th minute'

print(report)

#Part 2

player = ("Jan Wouters")

first_name = player.split()[0]
print(first_name)

last_name_len = len(player.split()[-1])
print(last_name_len)

name_short = f'{player[:1]}. {player.split()[-1]}' 
print(name_short)

chant = (len(first_name) * f'{first_name}! ').rstrip() 
print(chant)

good_chant = (" " != chant)
print(good_chant)