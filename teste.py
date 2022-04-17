# lst = [1,2,3]
# suma = 1
#
# for val in range(len(lst) + 10):
#     print('val: ', val)
#     print('suma 1: ',suma)
#     suma += val
#     print('suma 1: ',suma)
#

# import keyword
#
# print(keyword.kwlist)
#
# print(keyword.iskeyword('try'))
from pytest_cases import fixture, parametrize


@fixture
@parametrize()
def soma(x, y) -> int:
    return y + x


def divizao(x, y):
    return y * x

#
# def test_soma():
#     assert 7 == soma(2, 5)
#
#
# def test_divizao():
#     assert 7 == divizao(2, 5)
