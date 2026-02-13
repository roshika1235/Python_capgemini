import logging
logging.basicConfig(
    filename="movie.log",
    level=logging.DEBUG,
    format= "%(asctime)s - %(levelname)s - %(message)s"
)
class MovieTicket():
    max_strength=60
    ticket_price=200
    def __init__(self,book_no_seats,cancel_booking,cal_Tp,tot_occupied):
        self.book_no_seats=book_no_seats
        self.cancel_booking=cancel_booking
        self.cal_Tp=cal_Tp
        self.tot_occupied=tot_occupied
    def display(self):
        logging.info("number of seats booked %s",self.book_no_seats)
        logging.info("cancel booking %s",self.cancel_booking)
        logging.info("calculate total price %s",self.cal_Tp)
        logging.info("total members as of now %s",self.tot_occupied)
    def book_seat(self,seats):
        if seats<0:
            logging.error("enter proper number of seats %s")
        if self.max_strength-self.tot_occupied >=seats:
            logging.info("no of seats remained %s",self.max_strength-self.tot_occupied)
        else :
            logging.error("seats are occupied %s",self.max_strength-self.tot_occupied)
    def cancel_seats(self,seats):
        if seats<0:
            logging.error("cannot cancel enter valid data %s",seats)
        if seats>self.tot_occupied:
            logging.error("invalid input %s",seats)
        self.tot_occupied-=seats
        tot_price_reduced=seats*self.ticket_price
        logging.info("cancelled sucessfully %s",tot_price_reduced)
    def caltp(self,seats):
        tot_price=seats*self.ticket_price
        your_budget=self.cal_Tp-tot_price
        if seats<0:
            logging.error("enter valid %s",seats)
        if your_budget>=tot_price:
            logging.info("total_price %s",tot_price)
        else:
            logging.warning("insuffient amount % s",your_budget)
    @classmethod
    def update_t_cost(cls,new_cost):
        if new_cost>0:
            cls.ticket_price=new_cost
            logging.info("new ticket price %s",cls.ticket_price)
        else:
            logging.error("enter valid price %s",new_cost)
m1=MovieTicket(5,0,1000,40)
m1.display()
m1.book_seat(6)
m1.cancel_seats(4)
m1.caltp(6)
