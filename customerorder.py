class customers:
    def __init__(self):
        self.customer_id="211h43"
        self.first_name="Purma"
        self.last_name="varshitha"
        self.phone='9234564992'
        self.email='varshitha@gmail.com'
        self.street='alwal'
        self.city='hyderabad'
        self.state='telangana'
        self.zip_code='500010'
    def display(self):
        print(f"{self.customer_id},{self.first_name},{self.last_name},{self.phone},{self.email},{self.street},{self.city},{self.state},{self.zip_code}")
class orders(customers):
    def __init__(self):
        self.order_id='abc1123'
        self.customer_id="211h43"
        self.order_status='order placed'
        self.order_date='29/1/25'
        self.required_date='6/2/25'
        self.shipped_date='1/2/25'
        self.store_id='23sdff'
        self.staff_id='amaz123'
    def display(self):
        print(f"{self.order_id},{self.customer_id},{self.order_status},{self.order_date},{self.required_date},{self.shipped_date},{self.store_id},{self.staff_id}")
Cust=customers()
Order=orders()
print(Cust.__dict__)
print(Order.__dict__)

