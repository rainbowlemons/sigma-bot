import random

lines = open("words_shuffled.txt").readlines()
random.shuffle(lines)
open("words_shuffled.txt", "w").writelines(lines)
