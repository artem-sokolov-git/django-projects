import shutil
import unittest
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
        self.test_project.create_directory()
        self.assertTrue(self.test_project.path.exists())


if __name__ == "__main__":
    unittest.main()
