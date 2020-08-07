#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from member import Memba
from node import Node
import json

importedFile = json.load(open("test.json"))
nodes = []
names = []

print("[tree.py]")

class Tree:
    def __init__(self):
        self.nodes = make_tree()

    def searchName(self, name):
        results = []
        # print("Looking for: "+name)
        for i, mem in enumerate(names):
            found = name.lower() in mem
            # print(found)
            if found:
                results.append(self.nodes[i])
        return results

    def findRelativeOf(self, name, relation):
        found = self.searchName(name)[0]
        # print("Finding relative of:", found.data.name)
        if found is not None:
            # print(name + " found")
            relative = None
            if relation == 'father' and found.father is not None:
                relative = found.father
            if relation == 'mother':
                if found.mother is not None:
                    relative = found.mother
            if relation == 'mother':
                if found.mother is not None:
                    relative = found.mother
            if relative is not None:
                return relative

    def getChildren(self, name):
        found = self.searchName(name)[0]
        if found is not None:
            return found.children

    @staticmethod
    def displayInfo(nodesArr):
        # print(nodesArr)
        if nodesArr is not None:
            arrEl = nodesArr
            for n in arrEl:
                if n is not None:
                    mem = n.data
                    print("=" * 50)

                    print("Name".ljust(15), ":", mem.name)
                    print()

                    if mem.father_name is not None:
                        print("Father".ljust(15), ":", mem.father_name)
                        print()
                    if mem.mother_name is not None:
                        print("Mother".ljust(15), ":", mem.mother_name)
                        print()

                    print("Spouse Name".ljust(15), ":", mem.spouse_name)
                    print()

                    print("=" * 50)
                    print("\n")
        else:
            print("Person requested not found")
        input("Press any key to continue...")
        return


def make_tree():
    # add nodes to tree, saved in nodes list

    def make_member(m):
        currMem = Memba(m["key"], m["name"], m["father_name"], m["mother_name"], m["spouse_name"], m["s"])
        return currMem

    for curr_json in importedFile:
        mem = make_member(curr_json)
        new_node = Node(mem)
        nodes.append(new_node)
        names.append(mem.name.lower())
    # print(len(nodes))

    # print(names)

    # add father
    for mem in nodes:
        parent_name = mem.data.father_name.lower()
        if parent_name in names:
            index = names.index(parent_name)
            parent = nodes[index]
            mem.add_father(parent)
            parent.add_children(mem)

    for mem in nodes:
        parent_name = mem.data.mother_name.lower()
        if parent_name in names:
            index = names.index(parent_name)
            parent = nodes[index]
            mem.add_mother(parent)
            parent.add_children(mem)

    for mem in nodes:
        spouse_name = mem.data.spouse_name.lower()
        if spouse_name in names:
            index = names.index(spouse_name)
            nodes[index].add_spouse(mem)
            mem.add_spouse(nodes[index])

    return nodes
