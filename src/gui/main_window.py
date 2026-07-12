from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QFileDialog,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matrimony AI Agent")

        self.resize(900, 700)

        self.image_paths = []

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        title = QLabel("Matrimony AI Agent")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            margin:15px;
        """)

        layout.addWidget(title)

        self.select_button = QPushButton("Select Notebook Images")
        self.select_button.setFixedHeight(45)
        self.select_button.clicked.connect(self.select_images)

        layout.addWidget(self.select_button)

        self.image_list = QListWidget()
        layout.addWidget(self.image_list)

        self.status_label = QLabel("Status : Ready")
        self.status_label.setStyleSheet("font-size:16px;")

        layout.addWidget(self.status_label)

        self.start_button = QPushButton("Start Processing")
        self.start_button.clicked.connect(self.start_processing)
        self.start_button.setFixedHeight(45)
        self.start_button.setEnabled(False)

        layout.addWidget(self.start_button)

        central_widget.setLayout(layout)

    def select_images(self):

        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select Notebook Images",
            "",
            "Images (*.jpg *.jpeg *.png)"
        )

        if not files:
            return

        self.image_paths = files

        self.image_list.clear()

        for image in self.image_paths:
            self.image_list.addItem(image)

        self.status_label.setText(
            f"Status : {len(self.image_paths)} notebook image(s) selected"
        )

        self.start_button.setEnabled(True)

    def start_processing(self):
        print("START BUTTON CLICKED")
        print("Image Paths:", self.image_paths)
        print("Number of Images:", len(self.image_paths))

        if not self.image_paths:
            self.status_label.setText("Status : No notebook images selected")
            print("No images selected!")
        return

        self.status_label.setText("Status : Starting OCR...")

        print("===================================")
        print("Selected Notebook Images")
        print("===================================")

        for image in self.image_paths:
            print(image)

        print("===================================")