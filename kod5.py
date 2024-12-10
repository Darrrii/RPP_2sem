def create_report(employee):
    """Creates a report for an employee."""
    for key, value in employee.items():
        print(f"{key.capitalize()}: {value}")

employee_data = {
    "name": "John Doe",
    "age": 30,
    "department": "Engineering",
    "salary": 70000,
    "bonus": 5000,
    "performance_score": 4.5
}

create_report(employee_data)
