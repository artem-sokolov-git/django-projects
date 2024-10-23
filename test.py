import unittest
from pathlib import Path

from project_manager import Project


class TestProjectManager(unittest.TestCase):
    def setUp(self):
        self.test_name = "test_project"
        self.test_path = Path("./test_project")
        self.test_project = Project(self.test_name, self.test_path)
    