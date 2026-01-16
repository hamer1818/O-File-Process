import sys
from PyQt6.QtWidgets import QApplication
from app.views.main_window import MainWindow
from app.controllers.main_controller import MainController
from app.utils.translations import TRANSLATIONS

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    # Initialize View
    window = MainWindow(TRANSLATIONS)
    
    # Initialize Controller (connects View and Model)
    controller = MainController(window)
    
    # Show Window
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()