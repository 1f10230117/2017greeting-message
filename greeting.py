<<<<<<< HEAD
from datetime import datetime
def greet(name):
    message = 'Hello, ' + name + '-san!'
    print(message)
=======
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'
    print(message + "," + name +  "-san!")


greet("Inoue")
print("INIAD")
>>>>>>> pr/2
