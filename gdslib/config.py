"""
stores configuration variables

"""

__all__ = ["CONFIG"]

import pathlib


module_path = pathlib.Path(__file__).parent.absolute()
repo_path = module_path.parent


class Config:
    module = module_path
    repo = repo_path
    sp = repo_path / "sp"


CONFIG = Config()

if __name__ == "__main__":
    print(CONFIG.sp)
