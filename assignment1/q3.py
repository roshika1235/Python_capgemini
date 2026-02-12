class LibraryBook():
    fine_per_day=20
    min_day_kept=10
    def __init__(self,issue_book,return_book,cal_fine):
        self.issue_book=issue_book
        self.return_book=return_book
        self.cal_fine=cal_fine
        self.day_kept=days_kept
    def book_issue(self,issued):
        if not self.return_book:
            print("book unavalable to issue")
        else:
            print("issued ")
    def fun_return(self,amount):
        if self.cal_fine-amount==0:
            print("book returned sucessfull")
        else:
            print("fine pending")
    def cal_fine(self,cal_ 
        