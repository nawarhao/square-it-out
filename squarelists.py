def process_squares(start, end):
    squares = []
    
    for num in range(start, end + 1):
        squares.append(num ** 2)
    
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    
    print("All square values:", squares)
    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)

# Example usage:
process_squares(1, 10)
