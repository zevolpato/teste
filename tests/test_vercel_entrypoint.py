import importlib
import sys
import unittest
from pathlib import Path


class VercelEntrypointTests(unittest.TestCase):
    def test_database_url_without_pgbouncer_param(self):
        project_root = Path(__file__).resolve().parents[1]
        if str(project_root) not in sys.path:
            sys.path.insert(0, str(project_root))

        import mysite.settings as settings

        sanitized = settings.normalize_database_url(
            "postgres://user:pass@host:5432/db?pgbouncer=true&sslmode=require"
        )

        self.assertIn("sslmode=require", sanitized)
        self.assertNotIn("pgbouncer", sanitized)
    def test_api_index_imports(self):
        project_root = Path(__file__).resolve().parents[1]
        if str(project_root) not in sys.path:
            sys.path.insert(0, str(project_root))

        module = importlib.import_module("api.index")
        self.assertTrue(callable(getattr(module, "handler", None)))


if __name__ == "__main__":
    unittest.main()
