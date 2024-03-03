import argparse
import csv

from typing import List
from collections import OrderedDict

def visualize_graph(graph: List[List[int]], row_mappings: OrderedDict):
    row_labels = list(row_mappings.keys())
    for i, row in enumerate(graph):
        print(f'{row} - {row_labels[i]}')


def build_graph(dir: str, row_mappings: OrderedDict,
                          col_mappings: OrderedDict) -> List[List[int]]:
    row_size = len(row_mappings.keys())
    col_size = len(col_mappings.keys())
    graph: List[List[int]] = [[0 for col in range(0, col_size)] for row in range(0, row_size)]
    with open(f'{dir}/stars.csv', 'r') as mapping:
        reader = csv.DictReader(mapping)
        for record in reader:
            # These two "index" calls are O(n) operations
            row = row_mappings.get(record['person_id'])
            col = col_mappings.get(record['movie_id'])
            if row is None or col is None:
                raise ValueError(f'Row or Col not found for {record}')
            graph[row][col] = 1
    print("Finished Building Graph")

    return graph


def build_dimensions(dir: str) -> (OrderedDict, OrderedDict):
    # this will open the people.csv and movies.csv
    # file and just read the id columns of both and set
    # our rows and cols
    # This is basically the translation of
    # the array IDX to the actual ids.

    # Person_id -> graph_idx
    row_mappings = OrderedDict()
    # Movie_id -> graph_idx
    col_mappings = OrderedDict()


    with open(f'{dir}/movies.csv', 'r') as movies_csv:
        reader = csv.DictReader(movies_csv)
        idx = 0
        for row in reader:
            col_mappings[row['id']] = idx
            idx += 1
    with open(f'{dir}/people.csv', 'r') as people_csv:
        reader = csv.DictReader(people_csv)
        idx = 0
        for row in reader:
            row_mappings[row['id']] = idx
            idx += 1
    print(f"Finished Building Dimensions: {len(col_mappings)}, {len(row_mappings)}")
    return (row_mappings, col_mappings)


def main():
    arg_parser = argparse.ArgumentParser(description='Visualize the graph')
    arg_parser.add_argument('dir', type=str, help='path to the people and movie directory')

    args = arg_parser.parse_args()
    (row_mappings, col_mappings) = build_dimensions(args.dir)
    graph = build_graph(args.dir, row_mappings, col_mappings)
    visualize_graph(graph, row_mappings)


if __name__ == "__main__":
    main()
