from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QButtonGroup, 
    QStackedWidget, QWidget, QLineEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from .modern_button import ModernButton

class ActionCenter(QFrame):
    def __init__(self):
        super().__init__()
        self.setProperty("class", "action-panel")
        self.setStyleSheet("background-color: white; border-left: 1px solid #e0e0e0;")
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        
        self.lbl_title = QLabel("Action Center")
        self.lbl_title.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 15px;")
        self.layout.addWidget(self.lbl_title)

        self._init_tabs()
        self._init_pages()

    def _init_tabs(self):
        self.tabs_layout = QHBoxLayout()
        self.btn_rename = QPushButton("Batch Rename")
        self.btn_copy = QPushButton("Copy & Rename")
        self.btn_delete = QPushButton("Secure Deletion")
        
        self.btn_rename.setCheckable(True)
        self.btn_rename.setChecked(True)
        self.btn_copy.setCheckable(True)
        self.btn_delete.setCheckable(True)

        self.tab_group = QButtonGroup()
        self.tab_group.addButton(self.btn_rename, 0)
        self.tab_group.addButton(self.btn_copy, 1)
        self.tab_group.addButton(self.btn_delete, 2)
        
        style = """
            QPushButton {
                border: 1px solid #e0e0e0;
                background: transparent;
                padding: 8px;
                color: #666;
                border-radius: 4px;
                margin-right: 5px;
            }
            QPushButton:checked {
                color: #fff;
                background-color: #007bff;
                border: 1px solid #0056b3;
                font-weight: bold;
            }
            QPushButton:hover {
                border: 1px solid #007bff;
                color: #333;
            }
        """
        for btn in [self.btn_rename, self.btn_copy, self.btn_delete]:
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(style)
            btn.setMinimumWidth(80)
            self.tabs_layout.addWidget(btn)
        
        self.tabs_layout.setSpacing(5)
        self.layout.addLayout(self.tabs_layout)
        self.layout.addSpacing(20)

    def _init_pages(self):
        self.stack = QStackedWidget()
        
        # Rename Page
        self.page_rename = QWidget()
        l_rename = QVBoxLayout(self.page_rename)
        self.inp_rename_old = QLineEdit()
        self.inp_rename_new = QLineEdit()
        self.btn_exec_rename = ModernButton("Rename Files", primary=True)
        
        self.lbl_rename_find = QLabel("Find:")
        self.lbl_rename_replace = QLabel("Replace with:")
        
        # Rename Status
        self.lbl_rename_stats = QLabel("")
        self.lbl_rename_stats.setStyleSheet("color: #666; font-size: 12px; margin-bottom: 5px;")
        
        l_rename.addWidget(self.lbl_rename_find)
        l_rename.addWidget(self.inp_rename_old)
        l_rename.addWidget(self.lbl_rename_replace)
        l_rename.addWidget(self.inp_rename_new)
        l_rename.addSpacing(10)
        l_rename.addWidget(self.lbl_rename_stats) # Added status label
        l_rename.addWidget(self.btn_exec_rename)
        l_rename.addStretch()
        
        # Copy Page
        self.page_copy = QWidget()
        l_copy = QVBoxLayout(self.page_copy)
        self.inp_copy_old = QLineEdit()
        self.inp_copy_new = QLineEdit()
        self.btn_exec_copy = ModernButton("Copy and Rename", primary=True)
        
        self.lbl_copy_find = QLabel("Find:")
        self.lbl_copy_replace = QLabel("Replace with:")
        
        # Copy Status
        self.lbl_copy_stats = QLabel("")
        self.lbl_copy_stats.setStyleSheet("color: #666; font-size: 12px; margin-bottom: 5px;")
        
        l_copy.addWidget(self.lbl_copy_find)
        l_copy.addWidget(self.inp_copy_old)
        l_copy.addWidget(self.lbl_copy_replace)
        l_copy.addWidget(self.inp_copy_new)
        l_copy.addSpacing(10)
        l_copy.addWidget(self.lbl_copy_stats) # Added status label
        l_copy.addWidget(self.btn_exec_copy)
        l_copy.addStretch()

        # Delete Page
        self.page_delete = QWidget()
        l_delete = QVBoxLayout(self.page_delete)
        self.inp_delete = QLineEdit()
        self.btn_exec_delete = ModernButton("Delete Files", primary=False)
        self.btn_exec_delete.setStyleSheet("background-color: #dc3545; color: white; border: 1px solid #bd2130; padding: 10px; border-radius: 6px;")
        
        self.lbl_delete_match = QLabel("Text to match:")
        self.lbl_delete_warn = QLabel("Warning: This action cannot be undone.")
        
        # Delete Status
        self.lbl_delete_stats = QLabel("")
        self.lbl_delete_stats.setStyleSheet("color: #666; font-size: 12px; margin-bottom: 5px;")
        
        l_delete.addWidget(self.lbl_delete_match)
        l_delete.addWidget(self.inp_delete)
        l_delete.addSpacing(10)
        l_delete.addWidget(self.lbl_delete_stats) # Added status label
        l_delete.addWidget(self.btn_exec_delete)
        l_delete.addWidget(self.lbl_delete_warn)
        l_delete.addStretch()


        self.stack.addWidget(self.page_rename)
        self.stack.addWidget(self.page_copy)
        self.stack.addWidget(self.page_delete)
        
        self.layout.addWidget(self.stack)

        # Help Button
        self.layout.addStretch()
        self.btn_help = ModernButton("How to Use", primary=False)
        self.btn_help.setIcon(QIcon.fromTheme("help-browser"))
        self.btn_help.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: 1px solid #d1d1d6;
                padding: 8px;
                border-radius: 6px;
                color: #555;
            }
            QPushButton:hover {
                background-color: #e5e5ea;
                border: 1px solid #bcbcbc;
            }
        """)
        self.layout.addWidget(self.btn_help)

        self.tab_group.idClicked.connect(self.stack.setCurrentIndex)

    def update_texts(self, t):
        self.lbl_title.setText(t['action_center'])
        self.btn_rename.setText(t['batch_rename'])
        self.btn_copy.setText(t['copy_rename'])
        self.btn_delete.setText(t['secure_delete'])
        
        self.inp_rename_old.setPlaceholderText(t['find'])
        self.inp_rename_new.setPlaceholderText(t['replace'])
        self.btn_exec_rename.setText(t['execute_rename'])
        self.lbl_rename_find.setText(t['find'])
        self.lbl_rename_replace.setText(t['replace'])
        
        self.inp_copy_old.setPlaceholderText(t['find'])
        self.inp_copy_new.setPlaceholderText(t['replace'])
        self.btn_exec_copy.setText(t['execute_copy'])
        self.lbl_copy_find.setText(t['find'])
        self.lbl_copy_replace.setText(t['replace'])
        
        self.inp_delete.setPlaceholderText(t['delete_placeholder'])
        self.btn_exec_delete.setText(t['execute_delete'])
        self.lbl_delete_match.setText(t['delete_placeholder'])
        self.lbl_delete_warn.setText(t['delete_warning'])
        
        self.btn_help.setText(t['help_btn'])
