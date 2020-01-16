from MainWindow_UI import Ui_MainWindow, QtCore, QtGui, QtWidgets
from Indice import *

class MainWindowUser(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #-----------------------------------------------------
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)  #resized the last column to fit in the table
        #self.tableWidget.setColumnWidth(5, 80)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch) 
        self.filename = None
        self.data = pd.DataFrame(columns=["CODIGO", "ASIGNATURA", "UV", "SECCION", "AÑO", "PERIODO", 
                                                "CALIFICACION", "OBS"])

        self.promButton.clicked.connect(self.qPromData)
        self.addButton.clicked.connect(self.qAdd)
        self.removeButton.clicked.connect(self.qRemove)
        self.resetButton.clicked.connect(self.qReset)
        self.loadButton.clicked.connect(self.qOpenAFile)
        

    def qOpenAFile(self):
        self.filename = None
        explorer = QtWidgets.QFileDialog()
        currentDir = explorer.directory().canonicalPath()
        self.filename, typefilter = explorer.getOpenFileName(None, "Open File", currentDir, "TSV (*.tsv)")
        if self.filename:
            self.data = readData(self.filename)
            self.qTableRefresh()
            
    

    def qPromData(self):
        if(not self.data.empty):
            average = prom(self.data)
            self.promLine.setText("%.4f" % average)

    def qGetName(self,dataType):  
    
        text,okPressed = QtWidgets.QInputDialog.getText(self,"",("Escriba su %s" % dataType), QtWidgets.QLineEdit.Normal, "") 
        if(okPressed and text != ''):
            return text
        else:
            return False

    def qTableRefresh(self):
        
        for index, row in self.data.iterrows():
            
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem("%s" % row["ASIGNATURA"]))
            self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem("%s" % row["CALIFICACION"]))
            self.tableWidget.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem("%s" % row["UV"]))
       


    def qAdd(self):
        subject = self.qGetName("ASIGNATURA: ")
        uv = int(self.qGetName("UV: "))
        rate = int(self.qGetName("CALIFICACION: "))

        if(subject and uv and rate):
            self.data = self.data.append({"ASIGNATURA":subject, 
                            "UV":uv, 
                            "CALIFICACION":rate}, ignore_index=True)
            
            self.tableWidget.setRowCount(0)
            self.qTableRefresh()

    def qRemove(self):
        selectedItems = self.tableWidget.selectedItems()
        if(selectedItems):
            for item in selectedItems:
                name = item.text()

                pos = (self.data[self.data["ASIGNATURA"]==name]).index.values[0] 
                self.data = self.data.drop([pos], axis=0)
                
            self.tableWidget.setRowCount(0)
            self.qTableRefresh()
        else:
            name = self.qGetName("ASIGNATURA")
            if(name):
                pos = (self.data[self.data["ASIGNATURA"]==name]).index.values[0] 
                self.data = self.data.drop([pos], axis=0)
                
                self.tableWidget.setRowCount(0)
                self.qTableRefresh()

    def qReset(self):
        self.filename = None
        self.data = readData(self.filename)
        self.tableWidget.setRowCount(0)
        self.qTableRefresh()
#------------------------------------
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindowUser()
    window.show()
    app.exec_()
    #--------------------------------