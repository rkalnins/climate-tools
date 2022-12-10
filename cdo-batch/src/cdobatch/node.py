from __future__ import annotations
import os


class Node:
    parent: Node
    children: list
    name: str
    path: str
    files: list

    def __init__(self, name, path, files=None):
        self.name = name
        self.path = path
        self.children = list()

        if files is None:
            self.files = list()
        else:
            self.files = files

    def get_root_path(self):

        # this is the root node
        if self.parent is None:
            return ""

        return os.path.join(self.parent.get_root_path(), self.path)

    def add_child(self, node):
        node.parent = self
        children.append(node)

    @classmethod
    def from_dict(d):
        return cls(d["name"], d["path"], d["files"])

    def to_dict():
        return {"name": self.name, "path": self.path, "files": self.files}
