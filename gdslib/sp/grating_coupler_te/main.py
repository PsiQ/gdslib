

import pathlib
import json
import lumapi


dirpath = pathlib.Path(__file__).parent.absolute()

s = lumapi.FDTD()
s.cd(str(dirpath))
s.eval("main;")

d = {k: list(abs(s.getv(k).flatten())) for k in ["S11", "S12", "S21", "S22", "f"]}

with open(dirpath / "GC_sparameters.json", "w") as f:
    f.write(json.dumps(d))

    