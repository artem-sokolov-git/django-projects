from pathlib import Path


class Project:
    def __init__(self, name: str, path: Path):
        self.name = name
        self.path = path

    def create_directory(self):
        if self.path.exists():
            raise FileExistsError(f"{self.name} уже существует!")
        self.path.mkdir(parents=True)