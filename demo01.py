# 变量
height = 15


# 定义树
def design_tree():

    for i in range(height):

        print((' ' * (height - i)) + ('*' * ((2 * i) + 1)))

    print((' ' * height) + '|')


design_tree()
