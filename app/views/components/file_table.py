from PyQt6.QtWidgets import QTableWidget, QHeaderView, QAbstractItemView, QTableWidgetItem, QStyle
from PyQt6.QtCore import Qt

class FileTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setColumnCount(4)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.verticalHeader().setVisible(False)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setShowGrid(False)
        self.setAlternatingRowColors(True)
        # Force high contrast style
        self.setStyleSheet("""
            QTableWidget {
                background-color: white;
                alternate-background-color: #f8f9fa;
                selection-background-color: #007bff;
                selection-color: white;
                border: 1px solid #e0e0e0;
            }
            QTableWidget::item {
                background-color: white;
                color: #333333;
                padding: 5px;
            }
            QTableWidget::item:selected {
                background-color: #007bff;
                color: white;
            }
        """)

    def update_headers(self, headers_list):
        self.setHorizontalHeaderLabels(headers_list)

    def populate(self, files_data):
        self.setRowCount(0)
        for row, file_info in enumerate(files_data):
            self.insertRow(row)
            
            # Name with Icon
            item_name = QTableWidgetItem(file_info['name'])
            try:
                icon = self.style().standardIcon(QStyle.StandardPixmap.SP_FileIcon)
                item_name.setIcon(icon)
            except:
                pass
            
            self.setItem(row, 0, item_name)
            self.setItem(row, 1, QTableWidgetItem(file_info['extension']))
            
            # Size formatting
            size_mb = file_info['size'] / (1024 * 1024)
            self.setItem(row, 2, QTableWidgetItem(f"{size_mb:.2f} MB"))
            
            # Date formatting (could be passed pre-formatted, but doing here for now)
            import datetime
            dt = datetime.datetime.fromtimestamp(file_info['timestamp']).strftime('%Y-%m-%d %H:%M')
            self.setItem(row, 3, QTableWidgetItem(dt))

