def gcd(front: int, divisor: int) -> int:
    while divisor:
        remainder = front % divisor  # calculate remainder
        front = divisor              # divisor to front
        divisor = remainder          # remainder to divisor
    return front                     # as soon as the divisor becomes 0, the divisor goes to the front


if __name__ == "__main__":
    print(gcd(12, 16))
