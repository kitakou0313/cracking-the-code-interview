import unittest


class CallCenter():
    def __init__(self, respondents, managers, directors):
        self.respondents, self.managers, self.director = respondents, managers, directors
        self.respondentsQueue = []
        self.callQueue = []

        for respondent in self.respondents:
            respondent.callCenter = self
            if respondent.call is None:
                self.respondentsQueue.append(respondent)

        for manager in self.managers:
            manager.callCenter = self

        self.director.callCenter = self

    def route_call(self, call):
        if len(self.respondentsQueue) == 0:
            self.callQueue.append(call)
        else:
            self.respondentsQueue.pop(0).takeWork(call)

    def routeRespondant(self, respondent):
        if len(self.callQueue) == 0:
            self.respondentsQueue.append(respondent)
        else:
            respondent.takeWork(self.callQueue.pop(0))


class Call():
    def __init__(self, job):
        self.issue = job
        self.employee = None

    def resolve(self, handle):
        if handle:
            self.issue = None
            self.employee.finishWork()
        else:
            self.employee.escalate(self)


class Employee():
    def __init__(self, name, boss=None):
        self.name, self.boss = name, boss
        self.call = None
        self.callCenter = None

    def takeWork(self, call):
        self.call = call
        call.employee = self

    def finishWork(self):
        self.call = None
        self.callCenter.routeRespondant(self)


class Respondent(Employee):
    def escalate(self, call):
        self.boss.takeWork(call)
        self.call = None
        self.callCenter.routeRespondant(self)

    def finishWork(self):
        self.call = None
        self.callCenter.routeRespondant(self)


class Director(Employee):
    def escalate(self, call):
        self.boss.takeWork(call)
        self.call = None

    def finishWork(self):
        self.call = None


class Manager(Employee):
    def escalate(self, call):
        self.boss.takeWork(call)
        self.call = None

    def finishWork(self):
        self.call = None


class Test(unittest.TestCase):
    def test_call_center(self):
        lashaun = Director("Lashaun")

        juan = Manager("Juan", lashaun)
        sally = Manager("Sally", lashaun)

        boris = Respondent("Boris", juan)
        sam = Respondent("Sam", juan)
        jordan = Respondent("Jordan", sally)
        casey = Respondent("Casey", sally)

        center = CallCenter([boris, sam, jordan, casey],
                            [juan, lashaun], sally)

        call1 = Call("The toilet")
        call2 = Call("The webpage")
        call3 = Call("The email")
        call4 = Call("The lizard")
        call5 = Call("The cloudy weather")
        call6 = Call("The noise")

        self.assertEqual(len(center.respondentsQueue), 4)
        center.route_call(call1)
        center.route_call(call2)
        self.assertEqual(len(center.respondentsQueue), 2)
        center.route_call(call3)
        center.route_call(call4)
        center.route_call(call5)
        center.route_call(call6)
        self.assertEqual(center.callQueue, [call5, call6])
        call1.resolve(True)
        self.assertEqual(call1.issue, None)
        self.assertEqual(len(center.callQueue), 1)
        self.assertEqual(sally.call, None)
        self.assertEqual(lashaun.call, None)

        call4.resolve(False)
        self.assertEqual(sally.call, call4)

        call4.resolve(False)
        self.assertEqual(sally.call, None)
        self.assertEqual(lashaun.call, call4)

        call4.resolve(True)
        self.assertEqual(lashaun.call, None)

        call6.resolve(True)
        self.assertEqual(len(center.respondentsQueue), 1)


if __name__ == "__main__":
    unittest.main()
