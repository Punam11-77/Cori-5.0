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

        # Current screen
        self.screen = "command_menu"

        # Current INSERT action
        self.action_index = 0

        # Command descriptions
        self.command_descriptions = {
            "INSERT": "Insert a new RAPID instruction.",
            "TOUCH-UP": "Update robot target position.",
            "DELETE": "Delete selected RAPID instruction.",
            "EXPORT": "Export RAPID program."
        }

        # INSERT menu actions
        self.insert_actions = [
            "MOVJ",
            "MOVL",
            "ARCLON",
            "ARCLOFF",
            "Cancel"
        ]

        # --------------------------------------------------
        # WINDOW STYLE
        # --------------------------------------------------

        self.setStyleSheet("""
            QWidget {
                background-color: #f5f7fa;
                font-size: 18px;
            }
        """)

        # --------------------------------------------------
        # MAIN LAYOUT
        # --------------------------------------------------

        main_layout = QVBoxLayout()

        # --------------------------------------------------
        # TITLE
        # --------------------------------------------------

        title = QLabel("ABB Rapid Editor")

        title.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
            padding: 10px;
        """)

        main_layout.addWidget(title)

        # --------------------------------------------------
        # RAPID PROGRAM
        # --------------------------------------------------

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

        # --------------------------------------------------
        # COMMANDS
        # --------------------------------------------------

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

        # --------------------------------------------------
        # ACTION DETAILS
        # --------------------------------------------------

        details_title = QLabel("ACTION DETAILS")

        details_title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
        """)

        self.details = QLabel()

        self.details.setWordWrap(True)

        self.details.setStyleSheet("""
            QLabel {
                background: white;
                border: 2px solid #d9d9d9;
                padding: 20px;
            }
        """)

        details_layout = QVBoxLayout()

        details_layout.addWidget(details_title)
        details_layout.addWidget(self.details)

        # --------------------------------------------------
        # CONTENT LAYOUT
        # --------------------------------------------------

        content_layout = QHBoxLayout()

        content_layout.addLayout(rapid_layout, 4)
        content_layout.addLayout(command_layout, 3)
        content_layout.addLayout(details_layout, 3)

        main_layout.addLayout(content_layout)

        # --------------------------------------------------
        # BUTTONS
        # --------------------------------------------------

        b1 = QPushButton("B1 ↑")
        b2 = QPushButton("B2 ↓")
        b3 = QPushButton("B3 SELECT")

        blue_style = """
            QPushButton {
                background: #2563EB;
                color: white;
                font-weight: bold;
                padding: 15px;
                border-radius: 5px;
            }

            QPushButton:hover {
                background: #1D4ED8;
            }
        """

        green_style = """
            QPushButton {
                background: #22C55E;
                color: white;
                font-weight: bold;
                padding: 15px;
                border-radius: 5px;
            }

            QPushButton:hover {
                background: #16A34A;
            }
        """

        b1.setStyleSheet(blue_style)
        b2.setStyleSheet(blue_style)
        b3.setStyleSheet(green_style)

        button_layout = QHBoxLayout()

        button_layout.addWidget(b1)
        button_layout.addWidget(b2)
        button_layout.addWidget(b3)

        main_layout.addLayout(button_layout)

        # --------------------------------------------------
        # STATUS
        # --------------------------------------------------

        self.status_label = QLabel("Mode: Command Selection")

        self.status_label.setStyleSheet("""
            QLabel {
                font-weight: bold;
                padding: 10px;
            }
        """)

        main_layout.addWidget(self.status_label)

        # Set layout
        self.setLayout(main_layout)

        # --------------------------------------------------
        # SIGNALS
        # --------------------------------------------------

        self.command_list.currentTextChanged.connect(
            self.update_details
        )

        self.rapid_list.currentTextChanged.connect(
            self.update_rapid_details
        )

        b1.clicked.connect(self.move_up)
        b2.clicked.connect(self.move_down)
        b3.clicked.connect(self.select_action)

        # Initial display
        self.update_details("INSERT")

    # ======================================================
    # UPDATE RAPID DETAILS
    # ======================================================

    def update_rapid_details(self, text):

        current_command = self.command_list.currentItem()

        if current_command:
            self.update_details(
                current_command.text()
            )

    # ======================================================
    # UPDATE DETAILS
    # ======================================================

    def update_details(self, command):

        # --------------------------------------------------
        # COMMAND MENU
        # --------------------------------------------------

        if self.screen == "command_menu":

            selected_item = self.rapid_list.currentItem()

            if selected_item:
                selected_line = selected_item.text()
            else:
                selected_line = "No line selected"

            description = self.command_descriptions.get(
                command,
                ""
            )

            self.details.setText(
                f"Selected Line:\n"
                f"{selected_line}\n\n"
                f"Selected Command:\n"
                f"{command}\n\n"
                f"{description}"
            )

        # --------------------------------------------------
        # INSERT MENU
        # --------------------------------------------------

        elif self.screen == "insert_menu":

            text = "INSERT ACTIONS\n\n"

            for i, item in enumerate(self.insert_actions):

                if i == self.action_index:
                    text += f"[ {item} ]\n"
                else:
                    text += f"{item}\n"

            self.details.setText(text)

        # --------------------------------------------------
        # RECORD SCREEN
        # --------------------------------------------------

        elif self.screen == "record_screen":

            current_action = self.insert_actions[
                self.action_index
            ]

            self.details.setText(
                "Press SELECT to record\n\n"
                f"[ {current_action} ]"
            )

    # ======================================================
    # MOVE UP
    # ======================================================

    def move_up(self):

        # INSERT MENU
        if self.screen == "insert_menu":

            if self.action_index > 0:
                self.action_index -= 1

            self.update_details("INSERT")

            return

        # COMMAND MENU
        row = self.command_list.currentRow()

        if row > 0:
            self.command_list.setCurrentRow(
                row - 1
            )

    # ======================================================
    # MOVE DOWN
    # ======================================================

    def move_down(self):

        # INSERT MENU
        if self.screen == "insert_menu":

            if self.action_index < len(
                self.insert_actions
            ) - 1:

                self.action_index += 1

            self.update_details("INSERT")

            return

        # COMMAND MENU
        row = self.command_list.currentRow()

        if row < self.command_list.count() - 1:

            self.command_list.setCurrentRow(
                row + 1
            )

    # ======================================================
    # SELECT BUTTON
    # ======================================================

    def select_action(self):

        current_command = self.command_list.currentItem()

        if current_command is None:
            return

        command = current_command.text()

        # ==================================================
        # INSERT
        # ==================================================

        if command == "INSERT":

            # ----------------------------------------------
            # COMMAND MENU -> INSERT MENU
            # ----------------------------------------------

            if self.screen == "command_menu":

                self.screen = "insert_menu"

                self.action_index = 0

                self.status_label.setText(
                    "Mode: INSERT Action Menu"
                )

                self.update_details("INSERT")

                return

            # ----------------------------------------------
            # INSERT MENU -> RECORD SCREEN
            # ----------------------------------------------

            elif self.screen == "insert_menu":

                selected = self.insert_actions[
                    self.action_index
                ]

                # Cancel
                if selected == "Cancel":

                    self.screen = "command_menu"

                    self.status_label.setText(
                        "Mode: Command Selection"
                    )

                    self.update_details("INSERT")

                    return

                # Select MOVJ / MOVL / ARCLON / ARCLOFF
                self.screen = "record_screen"

                self.status_label.setText(
                    f"Ready To Record: {selected}"
                )

                self.update_details("INSERT")

                return

            # ----------------------------------------------
            # RECORD SCREEN -> INSERT
            # ----------------------------------------------

            elif self.screen == "record_screen":

                selected = self.insert_actions[
                    self.action_index
                ]

                QMessageBox.information(
                    self,
                    "Success",
                    f"{selected} inserted successfully."
                )

                self.screen = "command_menu"

                self.status_label.setText(
                    "Mode: Command Selection"
                )

                self.update_details("INSERT")

                return

        # ==================================================
        # TOUCH-UP
        # ==================================================

        elif command == "TOUCH-UP":

            self.details.setText(
                "TOUCH-UP\n\n"
                "Press SELECT to record."
            )

            QMessageBox.information(
                self,
                "Success",
                "Touch-Up Executed Successfully!"
            )

            return

        # ==================================================
        # DELETE
        # ==================================================

        elif command == "DELETE":

            selected_item = self.rapid_list.currentItem()

            if selected_item is None:
                QMessageBox.warning(
                    self,
                    "Delete",
                    "No instruction selected."
                )
                return

            selected_line = selected_item.text()

            result = QMessageBox.question(
                self,
                "Confirm Delete",
                f"Delete this instruction?\n\n"
                f"{selected_line}",
                QMessageBox.StandardButton.Yes
                | QMessageBox.StandardButton.No
            )

            if result == QMessageBox.StandardButton.Yes:

                row = self.rapid_list.currentRow()

                self.rapid_list.takeItem(row)

                # Select another row if possible
                if self.rapid_list.count() > 0:

                    new_row = min(
                        row,
                        self.rapid_list.count() - 1
                    )

                    self.rapid_list.setCurrentRow(
                        new_row
                    )

                self.details.setText(
                    "DELETE\n\n"
                    "Instruction deleted successfully."
                )

                QMessageBox.information(
                    self,
                    "Success",
                    "Selected instruction deleted."
                )

            return

        # ==================================================
        # EXPORT
        # ==================================================

        elif command == "EXPORT":

            self.details.setText(
                "EXPORT\n\n"
                "Program exported successfully."
            )

            QMessageBox.information(
                self,
                "Success",
                "Program exported successfully."
            )

            return


# ==========================================================
# APPLICATION START
# ==========================================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = ABBEditor()

    window.show()

    sys.exit(app.exec())
