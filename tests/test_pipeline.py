import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src import main as etl


class PipelineTests(unittest.TestCase):
    def test_extracts_all_sample_users(self):
        users = etl.extract_users()

        self.assertEqual(len(users), 5)
        self.assertTrue(all(column in users[0] for column in etl.REQUIRED_COLUMNS))

    def test_rejects_input_without_required_columns(self):
        with tempfile.TemporaryDirectory() as directory:
            invalid_csv = Path(directory) / "clientes.csv"
            invalid_csv.write_text("id,nome\n1,Geovanna\n", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "Colunas obrigatórias ausentes"):
                etl.extract_users(invalid_csv)

    def test_local_messages_respect_character_limit(self):
        with patch.dict(os.environ, {}, clear=True):
            users = etl.extract_users()
            transformed = etl.transform_users(users)

        self.assertTrue(all(len(user["news_description"]) <= 100 for user in transformed))

    def test_load_creates_csv_and_json(self):
        users = [{"id": 1, "nome": "Teste", "news_description": "Mensagem"}]

        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            with (
                patch.object(etl, "OUTPUT_DIR", output_dir),
                patch.object(etl, "OUTPUT_CSV", output_dir / "resultado.csv"),
                patch.object(etl, "OUTPUT_JSON", output_dir / "resultado.json"),
            ):
                etl.load_users(users)

                self.assertTrue(etl.OUTPUT_CSV.exists())
                self.assertTrue(etl.OUTPUT_JSON.exists())


if __name__ == "__main__":
    unittest.main()
