def minimizeBias(ratings):
    ratings.sort(reverse=True)
    
    result = 0
    while len(ratings) > 0:
      a = ratings.pop()
      b = ratings.pop()

      result += b-a # Not need abs() because alwais b >= a

    return result



if __name__ == '__main__':
    ratings_count = int(input().strip())

    ratings = []

    for _ in range(ratings_count):
        ratings_item = int(input().strip())
        ratings.append(ratings_item)

    result = minimizeBias(ratings)

    print(result)