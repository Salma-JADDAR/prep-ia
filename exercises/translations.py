
# T2.1 - Check score
def check_score(score: int) -> str:
    if score >= 10:
        return "Admis"
    else:
        return "Recalé"



# T2.2 - Sum of prices
def sum_prices(prices: list) -> int:
    total = 0
    for price in prices:
        total += price
    return total


# T2.3 - Describe user
def describe_user(user: dict) -> str:
    return f"{user['name']} habite à {user['city']}"



# T2.4 - Filter with filter()
def filter_positive_filter(numbers: list) -> list:
    return list(filter(lambda n: n > 0, numbers))



# T2.4 - Filter with comprehension
def filter_positive_comprehension(numbers: list) -> list:
    return [n for n in numbers if n > 0]


# T2.5 - Count words
def count_words(words: list) -> dict:
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts