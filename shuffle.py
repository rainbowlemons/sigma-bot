#!/usr/bin/python
import random

lines = open("words_alpha.txt").readlines()
random.shuffle(lines)
open("words_shuffled.txt", "w").writelines(lines)
