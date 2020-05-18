import pathlib

cwd = pathlib.Path(__file__).parent.absolute()

# print(list(cwd.glob('*/*.dat')))
# print(list(cwd.glob('*/*.json')))

for p in cwd.glob("*/*.json"):
    p.rename(p.parent / (p.stem + "_220.json"))


for p in cwd.glob("*/*.dat"):
    p.rename(p.parent / (p.stem + "_220.dat"))
