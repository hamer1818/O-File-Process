from PyQt6.QtWidgets import QFrame, QVBoxLayout, QButtonGroup, QLabel
from PyQt6.QtCore import QStandardPaths, Qt, pyqtSignal, QUrl
from PyQt6.QtGui import QIcon, QPixmap, QDesktopServices
from .modern_button import ModernButton

class SidebarItem(ModernButton):
    def __init__(self, text, icon_name, path, parent=None):
        super().__init__(text)
        self.path = path
        self.setIcon(QIcon.fromTheme(icon_name))
        self.setCheckable(True)
        self.setAutoExclusive(True)
        self.setFixedHeight(40)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setProperty("class", "sidebar-item")
        self.setStyleSheet("""
            text-align: left; 
            padding-left: 15px; 
            border: 1px solid transparent; 
            border-radius: 6px; 
            color: #555;
            background-color: transparent;
        """)

class Sidebar(QFrame):
    folder_selected = pyqtSignal(str)
    
    def __init__(self, translations):
        super().__init__()
        self.setProperty("class", "sidebar")
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10, 20, 10, 20)
        self.layout.setSpacing(5)
        self.sidebar_buttons = {}
        self.translations = translations
        self._setup_ui()

    def _setup_ui(self):
        # Logo Area
        logo_label = QLabel()
        pixmap = QIcon.fromTheme("application-x-executable").pixmap(48, 48)
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(logo_label)
        
        app_title = QLabel("O File\nProcessor")
        app_title.setStyleSheet("font-weight: bold; font-size: 16px; margin-bottom: 20px; color: #2c3e50;")
        app_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(app_title)

        # Select Folder Button
        self.btn_select_folder = ModernButton("Select Folder", primary=True)
        self.btn_select_folder.setIcon(QIcon.fromTheme("folder-open"))
        self.sidebar_buttons['select_folder_btn'] = self.btn_select_folder
        self.layout.addWidget(self.btn_select_folder)
        self.layout.addSpacing(20)

        # Standard Locations
        self.nav_group = QButtonGroup()
        self.nav_group.buttonClicked.connect(self._on_nav_clicked)
        
        locations = [
            ("desktop", QStandardPaths.StandardLocation.DesktopLocation, "user-desktop"),
            ("documents", QStandardPaths.StandardLocation.DocumentsLocation, "folder-documents"),
            ("downloads", QStandardPaths.StandardLocation.DownloadLocation, "folder-download"),
            ("music", QStandardPaths.StandardLocation.MusicLocation, "folder-music"),
            ("pictures", QStandardPaths.StandardLocation.PicturesLocation, "folder-pictures"),
            ("videos", QStandardPaths.StandardLocation.MoviesLocation, "folder-videos"),
        ]

        for key, loc_enum, icon in locations:
            path = QStandardPaths.writableLocation(loc_enum)
            initial_text = self.translations['en'].get(key, key.capitalize())
            btn = SidebarItem(initial_text, icon, path)
            self.layout.addWidget(btn)
            self.nav_group.addButton(btn)
            self.sidebar_buttons[key] = btn

        self.layout.addStretch()

        # GitHub Link
        self.btn_github = ModernButton("GitHub Repository", primary=False)
        self.btn_github.setIcon(QIcon.fromTheme("applications-internet"))
        self.btn_github.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_github.setStyleSheet("""
            text-align: left; 
            padding-left: 15px; 
            border: 1px solid transparent; 
            border-radius: 6px; 
            color: #555;
            background-color: transparent;
            font-size: 12px;
        """)
        self.btn_github.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/hamer1818/O-File-Process")))
        self.layout.addWidget(self.btn_github)


    def _on_nav_clicked(self, button):
        if hasattr(button, 'path'):
            self.folder_selected.emit(button.path)

    def update_texts(self, t):
        self.btn_select_folder.setText(t['select_folder'])
        # Update standard location buttons
        for key, btn in self.sidebar_buttons.items():
            if key != 'select_folder_btn':
                 btn.setText(t.get(key, key.capitalize()))
