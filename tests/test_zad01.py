import unittest

from src.zad01.main import Note


class NoteTest(unittest.TestCase):
    def test_get_name_1(self):
        self.assertEqual("Adam", Note("Adam", 4.5).get_name())

    def test_get_name_2(self):
        self.assertEqual("Andrzej", Note("Andrzej", 3).get_name())

    def test_get_note_1(self):
        self.assertEqual(4.5, Note("Adam", 4.5).get_note())

    def test_get_note_2(self):
        self.assertEqual(3.0, Note("Andrzej", 3.0).get_note())

    def test_name_none_type_exception(self):
        with self.assertRaises(TypeError):
            Note(None, 4.5)

    def test_name_empty_exception(self):
        with self.assertRaises(ValueError):
            Note("", 4.5)

    def test_note_less_than_2_exception(self):
        with self.assertRaises(ValueError):
            Note("Adam", 1.5)

    def test_note_greater_than_6_exception(self):
        with self.assertRaises(ValueError):
            Note("Adam", 6.5)
