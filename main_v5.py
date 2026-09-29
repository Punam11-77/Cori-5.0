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

        self.active_panel = "commands"

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

        # RAPID PANEL
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

            QListWidget::item:hover {
                background: #dbeafe;
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
        command_title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
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

            QListWidget::item:hover {
                background: #dbeafe;
            }

            QListWidget::item:selected {
                background: #0078D4;
                color: white;
            }
        """)

        command_layout = QVBoxLayout()
        command_layout.addWidget(command_title)
        command_layout.addWidget(self.command_list)

        # ACTION DETAILS
        details_title = QLabel("ACTION DETAILS")
        details_title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
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

        # CONTENT
        content_layout = QHBoxLayout()

        content_layout.addLayout(rapid_layout, 4)
        content_layout.addLayout(command_layout, 3)
        content_layout.addLayout(details_layout, 3)

        # BUTTONS
        b1 = QPushButton("B1 ↑")
        b2 = QPushButton("B2 ↓")
        b3 = QPushButton("B3 SELECT")

        blue_style = """
        QPushButton{
            background:#2563EB;
            color:white;
            font-weight:bold;
            padding:15px;
        }
        """

        b1.setStyleSheet(blue_style)
        b2.setStyleSheet(blue_style)

        b3.setStyleSheet("""
        QPushButton{
            background:#22C55E;
            color:white;
            font-weight:bold;
            padding:15px;
        }
        """)

        button_layout = QHBoxLayout()
        button_layout.addWidget(b1)
        button_layout.addWidget(b2)
        button_layout.addWidget(b3)

        self.status_label = QLabel(
            "Mode: Command Selection"
        )

        self.status_label.setStyleSheet("""
            font-weight:bold;
            padding:10px;
        """)

        main_layout.addWidget(title)
        main_layout.addLayout(content_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.status_label)

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

        b1.clicked.connect(self.move_up)
        b2.clicked.connect(self.move_down)
        b3.clicked.connect(self.select_action)

        self.update_details("INSERT")

    def update_details(self, command):

        selected_line = self.rapid_list.currentItem().text()

        description = self.command_descriptions.get(
            command,
            "No description available."
        )

        self.details.setText(
            f"Active Panel: {self.active_panel.upper()}\n\n"
            f"Selected Line:\n{selected_line}\n\n"
            f"Selected Command:\n{command}\n\n"
            f"Description:\n{description}"
        )

    def move_up(self):

        if self.active_panel == "commands":

            row = self.command_list.currentRow()

            if row > 0:
                self.command_list.setCurrentRow(row - 1)

        else:

            row = self.rapid_list.currentRow()

            if row > 0:
                self.rapid_list.setCurrentRow(row - 1)

    def move_down(self):

        if self.active_panel == "commands":

            row = self.command_list.currentRow()

            if row < self.command_list.count() - 1:
                self.command_list.setCurrentRow(row + 1)

        else:

            row = self.rapid_list.currentRow()

            if row < self.rapid_list.count() - 1:
                self.rapid_list.setCurrentRow(row + 1)

    def select_action(self):

        if self.active_panel == "commands":

            command = self.command_list.currentItem().text()

            self.status_label.setText(
                f"Selected Command: {command} | Select RAPID Line"
            )

            self.active_panel = "rapid"

            self.update_details(command)

        else:

            line = self.rapid_list.currentItem().text()
            command = self.command_list.currentItem().text()

            QMessageBox.information(
                self,
                "Command Executed",
                f"Command: {command}\n\nApplied To:\n{line}"
            )

            self.active_panel = "commands"

            self.status_label.setText(
                "Mode: Command Selection"
            )

            self.update_details(command)


app = QApplication(sys.argv)

window = ABBEditor()
window.show()

sys.exit(app.exec())