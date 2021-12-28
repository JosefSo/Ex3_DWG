from unittest import TestCase

from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        a_algo = GraphAlgo()
        file = "../data/G1.json"
        a_algo.load_from_json(file)
        a = a_algo.get_graph().v_size()
        self.assertEqual(a, 17)

    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_dijkstra(self):
        a_algo = GraphAlgo()
        file = "../data/G1.json"
        a_algo.load_from_json(file)
        a = a_algo.dijkstra(0)
        var = len(a)
        self.assertEqual(var, 2)

    def test_shortest_path(self):
        a_algo = GraphAlgo()
        file = "../data/G1.json"
        a_algo.load_from_json(file)
        d,l = a_algo.shortest_path(1, 5)
        self.assertEqual(5.091901160431474,d)
        self.assertEqual(1, l[0].getId())
        self.assertEqual(2, l[1].getId())
        self.assertEqual(6, l[2].getId())
        self.assertEqual(5, l[3].getId())


    def test_tsp(self):
        self.fail()

    def test_center_point(self):
        algo = GraphAlgo()
        file = "../data/G1.json"
        algo.load_from_json(file)
        c,d= algo.centerPoint()
        self.assertEqual(8,c)
        self.assertEqual(9.925289024973141, d)

        algo = GraphAlgo()
        file = "../data/G2.json"
        algo.load_from_json(file)
        c, d = algo.centerPoint()
        self.assertEqual(0, c)
        self.assertEqual(7.819910602212574, d)

        algo = GraphAlgo()
        file = "../data/G3.json"
        algo.load_from_json(file)
        c, d = algo.centerPoint()
        self.assertEqual(40, c)
        self.assertEqual(9.291743173960954, d)

        algo = GraphAlgo()
        file = "../data/1000Nodes.json"
        algo.load_from_json(file)
        c, d = algo.centerPoint()
        self.assertEqual(362, c)
        self.assertEqual(1185.9594924690523, d)