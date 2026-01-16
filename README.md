# O File Processor

**O File Processor** is a modern, **PyQt6-based** desktop application for professional file management. Built with a clean **MVC architecture**, it offers batch renaming, copying, and secure deletion with an intuitive 3-panel interface.

[![GitHub](https://img.shields.io/badge/GitHub-hamer1818%2FO--File--Process-blue?logo=github)](https://github.com/hamer1818/O-File-Process)

---

## 🚀 Key Features

### 📁 Smart Folder Navigation
- **Quick Access Sidebar:** One-click access to Desktop, Documents, Downloads, Music, Pictures, and Videos
- **Custom Folder Selection:** Browse and select any directory on your system
- **Real-time File List:** Files displayed with name, type, size, and modification date

### 🔍 Live Search & Preview
- **Instant Filtering:** Search files as you type
- **Live Action Preview:** See exactly how many files will be affected before executing any action
- **Color-coded Feedback:** Green for matches found, red for no matches

### 📝 Batch Rename
- **Find & Replace:** Replace specific text in multiple file names at once
- **Preview Count:** Shows matching file count before renaming
- **Safe Operation:** Original files are renamed, not duplicated

### 📋 Copy & Rename
- **Preserve Originals:** Create copies with modified names
- **Simultaneous Operation:** Copy and rename in a single action
- **Ideal for Versioning:** Keep backups while creating new versions

### 🗑️ Secure Deletion
- **Pattern Matching:** Delete files containing specific text
- **Confirmation Dialog:** Lists all files before deletion
- **Warning System:** Clear alerts to prevent accidental deletion

### 🌍 Multi-Language Support (6 Languages)
| Language | Flag |
|----------|------|
| English | 🇬🇧 |
| Türkçe | 🇹🇷 |
| Azərbaycanca | 🇦🇿 |
| Español | 🇪🇸 |
| Русский | 🇷🇺 |
| 中文 | 🇨🇳 |

### ✨ Modern UI
- **3-Panel Layout:** Sidebar, File List, Action Center
- **Custom Scrollbar:** Sleek, modern scrollbar design
- **Responsive Design:** Minimum size constraints prevent UI breakage
- **Built-in Help:** Localized user manual accessible via Help button

---

## �️ Project Structure (MVC Architecture)

```
O-File-Process/
├── main.py                    # Application entry point
├── app/
│   ├── models/
│   │   └── file_manager.py    # File operations logic
│   ├── views/
│   │   ├── main_window.py     # Main window assembly
│   │   └── components/
│   │       ├── sidebar.py     # Left navigation panel
│   │       ├── file_table.py  # Center file list
│   │       ├── action_center.py # Right action panel
│   │       └── modern_button.py # Custom button widget
│   ├── controllers/
│   │   └── main_controller.py # Connects Model and View
│   └── utils/
│       ├── translations.py    # Multi-language strings
│       └── styles.py          # QSS stylesheets
└── requirements.txt
```

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/hamer1818/O-File-Process.git
cd O-File-Process
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

```bash
python main.py
```

### Quick Start:
1. **Select a folder** from the sidebar or use "Select Folder" button
2. **Search files** using the filter box (optional)
3. **Choose an action** from the right panel:
   - **Batch Rename:** Enter old text → new text → click Rename
   - **Copy & Rename:** Same as above, but creates copies
   - **Secure Delete:** Enter matching text → confirm deletion
4. **Check the preview** (shows matching file count) before executing

---

## ⚙️ Technical Details

| Component | Technology |
|-----------|------------|
| Language | Python 3.8+ |
| GUI Framework | PyQt6 |
| Architecture | MVC (Model-View-Controller) |
| File Operations | `os`, `shutil` |

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

*Developer: [Hamer1818](https://github.com/hamer1818)*