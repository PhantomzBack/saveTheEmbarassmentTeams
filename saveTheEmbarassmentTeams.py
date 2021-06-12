from selenium import webdriver
driver = webdriver.Chrome()
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5.QtCore as QtCore
import sys

app = QApplication(sys.argv)
class Worker(QObject):
    finished=pyqtSignal()
    def __init__(self, driver):
        super().__init__()
        self.driver=driver
        self.continueRunning=True

    def checkForMute(self):
        print("waiting for mute")
        self.driver.execute_script(script=jsScriptExpectingMute)
        print("Muted")
        self.finished.emit()

    def stop(self):
        pass


class Main(QMainWindow):
    def __init__(self, driver, app):
        super().__init__()
        self.driver=driver
        self.app=app
        size = self.screen().size()
        print(size.width(), size.height())
        self.setGeometry(int((size.width()/2)-140),int((size.height())-300),280,80)
        self.setWindowOpacity(.7)
        self.setStyleSheet("background-color: rgb(255,255,0); font-size: 20px;border-radius: 5px; border-width: 20px;border-color: rgb(255,255,0);")
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.initUI()
        self.show()

    def stopApp(self):
        print("Quitting")
        qApp.quit()

    def initUI(self):
        self.mainWidget=QLabel("WARNING! Unmuted on teams\n \tAvert Crisis")
        self.setCentralWidget(self.mainWidget)
        self.thread = QThread()
        self.worker = Worker(driver=driver)
        self.worker.moveToThread(self.thread)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.stopApp)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.started.connect(self.worker.checkForMute)


        self.thread.start()



driver.get("http://teams.microsoft.com")
foundMuteButton=False
while(foundMuteButton==False):
    input("Press enter once you have started the meeting")
    foundMuteButton=True
    try:
        muteButton=driver.find_element_by_id("microphone-button")
    except:
        foundMuteButton=False
        print("Uh oh! Ensure that you are on the meeting, and can see the mute button, and press enter again")




jsScriptExpectingMute="""while(document.getElementById("microphone-button").getAttribute("aria-label")!="Unmute"){
await new Promise(r => setTimeout(r, 1000));
}
console.log("Done234");"""
jsScriptExpectingUnmute="""while(document.getElementById("microphone-button").getAttribute("aria-label")!="Mute"){
await new Promise(r => setTimeout(r, 1000));
}
console.log("Done567");"""
while(1):
    print("Hello1")
    if(muteButton.get_attribute("aria-label")=="Mute"):
        muted=False
    else:
        muted=True
    if(not muted):
        main = Main(driver=driver, app=app)
        app.exec_()
    else:
        print("Waiting for unmute")
        driver.execute_script(script=jsScriptExpectingUnmute)
        print("UnMuted")

    print("Hello")