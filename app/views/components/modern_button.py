from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt

class ModernButton(QPushButton):
    def __init__(self, text, primary=False):
        super().__init__(text)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.primary = primary
        self.setProperty("class", "primary" if primary else "secondary")
        
        # Inline style to ensure visibility/reliability as requested
        if primary:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #007bff;
                    color: white;
                    border: 1px solid #0056b3;
                    padding: 10px 20px;
                    border-radius: 6px;
                    font-weight: 600;
                }
                QPushButton:hover {
                    background-color: #0056b3;
                }
                QPushButton:pressed {
                    background-color: #004085;
                }
            """)
