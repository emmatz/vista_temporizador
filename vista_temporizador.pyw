import sys
import re
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from interfaces.mainWindow import Ui_MainWindow
from interfaces.mensajeEmer import Ui_Form


class CountdownApp(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)

    self.pushButtonInicio.clicked.connect(self.start_timer)
    self.pushButtonSalir.clicked.connect(self.close)

    # Temporizador (QTimer)
    self.timer = QTimer(self)
    self.timer.timeout.connect(self.update_time)

    self.seconds_left = 0
    self.timer_running = False

    # self.subventana = None

  def start_timer(self):
    # Leer el tiempo ingresado por el usuario
    time_input = self.lineEdit.text()

    # Validar que el input sea correcto
    if time_input:
      try:
        # Convertir el tiempo ingresado en segundos
        self.seconds_left = self.parse_time_to_seconds(time_input)
        self.update_time()
        self.timer.start(1000)  # Actualiza cada segundo
        self.pushButtonInicio.setText("Reiniciar")  # Cambiar texto del botón
        self.timer_running = True
      except ValueError:
        self.label.setText("Formato de tiempo no válido.")
        return
    else:
      self.label.setText("Por favor ingrese un tiempo.")

  def update_time(self):
    if self.seconds_left > 0:
      self.seconds_left -= 1
      self.lcdNumber.display(self.format_time(self.seconds_left))  # Muestra el tiempo en formato hh:mm:ss
      if self.seconds_left <= 10:
        self.lcdNumber.setStyleSheet("background-color: red; color: white;")
      else:
        self.lcdNumber.setStyleSheet("background-color: black; color: white;")
    else:
      self.timer.stop()
      self.lcdNumber.display("00:00:00")  # Muestra 00:00:00 cuando termina
      self.openNewWindow()
      self.pushButtonInicio.setText("Iniciar Nuevamente")  # Restablece el texto del botón
      self.timer_running = False

  def parse_time_to_seconds(self, time_str):
    # Inicializar el total de segundos
    total_seconds = 0

    # Expresión regular para capturar las horas, minutos y segundos
    time_pattern = r"(\d+)(h|m|s)?"

    # Buscar los valores en el formato "1h", "30s", "1h 20m", etc.
    matches = re.findall(time_pattern, time_str)

    if not matches:
      raise ValueError("Formato de tiempo inválido.")

    for match in matches:
      value, unit = match
      value = int(value)

      if unit == "h":
        total_seconds += value * 3600  # horas a segundos
      elif unit == "m":
        total_seconds += value * 60  # minutos a segundos
      elif unit == "s" or unit == "":  # Si no hay unidad, se asume segundos
        total_seconds += value
      else:
        raise ValueError("Unidad de tiempo inválida.")

    return total_seconds

  def format_time(self, seconds):
    # Convierte segundos a formato hh:mm:ss
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

  def openNewWindow(self):
    # self.advise = viewMessage()
    self.advise = viewMessage(self)
    # Asegurarse de que la subventana tenga las banderas de ventana top-level
    self.advise.setWindowFlags(self.advise.windowFlags() | Qt.WindowStaysOnTopHint)
    self.advise.show()
    # Activar la ventana y elevarla
    self.advise.activateWindow() # Asegura que se active la ventana
    self.advise.raise_()  # Asegura que se eleve por encima de otras ventanas

class viewMessage(QWidget, Ui_Form):
  def __init__(self, main_window):
    super().__init__()
    self.setupUi(self)
    self.mainWin = main_window
    self.pushButton.clicked.connect(self.exit_and_restart)

  def exit_and_restart(self):
    self.mainWin.start_timer()
    self.close()


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = CountdownApp()
  window.show()
  sys.exit(app.exec())
