import unittest


class ChatServer():
    def __init__(self):


class Participant():
    def __init__(self, name):
        self.__name = name


class Test(unittest.TestCase):
    def test_chat_server(self):
        server = ChatServer()
        albert = Participant("Albert")
        jordi = Participant("Jordi")
        martha = Participant("Martha")
        kat = Participant("Kat")
        self.assertEqual(server.participants, set())
        server.join(albert)
        for i in xrange(12):
            server.send_all(albert, i)
        server.join(jordi)
        server.leave(jordi)
        server.join(martha)
        self.assertEqual(server.participants, {albert, martha})
        self.assertEqual(albert.history, [('Albert', i) for i in xrange(12)])
        self.assertEqual(martha.history, [('Albert', i)
                                          for i in xrange(4, 12)])
        self.assertEqual(jordi.history, [])
        server.send_all(martha, "AlphaGo's victory was surprising!")
        server.join(kat)
        server.send_all(kat, "It's too bad Arimaa didn't outlast Go.")
        self.assertEqual(kat.history[-1], albert.history[-1])


if __name__ == "__main__":
    unittest.main()
