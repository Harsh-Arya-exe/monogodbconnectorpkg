import os 
from pathlib import Path

package_name = "mongodb_connect"

list_of_files = [
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "testing/__init__.py",
    "testing/unit/__init__.py",
    "testing/unit/test_unit.py",
    "tests/integration/__init__.py",
    "tests/integration/test_int.py",
    "experiment/experiments.ipynb",
    "requirements.txt",
    "requirements_dev.txt",
    "init_setup.sh",
    "pyproject.toml",
    "setup.py",
    "setup.cfg",
    "tox.ini"
]


for file_path in list_of_files:
    file_path = Path(file_path)
    dir_name, file_name = os.path.split(file_path)
    if dir_name != "":
        os.makedirs(dir_name, exist_ok=True)
    
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, 'w') as f:
            pass