import datetime

from ..data_model import Task
from ..graph import create_graph
from ..parser import parse
from ..tests.test_class import WhatNextTestCase


class TestCreateTasks(WhatNextTestCase):
    def test_create_multiple_tasks(self):
        graph = create_graph()

        command = "A! @seankruzel http://twitter.com -> B #gold!! & C by 2020/02/20 -> D @john @jeff"
        graph = parse(graph, command)

        # Assert graph structure is correct
        self.assertEqual(len(graph), 4)
        self.assertTupleEqual(tuple(graph.edges), ((0, 1), (0, 2), (1, 3), (2, 3)))

        # Assert properties are correct and are parsed into valid Tasks
        task_a = graph.nodes[0]["task"]
        task_b = graph.nodes[1]["task"]
        task_c = graph.nodes[2]["task"]
        task_d = graph.nodes[3]["task"]

        self.assertIsInstance(task_a, Task)
        self.assertIsInstance(task_b, Task)
        self.assertIsInstance(task_c, Task)
        self.assertIsInstance(task_d, Task)

        self.assertEqual(task_a.task_id, 0)
        self.assertEqual(task_b.task_id, 1)
        self.assertEqual(task_c.task_id, 2)
        self.assertEqual(task_d.task_id, 3)

        self.assertEqual(task_a.importance, 1)
        self.assertEqual(task_b.importance, 2)
        self.assertEqual(task_c.importance, 0)
        self.assertEqual(task_d.importance, 0)

        self.assertEqual(task_a.name, "A! @seankruzel http://twitter.com")
        self.assertEqual(task_b.name, "B #gold!!")
        self.assertEqual(task_c.name, "C by 2020/02/20")
        self.assertEqual(task_d.name, "D @john @jeff")

        self.assertEqual(task_a.completed or None, None)
        self.assertEqual(task_b.completed or None, None)
        self.assertEqual(task_c.completed or None, None)
        self.assertEqual(task_d.completed or None, None)

        self.assertEqual(task_a.due, None)
        self.assertEqual(task_b.due, None)
        self.assertEqual(task_c.due, datetime.datetime(2020, 2, 20))
        self.assertEqual(task_d.due, None)

        self.assertEqual(task_a.tags, [])
        self.assertEqual(task_b.tags, ["#gold"])
        self.assertEqual(task_c.tags, [])
        self.assertEqual(task_d.tags, [])

        self.assertEqual(task_a.urls, ["http://twitter.com"])
        self.assertEqual(task_b.urls, [])
        self.assertEqual(task_c.urls, [])
        self.assertEqual(task_d.urls, [])

        self.assertEqual(task_a.users, ["@seankruzel"])
        self.assertEqual(task_b.users, [])
        self.assertEqual(task_c.users, [])
        self.assertEqual(task_d.users, ["@john", "@jeff"])

        self.assertEqual(task_a.notes, [])
        self.assertEqual(task_b.notes, [])
        self.assertEqual(task_c.notes, [])
        self.assertEqual(task_d.notes, [])

        self.assertEqual(task_a.time_logs, None)
        self.assertEqual(task_b.time_logs, None)
        self.assertEqual(task_c.time_logs, None)
        self.assertEqual(task_d.time_logs, None)

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
    t = TestCreateTasks()
    t.setUpClass()
    t.test_create_multiple_tasks()
    t.test_dont_duplicate_existing()
    t.tearDownClass()
