from PySide import QtCore, QtGui
import sys
from ui import Ui_Form

# Create application
app = QtGui.QApplication(sys.argv)


# Create form and init UI
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()


# Hook logic 
def encrypt():
	ui.textEdit.setText( "Button is pressed" )

ui.pushButton.clicked.connect( encrypt )

# Run main loop 
sys.exit(app.exec_())

    

    
