import sys, json
import pandas as pd


df = pd.read_json (sys.argv[1])
df.to_csv ('output.csv', index = None)
