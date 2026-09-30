import unittest
from datetime import date

from examples.agent_loop.main import run
from examples.eval_harness.main import evaluate
from examples.memory.main import Memory, MemoryStore
from examples.secure_tool_gateway.main import decide
from examples.tool_use.main import execute


class ExampleTests(unittest.TestCase):
    def test_agent_loop_stops(self):
        state = run("test")
        self.assertEqual(state.events[-1]["stop_reason"], "success")

    def test_tool_validation(self):
        self.assertEqual(execute("add", {"a": 2, "b": 3})["value"], 5)
        self.assertFalse(execute("add", {"a": 2})["ok"])

    def test_memory_requires_source(self):
        store = MemoryStore()
        with self.assertRaises(ValueError):
            store.remember(Memory("u", "x", "", 0.9, date(2027, 1, 1)))

    def test_eval_checks_trajectory(self):
        results = evaluate()
        self.assertTrue(results[0]["passed"])
        self.assertFalse(results[1]["passed"])

    def test_gateway_requires_approval(self):
        self.assertEqual(decide("send_email", {"to": "a"})["effect"], "approve")
        self.assertEqual(decide("delete_account", {})["effect"], "deny")


if __name__ == "__main__":
    unittest.main()
