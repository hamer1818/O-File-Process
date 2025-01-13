def main():
    app = QApplication([])
    app.setWindowIcon(QIcon('logo.jpeg'))
    window = FileProcessorApp()
    window.show()
    app.exec()

if __name__ == "__main__":
    main() 