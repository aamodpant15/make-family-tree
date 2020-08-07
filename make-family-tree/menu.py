#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from tree import Tree

# MENU
os.system("clear")
print("="*50)
print("FAMILY LOOKUP".center(50))
print("="*50)
# print('\n')

# =================================================================================

tree = Tree()
while True:
    print("""
1. Find by name
2. Find father of 
3. Find mother of 
4. Find children of 
5. Exit
""")

    menu_input = input("Choose 1/2/3/4/5\n")

    output = []

    if menu_input == str(1):
        # Fresh output
        output = []
        name_to_search = input("Enter name to find\n")
        output.extend(tree.searchName(name_to_search))
        tree.displayInfo(output)

    elif menu_input == str(2):
        name_to_search = input("Enter name to find father\n")
        output.append(tree.findRelativeOf(name_to_search, "father"))
        tree.displayInfo(output)

    elif menu_input == str(3):
        name_to_search = input("Enter name to find mother\n")
        output.append(tree.findRelativeOf(name_to_search, "mother"))
        tree.displayInfo(output)

    elif menu_input == str(4):
        name_to_search = input("Enter name to find children\n")
        output.extend(tree.getChildren(name_to_search))
        tree.displayInfo(output)

    elif menu_input == str(5):
        break

    else:
        print("Choose a valid option")

    os.system("clear")
