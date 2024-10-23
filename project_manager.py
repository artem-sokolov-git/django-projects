import subprocess
from pathlib import Path


class Project:
    def __init__(self, name: str, path: Path):
        self.name = name
        self.path = path
        self.venv = self.path / ".venv"

    def create_directory(self):
        if self.path.exists():
            raise FileExistsError(f"{self.name} уже существует!")
        # ? Опционально: Создать проверку на корректное имя
        self.path.mkdir(parents=True)

    def create_virtualenv(self):
        if self.venv.exists():
            raise FileExistsError("Виртуальное окружение уже создано!")
        try:
            subprocess.run(["python", "-m", "venv", self.venv], check=True)
        except subprocess.CalledProcessError as e:
            return print(e)

    def update_pip(self):
        if not self.venv.exists():
            raise FileNotFoundError("Виртуальное окружение на найдено!")
        try:
            subprocess.run([self.venv / "bin" / "pip", "install", "--upgrade", "pip"])
        except subprocess.CalledProcessError as e:
            return print(e)
