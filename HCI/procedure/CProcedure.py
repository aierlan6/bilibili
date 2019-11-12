s1_condition = ['start',
                ['goal', 'IS', 'count-from'],
                ['start', '=', 'sxx']]
s1_result = [['goal', 'count', 'num1'],
             ['retrieval', 'nmsl', 'counter-order'],
             ['first', '=', 'num1']]

s2_condition = ['first', 64.0,
                ['goal', 'ahh', 'count-from'],
                ['start', '=', 'num1']]
s2_result = [['goal', 'count', 'num1'],
             ['retrieval', 'IS', 'counter-order'],
             ['haiyoushui', '=', 'num1']]


class proModeling(object):

    def __init__(self):

        self.time = []  # 此处为视频时间，当为负数时，表示是手工建模
        self.name = []  # 函数名
        self.condition = []
        self.result = []
        self.model = []
        self.len = 0

    def getname(self, condition):
        return condition[0]

    def isVideo(self, condition):
        if isinstance(condition[1], float):
            return True
        else:
            return False

    def makeModel(self):
        m = ''
        # 开头
        m += '(P ' + self.name[self.len-1] + '\n'
        # 条件
        m += self.addModel(self.condition[self.len-1])
        # self.addModel(self.condition)
        m += '==>\n'
        # 结果
        m += self.addModel(self.result[self.len-1])
        m += ')\n'
        return m

    def addModel(self, s):
        temp = ''
        for con in s:
            # print(con[0])
            if (con[0] == 'goal') or (con[0] == 'retrieval'):
                # temp += '\t=' + con[0] + '>\n'      # 此处的 = 或 - 或 + 不知道在什么情况下是什么
                temp += '    =' + con[0] + '>\n'
                if con[1] == 'IS':
                    # temp += '\t\tISA\t\t\t' + con[2] + '\n'
                    temp += '        ISA        ' + con[2] + '\n'
                else:
                    # temp += '\t\t' + con[1] + '\t\t=' + con[2] + '\n'
                    temp += '        ' + con[1] + '        =' + con[2] + '\n'
            else:
                if con[1] == '=':
                    # temp += '\t\t' + con[0] + '\t\t' + con[1] + con[2] + '\n'
                    temp += '        ' + con[0] + '        ' + con[1] + con[2] + '\n'
                else:
                    pass
        return temp

    def moremodel(self, condition, result):

        self.len += 1

        if self.isVideo(condition):
            self.time.append(condition[1])
            self.condition.append(condition[2:])
        else:
            self.time.append(-1)
            self.condition.append(condition[1:])

        self.name.append(self.getname(condition))

        self.result.append(result)
        r = self.makeModel()
        self.model.append(r)


def showall(pm):
    for i in range(pm.len):
        print('视频时间：' + str(pm.time[i]))
        print('函数名字：' + pm.name[i])
        print('模型函数：\n' + pm.model[i])

    print('总共有' + str(pm.len) + '个模型函数')


if __name__ == '__main__':
    p = proModeling()
    p.moremodel(s1_condition, s1_result)
    # p.moremodel(s2_condition, s2_result)
    showall(p)
