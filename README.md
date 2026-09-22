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

## Development Progress

### Version 1 (main.py)

Implemented:

- Initial ABB Rapid Editor window
- Rapid program panel
- Command panel
- Action Details panel
- Basic styling

### Version 2 (main_v2.py)

Implemented:

- Dynamic command description details
- Command selection updates
- Execute button operations
- Popup confirmation messages

### Version 3 (main_v3.py)

Implemented:

- Selected RAPID instructions tracking
- Selected command tracking
- Action details update
- Improved font styling
- B1 and B2 control buttons
- Improved UI styling

### Version 4 (main_v4.py)

Implemented:

- introduces interactive navigation controls
- B1 buttons now navigate the RAPID Program list
- B2 buttons navigate the Command list
- Action Details update dynamically according to the selected RAPID instruction and command
- Hover effects were added to improve usability

---

## Project Structure

```text
CoRI-5.0
│
├── README.md
├── main.py
├── main_v2.py
├── main_v3.py
│
└── screenshots
├── figma_wireframe.png
└── ui_v3.png
```

---

## User Interface Screenshots

### Figma WireFrame
<img width="1005" height="754" alt="image" src="https://github.com/user-attachments/assets/5c49a099-db28-4032-8503-2a7c7b6c405b" />

### Current PyQt6 Implementation
<img width="1889" height="986" alt="UI_v3" src="https://github.com/user-attachments/assets/65073d30-4d55-4270-8d95-742b04f74a46" />

### Upgraded implementation
<img width="1896" height="968" alt="Näyttökuva 2026-09-22 134304" src="https://github.com/user-attachments/assets/cd3c4c83-6002-4780-91b7-2934182f6c62" />

---

## Technologies Used

- Python 3
- PyQt6
- Figma

---

## Future Improvements

Planned improvement include:

- Functional B1 navigation
- Function B2 navigation
- Insert and delete instruction functionality
- Program export support
- Hover-based interactions
- RAPID file import and export
- ABB-inspired industrial theme
- Robot communication integration
- Advanced command management features

---

### Current Stable Version

main_v4.py




