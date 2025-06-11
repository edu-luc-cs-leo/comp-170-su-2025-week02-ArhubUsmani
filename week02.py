def greet(name):
    return "Hello " + name + ". How are you?"
def greet_all_friends(friend_list):
    for friend in friend_list:
        print(greet(friend))
def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        print("no real solutions")
    else:
        x1 = (-b - (d ** 0.5)) / (2 * a)
        x2 = (-b + (d ** 0.5)) / (2 * a) 
        print("The solutions are x1=", x1, "and x2 =",x2)
my_friends = ["Ryan", "Moe", "Faiz"]
greet_all_friends(my_friends)
solve_quadratic(1, -3, 2)
solve_quadratic(1, 2, 5) 