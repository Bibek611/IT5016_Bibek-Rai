The assessment2 Python file is  part of a requisition management system, authored by me (Bibek Rai). It includes the following functionality:

Key Features:
Class Definition (RequisitionSystem):

This class handles requisition system and their approval process.
It uses a class attribute (unique_id_counter) to maintain unique IDs for each requisition.

Attributes:

self.requisitions: A list that stores all requisitions made by users.
approved_requisitions, pending_requisitions, and not_approved_requisitions: Counters for tracking the status of requisitions.

Methods:

staff_info: Gathers staff information (date, staff ID, name).
requisition_details: Accepts a list of items, calculates the total cost, and appends a requisition entry with a unique ID.
requisition_approval: Checks if a requisition is approved based on the total amount (less than 500 is approved; otherwise, it's pending).
respond_requisition: Allows a manager to respond to pending requisitions (either approve or reject them).

The code adheres to several software design principles:

1. Encapsulation:
The class encapsulates attributes and methods that define the requisition system, restricting direct access to class data, which is a good practice.

The RequisitionSystem class encapsulates both data (attributes like requisitions, approved_requisitions, etc.) and behavior (methods like staff_info, requisition_details, etc.).

By organizing everything within the class, it provides a clear and logical structure to manage requisitions efficiently while protecting data integrity.


2. Single Responsibility Principle (SRP):
Each method in the class seems to follow SRP, as each method performs a distinct task (e.g., collecting staff info, managing requisition details, and handling approvals).

3. DRY (Don’t Repeat Yourself):
The code avoids duplication by centralizing the logic in relevant methods. For example, checking the status of requisitions is handled inside the requisition_approval method, rather than duplicating the logic in various parts of the code.

​