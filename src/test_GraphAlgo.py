from unittest import TestCase

from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        algo = GraphAlgo()
        file = "../data/G1.json"
        algo.load_from_json(file)
        a=str(algo.get_graph())
        self.assertEqual("Graph: |V|=17, |E|=36", a)

    def test_load_from_json(self):
        algo = GraphAlgo()
        file = "../data/G1.json"
        algo.load_from_json(file)
        a = algo.get_graph().v_size()
        self.assertEqual(17,a)

        algo = GraphAlgo()
        file = "../data/G2.json"
        algo.load_from_json(file)
        a = algo.get_graph().v_size()
        self.assertEqual(31, a)

        algo = GraphAlgo()
        file = "../data/G3.json"
        algo.load_from_json(file)
        a = algo.get_graph().v_size()
        self.assertEqual(48, a)

        algo = GraphAlgo()
        file = "../data/10000Nodes.json"
        algo.load_from_json(file)
        a = algo.get_graph().v_size()
        self.assertEqual(10000, a)

        algo = GraphAlgo()
        file = "../data/10000Nodes.json"
        algo.load_from_json(file)
        a = algo.get_graph().v_size()
        self.assertEqual(10000, a)

        algo = GraphAlgo()
        file = "../data/100000Nodes.json"
        algo.load_from_json(file)
        a = algo.get_graph().v_size()
        self.assertEqual(100000, a)

    def test_save_to_json(self):
        # algo = GraphAlgo()
        # file = "../data/G1.json"
        # file2 = "../data/Saved_for_test_G1"
        # algo.load_from_json(file)
        # algo.save_to_json(file2)
        # algo.load_from_json(file2+".json")
        # a = algo.get_graph().v_size()
        # self.assertEqual(17, a)
        #
        # algo = GraphAlgo()
        # file = "../data/G2.json"
        # file2 = "../data/Saved_for_test_G2"
        # algo.load_from_json(file)
        # algo.save_to_json(file2)
        # algo.load_from_json(file2+".json")
        # a = algo.get_graph().v_size()
        # self.assertEqual(31, a)
        #
        # algo = GraphAlgo()
        # file = "../data/G3.json"
        # file2 = "../data/Saved_for_test_G3"
        # algo.load_from_json(file)
        # algo.save_to_json(file2)
        # algo.load_from_json(file2+".json")
        # a = algo.get_graph().v_size()
        # self.assertEqual(48, a)
        #
        # algo = GraphAlgo()
        # file = "../data/1000Nodes.json"
        # file2 = "../data/Saved_for_test_1000Nodes"
        # algo.load_from_json(file)
        # algo.save_to_json(file2)
        # algo.load_from_json(file2+".json")
        # a = algo.get_graph().v_size()
        # self.assertEqual(1000, a)
        #
        # algo = GraphAlgo()
        # file = "../data/10000Nodes.json"
        # file2 = "../data/Saved_for_test_10000Nodes"
        # algo.load_from_json(file)
        # algo.save_to_json(file2)
        # algo.load_from_json(file2+".json")
        # a = algo.get_graph().v_size()
        # self.assertEqual(10000, a)

        algo = GraphAlgo()
        file = "../data/100000Nodes.json"
        file2 = "../data/Saved_for_test_100000Nodes"
        algo.load_from_json(file)
        algo.save_to_json(file2)
        algo.load_from_json(file2+".json")
        a = algo.get_graph().v_size()
        self.assertEqual(100000, a)

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
        d,l = a_algo.shortest_path(0,16)
        self.assertEqual(1.3118716362419698,d)
        self.assertEqual(0, l[0].getId())
        self.assertEqual(16, l[1].getId())

        a_algo = GraphAlgo()
        file = "../data/G2.json"
        a_algo.load_from_json(file)
        d,l = a_algo.shortest_path(0,30)
        self.assertEqual(7.043765863063326,d)
        self.assertEqual(0, l[0].getId())
        self.assertEqual(16, l[1].getId())
        self.assertEqual(15, l[2].getId())
        self.assertEqual(14, l[3].getId())
        self.assertEqual(13, l[4].getId())
        self.assertEqual(30, l[5].getId())

        a_algo = GraphAlgo()
        file = "../data/G3.json"
        a_algo.load_from_json(file)
        d, l = a_algo.shortest_path(0, 47)
        self.assertEqual(17.146479706314675, d)
        self.assertEqual(0, l[0].getId())
        self.assertEqual(2, l[1].getId())
        self.assertEqual(3, l[2].getId())
        self.assertEqual(13, l[3].getId())
        self.assertEqual(14, l[4].getId())
        self.assertEqual(15, l[5].getId())
        self.assertEqual(39, l[6].getId())
        self.assertEqual(40, l[7].getId())
        self.assertEqual(41, l[8].getId())
        self.assertEqual(42, l[9].getId())
        self.assertEqual(43, l[10].getId())
        self.assertEqual(44, l[11].getId())
        self.assertEqual(46, l[12].getId())
        self.assertEqual(47, l[13].getId())

        a_algo = GraphAlgo()
        file = "../data/G3.json"
        a_algo.load_from_json(file)
        d, l = a_algo.shortest_path(0, 47)
        self.assertEqual(17.146479706314675, d)
        self.assertEqual(0, l[0].getId())
        self.assertEqual(2, l[1].getId())
        self.assertEqual(3, l[2].getId())
        self.assertEqual(13, l[3].getId())
        self.assertEqual(14, l[4].getId())
        self.assertEqual(15, l[5].getId())
        self.assertEqual(39, l[6].getId())
        self.assertEqual(40, l[7].getId())
        self.assertEqual(41, l[8].getId())
        self.assertEqual(42, l[9].getId())
        self.assertEqual(43, l[10].getId())
        self.assertEqual(44, l[11].getId())
        self.assertEqual(46, l[12].getId())
        self.assertEqual(47, l[13].getId())

        a_algo = GraphAlgo()
        file = "../data/1000Nodes.json"
        a_algo.load_from_json(file)
        d, l = a_algo.shortest_path(0, 999)
        self.assertEqual(672.951969037067, d)
        self.assertEqual(0, l[0].getId())
        self.assertEqual(769, l[1].getId())
        self.assertEqual(631, l[2].getId())
        self.assertEqual(195, l[3].getId())
        self.assertEqual(765, l[4].getId())
        self.assertEqual(661, l[5].getId())
        self.assertEqual(999, l[6].getId())

        a_algo = GraphAlgo()
        file = "../data/10000Nodes.json"
        a_algo.load_from_json(file)
        d, l = a_algo.shortest_path(0, 9999)
        self.assertEqual(1165.776078062164, d)
        self.assertEqual(0, l[0].getId())
        self.assertEqual(3744, l[1].getId())
        self.assertEqual(3730, l[2].getId())
        self.assertEqual(1877, l[3].getId())
        self.assertEqual(1339, l[4].getId())
        self.assertEqual(7476, l[5].getId())
        self.assertEqual(698, l[6].getId())
        self.assertEqual(6391, l[7].getId())
        self.assertEqual(9495, l[8].getId())
        self.assertEqual(2605, l[9].getId())
        self.assertEqual(9999, l[10].getId())

        a_algo = GraphAlgo()
        file = "../data/100000Nodes.json"
        a_algo.load_from_json(file)
        d, l = a_algo.shortest_path(0, 99999)
        print(l)
        self.assertEqual(725.678538356026, d)
        self.assertEqual(0, l[0].getId())
        self.assertEqual(59017, l[1].getId())
        self.assertEqual(44285, l[2].getId())
        self.assertEqual(61320, l[3].getId())
        self.assertEqual(80938, l[4].getId())
        self.assertEqual(83057, l[5].getId())
        self.assertEqual(53892, l[6].getId())
        self.assertEqual(56568, l[7].getId())
        self.assertEqual(68981, l[8].getId())
        self.assertEqual(30964, l[9].getId())
        self.assertEqual(23253, l[10].getId())
        self.assertEqual(50548, l[11].getId())
        self.assertEqual(97499, l[12].getId())
        self.assertEqual(99999, l[13].getId())

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
        #
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

        algo = GraphAlgo()
        file = "../data/10000Nodes.json"
        algo.load_from_json(file)
        c, d = algo.centerPoint()
        self.assertEqual(362, c)
        self.assertEqual(1185.9594924690523, d)

