from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout

import json

app = QApplication([])

''' Замітки в json '''
notes = {
    "Ласкаво просимо!": {
        "текст": "У цьому додатку можна створювати замітки з тегами...",
        "теги": ["розумні замітки", "інструкція"]
    }
}

with open("notes_data.json", "w") as file:
    json.dump(notes, file)

''' Інтерфейс програми '''

# параметри вікна програми
notes_win = QWidget()
notes_win.setWindowTitle('Розумні замітки')
notes_win.resize(900, 600)

# віджети вікна програми
list_notes = QListWidget()
list_notes_label = QLabel('Список заміток')

button_note_creat = QPushButton('Створити замітку')
button_note_del = QPushButton('Видалити замітку')
button_note_save = QPushButton('Зберегти замітку')

list_tags = QListWidget()
list_tags_label = QLabel('Список тегів')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введіть тег...')

field_text = QTextEdit()

button_tag_add = QPushButton('Додати до замітки')
button_tag_del = QPushButton('Відкріпити від замітки')
button_tag_search = QPushButton('Шукати замітки по тегу')

# розташування віджетів по лейаутам

layout_notes = QHBoxLayout() # головний лейаут

col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_creat)
row_1.addWidget(button_note_del)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

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


'''Функціонал програми'''
def show_note():
    # Отримуємо текст замітки з виділеною назвою і відображаємо його в полі редагування
    # Отримуємо вибрану назву замітки зі списку із виділеною позицією
    key = list_notes.selectedItems()[0].text()
    # Виводимо цю назву у консоль для налагодження
    print(key)
    # Встановлюємо текст замітки у полі редагування (поле тексту)
    field_text.setText(notes[key]["текст"])
    # Очищаємо список тегів
    list_tags.clear()
    # Додаємо теги замітки у список тегів для відображення
    list_tags.addItems(notes[key]["теги"])




'''Функціонал програми'''



'''Робота з текстом замітки'''
# Функція для додавання нової замітки.
def add_note():
    # Відображає діалогове вікно для отримання назви нової замітки.
    # `note_name` буде містити введену користувачем назву замітки, а `ok` вказує, чи користувач підтвердив введення.
    note_name, ok = QInputDialog.getText(notes_win, "Додати замітку", "Назва замітки: ")
    # Перевірка, чи користувач ввів назву замітки та чи натиснув "ОК".
    if ok and note_name != "":
        # Створюємо нову замітку у словнику `notes` з порожнім текстом та списком тегів.
        notes[note_name] = {"текст": "", "теги": []}
        # Додаємо назву нової замітки до віджету списку `list_notes`.
        list_notes.addItem(note_name)
        # Додаємо можливі теги для нової замітки до віджету списку `list_tags`.
        # Примітка: У початковому коді список тегів для нової замітки порожній.
        list_tags.addItems(notes[note_name]["теги"])
        # Виводимо змінений словник `notes` на консоль для перевірки.
        print(notes)
# Функція для відображення вмісту вибраної замітки у віджеті редагування `field_text`.
def show_note():
    # Отримуємо текст із замітки, яка має виділену назву в списку заміток.
    key = list_notes.selectedItems()[0].text()
    # Виводимо назву замітки на консоль (для перевірки).
    print(key)
    # Встановлюємо текст замітки у віджеті редагування `field_text`.
    field_text.setText(notes[key]["текст"])
    # Очищаємо вміст віджету `list_tags`.
    list_tags.clear()
    # Додаємо можливі теги замітки до віджету `list_tags`.
    list_tags.addItems(notes[key]["теги"])


# Функція для збереження змін у вибраній замітці.
def save_note():
    # Перевірка, чи є вибрані елементи в списку заміток (`list_notes.selectedItems()` повертає список вибраних елементів).
    if list_notes.selectedItems():
        # Отримуємо назву вибраної замітки, взявши перший вибраний елемент списку та отримавши його текст.
        key = list_notes.selectedItems()[0].text()
        # Оновлюємо текст вибраної замітки зі значенням, яке введено у віджеті `field_text`.
        notes[key]["текст"] = field_text.toPlainText()
        # Відкриваємо файл "notes_data.json" для запису та записуємо словник `notes` у форматі JSON.
        # `sort_keys=True` сортує ключі словника у відповідному порядку.
        # `ensure_ascii=False` дозволяє зберігати не-Latin символи у їхньому власному кодуванні.
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        # Виводимо змінений словник `notes` на консоль для перевірки.
        print(notes)
    else:
        # Якщо жодна замітка не вибрана, виводимо повідомлення про це.
        print("Замітка для збереження не вибрана!")


# Функція для вилучення вибраної замітки.
def del_note():
    # Перевірка, чи є вибрані елементи в списку заміток (`list_notes.selectedItems()` повертає список вибраних елементів).
    if list_notes.selectedItems():
        # Отримуємо назву вибраної замітки, взявши перший вибраний елемент списку та отримавши його текст.
        key = list_notes.selectedItems()[0].text()
        # Вилучаємо вибрану замітку зі словника `notes` за її назвою.
        del notes[key]
        # Очищаємо вміст віджетів `list_notes`, `list_tags` та `field_text`.
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        # Додаємо оновлений список заміток до віджету `list_notes`.
        list_notes.addItems(notes)
        # Відкриваємо файл "notes_data.json" для запису та записуємо словник `notes` у форматі JSON.
        # `sort_keys=True` сортує ключі словника у відповідному порядку.
        # `ensure_ascii=False` дозволяє зберігати не-Latin символи у їхньому власному кодуванні.
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        # Виводимо змінений словник `notes` на консоль для перевірки.
        print(notes)
    else:
        # Якщо жодна замітка не вибрана, виводимо повідомлення про це.
        print("Замітка для вилучення не обрана!")


