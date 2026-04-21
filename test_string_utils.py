import unittest
from string_utils import StringUtils

class TestStringUtils(unittest.TestCase):
    
    def test_reverse(self):
        """测试 reverse 方法"""
        self.assertEqual(StringUtils.reverse("hello"), "olleh")
        self.assertIsNone(StringUtils.reverse(None))
        self.assertEqual(StringUtils.reverse(""), "")

    def test_capitalize(self):
        """测试 capitalize 方法（该测试预期会因为代码中的缺陷而失败/报错）"""
        self.assertEqual(StringUtils.capitalize("hello"), "Hello")
        self.assertEqual(StringUtils.capitalize(""), "")
        self.assertEqual(StringUtils.capitalize("world"), "World")

def build_test_suite():
    """将多个单元测试打包为一个测试集 (Test Suite)"""
    suite = unittest.TestSuite()
    # 手动添加要执行的测试用例验证批量运行
    suite.addTest(TestStringUtils('test_reverse'))
    suite.addTest(TestStringUtils('test_capitalize'))
    return suite

if __name__ == '__main__':
    # 批量运行测试集
    runner = unittest.TextTestRunner(verbosity=2)
    suite = build_test_suite()
    runner.run(suite)
