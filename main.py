import os
import sys

from pathlib import Path
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QScrollArea,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
from groq import Groq
from dotenv import load_dotenv
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

class Chatbot(QWidget):
    def __init__(self):
        super().__init__()
        self.prompt = QLineEdit(self)
        self.get_answer_button = QPushButton("Get answer",self)
        self.answer_label = QLabel(self)
        self.prompt.setPlaceholderText("Enter a prompt: ")
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Chatbot")
        self.setGeometry(400, 400, 500, 500)
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.answer_label)
        self.scroll.setWidgetResizable(True)
        self.answer_label.setWordWrap(True)
        vbox = QVBoxLayout()

        vbox.addWidget(self.prompt)
        vbox.addWidget(self.get_answer_button)
        vbox.addWidget(self.scroll)

        self.setLayout(vbox)
        self.prompt.setAlignment(Qt.AlignCenter)
        self.answer_label.setAlignment(Qt.AlignCenter)

        self.prompt.setObjectName("prompt")
        self.get_answer_button.setObjectName("get_answer_button")
        self.answer_label.setObjectName("answer_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
                background-color: #ffffff;
            }

            QLineEdit#prompt{
                font-size: 20px;
                background-color: #ffffff;
            }

            QPushButton#get_answer_button{
                font-size: 35px;
                font-weight: bold;
                background-color: #ffffff;
            }

            QLabel#answer_label{
                font-size: 20px;
                background-color: #669bb0;
            }
        """)
        self.prompt.returnPressed.connect(self.get_answer)
        self.get_answer_button.clicked.connect(self.get_answer)

    def get_answer(self):
        self.get_answer_button.setEnabled(False)
        self.answer_label.setText("Loading...")
        self.answer_label.repaint()
        QApplication.processEvents()
        
        try:
            client = Groq(
                api_key=os.environ.get("GROQ_API_KEY"),
            )
            prompt = self.prompt.text()

            chat_completion = client.chat.completions.create(
                messages = [
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="openai/gpt-oss-120b", 
            )

            answer = chat_completion.choices[0].message.content
            self.answer_label.setText(answer)
        except Exception as e:
            self.answer_label.setText(f"Error: {e}")
        finally:
            self.get_answer_button.setEnabled(True)

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    chatbot_app = Chatbot()
    chatbot_app.show()
    sys.exit(app.exec_())
