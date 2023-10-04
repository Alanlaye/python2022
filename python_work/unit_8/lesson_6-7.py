#8.6将函数储存在模块中

#8.6.1 导入整个模块
###语法1：module_name.function_name()
###语法：模块名称+'.'+函数名称（）
import pizza
pizza.make_pizza(16,'aa')
pizza.make_pizza(19,'bb','cc')

#8.6.2 导入特定函数
###语法2：先用 from import 导入特定函数。那么调用时就可以直接使用函数名
from pizza import make_pizza
make_pizza(16,'df')

#8.6.3 使用as给函数指定别名
from pizza import make_pizza as mp
mp(16,'aa')

#8.6.4 使用as给模块指定别名
import pizza as p
p.make_pizza(16,'aa')

#8.6.5 导入模块中的所有函数
###由于导入了每个函数，可通过名称来调用每个函数，而无需使用句点表示法
###最好不要采用这种导入方法
###如果模块中有函 数的名称与你的项目中使用的名称相同，可能导致意想不到的结果
from pizza import*
make_pizza(16,'aa')

