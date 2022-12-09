# CDO batching tool

A tool for creating, manipulating, and reading NetCDF files with CDO.

Users can create, split, copy, groups (nodes) of files on which to apply
CDO operators. 

## Example Usage

Apply an operator with variable parameters to a collection of nodes.

```python
from cdobatch.record import Record
from cdobatch.node import Node
from cdobatch.op import Command, BatchOperator

r = Record(index_path="CMIP6_data/tas/MODELS_filtered/ssp585", node_name="root")

# split tree recursively twice using filesystem paths
input_nodes = r.fs_split(2)


commands = list()
output_node = Node("outputs", "iceshelves")


for shelf in shelves:

op = BatchOperator(commands)

for n in input_nodes:
    for shelf in shelves:
        path_parts = n.get_path_from_root()[-1:]

        path = f"iceshelves/{shelf["name"]}/{path_parts[1]}/{path_parts[0]}"
        name = f"{shelf["name"]}_{path_parts[1]}_{path_parts[0]}"

        output_node = Node(name, path)
        output_node.add_child(output_node)

        # each command maps to an output node
        c = Command("sellatlonbox",
                    shelf["coords"],
                    output=output_node,
                    opvar={"shelf": shelf["name"]}
            )

        commands.append(c)


# apply operator to all leaf nodes with files
for n in nodes:
    n.apply(op)

```


