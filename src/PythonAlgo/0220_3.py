# Programmers - Lv2 - PhoneNum List
def solution(phone_book):
    phone_book.sort()
    for i in range(0, len(phone_book)-1):
        tmp = phone_book[i]
        for j in range(i+1, len(phone_book)):
            if phone_book[j][:len(tmp)] == tmp:
                return False
    return True

phone_book = ["119", "97674223", "1195524421"]
phone_book2 = ["123","456","789"]
phone_book3 = ["12","123","1235","567","88"]
print(solution(phone_book3))