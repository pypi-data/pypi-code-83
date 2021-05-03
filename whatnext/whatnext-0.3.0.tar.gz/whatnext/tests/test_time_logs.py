from ..data_model import TimeLog
from ..graph import create_graph
from ..parser import parse
from ..tests.test_class import WhatNextTestCase
from ..time_logs import create_timelog, delete_timelog, update_timelog_note


class TestCRUDTimeLogs(WhatNextTestCase):
    def test_create_and_start_task(self):
        graph = create_graph()

        command = "simple task"
        graph = parse(graph, command)

        # Assert graph structure is correct
        graph = create_timelog(graph, 0, note="test note")
        task = graph.nodes[0]["task"]
        time_logs = task.time_logs

        self.assertEqual(len(graph), 1)
        self.assertTupleEqual(tuple(graph.edges), ())
        self.assertIsInstance(time_logs, list)
        self.assertEqual(len(time_logs), 1)
        self.assertIsInstance(time_logs[0], TimeLog)
        self.assertEqual(time_logs[0].note, "test note")
        self.assertEqual(time_logs[0].task_id, 0)
        self.assertEqual(time_logs[0].user_id, task.user_id)
        self.assertIsNotNone(time_logs[0].start_time)

        # update timelog
        update_timelog_note(graph, task.task_id, 0, "updated note")
        self.assertEqual(time_logs[0].note, "updated note")

        # delete timelog
        delete_timelog(graph, task.task_id, 0)
        self.assertEqual(len(task.time_logs), 0)


if __name__ == "__main__":
    t = TestCRUDTimeLogs()
    t.setUpClass()
    t.test_create_and_start_task()
    t.tearDownClass()
