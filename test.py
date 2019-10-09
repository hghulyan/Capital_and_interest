capital = int(input("Place in your capital : "))
years = int(input("How many years : "))
count = 1
cap_1 = capital
while years >= count:
    intrest_x = capital * 0.05
    intrest = capital * 1.05
    print("intrest",intrest_x)
    print("capital",capital)
    print("total",intrest + capital + intrest_x)
    print(count)
    count = count + 1
    intrest = capital * 1.05
    capital = capital + cap_1
    whole_year = (intrest + capital + intrest_x) * 12
    print("if you have the investment over all 12 months",whole_year)
