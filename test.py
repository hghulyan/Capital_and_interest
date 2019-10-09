capital = int(input("Place in your capital : "))
years = int(input("How many years : "))
count = 1
cap_1 = capital
while years >= count:
    interest_x = capital * 0.05
    interest = capital * 1.05
    print("interest",interest_x)
    print("capital",capital)
    print("total",interest + capital + interest_x)
    print(count)
    count = count + 1
    intrest = capital * 1.05
    capital = capital + cap_1
    whole_year = (interest + capital + interest_x) * 12
    print("if you have the investment over all 12 months",whole_year)
