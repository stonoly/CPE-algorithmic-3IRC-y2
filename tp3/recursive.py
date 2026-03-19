def recursive_upcreasing(n: int) -> None:
    if n == 0:
        return

    recursive_upcreasing(n - 1)
    print(n)

def terminal_recursive_upcreasing(n: int, base: int) -> int:
    print(base)
    if n == base:
        return n

    return terminal_recursive_upcreasing(n, base+1)

def recursive_decreasing(n: int) -> int:
    print(n)
    if n == 1:
        return n

    return recursive_decreasing(n-1)

def terminal_recursive_decreasing(n: int, base: int) -> int:
    print(n)
    if n == base:
        return n

    return terminal_recursive_decreasing(n-1, base)



if __name__ == "__main__":
    print("----Upcreasing----")
    print("Normal:")
    recursive_upcreasing(5)
    print("Terminal:")
    terminal_recursive_upcreasing(5, 1)
    print("----Decreasing----")
    print("Normal:")
    recursive_decreasing(5)
    print("Terminal:")
    terminal_recursive_upcreasing(5)
    
    