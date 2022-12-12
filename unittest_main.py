# import unittest
# from main import main
#
#
# class TestIPFound(unittest.TestCase):
#
#     def test_from_doc(self):
#         self.assertEqual(main("E:\\test\\ipv41", "4"), "192.168.1.0/29")
#
#     def test_new_data(self):
#         self.assertEqual(main("E:\\test\\ipv41", "4"), "192.168.0.0/25")
#         self.assertEqual(main("E:\\test\\ipv41", "4"), "192.168.0.0/23")
#         self.assertEqual(main("E:\\test\\ipv41", "4"), "192.168.1.0/27")
#
#     def test_error(self):
#         self.assertRaises(ValueError, main, "E:\\test\\ipv41", "4")
#         self.assertRaises(ValueError, main, "E:\\test\\ipv41", "4")
#         self.assertRaises(ValueError, main, "E:\\test\\ipv41", "4")
