def courseI():
    c1H = int(input("Enter credits for course 1: "));
    c1GSTR = input("Enter grade for course 1: ");
    return c1H, c1GSTR;

x, y = courseI();
print(x);
print(y);

for i in range(1, 7):
    print("I need", i, "scrubs");



