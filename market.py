def calculate_profit_or_loss(X, Y):
    if X > Y:
        return "LOSS"
    elif X < Y:
        return "PROFIT"
    else:
        return "NEUTRAL"

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read X and Y for each test case
    X, Y = map(int, input().split())
    
    # Calculate profit or loss
    result = calculate_profit_or_loss(X, Y)
    
    # Print the result
    print(result)

