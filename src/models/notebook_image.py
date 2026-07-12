from dataclasses import dataclass
from pathlib import Path


@dataclass
class NotebookImage:
    file_path: Path

    @property
    def file_name(self) -> str:
        return self.file_path.name

    @property
    def status(self) -> str:
        return "Waiting for OCR"