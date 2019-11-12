import re


class proChose(object):

    def __init__(self, path):
        with open(path, 'r') as f:
            self.content = f.read()

    def getNames(self):
        reg = re.compile('\(P (.*?)\n')
        return re.findall(reg, self.content)


if __name__ == '__main__':
    p = proChose('test.txt')
    print(p.getNames())
