import unittest

import lesson_check
import util


class TestFileList(unittest.TestCase):
    def setUp(self):
        self.reporter = util.Reporter(None)

    def test_file_list_has_expected_entries(self):
        # For first pass, simply assume that all required files are present
        all_filenames = [item[1].replace('%', '')
                         for item in lesson_check.REQUIRED_FILES]

        lesson_check.check_fileset('', self.reporter, all_filenames)
        self.assertEqual(len(self.reporter.messages), 0)


if __name__ == "__main__":
    unittest.main()
