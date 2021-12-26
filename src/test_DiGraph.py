from unittest import TestCase

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
class TestDiGraph(TestCase):
    def test_v_size(self):
        g_algo = GraphAlgo()
        file = "../data/G1.json"
        g_algo.load_from_json(file)
        a = g_algo.get_graph().v_size()
        self.assertEqual(a, 17)


    def test_e_size(self):
        g_algo = GraphAlgo()
        file = "../data/G1.json"
        g_algo.load_from_json(file)
        a = g_algo.get_graph().e_size()
        self.assertEqual(a, 36)

    def test_get_all_v(self):
        g_algo = GraphAlgo()
        file = "../data/G1.json"
        g_algo.load_from_json(file)
        a = g_algo.get_graph().get_all_v()
        i=0
        for k,v in a.items():
            self.assertEqual(v.getId(),i)
            self.assertEqual(k,i)
            i=i+1

    def test_all_in_edges_of_node(self):
        g_algo = GraphAlgo()
        file = "../data/G1.json"
        g_algo.load_from_json(file)
        a = g_algo.get_graph().all_in_edges_of_node(1).keys()
        self.assertEqual(a, {0,2})


    def test_all_out_edges_of_node(self):
        g_algo = GraphAlgo()
        file = "../data/G1.json"
        g_algo.load_from_json(file)
        a = g_algo.get_graph().all_out_edges_of_node(1).keys()
        self.assertEqual(a, {0, 2})

    def test_get_mc(self):


    def test_add_edge(self):
        self.fail()

    def test_add_node(self):
        self.fail()

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()
