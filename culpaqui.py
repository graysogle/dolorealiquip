from PyQt5.QtWidgets import QApplication, QLabel, QGraphicsBlurEffect
import sys

app = QApplication(sys.argv)
label = QLabel('Blur Effect')
blur = QGraphicsBlurEffect()
blur.setBlurRadius(10)
label.setGraphicsEffect(blur)
label.show()
sys.exit(app.exec_())
