import subprocess
from pathlib import Path


class Project:
    def __init__(self, name: str, path: Path):
        self.name = name
        self.path = path
        self.venv = self.path / ".venv"

    def create_directory(self):
        """Создает директорию с именем проекта"""
        if self.path.exists():
            raise FileExistsError(f"{self.name} уже существует!")

        # ? Опционально: Создать проверку на корректное имя
        self.path.mkdir(parents=True)

    def create_virtualenv(self):
        """Создает в папке проекта виртуальное окружение"""
        if self.venv.exists():
            raise FileExistsError("Виртуальное окружение уже создано!")

        try:
            subprocess.run(["python", "-m", "venv", self.venv], check=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Ошибка при создании виртуального окружения: {e}")

    def update_pip(self):
        """Запускает команду обновления pip"""
        if not self.venv.exists():
            raise FileNotFoundError("Виртуальное окружение на найдено!")

        try:
            subprocess.run(
                [self.venv / "bin" / "pip", "install", "--upgrade", "pip"], check=True
            )
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Ошибка при обновлении pip: {e}")