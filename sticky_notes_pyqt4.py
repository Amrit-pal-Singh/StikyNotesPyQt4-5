import sys
from PyQt4 import QtGui, QtCore, QtGui
from PyQt4.QtCore import Qt

x = 300
y = 300



class TitleBar(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        css = """
        QWidget{
            Background: #CC9900;
            color:black;
            font:12px bold;
            font-weight:bold;
            border-radius: 1px;
            height: 11px;
        }
        QDialog{
            font-size:12px;
            color: black;
        }
        QToolButton{
            Background:#CC9900;
            font-size:11px;
        }
        """
        self.setStyleSheet(css)
        minimize = QtGui.QToolButton(self)
        close = QtGui.QToolButton(self)
        minimize.setIcon(QtGui.QIcon("min.png"))
        close.setIcon(QtGui.QIcon("close.png"))
        minimize.setMinimumHeight(20)
        close.setMinimumHeight(20)

        layout = QtGui.QHBoxLayout(self)


        edit_button = QtGui.QToolButton(self)
        add_button = QtGui.QToolButton(self)

        edit_button.setMinimumHeight(20)
        add_button.setMinimumHeight(20)

        edit_button.setIcon(QtGui.QIcon(''))
        add_button.setIcon(QtGui.QIcon('add.png'))
        
        #layout.addWidget(edit_button)
        layout.addWidget(add_button)


        #layout.addWidget(minimize)
        layout.addWidget(close)
        
        layout.insertStretch(1,0)
        layout.setSpacing(0)

        self.maxNormal=False
        close.clicked.connect(self.close_func)
        minimize.clicked.connect(self.minimize_func)



    
    def add_new_window(self):
        self.nw = Frame()
        global x
        x += 270
        self.nw.move(x , y)


    def close_func(self):
        sys.exit()

    def minimize_func(self):
        box.showMinimized()

####

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            box.moving = True 
            box.offset = event.pos()

    def mouseMoveEvent(self,event):
        if box.moving: box.move(event.globalPos()-box.offset)

####


    def showSmall(self):
        box.showMinimized()

    def close(self):
        box.close()

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            box.moving = True 
            box.offset = event.pos()

    def mouseMoveEvent(self,event):
        if box.moving: box.move(event.globalPos()-box.offset)


####

####

class Frame(QtGui.QFrame):  
    def __init__(self, parent = None):
        QtGui.QFrame.__init__(self, parent)
        self.m_mouse_down= False        
        css = """
        QFrame{
            Background:  #FFDE00;
            color:black;
            font:20px ;
            font-weight:bold;
            }
        """
        self.setStyleSheet(css)
        self.setMouseTracking(True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.titleBar_ = TitleBar(self)
        vBox = QtGui.QVBoxLayout(self)
        vBox.addWidget(self.titleBar_)
        vBox.setContentsMargins(0, 0, 0, 0)
        #vBox.setMargin(0)
        vBox.setSpacing(0)
        layout = QtGui.QVBoxLayout(self)
        # layout.setMargin(3)
        layout.setSpacing(0)
        
        self.textEdit = GrowingTextEdit()       
        layout.addWidget(self.textEdit)
        
        
        vBox.addLayout(layout)
        

    
    def add_new_window(self):
        self.nw = widget()
        global x
        x += 270
        self.nw.move(x , y)

    
    def titleBar(self):
        return self.titleBar_
    

    def mousePressEvent(self,event):
        self.m_old_pos = event.pos()
        self.m_mouse_down = event.button()== Qt.LeftButton

    def mouseMoveEvent(self,event):
        x=event.x()
        y=event.y()

    def mouseReleaseEvent(self,event):
        m_mouse_down=False






class GrowingTextEdit(QtGui.QTextEdit):
    def __init__(self, *args, **kwargs):
        super(GrowingTextEdit, self).__init__(*args, **kwargs)  
        self.document().contentsChanged.connect(self.sizeChange)
        self.setMinimumWidth(230)
        self.setMinimumHeight(150)
        self.heightMin = 0
        self.heightMax = 400

    def sizeChange(self):
        docHeight = self.document().size().height()
        if self.heightMin <= docHeight <= self.heightMax:
            self.setMinimumHeight(docHeight)






if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    box = Frame()
    box.move(x,y)    
    box.show()
    app.exec_()