'''Работа з тегами замітки'''


# Функція для додавання тегу до вибраної замітки.
def add_tag():
    # Перевірка, чи є вибрані елементи в списку заміток (`list_notes.selectedItems()` повертає список вибраних елементів).
    if list_notes.selectedItems():
        # Отримуємо назву вибраної замітки, взявши перший вибраний елемент списку та отримавши його текст.
        key = list_notes.selectedItems()[0].text()
        # Отримуємо текст тегу, введений користувачем у віджеті `field_tag`.
        tag = field_tag.text()
        # Перевірка, чи тег вже не існує у списку тегів обраної замітки.
        if not tag in notes[key]["теги"]:
            # Якщо тег ще не існує, додаємо його до списку тегів обраної замітки.
            notes[key]["теги"].append(tag)
            # Додаємо тег до віджету `list_tags`, щоб він відображався користувачу.
            list_tags.addItem(tag)
            # Очищаємо вміст віджету `field_tag` (поле для введення тегу).
            field_tag.clear()
        # Відкриваємо файл "notes_data.json" для запису та записуємо оновлений словник `notes` у форматі JSON.
        # `sort_keys=True` сортує ключі словника у відповідному порядку.
        # `ensure_ascii=False` дозволяє зберігати не-Latin символи у їхньому власному кодуванні.
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        # Виводимо змінений словник `notes` на консоль для перевірки.
        print(notes)
    else:
        # Якщо жодна замітка не вибрана, виводимо повідомлення про це.
        print("Замітка для додавання тега не обрана!")


# Функція для вилучення обраного тегу з обраної замітки.
def del_tag():
    # Перевірка, чи є вибрані елементи в списку тегів (`list_tags.selectedItems()` повертає список вибраних елементів).
    if list_tags.selectedItems():
        # Отримуємо назву вибраної замітки, взявши перший вибраний елемент списку заміток та отримавши його текст.
        key = list_notes.selectedItems()[0].text()
        # Отримуємо текст вибраного тегу, взявши перший вибраний елемент списку тегів та отримавши його текст.
        tag = list_tags.selectedItems()[0].text()
        # Вилучаємо обраний тег із списку тегів обраної замітки.
        notes[key]["теги"].remove(tag)
        # Очищаємо вміст віджету `list_tags`.
        list_tags.clear()
        # Додаємо оновлені теги до віджету `list_tags` для відображення їх користувачу.
        list_tags.addItems(notes[key]["теги"])
        # Відкриваємо файл "notes_data.json" для запису та записуємо оновлений словник `notes` у форматі JSON.
        # `sort_keys=True` сортує ключі словника у відповідному порядку.
        # `ensure_ascii=False` дозволяє зберігати не-Latin символи у їхньому власному кодуванні.
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        # Якщо жодний тег не вибрано, виводимо повідомлення про це.
        print("Тег для вилучення не обраний!")


# Функція для пошуку заміток за тегом або скидання пошуку.
def search_tag():
    # Виводимо текст кнопки `button_tag_search` на консоль (для перевірки).
    print(button_tag_search.text())
    # Отримуємо текст тегу, введений користувачем у віджеті `field_tag`.
    tag = field_tag.text()
    # Перевірка, чи текст кнопки є "Шукати замітки по тегу" і чи введено значення тегу.
    if button_tag_search.text() == "Шукати замітки по тегу" and tag:
        # Виводимо текст тегу на консоль (для перевірки).
        print(tag)
        # Створюємо порожній словник `notes_filtered`, де будуть зберігатися замітки з обраним тегом.
        notes_filtered = {}
        # Проходимося по всіх замітках у словнику `notes`.
        for note in notes:
            # Перевіряємо, чи обраний тег є серед тегів поточної замітки.
            if tag in notes[note]["теги"]:
                # Якщо тег є у замітці, додаємо замітку до словника `notes_filtered`.
                notes_filtered[note] = notes[note]
        # Змінюємо текст кнопки `button_tag_search` на "Скинути пошук".
        button_tag_search.setText("Скинути пошук")
        # Очищаємо вміст віджетів `list_notes` та `list_tags`.
        list_notes.clear()
        list_tags.clear()
        # Додаємо вміст словника `notes_filtered` (замітки з обраним тегом) до віджету `list_notes`.
        list_notes.addItems(notes_filtered)
        # Виводимо текст кнопки `button_tag_search` на консоль після зміни (для перевірки).
        print(button_tag_search.text())
    # Перевірка, чи текст кнопки є "Скинути пошук".
    elif button_tag_search.text() == "Скинути пошук":
        # Очищаємо вміст віджетів `field_tag`, `list_notes` та `list_tags`.
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        # Додаємо всі замітки (загальний список) до віджету `list_notes`.
        list_notes.addItems(notes)
        # Змінюємо текст кнопки `button_tag_search` на "Шукати замітки по тегу".
        button_tag_search.setText("Шукати замітки по тегу")
        # Виводимо текст кнопки `button_tag_search` на консоль після зміни (для перевірки).
        print(button_tag_search.text())
    else:
        # Якщо не виконується жодна з умов вище, не виконуємо жодних дій.
        pass



''' запуск програми '''
# підключення обробки подій
button_note_creat.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(del_note)
button_tag_add.clicked.connect(add_tag)
button_tag_del.clicked.connect(del_tag)
button_tag_search.clicked.connect(search_tag)


notes_win.show()

with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)


app.exec_()

