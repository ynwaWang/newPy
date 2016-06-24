#!/usr/bin/python
# encoding:utf-8

import json
from collections import defaultdict


def get_counts(sequence):
    results = defaultdict(int)
    for x in sequence:
        results[x] += 1
    return results


def top_count(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

path = 'usagov_bitly_data2011-12-31-1325367027'
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
counts = get_counts(time_zones)
top_count(counts)



