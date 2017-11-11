from operator import itemgetter


def read_jobs(filename):
    """
    Read a list of jobs from a file.
    :param filename: source file name
    :return: list of jobs. Each job is a list of two elements: weight (wi), and length (li).
    """

    fp = open(filename)

    jobs = []

    one_line = fp.readline()
    total_jobs = int(one_line)
    one_line = fp.readline()

    while one_line != "":
        str_list = one_line.split()
        weight = int(str_list[0])
        length = int(str_list[1])
        greedy1 = weight - length
        greedy2 = float(weight)/float(length)
        job = [weight, length, greedy1, greedy2]
        jobs.append(job)
        one_line = fp.readline()

    if len(jobs) != total_jobs:
        print("Mismatch in number of jobs. Specified - %d, actual - %d" % (total_jobs, len(jobs)))
        exit(-1)

    return jobs


def greedy_by_difference(jobs):
    """
    
    :param jobs: list of jobs
    :return: weighted completion time
    """
    jobs_order = sorted(jobs, key=itemgetter(0), reverse=True)
    jobs_order.sort(key=itemgetter(2), reverse=True)

    return get_weighted_completion(jobs_order)


def greedy_by_ratio(jobs):
    """
    
    :param jobs: list of jobs
    :return: weighted completion time
    """

    jobs_order = sorted(jobs, key=itemgetter(0), reverse=True)
    jobs_order.sort(key=itemgetter(3), reverse=True)

    return get_weighted_completion(jobs_order)


def get_weighted_completion(jobs):
    """
    
    :param jobs: ordered list of jobs
    :return: weighted completion time for this list
    """

    completion_time = 0
    weighted_completion = 0

    for i in range(len(jobs)):
        weighted_completion += jobs[i][0] * (completion_time + jobs[i][1])
        completion_time += jobs[i][1]

    return weighted_completion


if __name__ == '__main__':
    jobs = read_jobs('tests/jobs.txt')
    score1 = greedy_by_difference(jobs)
    score2 = greedy_by_ratio(jobs)
    print("Using (w-l): %d" % score1)
    print("Using (w/l): %d" % score2)