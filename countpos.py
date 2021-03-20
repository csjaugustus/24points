import itertools

def countpos(user_input):
    # Added together, this contains the maximum all of the cards and its variances equal to
    total = []
    eqv = {
        "j": [1,11],
        "q": [1,12],
        "k": [1,13]
    }

    # Go through and add all of these variances
    for i in user_input:
        total.extend(eqv[i])

    # Get the permutations of up to 3
    result = list(itertools.permutations(total, len(user_input)))

    sorted_result = []
    sums = []

    # Removes duplicates
    for tup in result:
        arr = list(tup)

        try:
            # Check for duplicates
            sums.index(sum(arr))
        except:
            # If not duplicates, append
            sorted_result.append(arr)
            sums.append(sum(arr))

    return sorted_result
