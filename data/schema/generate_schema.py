import json
from data.schema.schema import schema
import sys
from graphql.utils import schema_printer


def generate_schema():
    my_schema_str = schema_printer.print_schema(schema)
    fp = open("../ag-control/src/data/schema.graphql", "w")
    fp.write(my_schema_str)
    fp.close()
