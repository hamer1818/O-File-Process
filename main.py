import os
import shutil
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, 
    QLineEdit, QListWidget, QHBoxLayout, QMessageBox, QButtonGroup
)
from PyQt6.QtCore import QTranslator, QLocale
from PyQt6.QtGui import QIcon, QFont

class FileProcessorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.translations = {
            'en': {
                'window_title': 'O File Processor',
                'selected_folder': 'Selected Folder: ',
                'none': 'None',
                'select_folder': 'Select Folder',
                'filter_label': 'Filter Files (e.g., "english"):',
                'apply_filter': 'Apply Filter',
                'rename_placeholder': 'Rename: Replace "old" with "new"',
                'rename_btn': 'Rename Files',
                'copy_btn': 'Copy and Rename Files',
                'warning': 'Warning',
                'success': 'Success',
                'no_folder': 'No folder selected.',
                'enter_filter': 'Please enter a filter text.',
                'enter_pattern': 'Please enter a valid rename pattern (e.g., "english turkish").',
                'files_renamed': 'Files renamed successfully.',
                'files_copied': 'Files copied and renamed successfully.',
                'help_text': 'Instructions:\n\n1. Select a folder using the "Select Folder" button\n2. Use the filter to search for specific files\n3. To rename files, enter the text to replace in format: "old new"\n4. Click "Rename Files" to rename or "Copy and Rename" to create copies',
                'language': 'English',
                'clear_filter': 'Clear Filter',
                'delete_files': 'Delete Files',
                'delete_placeholder': 'Enter text to find files to delete (e.g., "en")',
                'delete_warning': 'Warning! This will permanently delete all files containing "{}" in their names.\n\nFound {} files to delete:\n\n{}\n\nDo you want to continue?',
                'no_matching_files': 'No files found containing "{}"',
                'files_deleted': '{} files have been deleted successfully.',
            },
            'tr': {
                'window_title': 'O File Processor',
                'selected_folder': 'Seçilen Klasör: ',
                'none': 'Yok',
                'select_folder': 'Klasör Seç',
                'filter_label': 'Dosyaları Filtrele (örn: "english"):',
                'apply_filter': 'Filtreyi Uygula',
                'rename_placeholder': 'Yeniden Adlandır: "eski" yi "yeni" ile değiştir',
                'rename_btn': 'Dosyaları Yeniden Adlandır',
                'copy_btn': 'Kopyala ve Yeniden Adlandır',
                'warning': 'Uyarı',
                'success': 'Başarılı',
                'no_folder': 'Klasör seçilmedi.',
                'enter_filter': 'Lütfen filtre metni girin.',
                'enter_pattern': 'Lütfen geçerli bir yeniden adlandırma deseni girin (örn: "english turkish").',
                'files_renamed': 'Dosyalar başarıyla yeniden adlandırıldı.',
                'files_copied': 'Dosyalar başarıyla kopyalandı ve yeniden adlandırıldı.',
                'help_text': 'Kullanım Talimatları:\n\n1. "Klasör Seç" düğmesini kullanarak bir klasör seçin\n2. Belirli dosyaları aramak için filtreyi kullanın\n3. Dosyaları yeniden adlandırmak için metni şu formatta girin: "eski yeni"\n4. Yeniden adlandırmak için "Dosyaları Yeniden Adlandır" veya kopya oluşturmak için "Kopyala ve Yeniden Adlandır" a tıklayın',
                'language': 'Türkçe',
                'clear_filter': 'Filtreyi Temizle',
                'delete_files': 'Dosyaları Sil',
                'delete_placeholder': 'Silinecek dosyaları bulmak için metin girin (örn: "en")',
                'delete_warning': 'Uyarı! Bu işlem, adında "{}" içeren tüm dosyaları kalıcı olarak silecektir.\n\nSilinecek {} dosya bulundu:\n\n{}\n\nDevam etmek istiyor musunuz?',
                'no_matching_files': '"{}" içeren dosya bulunamadı',
                'files_deleted': '{} dosya başarıyla silindi.',
            },
            'az': {
                'window_title': 'O File Processor',
                'selected_folder': 'Seçilmiş Qovluq: ',
                'none': 'Yox',
                'select_folder': 'Qovluq Seç',
                'filter_label': 'Faylları Filtrələ (məs: "english"):',
                'apply_filter': 'Filtri Tətbiq Et',
                'rename_placeholder': 'Yenidən Adlandır: "köhnə" ni "yeni" ilə əvəz et',
                'rename_btn': 'Faylları Yenidən Adlandır',
                'copy_btn': 'Kopyala və Yenidən Adlandır',
                'warning': 'Xəbərdarlıq',
                'success': 'Uğurlu',
                'no_folder': 'Qovluq seçilməyib.',
                'enter_filter': 'Zəhmət olmasa filtr mətni daxil edin.',
                'enter_pattern': 'Zəhmət olmasa düzgün yenidən adlandırma nümunəsi daxil edin (məs: "english turkish").',
                'files_renamed': 'Fayllar uğurla yenidən adlandırıldı.',
                'files_copied': 'Fayllar uğurla kopyalandı və yenidən adlandırıldı.',
                'help_text': 'İstifadə Təlimatları:\n\n1. "Qovluq Seç" düyməsini istifadə edərək bir qovluq seçin\n2. Xüsusi faylları axtarmaq üçün filtrdən istifadə edin\n3. Faylları yenidən adlandırmaq üçün mətni bu formatda daxil edin: "köhnə yeni"\n4. Yenidən adlandırmaq üçün "Faylları Yenidən Adlandır" və ya kopya yaratmaq üçün "Kopyala və Yenidən Adlandır" düyməsinə klikləyin',
                'language': 'Azərbaycanca',
                'clear_filter': 'Filtri Təmizlə',
                'delete_files': 'Faylları Sil',
                'delete_placeholder': 'Silinecek faylları bulmak için metin girin (məs: "en")',
                'delete_warning': 'Uyarı! Bu işlem, adında "{}" içeren tüm faylları kalıcı olarak silecektir.\n\nSilinecek {} fayl bulundu:\n\n{}\n\nDevam etmek istiyor musunuz?',
                'no_matching_files': '"{}" içeren fayl bulunamadı',
                'files_deleted': '{} fayl başarıyla silindi.',
            },
            'es': {
                'window_title': 'O File Processor',
                'selected_folder': 'Carpeta Seleccionada: ',
                'none': 'Ninguna',
                'select_folder': 'Seleccionar Carpeta',
                'filter_label': 'Filtrar Archivos (ej: "english"):',
                'apply_filter': 'Aplicar Filtro',
                'rename_placeholder': 'Renombrar: Reemplazar "viejo" con "nuevo"',
                'rename_btn': 'Renombrar Archivos',
                'copy_btn': 'Copiar y Renombrar Archivos',
                'warning': 'Advertencia',
                'success': 'Éxito',
                'no_folder': 'No se ha seleccionado ninguna carpeta.',
                'enter_filter': 'Por favor, ingrese un texto de filtro.',
                'enter_pattern': 'Por favor, ingrese un patrón de renombrado válido (ej: "english turkish").',
                'files_renamed': 'Archivos renombrados exitosamente.',
                'files_copied': 'Archivos copiados y renombrados exitosamente.',
                'help_text': 'Instrucciones:\n\n1. Seleccione una carpeta usando el botón "Seleccionar Carpeta"\n2. Use el filtro para buscar archivos específicos\n3. Para renombrar archivos, ingrese el texto a reemplazar en formato: "viejo nuevo"\n4. Haga clic en "Renombrar Archivos" para renombrar o "Copiar y Renombrar" para crear copias',
                'language': 'Español',
                'clear_filter': 'Limpiar Filtro',
                'delete_files': 'Eliminar Archivos',
                'delete_placeholder': 'Ingrese texto para encontrar archivos para eliminar (e.g., "en")',
                'delete_warning': 'Advertencia! Esto eliminará permanentemente todos los archivos que contengan "{}" en su nombre.\n\nSe encontraron {} archivos para eliminar:\n\n{}\n\n¿Quiere continuar?',
                'no_matching_files': 'No se encontraron archivos que contengan "{}"',
                'files_deleted': '{} archivos han sido eliminados exitosamente.',
            },
            'ru': {
                'window_title': 'O File Processor',
                'selected_folder': 'Выбранная Папка: ',
                'none': 'Нет',
                'select_folder': 'Выбрать Папку',
                'filter_label': 'Фильтровать Файлы (напр: "english"):',
                'apply_filter': 'Применить Фильтр',
                'rename_placeholder': 'Переименовать: Заменить "старое" на "новое"',
                'rename_btn': 'Переименовать Файлы',
                'copy_btn': 'Копировать и Переименовать',
                'warning': 'Предупреждение',
                'success': 'Успех',
                'no_folder': 'Папка не выбрана.',
                'enter_filter': 'Пожалуйста, введите текст для фильтра.',
                'enter_pattern': 'Пожалуйста, введите правильный шаблон переименования (напр: "english turkish").',
                'files_renamed': 'Файлы успешно переименованы.',
                'files_copied': 'Файлы успешно скопированы и переименованы.',
                'help_text': 'Инструкции:\n\n1. Выберите папку, используя кнопку "Выбрать Папку"\n2. Используйте фильтр для поиска конкретных файлов\n3. Для переименования файлов введите текст для замены в формате: "старое новое"\n4. Нажмите "Переименовать Файлы" для переименования или "Копировать и Переименовать" для создания копий',
                'language': 'Русский',
                'clear_filter': 'Очистить Фильтр',
                'delete_files': 'Удалить Файлы',
                'delete_placeholder': 'Введите текст для поиска файлов для удаления (например: "en")',
                'delete_warning': 'Предупреждение! Это действие удалит все файлы, содержащие "{}" в названии.\n\nНайдено {} файлов для удаления:\n\n{}\n\nВы действительно хотите продолжить?',
                'no_matching_files': 'Файлов, содержащих "{}", не найдено',
                'files_deleted': '{} файлов успешно удалены.',
            },
            'zh': {
                'window_title': 'O File Processor',
                'selected_folder': '已选择文件夹：',
                'none': '无',
                'select_folder': '选择文件夹',
                'filter_label': '过滤文件（例如："english"）：',
                'apply_filter': '应用过滤器',
                'rename_placeholder': '重命名：将"旧"替换为"新"',
                'rename_btn': '重命名文件',
                'copy_btn': '复制并重命名文件',
                'warning': '警告',
                'success': '成功',
                'no_folder': '未选择文件夹。',
                'enter_filter': '请输入过滤文本。',
                'enter_pattern': '请输入有效的重命名模式（例如："english turkish"）。',
                'files_renamed': '文件重命名成功。',
                'files_copied': '文件复制并重命名成功。',
                'help_text': '使用说明：\n\n1. 使用"选择文件夹"按钮选择一个文件夹\n2. 使用过滤器搜索特定文件\n3. 要重命名文件，请按以下格式输入文本："旧 新"\n4. 点击"重命名文件"进行重命名或点击"复制并重命名"创建副本',
                'language': '中文',
                'clear_filter': '清除过滤器',
                'delete_files': '删除文件',
                'delete_placeholder': '输入文本以查找要删除的文件 (例如："en")',
                'delete_warning': '警告！这将永久删除所有包含"{}"的文件。\n\n找到{}个要删除的文件：\n\n{}\n\n确定要继续吗？',
                'no_matching_files': '没有找到包含"{}"的文件',
                'files_deleted': '{}个文件已成功删除。',
            }
        }
        
        self.current_language = 'en'
        self.setup_ui()
        self.update_translations()

    def setup_ui(self):
        self.setGeometry(100, 100, 800, 600)
        self.setFont(QFont('Arial', 10))

        # Layouts
        self.layout = QVBoxLayout()
        self.language_layout = QHBoxLayout()
        self.filter_layout = QHBoxLayout()

        # Language buttons
        self.language_group = QButtonGroup()
        self.language_group.buttonClicked.connect(self.change_language)
        
        languages = [
            ('English', 'en'), ('Türkçe', 'tr'), ('Azərbaycanca', 'az'),
            ('Español', 'es'), ('Русский', 'ru'), ('中文', 'zh')
        ]
        
        for lang_name, lang_code in languages:
            btn = QPushButton(lang_name)
            btn.setCheckable(True)
            btn.setProperty('lang_code', lang_code)
            if lang_code == self.current_language:
                btn.setChecked(True)
            self.language_layout.addWidget(btn)
            self.language_group.addButton(btn)

        self.layout.addLayout(self.language_layout)

        # Help text
        self.help_label = QLabel()
        self.help_label.setWordWrap(True)
        self.layout.addWidget(self.help_label)

        # Folder selection
        self.folder_label = QLabel()
        self.layout.addWidget(self.folder_label)

        self.select_folder_btn = QPushButton()
        self.select_folder_btn.clicked.connect(self.select_folder)
        self.layout.addWidget(self.select_folder_btn)

        # File list
        self.file_list = QListWidget()
        self.layout.addWidget(self.file_list)

        # Filter
        self.filter_label = QLabel()
        self.filter_input = QLineEdit()
        self.filter_btn = QPushButton()
        self.filter_btn.clicked.connect(self.filter_files)

        self.filter_layout.addWidget(self.filter_label)
        self.filter_layout.addWidget(self.filter_input)
        self.filter_layout.addWidget(self.filter_btn)
        self.layout.addLayout(self.filter_layout)

        # Rename
        self.rename_input = QLineEdit()
        self.layout.addWidget(self.rename_input)

        self.rename_btn = QPushButton()
        self.rename_btn.clicked.connect(self.rename_files)
        self.layout.addWidget(self.rename_btn)

        self.copy_btn = QPushButton()
        self.copy_btn.clicked.connect(self.copy_and_rename_files)
        self.layout.addWidget(self.copy_btn)

        # Filter layout'a temizleme butonu ekleme
        self.clear_filter_btn = QPushButton()
        self.clear_filter_btn.clicked.connect(self.clear_filter)
        self.filter_layout.addWidget(self.clear_filter_btn)

        # Dosya silme bölümü
        self.delete_layout = QHBoxLayout()
        
        self.delete_input = QLineEdit()
        self.delete_btn = QPushButton()
        self.delete_btn.clicked.connect(self.delete_files)
        
        self.delete_layout.addWidget(self.delete_input)
        self.delete_layout.addWidget(self.delete_btn)
        
        self.layout.addLayout(self.delete_layout)

        self.setLayout(self.layout)
        self.selected_folder = None

    def change_language(self, button):
        self.current_language = button.property('lang_code')
        self.update_translations()

    def update_translations(self):
        texts = self.translations[self.current_language]
        self.setWindowTitle(texts['window_title'])
        self.folder_label.setText(f"{texts['selected_folder']}{texts['none']}")
        self.select_folder_btn.setText(texts['select_folder'])
        self.filter_label.setText(texts['filter_label'])
        self.filter_btn.setText(texts['apply_filter'])
        self.rename_input.setPlaceholderText(texts['rename_placeholder'])
        self.rename_btn.setText(texts['rename_btn'])
        self.copy_btn.setText(texts['copy_btn'])
        self.help_label.setText(texts['help_text'])
        self.clear_filter_btn.setText(texts['clear_filter'])
        self.delete_input.setPlaceholderText(texts['delete_placeholder'])
        self.delete_btn.setText(texts['delete_files'])

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, self.translations[self.current_language]['select_folder'])
        if folder:
            self.selected_folder = folder
            self.folder_label.setText(f"{self.translations[self.current_language]['selected_folder']}{folder}")
            self.list_files()

    def list_files(self):
        if not self.selected_folder:
            return

        self.file_list.clear()
        for file_name in os.listdir(self.selected_folder):
            if os.path.isfile(os.path.join(self.selected_folder, file_name)):
                self.file_list.addItem(file_name)

    def filter_files(self):
        if not self.selected_folder:
            QMessageBox.warning(self, 
                self.translations[self.current_language]['warning'],
                self.translations[self.current_language]['no_folder'])
            return

        filter_text = self.filter_input.text()
        if not filter_text:
            QMessageBox.warning(self, 
                self.translations[self.current_language]['warning'],
                self.translations[self.current_language]['enter_filter'])
            return

        self.file_list.clear()
        for file_name in os.listdir(self.selected_folder):
            if os.path.isfile(os.path.join(self.selected_folder, file_name)) and filter_text.lower() in file_name.lower():
                self.file_list.addItem(file_name)

    def rename_files(self):
        if not self.selected_folder:
            QMessageBox.warning(self, 
                self.translations[self.current_language]['warning'],
                self.translations[self.current_language]['no_folder'])
            return

        rename_text = self.rename_input.text()
        if not rename_text or " " not in rename_text:
            QMessageBox.warning(self, 
                self.translations[self.current_language]['warning'],
                self.translations[self.current_language]['enter_pattern'])
            return

        old, new = rename_text.split(" ", 1)
        for i in range(self.file_list.count()):
            file_name = self.file_list.item(i).text()
            if old in file_name:
                old_path = os.path.join(self.selected_folder, file_name)
                new_name = file_name.replace(old, new)
                new_path = os.path.join(self.selected_folder, new_name)
                try:
                    os.rename(old_path, new_path)
                except Exception as e:
                    QMessageBox.warning(self, 
                        self.translations[self.current_language]['warning'],
                        str(e))
                    return

        QMessageBox.information(self, 
            self.translations[self.current_language]['success'],
            self.translations[self.current_language]['files_renamed'])
        self.list_files()

    def copy_and_rename_files(self):
        if not self.selected_folder:
            QMessageBox.warning(self, 
                self.translations[self.current_language]['warning'],
                self.translations[self.current_language]['no_folder'])
            return

        rename_text = self.rename_input.text()
        if not rename_text or " " not in rename_text:
            QMessageBox.warning(self, 
                self.translations[self.current_language]['warning'],
                self.translations[self.current_language]['enter_pattern'])
            return

        old, new = rename_text.split(" ", 1)
        for i in range(self.file_list.count()):
            file_name = self.file_list.item(i).text()
            if old in file_name:
                old_path = os.path.join(self.selected_folder, file_name)
                new_name = file_name.replace(old, new)
                new_path = os.path.join(self.selected_folder, new_name)
                try:
                    shutil.copy(old_path, new_path)
                except Exception as e:
                    QMessageBox.warning(self, 
                        self.translations[self.current_language]['warning'],
                        str(e))
                    return

        QMessageBox.information(self, 
            self.translations[self.current_language]['success'],
            self.translations[self.current_language]['files_copied'])
        self.list_files()

    def clear_filter(self):
        self.filter_input.clear()
        self.list_files()

    def delete_files(self):
        if not self.selected_folder:
            QMessageBox.warning(self, 
                self.translations[self.current_language]['warning'],
                self.translations[self.current_language]['no_folder'])
            return

        search_text = self.delete_input.text().strip()
        if not search_text:
            QMessageBox.warning(self, 
                self.translations[self.current_language]['warning'],
                self.translations[self.current_language]['enter_filter'])
            return

        # Find files to delete
        files_to_delete = []
        for file_name in os.listdir(self.selected_folder):
            if os.path.isfile(os.path.join(self.selected_folder, file_name)) and search_text.lower() in file_name.lower():
                files_to_delete.append(file_name)

        if not files_to_delete:
            QMessageBox.information(self, 
                self.translations[self.current_language]['warning'],
                self.translations[self.current_language]['no_matching_files'].format(search_text))
            return

        # Show confirmation message to user
        file_list_str = "\n".join(files_to_delete)
        reply = QMessageBox.question(self, 
            self.translations[self.current_language]['warning'],
            self.translations[self.current_language]['delete_warning'].format(
                search_text, len(files_to_delete), file_list_str
            ),
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            # Delete files
            for file_name in files_to_delete:
                try:
                    os.remove(os.path.join(self.selected_folder, file_name))
                except Exception as e:
                    QMessageBox.warning(self, 
                        self.translations[self.current_language]['warning'],
                        str(e))
                    return

            QMessageBox.information(self, 
                self.translations[self.current_language]['success'],
                self.translations[self.current_language]['files_deleted'].format(len(files_to_delete)))
            
            # Update file list
            self.list_files()
if __name__ == "__main__":
    app = QApplication([])
    window = FileProcessorApp()
    window.show()
    app.exec()