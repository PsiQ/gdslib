import pathlib
import json
import pandas as pd


def json_to_csv(dirpathin, dirpathout=None):
    """ takes a path and converts all the JSON files into CSV """
    dirpathin = pathlib.Path(dirpathin)
    dirpathout = dirpathout or dirpathin / "csv"
    dirpathout = pathlib.Path(dirpathout)

    for f in dirpathin.glob("*.json"):
        filename = f.stem
        r = json.loads(open(f).read())
        df = pd.DataFrame(r)
        df.to_csv(dirpathout / f"{filename}.csv")


if __name__ == "__main__":
    json_to_csv("/home/jmatres/dash/data/")
