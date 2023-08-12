from pypdf import PdfReader
from conftest import path_resources
import os

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_open_pdf():
    pdf = PdfReader(os.path.join(path_resources, 'docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(pdf.pages)
    assert number_of_pages == 412

    page_403 = pdf.pages[402]
    page_403_text = page_403.extract_text()
    assert "CaptureFixture" in page_403_text