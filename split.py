#!/usr/bin/env python3
"""Splits tagged data into training, development, and test sets."""

import argparse
from typing import Iterator, List
import random

#reads data one sentence at a time
def read_tags(path: str) -> Iterator[List[List[str]]]:
    with open(path, "r") as source:
        lines = []
        for line in source:
            line = line.rstrip()
            if line:  # Line is contentful.
                lines.append(line.split())
            else:  # Line is blank.
                yield lines.copy()
                lines.clear()
    # Just in case someone forgets to put a blank line at the end...
    if lines:
        yield lines    
        
#splits and randomizes data
def main(args: argparse.Namespace) -> None:
    corpus = list(read_tags(args.input))
    random.seed(args.seed)
    random.shuffle(corpus)
    args.train = corpus[:8758]
    args.dev = corpus[8758:9854]
    args.test = corpus[9854:]
    
    #writes dev, train, and test sets to files
    def write_tags(sliced_arg, file_name):
        for sentence in sliced_arg:
            print(sentence)
            for word in sentence:
                print(' '.join(word), file=open(file_name, "a"))
        return
    write_tags(args.train, "train.tag")
    write_tags(args.dev, "dev.tag")
    write_tags(args.test, "test.tag")
        

if __name__ == "__main__":
    #declare arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", help="seed for randomizer", required=True)
    parser.add_argument("input", help="input connll2000 file")
    parser.add_argument("train", help="80% training set data")
    parser.add_argument("dev", help="10% development set")
    parser.add_argument("test", help="10% test set")
    #parse arguments and pass them to `main`
    main(parser.parse_args())
    
    ...
