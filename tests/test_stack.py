"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):
    def test_stack_node(self):
        nodes_1 = Node(1, 3)
        nodes_2 = Node(0, 'a')
        self.assertEqual(type(nodes_1.data), int)
        self.assertEqual(type(nodes_2.next_node), str)

    def test_stack(self):
        stacks = Stack()
        stacks.push(1)
        stacks.push(3)
        self.assertEqual(len(stacks.list_stack), 2)
        stacks.pop()
        self.assertEqual(len(stacks.list_stack), 1)

if __name__ == '__main__':
    unittest.main()