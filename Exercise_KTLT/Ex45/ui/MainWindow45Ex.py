import functools

from PyQt6.QtWidgets import QPushButton

from Exercise_KTLT.Ex45.ui.MainWindow45 import Ui_MainWindow


class MainWindow45Ex(Ui_MainWindow):
    def __init__(self):
        self.dataset=[]
        self.selected_index=-1
        self.previous_button=None
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.process_save)
        self.pushButtonRemove.clicked.connect(self.process_remove)
        self.pushButtonFilter_Year.clicked.connect(self.process_filter_year)
        self.pushButtonSearch_ISBN.clicked.connect(self.process_search_isbn)
        self.pushButtonSearch_Title.clicked.connect(self.process_search_title)
        self.pushButtonFilter_Publisher.clicked.connect(self.process_filter_publisher)
    def check_duplicated_isbn(self,isbn):
        for book in self.dataset:
            if book["isbn"]==isbn:
                return True
        return False
    def process_save(self):
        isbn=self.lineEditISBN.text()
        title=self.lineEditTitle.text()
        author=self.lineEditAuthor.text()
        publisher=self.lineEditPublisher.text()
        year=self.lineEditYear.text()
        book={"isbn":isbn,
              "title":title,
              "author":author,
              "publisher":publisher,
              "year":year}
        if self.check_duplicated_isbn(isbn)==False:
            self.dataset.append(book)
        else:
            self.dataset[self.selected_index]=book
        self.showbook_on_gui()

    def showbook_on_gui(self):
        self.clearLayout(self.verticalLayoutBook)
        for i in range(len(self.dataset)):
            book = self.dataset[i]
            title = f"{book['title']}"
            btn = QPushButton(text=title)
            btn.setStyleSheet("background-color: rgb(155, 156, 152);")
            self.verticalLayoutBook.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail, i))
    def show_detail(self,i):
        book=self.dataset[i]
        self.lineEditISBN.setText(book["isbn"])
        self.lineEditTitle.setText(book["title"])
        self.lineEditAuthor.setText(book["author"])
        self.lineEditPublisher.setText(book["publisher"])
        self.lineEditYear.setText(book["year"])
        self.selected_index=i
        btn=self.MainWindow.sender()
        if self.previous_button!=None:
            self.previous_button.setStyleSheet("background-color: rgb(155, 156, 152);")
        btn.setStyleSheet("background-color: rgb(235, 225, 52);")
        self.previous_button=btn
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def process_remove(self):
        if self.selected_index == -1:
            return
        self.dataset.pop(self.selected_index)
        self.selected_index = -1
        self.previous_button = None
        self.lineEditISBN.clear()
        self.lineEditTitle.clear()
        self.lineEditAuthor.clear()
        self.lineEditPublisher.clear()
        self.lineEditYear.clear()
        self.showbook_on_gui()

    def process_search_title(self):
        search_text = self.lineEditTitle.text().lower()
        for book in self.dataset:
            if search_text == book["title"].lower():
                self.lineEditISBN.setText(book["isbn"])
                self.lineEditTitle.setText(book["title"])
                self.lineEditAuthor.setText(book["author"])
                self.lineEditPublisher.setText(book["publisher"])
                self.lineEditYear.setText(book["year"])

    def process_search_isbn(self):
        isbn = self.lineEditISBN.text()
        for book in self.dataset:
            if isbn == book["isbn"]:
                self.lineEditISBN.setText(book["isbn"])
                self.lineEditTitle.setText(book["title"])
                self.lineEditAuthor.setText(book["author"])
                self.lineEditPublisher.setText(book["publisher"])
                self.lineEditYear.setText(book["year"])

    def process_filter_year(self):
        book_year=[]
        self.clearLayout(self.verticalLayoutBook)
        year = self.lineEditYear.text()
        for book in self.dataset:
            if year == book["year"]:
                book_year.append(book)
        for i in range(len(book_year)):
            book = book_year[i]
            title = f"{book['title']}"
            btn = QPushButton(text=title)
            btn.setStyleSheet("background-color: rgb(155, 156, 152);")
            self.verticalLayoutBook.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail, i))

    def process_filter_publisher(self):
        book_publisher = []
        self.clearLayout(self.verticalLayoutBook)
        publisher = self.lineEditPublisher.text().lower()
        for book in self.dataset:
            if publisher == book["publisher"]:
                book_publisher.append(book)
        for i in range(len(book_publisher)):
            book = book_publisher[i]
            title = f"{book['title']}"
            btn = QPushButton(text=title)
            btn.setStyleSheet("background-color: rgb(155, 156, 152);")
            self.verticalLayoutBook.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail, i))
