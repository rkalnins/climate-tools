import json

from log import log
from node import Node


class Record:
    record_path: str
    root_nodes: list

    def __init__(
        self, load_path=None, index_path=None, record_name="netcdf_record.json", node_name="n"
    ):
        if load_path and index_path:
            log("invalid options: load_path and index_path provided")
            return

        if load_path:
            self.load(load_path)

        if index_path:
            self.create(index_path, node_name)

    def load(self, path):
        with open(load_path, "r") as record:
            raw = json.load(record)

    def dump(self, path):
        dump_contents = dict()
        dump_contents["nodes"] = [n.to_json() for n in self.nodes]

        with open(path, "w+") as f:
            json.dump(dump_contents, f)


