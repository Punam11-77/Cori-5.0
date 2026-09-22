import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)


class ABBEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ABB Rapid Editor")
        self.resize(1200, 700)

        self.setStyleSheet("""
            QWidget{
                background-color:#f5f7fa;
                font-size:14px;
            }
        """)

        main_layout = QVBoxLayout()

        # Header
        title = QLabel("ABB Rapid Editor")
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            padding:10px;
        """)

        # RAPID PROGRAM PANEL
        rapid_title = QLabel("RAPID PROGRAM")
        rapid_title.setStyleSheet("font-weight:bold;")

        rapid_list = QListWidget()
        rapid_list.addItems([
            "MoveJ pHome",
            "MoveL pPick",
            "ArcLOn",
            "ArcLOff",
            "MoveJ pSafe",
            "MoveL pPlace"
        ])
        rapid_list.setCurrentRow(0)

        rapid_list.setStyleSheet("""
            QListWidget{
                background:white;
                border:2px solid #d9d9d9;
            }

            QListWidget::item:selected{
                background:#0078D4;
                color:white;
            }
        """)

        rapid_layout = QVBoxLayout()
        rapid_layout.addWidget(rapid_title)
        rapid_layout.addWidget(rapid_list)

        # COMMAND PANEL
        command_title = QLabel("COMMANDS")
        command_title.setStyleSheet("font-weight:bold;")

        command_list = QListWidget()
        command_list.addItems([
            "INSERT",
            "TOUCH-UP",
            "DELETE",
            "EXPORT"
        ])

        command_list.setCurrentRow(0)

        command_list.setStyleSheet("""
            QListWidget{
                background:white;
                border:2px solid #d9d9d9;
            }

            QListWidget::item:selected{
                background:#0078D4;
                color:white;
            }
        """)

        command_layout = QVBoxLayout()
        command_layout.addWidget(command_title)
        command_layout.addWidget(command_list)

        # DETAILS PANEL
        details_title = QLabel("ACTION DETAILS")
        details_title.setStyleSheet("font-weight:bold;")

        details = QLabel(
            "Selected Command: INSERT\n\n"
            "Description:\n"
            "Insert a new RAPID instruction."
        )

        details.setStyleSheet("""
            background:white;
            border:2px solid #d9d9d9;
            padding:15px;
        """)

        details_layout = QVBoxLayout()
        details_layout.addWidget(details_title)
        details_layout.addWidget(details)

        # CONTENT AREA
        content_layout = QHBoxLayout()
        content_layout.addLayout(rapid_layout)
        content_layout.addLayout(command_layout)
        content_layout.addLayout(details_layout)

        # BUTTONS
        b1 = QPushButton("B1 Navigation")
        b2 = QPushButton("B2 Navigation")
        b3 = QPushButton("EXECUTE")

        b1.setStyleSheet("""
            QPushButton{
                background:#2563EB;
                color:white;
                padding:10px;
            }
        """)

        b2.setStyleSheet("""
            QPushButton{
                background:#2563EB;
                color:white;
                padding:10px;
            }
        """)

        b3.setStyleSheet("""
            QPushButton{
                background:#22C55E;
                color:white;
                font-weight:bold;
                padding:10px;
                border-radius:6px;
            }
        """)

        button_layout = QHBoxLayout()
        button_layout.addWidget(b1)
        button_layout.addWidget(b2)
        button_layout.addWidget(b3)

        # ADD ALL TO MAIN LAYOUT
        main_layout.addWidget(title)
        main_layout.addLayout(content_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)


app = QApplication(sys.argv)

window = ABBEditor()
window.show()

sys.exit(app.exec())