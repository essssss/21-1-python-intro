def greet(person):
    return f"Hello there, {person}"


def divide(a, b):
    if type(a) is int and type(b) is int:
        return a/b
    return "a and b must be integers"

def three_things(a,b,c):
    print("HI")


def send_email(to_email, from_email, subject, body):
  email = f"""
    to: {to_email}
    from: {from_email}
    subject: {subject}
    ----------------------
    body: {body}
    """
  print(email)

send_email(subject="MEAOW", to_email="blue@cat.com",
   from_email="Colt@people.com", body="Hi, you are cat. meaow")

def add_limited_numbers(a, b):
    """Add two numbers, making sure sum caps at 100"""
    
    sum = a + b
    # Does this need more context or info?
    if sum > 100:
        sum = 100
    return sum