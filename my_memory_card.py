#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,  QRadioButton, QMessageBox, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle
from random import randint
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
def show():
    button.setText('Следующий вопрос')
    RadioGroupBox.hide()
    RadioGroupBox1.show()
def show_question():
    button.setText('Ответить')
    RadioGroupBox1.hide()
    RadioGroupBox.show()
    RadioGroupBox2.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    RadioGroupBox2.setExclusive(True)
def ask(q: Question):
    shuffle(answer)
    text.setText(q.question)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    button6.setText(q.right_answer)
    show_question()
def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        main_win.score +=1
    else:
        if answer[1].isChecked():
            show_correct('Неправильно')
        if answer[2].isChecked():
            show_correct('Неправильно')
        if answer[3].isChecked():
            show_correct('Неправильно')
    print('Статистика:')
    print('-Всего вопросов:', main_win.total)
    print('-Правильных ответов:', main_win.score)
    print('-Рейтинг:', main_win.score/main_win.total * 100)
def show_correct(res):
    button5.setText(res)
    show()
def next_question():
    main_win.total +=1
    main_win.cur_question = randint(0, len(a) -1)
    q = a[main_win.cur_question]
    ask(q)
def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
app = QApplication([])
main_win = QWidget()
main_win.resize(400,200)
main_win.setWindowTitle('Memory Card')

text = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')
button1 = QRadioButton('Энцы')
button2 = QRadioButton('Чулымцы')
button3 = QRadioButton('Смурфы')
button4 = QRadioButton('Алеуты')
button = QPushButton('Ответить')
answer = [button1, button2, button3, button4]

RadioGroupBox2 = QButtonGroup()
RadioGroupBox2.addButton(button1)
RadioGroupBox2.addButton(button2)
RadioGroupBox2.addButton(button3)
RadioGroupBox2.addButton(button4)


line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line22 = QVBoxLayout()
line222 = QVBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line1.addWidget(text,alignment = Qt.AlignCenter)
line22.addWidget(button1)
line22.addWidget(button2)
line222.addWidget(button3)
line222.addWidget(button4)
line4.addStretch(1)
line4.addWidget(button)
line4.addStretch(1)
line2.addLayout(line22)
line2.addLayout(line222)
RadioGroupBox.setLayout(line2)
line.addLayout(line1,stretch = 1)
line3.addWidget(RadioGroupBox)
line.addLayout(line3,stretch = 1)
line.addLayout(line4,stretch = 1)


RadioGroupBox1 = QGroupBox('Результат теста')
button5 = QLabel('Правильно/Неправильно')
button6 = QLabel('Правильный ответ')
line7 = QVBoxLayout()
line5 = QHBoxLayout()
line6 = QHBoxLayout()
line5.addWidget(button5,alignment = Qt.AlignCenter)
line5.addStretch(5)
line6.addWidget(button6,alignment = Qt.AlignCenter)
line7.addLayout(line5,stretch = 2)
line7.addLayout(line6,stretch = 2)
line7.setSpacing(20)
RadioGroupBox1.setLayout(line7)
line3.addWidget(RadioGroupBox1)
RadioGroupBox1.hide()
a = list()
a.append(Question('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Испанский', 'Бразильский'))
a.append(Question('Какой национальности не существует?', 'Энцы' , 'Смурфы', 'Чулымцы', 'Алеуты'))
a.append(Question('Какого цвета нет в флаге России', 'Зелёный','Красный', 'Синий','Белый'))
main_win.cur_question = -1
main_win.total = 0
main_win.score = 0
next_question()
button.clicked.connect(click_OK)
main_win.setLayout(line)
main_win.show()
app.exec_()