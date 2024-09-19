

""" A New Python file is generated for Part B
    Author: Bibek Rai
"""

class RequisitionSystem:
    unique_id_counter = 10000  # Global unique ID counter

    def __init__(self):
        self.requisitions = []  # To store all requisitions
        self.approved_requisitions  = 0
        self.pending_requisitions  = 0
        self.not_approved_requisitions  = 0

    # Method to collect user information
    def staff_info(self, date, staffid, name):
        self.date = name
        self.staffid = staffid
        self.name = name

    # Method to accept list of request items and calculate total cost
    def requisition_details(self, items):
        total = sum(item['cost'] for item in items)
        self.requisitions.append({
            'id': RequisitionSystem.unique_id_counter,
            'name': self.name,
            'items': items,
            'total': total,
            'status': 'pending'
        })
        RequisitionSystem.unique_id_counter += 1
        return total, items

    # Method to check if request is approved based on total amount
    def requisition_approval(self):
        for requisition in self.requisitions :
            if requisition ['total'] < 500:
                requisition['status'] = 'approved'
                self.approved_requisitions  += 1
            else:
                requisition['status'] = 'pending'
                self.pending_requisitions += 1

    # Method for manager to respond to pending requests
    def respond_requisition(self, requisition_id, response):
        for requisition in self.requisitions:
            if requisition ['id'] == requisition_id and requisition['status'] == 'pending':
                if response == 'Approved':
                    requisition['status'] = 'approved'
                    self.approved_requisitions  += 1
                    self.pending_requisitions  -= 1
                else:
                    requisition['status'] = 'not approved'
                    self.not_approved_requisitions+= 1
                    self.pending_requisitions -= 1
""" A New Python file is generated for Part B
    Author: Bibek Rai
"""

class RequisitionSystem:
    unique_id_counter = 10000  # Global unique ID counter

    def __init__(self):
        self.requests = []  # To store all requests
        self.approved_requests = 0
        self.pending_requests = 0
        self.not_approved_requests = 0

    # Method to collect user information
    def staff_info(self, date, staffid, name):
        self.date = date
        self.staffid = staffid
        self.name = name

    # Method to accept list of request items and calculate total cost
    def requisition_details(self, items):
        total = sum(item['cost'] for item in items)
        self.requests.append({
            'id': RequisitionSystem.unique_id_counter,
            'name': self.name,
            'items': items,
            'total': total,
            'status': 'pending'
        })
        RequisitionSystem.unique_id_counter += 1
        return total, items

    # Method to check if request is approved based on total amount
    def requisition_approval(self):
        for request in self.requests:
            if request['total'] < 500:
                request['status'] = 'approved'
                self.approved_requests += 1
            else:
                request['status'] = 'pending'
                self.pending_requests += 1

    # Method for manager to respond to pending requests
    def respond_requisition(self, request_id, response):
        for request in self.requests:
            if request['id'] == request_id and request['status'] == 'pending':
                if response == 'Approved':
                    request['status'] = 'approved'
                    self.approved_requests += 1
                    self.pending_requests -= 1
                else:
                    request['status'] = 'not approved'
                    self.not_approved_requests += 1
                    self.pending_requests -= 1

    # Method to display all request details
    def display_requisition(self):
        for request in self.requests:
            print(f"Request ID: {request['id']}, Name: {request['name']}, Total: {request['total']}, Status: {request['status']}")

    # Method to show requisition statistics
    def requisition_statistic(self):
        print(f"Total requests: {len(self.requests)}")
        print(f"Approved requests: {self.approved_requests}")
        print(f"Pending requests: {self.pending_requests}")
        print(f"Not approved requests: {self.not_approved_requests}")



# request system was initialized
system = RequisitionSystem()


# here is my submition of  staff info
system.staff_info("03/04/2024", "FN19", "John Paul")

#  requisition details submition
items = [{'John Paul': 'Copy', 'cost': 200}, {'John Paul': 'pen', 'cost': 250}]
total, items = system.requisition_details(items)
print(f"Total cost: {total}, Items: {items}")

# here is my submition of  staff info
system.staff_info("05/04/2024", "FN19", "Tracy Brown")
#  requisition details submition
items = [{'Tracy Brown': 'Computer', 'cost': 600}, {'Tracy Brown': 'Jacket', 'cost': 400}]
total, items = system.requisition_details(items)
print(f"Total cost: {total}, Items: {items}")

# here is my submition of  staff info
system.staff_info("07/05/2024", "FN19", "Emma Wellington")
items = [{'Emma Wellington': 'Table', 'cost': 1500}, {'Emma Wellington': 'Laptop', 'cost': 2000}]
total, items = system.requisition_details(items)
print(f"Total cost: {total}, Items: {items}")

# here is my submition of  staff info
system.staff_info("03/05/2024", "FN19", "Catlin White")
items = [{'Catlin White': 'Book', 'cost': 200}, {'Catlin White': 'watch', 'cost': 190}]
total, items = system.requisition_details(items)
print(f"Total cost: {total}, Items: {items}")


# Approve or decline request based on amount
system.requisition_approval()

# Manager can respond to pending requests
system.respond_requisition(1, 'Approved')

# Display all requests
system.display_requisition()

# Display request statistics
system.requisition_statistic()



