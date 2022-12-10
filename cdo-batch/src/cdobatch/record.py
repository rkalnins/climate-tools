from __future__ import annotations
import json
import os
import cdo


from log import log
from node import Node


class Record:
    path: str
    index_name: str
    root_nodes: list

    def __init__(self, index_path=None, index_name="dataset.json"):
        if load_path and index_path:
            log("invalid options: load_path and index_path provided")
            return

        self.path = path
        self.index_name = index_name
        self.root_nodes = list()

    def __enter__(self):
        # attempt to open index, if given directory, index it
        if os.path.isfile(self.path):
            self.load()
        else:
            self.index()
            index_name += self.index_name

    def __exit__(self, *args):
        self.dump()

    def get_node(self, name):
        for n in self.root_nodes:
            if n.name == name:
                return n

    def add_node(self, node):
        self.root_nodes.append(node)

    def index(self):
        all_paths = []

        # get all files
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(".nc"):
                    all_paths.append(os.path.join(root, file))

        # create root node with all files
        self.root_nodes.append(Node("root", self.index_path, files=all_paths))

    def load(self):
        with open(self.load_path, "r") as record:
            raw = json.load(record)

            for n_raw in raw["nodes"]:
                root_nodes.append(Node.from_dict(n_raw))

    def dump(self):
        dump_contents = dict()
        dump_contents["nodes"] = [n.to_dict() for n in self.nodes]

        with open(self.path, "w+") as f:
            json.dump(dump_contents, f)
