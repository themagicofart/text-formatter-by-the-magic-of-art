from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5.QtGui import QPixmap, QPainter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class FileUtils:
    def __init__(self, parent):
        self.parent = parent

    def export_image(self, widget):
        path, _ = QFileDialog.getSaveFileName(self.parent, "Save as Image", "", "PNG Files (*.png)")
        if path:
            pixmap = QPixmap(widget.size())
            widget.render(pixmap)
            pixmap.save(path, "PNG")

    def export_pdf(self, text):
        path, _ = QFileDialog.getSaveFileName(self.parent, "Save as PDF", "", "PDF Files (*.pdf)")
        if path:
            c = canvas.Canvas(path, pagesize=A4)
            width, height = A4
            c.setFont("Helvetica", 14)
            c.drawString(50, height - 100, text)
            c.save()

    def copy_to_clipboard(self, text):
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
