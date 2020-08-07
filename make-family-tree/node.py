#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
data -> member object
mother -> pointer to member object
father -> pointer to member object
spouse -> pointer to member object
children -> list of pointers to member objects
"""

print("[node.py]")

class Node:
    def __init__(self, data):  # , mother=None, father=None, spouse=None):
        self.data = data
        self.mother = None
        self.father = None
        self.spouse = None
        self.children = []

    def get_full_name(self):
        return self.data.first_name + " " + self.data.last_name

    def add_father(self, father):
        self.father = father

    def add_mother(self, mother):
        self.mother = mother

    def add_spouse(self, spouse):
        self.spouse = spouse

    # pointer to child
    def add_children(self, child):
        self.children.append(child)
