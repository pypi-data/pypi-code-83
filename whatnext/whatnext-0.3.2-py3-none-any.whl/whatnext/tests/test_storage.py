from ..data_model import Task
from ..graph import create_graph, load, save
from ..parser import parse
from ..tests.test_class import WhatNextTestCase


class TestStorage(WhatNextTestCase):
    def test_save_and_load(self):
        graph = create_graph()

        command = """Today, I Woke up ->
        fell out of bed ->
Dragged a comb across my head ->
Found my way downstairs -> drank a #cup ->
looking up -> I noticed I was late!!! ->
Found my coat & grabbed my hat ->
Made the #bus in seconds flat ->
Found my way upstairs -> had a smoke #TODO http://quitsmoking.com ->
@somebody spoke & I went into a dream!"""

        graph = parse(graph, command)

        # Assert graph structure is correct
        self.assertEqual(len(graph), 14)
        save(graph)

        graph2 = load()
        self.assertEqual(len(graph2), 14)

        self.assertEqual(set(graph.nodes), set(graph2.nodes))
        self.assertEqual(set(graph.edges), set(graph2.edges))

        for node_id in graph.nodes:
            self.assertIsInstance(graph2.nodes[node_id]["task"], Task)
            print(graph.nodes[node_id])
            self.assertEqual(
                graph.nodes[node_id]["task"].user_id,
                graph2.nodes[node_id]["task"].user_id,
            )
            self.assertEqual(
                graph.nodes[node_id]["task"].task_id,
                graph2.nodes[node_id]["task"].task_id,
            )
            self.assertEqual(
                graph.nodes[node_id]["task"].project,
                graph2.nodes[node_id]["task"].project,
            )
            self.assertEqual(
                graph.nodes[node_id]["task"].name, graph2.nodes[node_id]["task"].name
            )
            self.assertEqual(
                graph.nodes[node_id]["task"].importance,
                graph2.nodes[node_id]["task"].importance,
            )
            self.assertEqual(
                graph.nodes[node_id]["task"].completed,
                graph2.nodes[node_id]["task"].completed,
            )
            self.assertEqual(
                graph.nodes[node_id]["task"].due,
                graph2.nodes[node_id]["task"].due,
            )
            self.assertEqual(
                graph.nodes[node_id]["task"].tags or [],
                graph2.nodes[node_id]["task"].tags or [],
            )
            self.assertEqual(
                graph.nodes[node_id]["task"].urls or [],
                graph2.nodes[node_id]["task"].urls or [],
            )
            self.assertEqual(
                graph.nodes[node_id]["task"].users or [],
                graph2.nodes[node_id]["task"].users or [],
            )
            self.assertEqual(
                graph.nodes[node_id]["task"].notes or [],
                graph2.nodes[node_id]["task"].notes or [],
            )
            self.assertEqual(
                graph.nodes[node_id]["task"].time_logs or [],
                graph2.nodes[node_id]["task"].time_logs or [],
            )

    def test_dont_duplicate_existing(self):
        graph = create_graph()

        command = "hip -> hop"
        graph = parse(graph, command)

        command = "hip -> hop"
        graph = parse(graph, command)

        command = "hop -> yadont stop"
        graph = parse(graph, command)

        command = "0 -> 2"
        graph = parse(graph, command)

        # Assert graph structure is correct
        self.assertEqual(len(graph), 3)
        self.assertTupleEqual(tuple(graph.edges), ((0, 1), (0, 2), (1, 2)))

        # Assert properties are correct and are parsed into valid Tasks
        task_a = graph.nodes[0]["task"]
        task_b = graph.nodes[1]["task"]
        task_c = graph.nodes[2]["task"]

        self.assertIsInstance(task_a, Task)
        self.assertIsInstance(task_b, Task)
        self.assertIsInstance(task_c, Task)

        self.assertEqual(task_a.task_id, 0)
        self.assertEqual(task_b.task_id, 1)
        self.assertEqual(task_c.task_id, 2)

        self.assertEqual(task_a.name, "hip")
        self.assertEqual(task_b.name, "hop")
        self.assertEqual(task_c.name, "yadont stop")

        self.assertEqual(task_a.completed or None, None)
        self.assertEqual(task_b.completed or None, None)
        self.assertEqual(task_c.completed or None, None)

        self.assertEqual(task_a.due, None)
        self.assertEqual(task_b.due, None)
        self.assertEqual(task_c.due, None)

        self.assertEqual(task_a.tags, [])
        self.assertEqual(task_b.tags, [])
        self.assertEqual(task_c.tags, [])

        self.assertEqual(task_a.urls, [])
        self.assertEqual(task_b.urls, [])
        self.assertEqual(task_c.urls, [])

        self.assertEqual(task_a.users, [])
        self.assertEqual(task_b.users, [])
        self.assertEqual(task_c.users, [])

        self.assertEqual(task_a.notes, [])
        self.assertEqual(task_b.notes, [])
        self.assertEqual(task_c.notes, [])

        self.assertEqual(task_a.time_logs, None)
        self.assertEqual(task_b.time_logs, None)
        self.assertEqual(task_c.time_logs, None)


if __name__ == "__main__":
    t = TestStorage()
    t.setUpClass()
    t.test_save_and_load()
    t.tearDownClass()
