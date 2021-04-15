
from PyQt5.QtWidgets import QDialog, QApplication
from dlgmain import Ui_Dialog


class finestra(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()

        #self.ui.pushButton_click(pushButton_click)

        self.ui.setupUi(self)
        self.show()


    # Codice scritto a mano ( nome evento creato da qt Designer visibile nel file esempio1.py)
    def ExitDialog(self) :

        self.close()

      # Codice scritto a mano ( nome evento creato da qt Designer visibile nel file esempio1.py)
    def pippo(self) :

        print('pippo')
        
       

   

if __name__ == '__main__' :

	app=QApplication([])
	appwindow=finestra()
	appwindow.show()
	app.exec_()
   
