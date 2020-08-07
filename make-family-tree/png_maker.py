#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tree import Tree
from os import system

tree = Tree()
nodes = tree.nodes
roots = []
string = []

system("./make_JSON.py")

def traverse(curr, currIndex):
    string[currIndex] += "\n"+curr.data.name + " (" + curr.data.s + ", id=" + str(curr.data.key) + ")\n"
    if curr.spouse is not None:
        string[currIndex] += curr.spouse.data.name + " (" + curr.spouse.data.s + ", id=" + str(curr.spouse.data.key) + ")\n"

    if len(curr.children) > 0:
        for child in curr.children:
            string[currIndex] += "\t" + child.data.name + " (" + child.data.s + ", id=" + str(child.data.key) + ")\n"

    if len(curr.children) > 0:
        for child in curr.children:
            if child.spouse is not None:
                traverse(child, currIndex)
    string[currIndex] += "\n"


for node in nodes:
    if node.father is None:
        if node.mother is None:
            if node.spouse.mother is None or node.spouse.father is None:
                roots.append(node)

for root in roots:
    if root.spouse in roots:
        index = roots.index(root.spouse)
        roots.pop(index)

for i, root in enumerate(roots):
    string.append("")
    traverse(root, i)
# print(len(roots))
# print(len(string))

for i in range(len(roots)):
    s = string[i]
    root = roots[i]
    first_name = root.data.name.split(" ")[0]
    filename = first_name + ".txt"
    f = open(filename, "w")
    f.write(s)
    f.close()

for root in roots:
    first_name = root.data.name.split(" ")[0]
    # ./familytreemaker.py -a 'Louis XIV' LouisXIVfamily.txt | dot -Tpng -o LouisXIVfamily.png
    command = """./familytreemaker.py -a '""" + root.data.name + """' """ + first_name + """.txt | dot -Tpng -o """ + first_name + """.png"""
    # print(command)
    system(command)
