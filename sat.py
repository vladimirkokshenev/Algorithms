import numpy
import random

def read_cnf(filename):
    fp = open(filename)

    n = int(fp.readline())
    cnf = {}
    one_line = fp.readline()
    i = 1

    while one_line != "":
        disjunction = map(int, one_line.split())
        cnf[i] = tuple(disjunction)
        i += 1
        one_line = fp.readline()

    return n, cnf


def get_trivial_variables(cnf):
    positive_inclusion = set([])
    negative_inclusion = set([])
    for disjunction in cnf:
        for k in range(2):
            if cnf[disjunction][k] > 0:
                positive_inclusion.add(cnf[disjunction][k])
            else:
                negative_inclusion.add(abs(cnf[disjunction][k]))
    only_positive_inclusion = positive_inclusion.difference(negative_inclusion)
    only_negative_inclusion = negative_inclusion.difference(positive_inclusion)
    return only_positive_inclusion, only_negative_inclusion


def exclude_closes_with_trivial_variables(cnf, only_positive_inclusion, only_negative_inclusion):

    closes_for_deletion = set([])

    for disjunction in cnf:
        for k in range(2):
            if cnf[disjunction][k] > 0 and cnf[disjunction][k] in only_positive_inclusion:
                closes_for_deletion.add(disjunction)
            if cnf[disjunction][k] < 0 and abs(cnf[disjunction][k]) in only_negative_inclusion:
                closes_for_deletion.add(disjunction)

    for disjunction in closes_for_deletion:
        del cnf[disjunction]


def cnf_reduction(cnf):

    continue_flag = True

    while continue_flag:
        only_positive_inclusion, only_negative_inclusion = get_trivial_variables(cnf)
        if only_positive_inclusion or only_negative_inclusion:
            exclude_closes_with_trivial_variables(cnf, only_positive_inclusion, only_negative_inclusion)
        else:
            continue_flag = False


def get_variable_set(cnf):
    variable_set = set([])
    for disjunction in cnf:
        for k in range(2):
            variable_set.add(abs(cnf[disjunction][k]))
    return variable_set


def get_random_assignment(variable_set):
    random_assignment = {}
    for v in variable_set:
        random_assignment[v] = random.sample(range(2), 1)[0]
    return random_assignment


def check_sat(cnf, variable_assignment):

    for disjunction in cnf:
        if cnf[disjunction][0] > 0:
            x1 = variable_assignment[cnf[disjunction][0]]
        else:
            x1 = 1 - variable_assignment[abs(cnf[disjunction][0])]
        if cnf[disjunction][1] > 0:
            x2 = variable_assignment[cnf[disjunction][1]]
        else:
            x2 = 1 - variable_assignment[abs(cnf[disjunction][1])]
        if x1 + x2 == 0:
            return False, disjunction
    return True, 0


def get_2sat_status(cnf):

    log2n = int(numpy.log2(len(cnf))) + 1
    variable_set = get_variable_set(cnf)

    for i in range(log2n):
        random_assignment = get_random_assignment(variable_set)
        for j in range(2*len(cnf)*len(cnf)):
            (sat_status, faulty_disjunction) = check_sat(cnf, random_assignment)
            if sat_status:
                return True
            else:
                change_var = abs(cnf[faulty_disjunction][random.sample(range(2), 1)[0]])
                random_assignment[change_var] = 1 - random_assignment[change_var]

    return False


if __name__ == '__main__':
    filename = 'tests/2sat6.txt'
    n, cnf = read_cnf(filename)
    cnf_reduction(cnf)
    print(filename)
    print(get_2sat_status(cnf))
