import os
from pathlib import Path

class Project:
    def __init__(self, name: str, path: Path):
        self.name = name
        self.path = path