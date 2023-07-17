def avg_age(comp):
    employ = comp.get("employees", {})
    s_emp = [employee["age"] for name, employee in employ.items() if employee.get("job_title", "").lower().startswith('s')]

    if not s_emp:
        return 0
    
    return sum(s_emp)/ len(s_emp)




comp = {
    'employees': {
        'John': {'age': 35, 'job_title': 'Manager'},
        'Emma': {'age': 28, 'job_title': 'Software Engineer'},
        'Kelly': {'age': 41, 'job_title': 'Senior Developer'},
        'Sam': {'age': 30, 'job_title': 'Software Engineer'},
        'Mark': {'age': 37, 'job_title': 'Senior Manager'},
        'Sara': {'age': 32, 'job_title': 'Software Engineer'},
    }
}

print(avg_age(comp))