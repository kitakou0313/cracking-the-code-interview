import unittest


def buildOrder(projects, dependencies):
    jobs = {}
    for job in projects:
        jobs[job] = gNode(job)

    for d in dependencies:
        jobs[d[1]].addEdge(jobs[d[0]])

    q = Queue()
    for job in jobs.values():
        if job.dependenciesNum == 0:
            q.add(job)
    ansOrder = []

    if not(q.is_not_empty()):
        return False

    while q.is_not_empty():
        job = q.remove()
        for njob in job.nextJobs:
            njob.dependenciesNum -= 1
            if njob.dependenciesNum < 0:
                return False
            if njob.dependenciesNum == 0:
                q.add(njob)

        ansOrder.append(job.data)

    return ansOrder if len(ansOrder) == len(projects) else Exception("Cycle detected")


class gNode():
    def __init__(self, data):
        self.data = data
        self.dependenciesNum = 0
        self.nextJobs = []

    def addEdge(self, nextJob):
        self.nextJobs.append(nextJob)
        nextJob.dependenciesNum += 1


class Queue():
    def __init__(self):     self.array = []
    def add(self, item):    self.array.append(item)
    def remove(self): return self.array.pop(0)
    def is_not_empty(self): return len(self.array) > 0


class Test(unittest.TestCase):
    def test_buildOrder(self):
        projects = ["A", "B", "C", "D", "E", "F", "G"]
        dependencies1 = [("C", "A"), ("B", "A"), ("F", "A"), ("F", "B"), ("F", "C"),
                         ("A", "E"), ("B", "E"), ("D", "G")]
        dependencies1 = [("A", "C"), ("A", "B"), ("A", "F"), ("B", "F"), ("C", "F"),
                         ("E", "A"), ("E", "B"), ("G", "D")]
        self.assertEqual(buildOrder(projects, dependencies1),
                         ["D", "F", "G", "B", "C", "A", "E"])
        dependencies2 = [("A", "B"), ("B", "C"), ("C", "D"),
                         ("D", "A"), ("A", "G")]
        self.assertEqual(buildOrder(
            projects, dependencies2).__class__, Exception)
        dependencies3 = [("A", "B"), ("A", "C"), ("E", "A"), ("E", "B"), ("A", "F"),
                         ("B", "F"), ("C", "F"), ("G", "D")]
        dependencies3 = [("B", "A"), ("C", "A"), ("A", "E"), ("B", "E"), ("F", "A"),
                         ("F", "B"), ("F", "C"), ("D", "G")]
        self.assertEqual(buildOrder(projects, dependencies3),
                         ["E", "G", "A", "D", "B", "C", "F"])


if __name__ == "__main__":
    unittest.main()
