"""
获取元素信息方法: Part2
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 4. is_displayed() 判断元素是否可见
# 说明: 该方法多用于对元素在页面内显示效果的判断时使用(元素不显示不意味着一定无法定位)
span = driver.find_element_by_name('sp1')
print('目标元素是否显示:', span.is_displayed())

# 5. is_enabled() 判断元素是否可用
# 说明: 该方法多用于判断目标元素是否可以进行交互时使用
can_btn = driver.find_element_by_id('cancelA')
print('目标元素是否可用:', can_btn.is_enabled())

# 6. is_selected() 判断元素是否选中，用来检查复选框或单选按钮是否被选中
# 场景: 如购物车页面, 不全选商品, 不让结算
check = driver.find_element_by_id('lyA')
print('目标元素是否被选中:', check.is_selected())

# 扩展: 判断条件
if check.is_selected():  # 选中的判断
    pass
if not check.is_selected():  # 未选中的判断
    pass

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()
