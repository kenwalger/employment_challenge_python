import unittest
import reverse_hash
import hash


class HashTestingMethods(unittest.TestCase):
    def test_dehash(self):
        self.assertEqual(reverse_hash.reverse_hash(680131659347), 'leepadg')

    def test_hash(self):
        self.assertEqual(hash.hasher('leepadg'), 680131659347)


if __name__ == '__main__':
    unittest.main()
