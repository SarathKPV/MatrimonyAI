from pathlib import Path

from src.models.notebook_image import NotebookImage


class ImageService:

    def __init__(self):
        self.images = []

    def add_images(self, paths):
        for path in paths:
            image = NotebookImage(Path(path))
            self.images.append(image)

    def clear(self):
        self.images.clear()