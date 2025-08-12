"""
Test module keygen
"""

import sys
import os
import unittest

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from ssh_manager.keygen import KeyGen

TEST_PATH = "id_rsa_test"


class TestSshKeyGeneration(unittest.TestCase):

    def test_verify_files_exist(self):
        self.generate_test_files()
        self.assertTrue(os.path.exists(TEST_PATH))
        self.assertTrue(os.path.exists(TEST_PATH + ".pub"))

    def test_verify_files_removed(self):
        self.remove_test_files(TEST_PATH)
        self.assertTrue(not os.path.exists(TEST_PATH))
        self.assertTrue(not os.path.exists(TEST_PATH))

    def generate_test_files(self):
        """
        Test the keygen module by creating a private/public keypair
        """
        key_gen = KeyGen()
        private_bytes, public_bytes = key_gen.generate_rsa_keypair()
        key_gen.save_keypair(TEST_PATH, private_bytes, public_bytes)

    def remove_test_files(self, file_path: str):
        """
        Remove test files after creation
        """
        os.remove(file_path)
        os.remove(file_path + ".pub")


if __name__ == "__main__":
    unittest.main()
