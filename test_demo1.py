import pytest
import allure

@allure.step("参数相加 : {0}，{1}")
def add(x, y):
    return x + y

@pytest.mark.parametrize('x', [0, 1])
@pytest.mark.parametrize('y', [2, 3])
def test_add(x, y):
    with allure.step("步骤1：输入两个参数"):
        print("输入参数：x->{}，y->{}".format(x, y))
    with allure.step("步骤2：调用相加方法"):
        result = add(x, y)
    with allure.step("步骤3：输出结果"):
        print("输出结果：{}".format(result))

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/'])