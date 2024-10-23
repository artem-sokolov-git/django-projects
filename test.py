import shutil
import subprocess
import unittest
import unittest.mock
from pathlib import Path

from project_manager import Project


class TestProjectManager(unittest.TestCase):
    def setUp(self):
        self.test_name = "test_project"
        self.test_path = Path("./test_project")
        self.test_project = Project(self.test_name, self.test_path)

    def tearDown(self):
        if self.test_project.path.exists():
            shutil.rmtree(self.test_project.path)

    def test_create_directory_success(self):
        """Тест на успешное создание папки"""
        self.test_project.create_directory()
        self.assertTrue(self.test_project.path.exists())

    # ? Опционально: Создать проверку на корректное имя

    def test_create_directory_already_exists(self):
        """Тест на выброс исключения, если папка уже существует"""
        self.test_project.create_directory()
        with self.assertRaises(FileExistsError):
            self.test_project.create_directory()

    def test_create_virtualenv_success(self):
        self.test_project.create_directory()
        self.test_project.create_virtualenv()
        self.assertTrue(self.test_project.venv.exists())

    def test_create_virtualenv_already_exists(self):
        """Тест на выброс исключения, если .venv уже существует"""
        self.test_project.create_virtualenv()
        with self.assertRaises(FileExistsError):
            self.test_project.create_virtualenv()

    def test_create_virtualenv_failure(self):
        self.test_project.create_directory()
        with unittest.mock.patch(
            "subprocess.run", side_effect=subprocess.CalledProcessError(1, "venv")
        ):
            with self.assertRaises(RuntimeError):
                self.test_project.create_virtualenv()

    def test_update_pip_success(self):
        self.test_project.create_directory()
        self.test_project.create_virtualenv()
        self.test_project.update_pip()

    def test_update_pip_no_virtualenv(self):
        with self.assertRaises(FileNotFoundError):
            self.test_project.update_pip()

    def test_update_pip_failure(self):
        self.test_project.create_directory()
        self.test_project.create_virtualenv()
        with unittest.mock.patch(
            "subprocess.run", side_effect=subprocess.CalledProcessError(1, "pip")
        ):
            with self.assertRaises(RuntimeError):
                self.test_project.update_pip()


if __name__ == "__main__":
    unittest.main()
