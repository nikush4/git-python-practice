from datetime import datetime

def greet(name):
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"Hey there, {name}! Current time: {current_time}"
if __name__ == "__main__":
    user = "World"
    print(greet(user))


# small update
# work in progress
# change
# temp branch test