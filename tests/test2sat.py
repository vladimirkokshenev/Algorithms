import unittest
import sys
sys.path.append('''C:\Git\Algorithms''')
import sat


# read_cnf(filename)
class TestReadCnf(unittest.TestCase):

    def test_read_cnf_base_case(self):
        n, cnf = sat.read_cnf('2sat00.txt')
        self.assertEqual(cnf, {1: (1, -2), 2: (-1, 2), 3: (3, 4), 4: (3, -4)})
        self.assertEqual(n, 4)


# get_trivial_variables(cnf)
class TestGetTrivialVariables(unittest.TestCase):

    def test_get_trivial_variables_when_exist(self):
        cnf = {1: (1, -2), 2: (-1, 2), 3: (3, 4), 4: (3, -4), 5: (5, -6), 6: (-5, -6)}
        only_positive_inclusion, only_negative_inclusion = sat.get_trivial_variables(cnf)
        self.assertEqual(only_positive_inclusion, {3})
        self.assertEqual(only_negative_inclusion, {6})

    def test_get_trivial_variables_when_not_exist(self):
        cnf = {1: (1, -2), 2: (-1, 2), 3: (3, 4), 4: (-3, -4)}
        only_positive_inclusion, only_negative_inclusion = sat.get_trivial_variables(cnf)
        self.assertEqual(only_positive_inclusion, set([]))
        self.assertEqual(only_negative_inclusion, set([]))


# exclude_closes_with_trivial_variables(cnf, only_positive_inclusion, only_negative_inclusion)
class TestExcludeClosesWithTrivialVariables(unittest.TestCase):

    def test_exclude_closes_with_trivial_variables(self):
        cnf = {1: (1, -2), 2: (-1, 2), 3: (3, 4), 4: (3, -4), 5: (5, -6), 6: (-5, -6)}
        only_positive_inclusion, only_negative_inclusion = sat.get_trivial_variables(cnf)
        sat.exclude_closes_with_trivial_variables(cnf, only_positive_inclusion, only_negative_inclusion)
        self.assertEqual(cnf, {1: (1, -2), 2: (-1, 2)})

    def test_exclude_closes_with_trivial_variables_when_not_exist(self):
        cnf = {1: (1, -2), 2: (-1, 2), 3: (3, 4), 4: (-3, -4)}
        only_positive_inclusion, only_negative_inclusion = sat.get_trivial_variables(cnf)
        sat.exclude_closes_with_trivial_variables(cnf, only_positive_inclusion, only_negative_inclusion)
        self.assertEqual(cnf, {1: (1, -2), 2: (-1, 2), 3: (3, 4), 4: (-3, -4)})


# cnf_reduction(cnf)
class TestCnfReduction(unittest.TestCase):

    def test_cnf_reduction(self):
        cnf = {1: (1, -2), 2: (2, 3), 3: (3, -4), 4: (-3, 4)}
        sat.cnf_reduction(cnf)
        self.assertEqual(cnf, {3: (3, -4), 4: (-3, 4)})


# get_variable_set(cnf)
class TestGetVariableSet(unittest.TestCase):

    def test_get_variable_set(self):
        cnf = {1: (1, -2), 2: (2, 3), 3: (3, -4), 4: (-3, 4)}
        variable_set = sat.get_variable_set(cnf)
        self.assertEqual(variable_set, {1, 2, 3, 4})


# get_random_assignment(variable_set)
class TestGetRandomAssignment(unittest.TestCase):

    def test_get_random_assignment(self):
        variable_set = {1, 3, 5}
        random_assignment = sat.get_random_assignment(variable_set)
        sanity_flag = True
        for v in random_assignment:
            if v not in variable_set:
                sanity_flag = False
            if random_assignment[v] != 0 and random_assignment[v] != 1:
                sanity_flag = False
        for v in variable_set:
            if v not in random_assignment:
                sanity_flag = False
        self.assertEqual(sanity_flag, True)


# check_sat(cnf, variable_assignment)
class TestCheckSat(unittest.TestCase):

    def test_check_sat_true(self):
        cnf = {1: (1, -2), 2: (-1, 2), 3: (3, 4), 4: (-3, -4)}
        variable_assignment = {1: 1, 2: 1, 3: 1, 4: 0}
        res = sat.check_sat(cnf, variable_assignment)
        self.assertEqual(res, (True, 0))

    def test_check_sat_false(self):
        cnf = {1: (1, -2), 2: (-1, 2), 3: (3, 4), 4: (-3, -4)}
        variable_assignment = {1: 1, 2: 1, 3: 1, 4: 1}
        res = sat.check_sat(cnf, variable_assignment)
        self.assertEqual(res, (False, 4))


# get_2sat_status(cnf)
class TestGet2SatStatus(unittest.TestCase):

    def test_get_2sat_status_true(self):
        cnf = {1: (1, -2), 2: (-1, 2), 3: (3, 4), 4: (-3, -4)}
        res = sat.get_2sat_status(cnf)
        self.assertEqual(res, True)

    def test_get_2sat_status_false(self):
        cnf = {1: (1, -2), 2: (-1, 2), 3: (3, 4), 4: (3, -4), 5: (-3, 5), 6: (-3, -5)}
        res = sat.get_2sat_status(cnf)
        self.assertEqual(res, False)


if __name__ == '__main__':
    unittest.main()
