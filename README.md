# Cori-5.0
# ABB Rapid Editor

## Overview
CoRI5.0 is a robotics project under which ABB Rapid editor is focused on program interaction and command management using a user interface and PYQt6.

The current development phase focuses on designing and implementing in PYQt-6.

The given interface allows users to:

- View Rapid program instructions
- Browse through available commands
- Display the action details
- Simulate command execution

This work started with a Figma layout with wireframe prototype and was later implemented in PyQt6.

---

## UI Design Process

The initial user interface was designed in Figma to visualize the expected layout.

### Figma Components

The interface got divided into three phases:

1. Rapid program Panel
2. Commands Panel
3. Action Details Panel

This helped defining the navigation flow before implementation in PyQt5.

---

## PyQt6 implementation

The Figma design was translated into a PyQt6 desktop application.

### Current Features

- RAPID Program list display
- Command selection panel
- Dynamic Action details panel
- Selected RAPID instruction tracking
- Selected Command tracking
- Execute button with popup confirmation
- User-friendly layout with selective highlights

  ---

  ## Current Workflow

 1. Select a RAPID program instruction.
2. Select a command from the command list.
3. View action details.
4. Execute the selected action.

---

## Project Structure

```text
CoRI-5.0
│
├── main.py
├── main_v2.py
├── main_v3.py
├── README.md
└── screenshots/
