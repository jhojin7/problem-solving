def solution(phone_book):
    S = set(phone_book)
    for num in phone_book:
        for i in range(len(num)):
            if num[:i] in S:
                return False
    return True
        
