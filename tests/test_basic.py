import unittest
from loopexec import ExecChecker
import time


def fun(collection_size, interrupt):
    """
    :param collection_size: number of elements in the collection
    :param interrupt: a number of an iteration, during which the status should be returned
    :return: a status bar representation of the progress of the for loop
    """
    ec = ExecChecker(collection_size)
    if interrupt == 0:
        return ec.status_bar
    counter = 0
    for _ in range(collection_size):
        # operations inside the loop
        time.sleep(.2)
        ec.update()
        counter += 1
        if counter == interrupt:
            return ec.status_bar
    return ec.status_bar


class MyTest(unittest.TestCase):
    """Unit test for ExecChecker, testing:
    (1) behaviour on invalid input - not positive number of elements in collection
    (2) status before entering the loop
    (3) status during the execution of the for loop
    (4) status at the end of the execution
    """

    def test_empty_collection(self):
        self.assertRaises(Exception, fun(0, 10))

    def test_init(self):
        self.assertEqual(fun(10, 0), 'Loop about to begin')

    def test_interrupt_middle(self):
        self.assertEqual(fun(10, 5), '|' + '.'*50 + ' '*50 + '|')

    def test_interrupt_end(self):
        self.assertEqual(fun(10, 10), '|' + '.'*100 + '|')
