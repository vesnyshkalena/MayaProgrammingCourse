import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui


class SelectionSetButton(QtWidgets.QPushButton):
    def __init__(self, name, selection):
        super(SelectionSetButton, self).__init__(name)
        self.name = name
        self.selection = selection

        self.setMinimumHeight(70)
        self.clicked.connect(self.set_selection)
        
    def set_selection(self):        
        cmds.select(self.selection, ne=False, r=True)


class SelectionSetTool(QtWidgets.QDialog):
    def __init__(self):
        super(SelectionSetTool, self).__init__()
        self.next_selection_set_id = 1
        self.setup_ui()
        
    def setup_ui(self):

        # create window
        self.setWindowTitle("Selection Set Tool")
        self.setObjectName("SelectionSetToolUIId")
        self.setMinimumSize(200, 300)
        self.setMaximumSize(300, 800)
        self.resize(300, 300)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # create main layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignTop)
        self.main_layout.setContentsMargins(5,5,5,5)
        self.setLayout(self.main_layout)

        # scroll area
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setMinimumHeight(200)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumWidth(190)
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.scroll_area_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scroll_area_widget)  

        self.scroll_layout = QtWidgets.QVBoxLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.setContentsMargins(0,0,0,0)
        self.scroll_layout.setSpacing(5)
        self.scroll_area_widget.setLayout(self.scroll_layout)
        self.main_layout.addWidget(self.scrollArea)

        # create button +
        self.btn0 = QtWidgets.QPushButton("+")
        self.btn0.setMinimumHeight(70)
        self.main_layout.addWidget(self.btn0)
        self.btn0.clicked.connect(self.create_selection_set)

        # for i in self.selection:
            # self.

    def create_selection_set(self):
        selected_objects = cmds.ls(sl=1,l=1)
        if len(selected_objects) == 0:
            cmds.warning("No selected objects for selecction set") 
            return
        set_name = "SelectionSet {}".format(self.next_selection_set_id)
        selection_set = cmds.sets(selected_objects, n=set_name)    
        btn = SelectionSetButton(selection_set, selection_set)
        self.scroll_layout.insertWidget(0, btn)
        self.next_selection_set_id += 1

                   
            
# clear UI
def main():
    if cmds.window("SelectionSetToolUIId", query=True, exists=True):
        cmds.deleteUI("SelectionSetToolUIId")
    if cmds.windowPref("SelectionSetToolUIId", exists=True):
        cmds.windowPref("SelectionSetToolUIId", remove=1)

    global myUI
    myUI = SelectionSetTool()
    myUI.show()

if __name__ == "__main__":
    main()
