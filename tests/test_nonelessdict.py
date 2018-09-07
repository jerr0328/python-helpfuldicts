from helpfuldicts import NonelessDict
from unittest import TestCase


class TestNonelessDict(TestCase):

    def testToFromNormalDictionary(self):
        sample_dict = {"hello": "world", "key": 42}
        noneless = NonelessDict(sample_dict)
        self.assertEqual(sample_dict, dict(noneless))

    def testNoneNotAdded(self):
        noneless = NonelessDict(hello="world", key=42)
        noneless['reality'] = None
        self.assertNotIn('reality', noneless)
        normal = dict(noneless)
        self.assertNotIn('reality', normal)

    def testEmptyNotAdded(self):
        noneless = NonelessDict(hello="world", key=42)
        noneless['empty'] = []
        self.assertNotIn('empty', noneless)
        normal = dict(noneless)
        self.assertNotIn('empty', normal)

    def testStrictNoneAddsEmpty(self):
        noneless = NonelessDict(hello="world", key=42)
        noneless.set_with_strict_none_check('empty', [])
        self.assertIn('empty', noneless)
        self.assertEqual(noneless['empty'], [])

    def testStrictNoneWithNone(self):
        noneless = NonelessDict(hello="world", key=42)
        noneless.set_with_strict_none_check('reality', None)
        self.assertNotIn('reality', noneless)
