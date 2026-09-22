import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)


class ABBEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ABB Rapid Editor")
        self.resize(1200, 700)

        self.command_descriptions = {
            "INSERT": "Insert a new RAPID instruction.",
            "TOUCH-UP": "Update robot target position.",
            "DELETE": "Delete selected RAPID instruction.",
            "EXPORT": "Export RAPID program."
        }

        self.setStyleSheet("""
            QWidget {
                background-color: #f5f7fa;
                font-size: 14px;
            }
        """)

        main_layout = QVBoxLayout()

        # HEADER
        title = QLabel("ABB Rapid Editor")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            padding: 10px;
        """)

        # RAPID PANEL
        rapid_title = QLabel("RAPID PROGRAM")
        rapid_title.setStyleSheet("font-weight: bold;")

        self.rapid_list = QListWidget()
        self.rapid_list.addItems([
            "MoveJ pHome",
            "MoveL pPick",
            "ArcLOn",
            "ArcLOff",
            "MoveJ pSafe",
            "MoveL pPlace"
        ])

        self.rapid_list.setCurrentRow(0)

        self.rapid_list.setStyleSheet("""
            QListWidget {
                background: white;
                border: 2px solid #d9d9d9;
            }

            QListWidget::item:selected {
                background: #0078D4;
                color: white;
            }
        """)

        rapid_layout = QVBoxLayout()
        rapid_layout.addWidget(rapid_title)
        rapid_layout.addWidget(self.rapid_list)

        # COMMAND PANEL
        command_title = QLabel("COMMANDS")
        command_title.setStyleSheet("font-weight: bold;")

        self.command_list = QListWidget()

        self.command_list.addItems([
            "INSERT",
            "TOUCH-UP",
            "DELETE",
            "EXPORT"
        ])

        self.command_list.setCurrentRow(0)

        self.command_list.setStyleSheet("""
            QListWidget {
                background: white;
                border: 2px solid #d9d9d9;
            }

            QListWidget::item:selected {
                background: #0078D4;
                color: white;
            }
        """)

        self.command_list.currentTextChanged.connect(
            self.update_details
        )

        command_layout = QVBoxLayout()
        command_layout.addWidget(command_title)
        command_layout.addWidget(self.command_list)

        # DETAILS PANEL
        details_title = QLabel("ACTION DETAILS")
        details_title.setStyleSheet("font-weight: bold;")

        self.details = QLabel(
            "Selected Command: INSERT\n\n"
            "Description:\n"
            "Insert a new RAPID instruction."
        )

        self.details.setStyleSheet("""
            background: white;
            border: 2px solid #d9d9d9;
            padding: 15px;
        """)

        details_layout = QVBoxLayout()
        details_layout.addWidget(details_title)
        details_layout.addWidget(self.details)

        # MAIN CONTENT
        content_layout = QHBoxLayout()

        content_layout.addLayout(rapid_layout, 4)
        content_layout.addLayout(command_layout, 3)
        content_layout.addLayout(details_layout, 2)

        # BUTTONS
        b1 = QPushButton("B1 Navigation")
        b2 = QPushButton("B2 Navigation")
        b3 = QPushButton("EXECUTE")

        b1.setStyleSheet("""
            QPushButton {
                background: #2563EB;
                color: white;
                padding: 10px;
            }
        """)

        b2.setStyleSheet("""
            QPushButton {
                background: #2563EB;
                color: white;
                padding: 10px;
            }
        """)

        b3.setStyleSheet("""
            QPushButton {
                background: #22C55E;
                color: white;
                font-weight: bold;
                padding: 10px;
                border-radius: 6px;
            }
        """)

        b3.clicked.connect(self.execute_command)

        button_layout = QHBoxLayout()
        button_layout.addWidget(b1)
        button_layout.addWidget(b2)
        button_layout.addWidget(b3)

        # ADD TO WINDOW
        main_layout.addWidget(title)
        main_layout.addLayout(content_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def update_details(self, command):

        description = self.command_descriptions.get(
            command,
            "No description available."
        )

        self.details.setText(
            f"Selected Command: {command}\n\n"
            f"Description:\n{description}"
        )

    def execute_command(self):

        command = self.command_list.currentItem().text()

        QMessageBox.information(
            self,
            "Success",
            f"{command} Executed Successfully!"
        )


app = QApplication(sys.argv)

window = ABBEditor()
window.show()

sys.exit(app.exec())