
class LibraryBook():
    fine_per_day=20
    min_day_kept=10
    def __init__(self,issue_book,return_book,cal_fine,day_kept):
        self.issue_book=issue_book
        self.return_book=return_book
        self.cal_fine=cal_fine
        self.day_kept=day_kept
    def book_issue(self):
        if not self.return_book:
            print("book unavalable to issue")
        else:
            print("issued ")
    def fun_return(self,amount):
        if self.cal_fine-amount==0:
            print("book returned sucessfull")
        else:
            print("fine pending")
    def cal_fine(self,fine):
        if self.day_kept>LibraryBook.min_day_kept:
            fine=self.day_kept*LibraryBook.fine_per_day
            print(fine)
        else:
            print("no fine")
    def show_details(self):
        print(self.fine_per_day,self.book_issue,self.cal_fine,self.day_kept,self.min_day_kept,self.return_book)
    @classmethod
    def update_fine(cls,fine):
        if fine>0:
            cls.fine_per_day=fine
            print("fine changed to" ,fine)
l1=LibraryBook()        
        