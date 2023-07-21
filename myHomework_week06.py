import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore

class MyWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle("Create Poly Objects")
        self.setMinimumSize(500, 200)
        self.setMaximumSize(700, 300)
        self.resize(500, 200)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout) # MyWindow.setLayout


        # Object Name
        self.object_name_widget = QtWidgets.QLineEdit()
        self.main_layout.addWidget(self.object_name_widget)
        self.object_name_widget.setPlaceholderText("Object Name")


        # RadioButtons
        self.radio_buttons_layout = QtWidgets.QHBoxLayout()
        self.radio_buttons_layout.setAlignment(QtCore.Qt.AlignTop)
        self.main_layout.addLayout(self.radio_buttons_layout)

        self.rbutton_sphere = QtWidgets.QRadioButton("Sphere")
        self.rbutton_sphere.setChecked(True)
        self.rbutton_cube = QtWidgets.QRadioButton("Cube")
        self.rbutton_cone = QtWidgets.QRadioButton("Cone")

        self.radio_buttons_layout.addWidget(self.rbutton_sphere)
        self.radio_buttons_layout.addWidget(self.rbutton_cube)
        self.radio_buttons_layout.addWidget(self.rbutton_cone)
        

        # Slider
        self.slider_layout = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(self.slider_layout)

        self.text_slider = QtWidgets.QLabel()
        self.text_slider.setText("Move x:")
        self.slider_layout.addWidget(self.text_slider)

        self.slider_range = QtWidgets.QLineEdit()
        self.slider_layout.addWidget(self.slider_range, stretch=1)
        self.slider_range.setText("0")

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_layout.addWidget(self.slider, stretch=3)
        self.slider.setMaximum(10)
        self.slider.valueChanged.connect(self.on_slider_value_changed)

        
        # Buttons
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setAlignment(QtCore.Qt.AlignBottom)
        self.main_layout.addLayout(self.buttons_layout)

        self.button_Create = QtWidgets.QPushButton("Create")
        self.button_Create.clicked.connect(self.on_button_Create_clicked)

        self.button_Apply = QtWidgets.QPushButton("Apply")
        self.button_Apply.clicked.connect(self.on_button_Apply_clicked)

        self.button_Cancel = QtWidgets.QPushButton("Cancel")
        self.button_Cancel.clicked.connect(self.close)

        self.buttons_layout.addWidget(self.button_Create)
        self.buttons_layout.addWidget(self.button_Apply)
        self.buttons_layout.addWidget(self.button_Cancel)

        
    def on_slider_value_changed(self, value):    
        self.slider_range.setText(str(value))

    def on_button_Create_clicked(self):
        self.on_button_Apply_clicked()
        self.close()  

    def on_button_Apply_clicked(self):
        self.object_name = self.object_name_widget.text()
        self.slider_value = self.slider.value()
        
        if self.rbutton_sphere.isChecked():
            obj = cmds.polySphere(name=self.object_name)
            
        elif self.rbutton_cube.isChecked():
            obj = cmds.polyCube(name=self.object_name)
            
        elif self.rbutton_cone.isChecked():
            obj = cmds.polyCone(name=self.object_name) 

        cmds.move(self.slider_value,0,0, obj)  

            
# clear UI
if cmds.window("MyTestUI", query=True, exists=True):
    cmds.deleteUI("MyTestUI")
if cmds.windowPref("MyTestUI", exists=True):
    cmds.windowPref("MyTestUI", remove=1)

a = MyWindow()
a.show()
