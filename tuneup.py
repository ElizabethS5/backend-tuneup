#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "ElizabethS5 ... with some assistance from Peter Marsh"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        val = func(*args, **kwargs)
        pr.disable()
        ps = pstats.Stats(pr).strip_dirs().sort_stats('cumtime')
        ps.print_stats(10)
        return val
    return wrapper


def read_movies(src):
    """Returns a list of movie titles"""
    # print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


# @profile
# def find_duplicate_movies(src):
#     """Returns a list of duplicate movies from a src list"""
#     movies = read_movies(src)
#     duplicates = []
#     while movies:
#         movie = movies.pop()
#         if is_duplicate(movie, movies):
#             duplicates.append(movie)
#     return duplicates

# @profile
def find_duplicate_movies_improved(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    movie_set = set()
    for movie in movies:
        length = len(movie_set)
        movie_set.add(movie)
        if length == len(movie_set):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(stmt="find_duplicate_movies_improved('movies.txt')",
                     setup="from __main__ import \
                         find_duplicate_movies_improved")
    num_repeats = 7
    num_runs = 5
    results = t.repeat(repeat=num_repeats, number=num_runs)
    print(
        f'Best time across {num_repeats} '
        + f'repeats of {num_runs} runs per repeat: '
        + f'{min(results) / float(num_runs)} sec'
    )


@profile
def main():
    """Computes a list of duplicate movie entries"""
    # result = find_duplicate_movies('movies.txt')
    result = find_duplicate_movies_improved('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
    timeit_helper()
