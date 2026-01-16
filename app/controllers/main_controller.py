import os
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from app.models.file_manager import FileManager
from app.utils.translations import TRANSLATIONS

class MainController:
    def __init__(self, view):
        self.view = view
        self.model = FileManager()
        self.current_folder = None
        
        # Connect Signals
        self.view.sidebar.folder_selected.connect(self.load_folder)
        self.view.sidebar.btn_select_folder.clicked.connect(self.select_folder_dialog)
        self.view.lang_combo.currentIndexChanged.connect(self.change_language)
        self.view.search_input.textChanged.connect(self.filter_files)
        
        # Action Center Signals
        # Action Center Signals
        self.view.action_center.btn_exec_rename.clicked.connect(self.rename_files)
        self.view.action_center.btn_exec_copy.clicked.connect(self.copy_files)
        self.view.action_center.btn_exec_delete.clicked.connect(self.delete_files)
        
        # Live Previews
        self.view.action_center.inp_rename_old.textChanged.connect(self.update_rename_preview)
        self.view.action_center.inp_copy_old.textChanged.connect(self.update_copy_preview)
        self.view.action_center.inp_delete.textChanged.connect(self.update_delete_preview)
        
        # Help
        self.view.action_center.btn_help.clicked.connect(self.show_help)

        # Initial State
        self.view.update_texts()

    def select_folder_dialog(self):
        folder = QFileDialog.getExistingDirectory(self.view, "Select Folder")
        if folder:
            self.load_folder(folder)

    def load_folder(self, folder_path):
        self.current_folder = folder_path
        self.view.lbl_current_folder.setText(folder_path)
        self.refresh_file_list()

    def refresh_file_list(self):
        if not self.current_folder:
            return
        filter_text = self.view.search_input.text()
        try:
            files_data = self.model.list_files(self.current_folder, filter_text)
            self.view.file_table.populate(files_data)
        except Exception as e:
            print(f"Error listing files: {e}")

    def filter_files(self):
        self.refresh_file_list()

    def change_language(self):
        idx = self.view.lang_combo.currentIndex()
        codes = ["en", "tr", "az", "es", "ru", "zh"]
        if idx < len(codes):
            self.view.current_language = codes[idx]
            self.view.update_texts()

    def show_help(self):
        t = TRANSLATIONS[self.view.current_language]
        msg = QMessageBox(self.view)
        msg.setWindowTitle(t['help_btn'])
        msg.setText(t['help_text'])
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def _show_message(self, title, text, icon="info"):
        msg = QMessageBox(self.view)
        msg.setWindowTitle(title)
        msg.setText(text)
        if icon == "warning":
            msg.setIcon(QMessageBox.Icon.Warning)
        else:
            msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def update_rename_preview(self):
        text = self.view.action_center.inp_rename_old.text()
        self._update_preview(text, self.view.action_center.lbl_rename_stats)

    def update_copy_preview(self):
        text = self.view.action_center.inp_copy_old.text()
        self._update_preview(text, self.view.action_center.lbl_copy_stats)

    def update_delete_preview(self):
        text = self.view.action_center.inp_delete.text()
        self._update_preview(text, self.view.action_center.lbl_delete_stats)

    def _update_preview(self, match_text, label_widget):
        if not self.current_folder or not match_text:
            label_widget.setText("")
            return
        
        # We can reuse get_files_to_delete for simple matching logic
        # Ideally, move the underlying logic to a generic 'find_files' in FileManager
        matches = self.model.get_files_to_delete(self.current_folder, match_text)
        count = len(matches)
        
        if count == 0:
            label_widget.setText("No matching files")
            label_widget.setStyleSheet("color: #dc3545; font-size: 12px; margin-bottom: 5px;")
        else:
            label_widget.setText(f"{count} matching files found")
            label_widget.setStyleSheet("color: #28a745; font-size: 12px; margin-bottom: 5px; font-weight: bold;")


    def rename_files(self):
        if not self.current_folder:
            t = TRANSLATIONS[self.view.current_language]
            self._show_message(t['warning'], t['no_folder'], "warning")
            return

        old_text = self.view.action_center.inp_rename_old.text()
        new_text = self.view.action_center.inp_rename_new.text()
        
        if not old_text:
            return

        count = self.model.rename_files(self.current_folder, old_text, new_text)
        self.refresh_file_list()
        
        t = TRANSLATIONS[self.view.current_language]
        self._show_message(t['success'], f"{count} {t['files_renamed']}")

    def copy_files(self):
        if not self.current_folder:
            return

        old_text = self.view.action_center.inp_copy_old.text()
        new_text = self.view.action_center.inp_copy_new.text()
        
        if not old_text:
            return

        count = self.model.copy_and_rename_files(self.current_folder, old_text, new_text)
        self.refresh_file_list()
        
        t = TRANSLATIONS[self.view.current_language]
        self._show_message(t['success'], f"{count} {t['files_copied']}")

    def delete_files(self):
        if not self.current_folder:
            return

        match_text = self.view.action_center.inp_delete.text()
        if not match_text:
            return

        t = TRANSLATIONS[self.view.current_language]
        
        # Confirmation
        files_to_delete = self.model.get_files_to_delete(self.current_folder, match_text)
        if not files_to_delete:
            self._show_message(t['warning'], t['no_match'], "warning")
            return

        confirm_msg = t['confirm_delete'].format(len(files_to_delete), match_text)
        reply = QMessageBox.question(self.view, t['warning'], confirm_msg, 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            count, _ = self.model.delete_files(self.current_folder, match_text)
            self.refresh_file_list()
            self._show_message(t['success'], t['files_deleted'].format(count))
