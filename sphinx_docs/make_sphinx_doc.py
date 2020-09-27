"""
make_sphinx_doc.py

USAGE ::

     python make_sphinx_doc.py
"""
# import os
# import sys
import pathlib
import subprocess


# constants
LOCATION_PYDOCUMENTS = str(
    pathlib.Path(__file__).resolve().parent.parent /
    "_target_projects" / "fastapi_nginx_template" / "app"
)
LOCATION_SOURCE = str(
    pathlib.Path(__file__).resolve().parent / "source"
)
LOCATION_BUILD = str(
    pathlib.Path(__file__).resolve().parent / "build"
)


if __name__ == "__main__":
    # import subprocess
    cmd_api = f"sphinx-apidoc -f -o {LOCATION_SOURCE} {LOCATION_PYDOCUMENTS}"
    print(cmd_api)

    cmd_doc = f"sphinx-build -b html {LOCATION_SOURCE} {LOCATION_BUILD}"
    print(cmd_doc)

    for cmd in [cmd_api, cmd_doc]:
        result = subprocess.run(cmd, check=True, shell=True)
        print(result)
