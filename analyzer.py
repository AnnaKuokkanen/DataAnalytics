import pandas as pd

def analyze(filename):
    print('analyzing....')
    df = pd.read_csv(filename)
    print(df)

def plot():
    print("Hello world")