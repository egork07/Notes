from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout)

app = QApplication([])

# Створюємо початкову нотатку
notes = [{
    'назва': 'Ласкаво просимо!',
    'текст': "Це найкращий додаток для заміток у світі!",
    'теги': ["Добро", "Інструкція"]
}]

notes_win = QWidget()
notes_win.setWindowTitle('Розумні нотатки')
notes_win.resize(900, 600)

list_notes = QListWidget()
list_notes_label = QLabel("Список заміток")

button_note_create = QPushButton('Створити замітку')
button_note_del = QPushButton('Видалити замітку')
button_note_save = QPushButton('Зберегти замітку')

filed_tag = QLineEdit('')
filed_tag.setPlaceholderText('Введіть тег')
filed_text = QTextEdit()
button_tag_add = QPushButton('Додати до замітки')
button_tag_del = QPushButton('Видалити з тегу')
button_tag_search = QPushButton('Шукати замітки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel()

layout_notes = QHBoxLayout()

col_1 = QVBoxLayout()
col_1.addWidget(filed_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_tag_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)

col_2.addWidget(filed_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)

notes_win.setLayout(layout_notes)

# Функція для відображення нотатки при виборі зі списку
def show_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        for note in notes:
            if note['назва'] == key:
                filed_text.setText(note['текст'])
                list_tags.clear()
                list_tags.addItems(note['теги'])

list_notes.itemClicked.connect(show_note)

# Функція для створення нової нотатки
def add_note():
    note_name, ok = QInputDialog.getText(notes_win, 'Додати замітку', 'Назва замітки:')
    if ok and note_name:
        new_note = {
            'назва': note_name,
            'текст': '',
            'теги': []
        }
        notes.append(new_note)
        list_notes.addItem(new_note['назва'])

button_note_create.clicked.connect(add_note)

# Функція для збереження нотатки
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        for note in notes:
            if note['назва'] == key:
                note['текст'] = filed_text.toPlainText()
        print(notes)
    else:
        print('Замітка для збереження не вибрана!')

button_note_save.clicked.connect(save_note)

notes_win.show()
app.exec_()
