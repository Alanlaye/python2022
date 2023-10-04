import unittest
from name_function import get_formatted_name
#导入模块unittest和要测试的函数get_formatted_name

class NamesTestCase(unittest.TestCase):
    #通过从unittest中继承父类TestCase
    #创建了一个名为NamesTestCase的子类
    def test_first_last_name(self):
    #创建一个方法，用于核实是否正确格式化名称
    #方法名必须以test_打头,由python自动调用
        formatted_name = get_formatted_name('aa','bb')
        self.assertEqual(formatted_name,'Aa Bb')
        #断言方法

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗?"""
        formatted_name = get_formatted_name( 
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
    
unittest.main()
#让Python运行这个文件中的测试

