#!/usr/bin/env python

import json

data = open("../data/cats.json")

cats = json.load(data)

print(cats)