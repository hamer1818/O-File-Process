MAIN_STYLE = """
    QWidget {
        font-family: 'Segoe UI', sans-serif;
        font-size: 13px;
        color: #333;
        background-color: #f5f5f7; 
    }
    QLineEdit {
        padding: 10px;
        border: 1px solid #d1d1d6;
        border-radius: 6px;
        background: white;
    }
    QLineEdit:focus {
        border: 1px solid #007bff;
    }
    /* Sidebar */
    QFrame[class="sidebar"] {
        background-color: #f0f0f3;
        border-right: 1px solid #e0e0e0;
    }
    QPushButton[class="sidebar-item"] {
        background-color: transparent;
        border: 1px solid transparent;
        border-radius: 6px;
        color: #555;
    }
    QPushButton[class="sidebar-item"]:hover {
        background-color: #e5e5ea;
        border: 1px solid #d1d1d6;
    }
    QPushButton[class="sidebar-item"]:checked {
        background-color: #e5e5ea;
        color: #000;
        font-weight: 600;
        border: 1px solid #d1d1d6;
    }
    /* Buttons */
    QPushButton[class="primary"] {
        background-color: #007bff;
        color: white;
        border: 1px solid #0056b3;
        padding: 10px 20px;
        border-radius: 6px;
        font-weight: 600;
    }
    QPushButton[class="primary"]:hover {
        background-color: #0056b3;
    }
    QPushButton[class="primary"]:pressed {
        background-color: #004085;
    }

    /* ScrollBar */
    QScrollBar:vertical {
        border: none;
        background: #f0f0f3;
        width: 10px;
        margin: 0px 0px 0px 0px;
        border-radius: 5px;
    }
    QScrollBar::handle:vertical {
        background: #c1c1c1;
        min-height: 20px;
        border-radius: 5px;
    }
    QScrollBar::handle:vertical:hover {
        background: #a8a8a8;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0px;
    }
    QScrollBar:horizontal {
        border: none;
        background: #f0f0f3;
        height: 10px;
        margin: 0px 0px 0px 0px;
        border-radius: 5px;
    }
    QScrollBar::handle:horizontal {
        background: #c1c1c1;
        min-width: 20px;
        border-radius: 5px;
    }
    QScrollBar::handle:horizontal:hover {
        background: #a8a8a8;
    }
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
        width: 0px;
    }
"""

TAB_BUTTON_STYLE = """
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

DELETE_BUTTON_STYLE = "background-color: #dc3545; color: white; border: 1px solid #bd2130; padding: 10px; border-radius: 6px;"
