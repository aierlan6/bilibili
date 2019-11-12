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

def get():
    return s2_condition, s2_result
def get1():
    return s1_condition, s1_result
def get2():
    return s2_condition, s2_result


from CProcedure import proModeling, showall
import sys
from procedure import Ui_SideBarDemo
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class myWindow(Ui_SideBarDemo, QWidget):

    def __init__(self):
        super(Ui_SideBarDemo, self).__init__()
        self.setupUi(self)
        self.names = []

        # 创建一个对象，存储多个模型函数
        self.models = proModeling()

        # 手工建模
        self.pushButton_4.clicked.connect(lambda: self.Preview(self.textBrowser_4))
        self.listWidget_4.itemClicked.connect(self.QLWclicked4)
        # self.listWidget_4.itemClicked.connect(lambda: self.QLWclicked(item=, tb=self.textBrowser_4))

        # 视频建模
        self.pushButton_2.clicked.connect(lambda: self.Preview(self.textBrowser_5))
        self.listWidget_6.itemClicked.connect(self.QLWclicked5)

    def Preview(self, tb):
        # condition, result = get()
        # if condition[0] not in self.names:
        #     self.names.append(condition[0])
        #     self.models.moremodel(condition, result)
        # else:
        #     QMessageBox.information(self, "Information",
        #                             self.tr("已有该函数名"))

        condition1, result1 = get1()
        if condition1[0] not in self.names:
            self.names.append(condition1[0])
            self.models.moremodel(condition1, result1)
        else:
            QMessageBox.information(self, "Information",
                                    self.tr("已有该函数名"))

        condition2, result2 = get2()
        if condition2[0] not in self.names:
            self.names.append(condition2[0])
            self.models.moremodel(condition2, result2)
        else:
            QMessageBox.information(self, "Information",
                                    self.tr("已有该函数名"))

        try:
            tb.setText(self.models.model[-1])

            self.listWidget_4.addItem(self.models.name[-1])
            self.listWidget_5.addItem(self.models.name[-1])
            self.listWidget_6.addItem(self.models.name[-1])
            # if self.models.name[-1] not in self.names:
            #     self.listWidget_4.addItem(self.models.name[-1])
            #     self.listWidget_5.addItem(self.models.name[-1])
            #     self.listWidget_6.addItem(self.models.name[-1])

        except Exception as e:
            print(e)

    def QLWclicked4(self, item):
        # print(item.text())
        try:
            # print(self.models.name.index(item.text()))
            self.textBrowser_4.setText(self.models.model[self.models.name.index(item.text())])
        except Exception as e:
            print(e)

    def QLWclicked5(self, item):
        # print(item.text())
        try:
            # print(self.models.name.index(item.text()))
            self.textBrowser_5.setText(self.models.model[self.models.name.index(item.text())])
        except Exception as e:
            print(e)

    def closeEvent(self, event):
        title = self.names[0] + '.txt'
        print(title)
        try:
            f = open(title, 'w')
            for i in self.models.model:
                f.write(i)
            f.close()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myWindow()
    window.show()
    sys.exit(app.exec_())
