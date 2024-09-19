class RequestSystem:
    unique_id_counter = 1  # Global unique ID counter

    def __init__(self):
        self.requests = []  # To store all requests
        self.approved_requests = 0
        self.pending_requests = 0
        self.not_approved_requests = 0

    # Method to collect user information
    def user_info(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    # Method to accept list of request items and calculate total cost
    def request_details(self, items):
        total = sum(item['cost'] for item in items)
        self.requests.append({
            'id': RequestSystem.unique_id_counter,
            'name': self.name,
            'items': items,
            'total': total,
            'status': 'pending'
        })
        RequestSystem.unique_id_counter += 1
        return total, items

    # Method to check if request is approved based on total amount
    def request_approval(self):
        for request in self.requests:
            if request['total'] < 150:
                request['status'] = 'approved'
                self.approved_requests += 1
            else:
                request['status'] = 'pending'
                self.pending_requests += 1

    # Method for manager to respond to pending requests
    def respond_request(self, request_id, response):
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
    def display_request(self):
        for request in self.requests:
            print(f"Request ID: {request['id']}, Name: {request['name']}, Total: {request['total']}, Status: {request['status']}")

    # Method to show request statistics
    def request_statistic(self):
        print(f"Total requests: {len(self.requests)}")
        print(f"Approved requests: {self.approved_requests}")
        print(f"Pending requests: {self.pending_requests}")
        print(f"Not approved requests: {self.not_approved_requests}")


# Sample usage:

# Initialize the request system
system = RequestSystem()

# Submit user info
system.user_info("John Doe", 30, "john@example.com")

# Submit request details
items = [{'name': 'Item1', 'cost': 50}, {'name': 'Item2', 'cost': 70}]
total, items = system.request_details(items)
print(f"Total cost: {total}, Items: {items}")

# Approve or decline request based on amount
system.request_approval()

# Manager can respond to pending requests
system.respond_request(1, 'Approved')

# Display all requests
system.display_request()

# Display request statistics
system.request_statistic()