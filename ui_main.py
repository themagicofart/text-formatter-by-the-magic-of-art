import os
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox,
    QPushButton, QFrame, QTextEdit, QHBoxLayout, QFileDialog,
    QSlider, QFontComboBox, QCheckBox
)
from PyQt5.QtCore import Qt
from style_manager import StyleManager
from file_utils import FileUtils
from effects import Effects


class TextDisplayApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ultimate Text Display App")
        self.setGeometry(100, 100, 1000, 700)

        self.style_manager = StyleManager()
        self.file_utils = FileUtils(self)
        self.effects = Effects()

        main_layout = QVBoxLayout()

        # --- Input Section ---
        input_layout = QVBoxLayout()
        self.entry = QLineEdit(self)
        self.entry.setText("It is said to deliver happiness. Being compassionate, it shares its eggs with injured people.")
        input_layout.addWidget(QLabel("Enter Text:"))
        input_layout.addWidget(self.entry)

        # Font selector
        font_layout = QHBoxLayout()
        self.font_combo = QFontComboBox()
        font_layout.addWidget(QLabel("Font:"))
        font_layout.addWidget(self.font_combo)

        # Font size slider
        self.size_slider = QSlider(Qt.Horizontal)
        self.size_slider.setRange(10, 72)
        self.size_slider.setValue(20)
        font_layout.addWidget(QLabel("Size:"))
        font_layout.addWidget(self.size_slider)
        input_layout.addLayout(font_layout)

        # Alignment options
        self.align_combo = QComboBox()
        self.align_combo.addItems(["Center", "Left", "Right", "Justify"])
        input_layout.addWidget(QLabel("Alignment:"))
        input_layout.addWidget(self.align_combo)

        # Built-in styles
        self.combo = QComboBox(self)
        self.combo.addItems(self.style_manager.get_style_names())
        input_layout.addWidget(QLabel("Choose Style:"))
        input_layout.addWidget(self.combo)

        # Custom stylesheet input
        self.custom_style_input = QTextEdit(self)
        self.custom_style_input.setPlaceholderText("Enter custom CSS here...")
        self.custom_style_input.setFixedHeight(80)
        self.custom_style_input.hide()
        input_layout.addWidget(QLabel("Custom Style:"))
        input_layout.addWidget(self.custom_style_input)

        # Checkboxes for effects
        self.typewriter_check = QCheckBox("Typewriter Effect")
        self.blink_check = QCheckBox("Blink Effect")
        self.glow_check = QCheckBox("Glow Animation")
        input_layout.addWidget(self.typewriter_check)
        input_layout.addWidget(self.blink_check)
        input_layout.addWidget(self.glow_check)

        # Buttons
        btn_layout = QHBoxLayout()
        display_btn = QPushButton("Display", self)
        display_btn.clicked.connect(self.update_display)
        btn_layout.addWidget(display_btn)

        export_img_btn = QPushButton("Export as Image", self)
        export_img_btn.clicked.connect(lambda: self.file_utils.export_image(self.display))
        btn_layout.addWidget(export_img_btn)

        export_pdf_btn = QPushButton("Export as PDF", self)
        export_pdf_btn.clicked.connect(lambda: self.file_utils.export_pdf(self.display.text()))
        btn_layout.addWidget(export_pdf_btn)

        copy_btn = QPushButton("Copy to Clipboard", self)
        copy_btn.clicked.connect(lambda: self.file_utils.copy_to_clipboard(self.display.text()))
        btn_layout.addWidget(copy_btn)

        input_layout.addLayout(btn_layout)
        main_layout.addLayout(input_layout)

        # --- Display Area ---
        self.outer_frame = QFrame(self)
        self.outer_frame.setFrameShape(QFrame.Box)
        self.outer_frame.setLineWidth(4)
        display_layout = QVBoxLayout(self.outer_frame)

        self.display = QLabel(self)
        self.display.setWordWrap(True)
        self.display.setAlignment(Qt.AlignCenter)
        display_layout.addWidget(self.display)
        main_layout.addWidget(self.outer_frame)

        self.setLayout(main_layout)

        # Signals
        self.combo.currentTextChanged.connect(self.on_style_change)
        self.entry.textChanged.connect(self.update_display)
        self.custom_style_input.textChanged.connect(self.update_display)
        self.font_combo.currentFontChanged.connect(self.update_display)
        self.size_slider.valueChanged.connect(self.update_display)
        self.align_combo.currentTextChanged.connect(self.update_display)

        self.update_display()

    def on_style_change(self, style):
        self.custom_style_input.setVisible(style == "Custom")

    def update_display(self):
        text = self.entry.text()
        style_name = self.combo.currentText()
        font = self.font_combo.currentFont().family()
        size = self.size_slider.value()
        align_map = {
            "Center": Qt.AlignCenter,
            "Left": Qt.AlignLeft,
            "Right": Qt.AlignRight,
            "Justify": Qt.AlignJustify
        }
        self.display.setAlignment(align_map[self.align_combo.currentText()])

        # Apply style
        stylesheet, frame_style = self.style_manager.get_style(style_name, font, size, self.custom_style_input.toPlainText())
        self.display.setText(text)
        self.display.setStyleSheet(stylesheet)
        self.outer_frame.setStyleSheet(frame_style)

        # Apply effects
        self.effects.clear_effects(self.display)
        if self.typewriter_check.isChecked():
            self.effects.typewriter(self.display, text)
        if self.blink_check.isChecked():
            self.effects.blink(self.display)
        if self.glow_check.isChecked():
            self.effects.glow(self.display)
