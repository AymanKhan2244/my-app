def calculate_tax(subtotal: float, rate: float = 0.05) -> float:
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")
    return round(subtotal * rate, 2)
