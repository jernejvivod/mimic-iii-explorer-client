import glob
import unittest

from mimic_iii_explorer_client.data_saving import save
from mimic_iii_explorer_client.mimic_iii_explorer_client.model.clinical_text_result import ClinicalTextResultDto
from mimic_iii_explorer_client.mimic_iii_explorer_client.model.target_extraction_result import ExtractedTargetDto

import os


class TestSave(unittest.TestCase):
    """Unit tests for data saving"""

    def test_save_empty(self):
        save.save_clinical_text(
            [],
            [],
            "fast-text",
            ".",
            None
        )

        files = glob.glob("data*.txt")
        self.assertEqual(len(files), 1)
        saved_file_path = files[0]
        with open(saved_file_path, 'r') as f:
            self.assertEqual(len(f.readlines()), 0)

        os.remove(saved_file_path)

    def test_save_simple(self):
        clinical_text_result_dto = ClinicalTextResultDto(1, 'this is a test')
        extracted_target_dto = ExtractedTargetDto(1, 0)

        save.save_clinical_text(
            [clinical_text_result_dto],
            [extracted_target_dto],
            "fast-text",
            ".",
            None
        )

        files = glob.glob("data*.txt")
        self.assertEqual(len(files), 1)
        saved_file_path = files[0]
        with open(saved_file_path, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 1)
            self.assertEqual('test __label__0\n', lines[0])

        os.remove(saved_file_path)
