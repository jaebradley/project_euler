"""
https://projecteuler.net/problem=39

If p is the perimeter of a right triangle, which value for p <= 1000 has the most solutions?
"""
import time


def return_pythagorean_triplets(perimeter):
    triplets = list()
    for x in range(1, perimeter - 2):
        for y in range(x + 1, perimeter - x - 1):
            z = perimeter - x - y
            if z ** 2 == x ** 2 + y ** 2:
                triplets.append([x, y, z])
    return triplets


def return_perimeter_with_most_pythagorean_triplet_solutions(upper_bound_perimeter):
    solution_dict = {
        'solution_count': 0,
        'value': 0
    }
    for candidate_perimeter in range(upper_bound_perimeter, 0, -1):
        print candidate_perimeter
        pythagorean_solutions = return_pythagorean_triplets(perimeter=candidate_perimeter)
        if len(pythagorean_solutions) > solution_dict['solution_count']:
            solution_dict['solution_count'] = len(pythagorean_solutions)
            solution_dict['value'] = candidate_perimeter
    return solution_dict['value']


def main(upper_bound_perimeter):
    start_time = time.time()

    solution_perimeter = return_perimeter_with_most_pythagorean_triplet_solutions(
        upper_bound_perimeter=upper_bound_perimeter
    )

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "perimeter value with the most solutions is {0}; took {1} seconds".format(solution_perimeter, execution_seconds)


main(1000)
