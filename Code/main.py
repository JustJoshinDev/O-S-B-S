from PySide6.QtWidgets import QFileDialog, QColorDialog, QMainWindow, QApplication
from PySide6.QtGui import QTextCharFormat, QFont, QTextCursor
import ui_main

class MyGUI(QMainWindow):  # Main window setup
    def __init__(self):         
        super(MyGUI, self).__init__()
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # Initialize default font settings
        self.ui.textSize.setValue(12)
        self.ui.fontSelect.setCurrentFont(QFont('Arial'))
        self.currentFormat = QTextCharFormat()  # Store current format
        
        self.setWindowTitle("Open Source Bible System v0.0")
        self.ui.textEdit.setAcceptRichText = True

        # Connect signals
        self.ui.textSize.valueChanged.connect(self.update_font_size)
        self.ui.fontSelect.currentFontChanged.connect(self.update_font_family)
        self.ui.colorButton.clicked.connect(self.choose_color)

        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)

    def save_file(self):
        #Saves a File to a custom ".osbn" File.
        options = QFileDialog.Option()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Open Source Bible Notes Files (*.osbn);;All Files (*)", options=options)
        if filename:
            with open(filename, "w") as f:
               f.write(self.ui.textEdit.toHtml())

    def open_file(self):
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
        self.ui.textSize.setValue(int(font_size) if font_size else 12)  # Set default if size isn't found

        # Update color in the UI (use the color button's stylesheet)
        color = char_format.foreground().color()
        if color.isValid():
            self.ui.colorButton.setStyleSheet(f"background-color: {color.name()};")

    def update_font_size(self):
        # Update font size only
        self.currentFormat.setFontPointSize(self.ui.textSize.value())
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

            self.ui.colorButton.setStyleSheet(f"background-color: {color.name()};") #Update color button

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()

if __name__ == '__main__':
    main()