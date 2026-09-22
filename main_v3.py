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
        self.resize(1400, 800)

        self.command_descriptions = {
            "INSERT": "Insert a new RAPID instruction.",
            "TOUCH-UP": "Update robot target position.",
            "DELETE": "Delete selected RAPID instruction.",
            "EXPORT": "Export RAPID program."
        }

        self.setStyleSheet("""
            QWidget {
                background-color: #f5f7fa;
                font-size: 18px;
            }
        """)

        main_layout = QVBoxLayout()

        # HEADER
        title = QLabel("ABB Rapid Editor")
        title.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
            padding: 10px;
        """)

        # LEFT PANEL
        rapid_title = QLabel("RAPID PROGRAM")
        rapid_title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
        """)

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

        # MIDDLE PANEL
        command_title = QLabel("COMMANDS")
        command_title.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
        """)

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

        command_layout = QVBoxLayout()
        command_layout.addWidget(command_title)
        command_layout.addWidget(self.command_list)

        # RIGHT PANEL
        details_title = QLabel("ACTION DETAILS")
        details_title.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
        """)

        self.details = QLabel()
        self.details.setStyleSheet("""
            background: white;
            border: 2px solid #d9d9d9;
            padding: 20px;
        """)

        details_layout = QVBoxLayout()
        details_layout.addWidget(details_title)
        details_layout.addWidget(self.details)

        # MAIN CONTENT
        content_layout = QHBoxLayout()

        content_layout.addLayout(rapid_layout, 4)
        content_layout.addLayout(command_layout, 3)
        content_layout.addLayout(details_layout, 3)

        # BUTTONS

        b1_up = QPushButton("B1 ▲")
        b1_down = QPushButton("B1 ▼")

        b2_up = QPushButton("B2 ▲")
        b2_down = QPushButton("B2 ▼")

        execute_btn = QPushButton("EXECUTE")

        blue_style = """
            QPushButton{
                background:#2563EB;
                color:white;
                font-weight:bold;
                padding:10px;
            }
        """

        b1_up.setStyleSheet(blue_style)
        b1_down.setStyleSheet(blue_style)
        b2_up.setStyleSheet(blue_style)
        b2_down.setStyleSheet(blue_style)

        execute_btn.setStyleSheet("""
            QPushButton{
                background:#22C55E;
                color:white;
                font-weight:bold;
                padding:12px;
                border-radius:8px;
            }
        """)

        button_layout = QHBoxLayout()

        button_layout.addWidget(b1_up)
        button_layout.addWidget(b1_down)

        button_layout.addSpacing(20)

        button_layout.addWidget(b2_up)
        button_layout.addWidget(b2_down)

        button_layout.addSpacing(20)

        button_layout.addWidget(execute_btn)

        main_layout.addWidget(title)
        main_layout.addLayout(content_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # SIGNALS

        self.command_list.currentTextChanged.connect(
            self.update_details
        )

        self.rapid_list.currentTextChanged.connect(
            lambda: self.update_details(
                self.command_list.currentItem().text()
            )
        )

        execute_btn.clicked.connect(
            self.execute_command
        )

        self.update_details("INSERT")

    def update_details(self, command):

        selected_line = self.rapid_list.currentItem().text()

        description = self.command_descriptions.get(
            command,
            "No description available."
        )

        self.details.setText(
            f"Selected Line:\n"
            f"{selected_line}\n\n"
            f"Selected Command:\n"
            f"{command}\n\n"
            f"Description:\n"
            f"{description}"
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