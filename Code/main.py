from PySide6.QtWidgets import QFileDialog, QColorDialog, QMainWindow, QApplication
from PySide6.QtGui import QTextCharFormat, QFont, QTextCursor
from PySide6.QtCore import QUrl, QFile
import os.path
import ui_main

class MyGUI(QMainWindow):  # Main window setup
    def __init__(self):         
        super(MyGUI, self).__init__()
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.bible_versions = {
            "American Standard Version": os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db', 'asv.html'),
            "King James Version": os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db', 'kjv.html'),
        }
        
        # Initialize default font settings
        self.bible_size_value = 8
        self.ui.testSize.setValue(12)
        self.ui.fontSelect.setCurrentFont(QFont('Arial'))
        self.currentFormat = QTextCharFormat()  # Store current format

        # Initialize KJV Bible
        html_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db', 'kjv.html')
        if os.path.isfile(html_file_path) and os.access(html_file_path, os.R_OK):
            self.ui.webEngineView.load(QUrl.fromLocalFile(html_file_path))
            self.ui.webEngineView.setZoomFactor(8)
            self.ui.actionShow_Bible.setText("Hide Bible")
        else:
            print(f"File not found or not readable: {html_file_path}")

        self.setWindowTitle("Open Source Bible System v0.0.3")
        self.ui.textEdit.setAcceptRichText(True)

        # Connect signals
        self.ui.testSize.valueChanged.connect(self.update_font_size)
        self.ui.fontSelect.currentFontChanged.connect(self.update_font_family)
        self.ui.colorButton.clicked.connect(self.choose_color)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionShow_Bible.triggered.connect(self.toggle_bible_window)
        self.ui.bibleSizeUp.clicked.connect(lambda: self.update_bible_size(-1))
        self.ui.bibleSizeDown.clicked.connect(lambda: self.update_bible_size(1))
        self.ui.bibleSelection.currentTextChanged.connect(self.update_bible_version)
        self.ui.bibleSelection.textActivated.connect(self.load_custom_bible)
        
    def update_bible_version(self):
        if self.ui.bibleSelection.currentText() != "Custom HTML...":
            self.ui.webEngineView.load(QUrl.fromLocalFile(os.path.abspath(self.bible_versions[self.ui.bibleSelection.currentText()])))
            self.ui.webEngineView.setZoomFactor(8)
    
    def load_custom_bible(self):
        if self.ui.bibleSelection.currentText() == "Custom HTML...":
            file, _ = QFileDialog.getOpenFileName(self, "Open File", "", "HTML Files (*.html)")
            self.ui.webEngineView.load(QUrl.fromLocalFile(file))
            self.ui.webEngineView.setZoomFactor(8)
    
    def toggle_bible_window(self):
        # Hides and shows the built-in Bible reader.
        if self.ui.dockWidget_2.isHidden():
            self.ui.dockWidget_2.show()
            self.ui.actionShow_Bible.setText("Hide Bible")
        else:
            self.ui.dockWidget_2.hide()
            self.ui.actionShow_Bible.setText("Show Bible")

    def update_bible_size(self, zoom_value):
        # Sets the scale of the built in Bible reader.
        self.bible_size_value += zoom_value
        self.ui.webEngineView.setZoomFactor(10 / self.bible_size_value)

    def save_file(self):
        # Saves a File to a custom ".osbn" File.
        options = QFileDialog.Option()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Open Source Bible Notes Files (*.osbn);;All Files (*)", options=options)
        if filename:
            with open(filename, "w") as f:
               f.write(self.ui.textEdit.toHtml())

    def open_file(self):
        # Opens notes from a custom ".osbn" File.
        options = QFileDialog.Option()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Open Source Bible Notes Files (*.osbn);;All Files (*)", options=options)
        if filename:
            with open(filename, "r") as f:
                self.ui.textEdit.setHtml(f.read())
                
            self.update_format_ui()

    def update_format_ui(self):
        # Get the format of the first character in the document
        cursor = self.ui.textEdit.textCursor()
        cursor.movePosition(QTextCursor.Start)  # Move to end of document
        self.ui.textEdit.setTextCursor(cursor)
        char_format = cursor.charFormat()

        # Update font family in the UI
        font_family = char_format.font().family()
        self.ui.fontSelect.setCurrentFont(QFont(font_family))

        # Update font size in the UI
        font_size = char_format.fontPointSize()
        self.ui.testSize.setValue(int(font_size) if font_size else 12)  # Set default if size isn't found

        # Update color in the UI (use the color button's stylesheet)
        color = char_format.foreground().color()
        if color.isValid():
            self.ui.colorButton.setStyleSheet(f"background-color: {color.name()};")

    def update_font_size(self):
        # Update font size only
        self.currentFormat.setFontPointSize(self.ui.testSize.value())
        self.ui.textEdit.setCurrentCharFormat(self.currentFormat)

    def update_font_family(self):
        # Update font family only
        self.currentFormat.setFont(QFont(self.ui.fontSelect.currentText()))
        self.ui.textEdit.setCurrentCharFormat(self.currentFormat)

    def choose_color(self):
        # Open color dialog and set color if valid
        color = QColorDialog.getColor()
        if color.isValid():
            self.currentFormat.setForeground(color)  # Update only color
            self.ui.textEdit.setCurrentCharFormat(self.currentFormat)

            self.ui.colorButton.setStyleSheet(f"background-color: {color.name()};") # Update color button

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()

if __name__ == '__main__':
    main()