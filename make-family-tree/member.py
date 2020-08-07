#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("[member.py]")

class Memba:
    def __init__(self, key, name, father_name, mother_name, spouse_name, s):
        self.key = key
        self.name = name
        self.father_name = father_name
        self.mother_name = mother_name
        self.spouse_name = spouse_name
        self.s = s

    def displayInfo(self):
        print(self.key)
        print(self.name)
        print(self.father_name)
        print(self.mother_name)
        print(self.spouse_name)