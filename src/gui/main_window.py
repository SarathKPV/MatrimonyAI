from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matrimony AI Agent")

        self.resize(900, 650)

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        title = QLabel("Matrimony AI Agent")

        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setStyleSheet("""
            font-size:26px;
            font-weight:bold;
            margin:20px;
        """)

        layout.addWidget(title)

        self.select_button = QPushButton("Select Girl Images")

        self.select_button.setFixedHeight(45)

        layout.addWidget(self.select_button)

        self.status = QLabel("Status : Ready")

        self.status.setStyleSheet("""
            font-size:16px;
            margin-top:20px;
        """)

        layout.addWidget(self.status)

        central.setLayout(layout)