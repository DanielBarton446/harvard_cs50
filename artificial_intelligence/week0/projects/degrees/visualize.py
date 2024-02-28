import argparse
import csv

from typing import List

# Person
row_keys = []
# Movie
col_keys = []


def visualize_graph(graph: List[List[int]]):
    for i, row in enumerate(graph):
        print(f'{row} - {row_keys[i]}')


def build_graph(dir: str) -> List[List[int]]:
    graph: List[List[int]] = [[0 for col in col_keys] for row in row_keys]
    with open(f'{dir}/stars.csv', 'r') as mapping:
        reader = csv.DictReader(mapping)
        for record in reader:
            row = row_keys.index(record['person_id'])
            col = col_keys.index(record['movie_id'])
            graph[row][col] = 1

    return graph


def set_keys(dir: str):
    # this will open the people.csv and movies.csv
    # file and just read the id columns of both and set
    # our rows and cols
    # This is basically the translation of
    # the array IDX to the actual ids.
    with open(f'{dir}/movies.csv', 'r') as movies_csv:
        reader = csv.DictReader(movies_csv)
        for row in reader:
            col_keys.append(row['id'])
    with open(f'{dir}/people.csv', 'r') as people_csv:
        reader = csv.DictReader(people_csv)
        for row in reader:
            row_keys.append(row['id'])


def main():
    arg_parser = argparse.ArgumentParser(description='Visualize the graph')
    arg_parser.add_argument('dir', type=str, help='path to the people and movie directory')

    args = arg_parser.parse_args()
    set_keys(args.dir)
    graph = build_graph(args.dir)
    visualize_graph(graph)


if __name__ == "__main__":
    main()
