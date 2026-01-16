from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame, QLabel, QComboBox, QLineEdit
from app.views.components.sidebar import Sidebar
from app.views.components.file_table import FileTable
from app.views.components.action_center import ActionCenter
from app.utils.styles import MAIN_STYLE

class MainWindow(QWidget):
    def __init__(self, translations):
        super().__init__()
        self.translations = translations
        self.current_language = 'en'
        self.setup_ui()
        self.setup_styles()

    def setup_ui(self):
        self.resize(1400, 900)
        self.setMinimumSize(800, 500)
        self.showMaximized()
        
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Components
        self.sidebar = Sidebar(self.translations)
        self.file_table = FileTable()
        self.action_center = ActionCenter()

        # Center Panel (Toolbar + Table)
        self.center_frame = QFrame()
        self.center_layout = QVBoxLayout(self.center_frame)
        self.center_layout.setContentsMargins(20, 20, 20, 20)
        
        # Toolbar
        self.top_toolbar = QHBoxLayout()
        self.lbl_current_folder = QLabel("No Folder Selected")
        self.lbl_current_folder.setStyleSheet("font-weight: bold; font-size: 14px; color: #333;")
        self.top_toolbar.addWidget(self.lbl_current_folder)
        self.top_toolbar.addStretch()
        
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["English", "Türkçe", "Azərbaycanca", "Español", "Русский", "中文"])
        self.top_toolbar.addWidget(self.lang_combo)
        self.center_layout.addLayout(self.top_toolbar)

        # Search
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search files...")
        self.center_layout.addWidget(self.search_input)

        # Table
        self.center_layout.addWidget(self.file_table)

        # Assembly
        self.main_layout.addWidget(self.sidebar, 1)
        self.main_layout.addWidget(self.center_frame, 3)
        self.main_layout.addWidget(self.action_center, 2)

    def setup_styles(self):
        self.setStyleSheet(MAIN_STYLE)

    def update_texts(self):
        t = self.translations[self.current_language]
        self.setWindowTitle(t['window_title'])
        self.sidebar.update_texts(t)
        self.action_center.update_texts(t)
        self.file_table.update_headers([t['name'], t['type'], t['size'], t['date']])
        self.search_input.setPlaceholderText(t['search_placeholder'])
        
        if self.lbl_current_folder.text() == "No Folder Selected" or self.lbl_current_folder.text() == self.translations['en']['no_folder']:
             self.lbl_current_folder.setText(t['no_folder'])
