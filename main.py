import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class GTAVehicleMarketTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GTA 5 Vehicle Market Tracker")
        self.setGeometry(100, 100, 900, 700)
        self.initUI()

    def initUI(self):
        pass  # Здесь будет интерфейс

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GTAVehicleMarketTracker()
    window.show()
    sys.exit(app.exec_())
