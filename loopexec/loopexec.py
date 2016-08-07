from time import time


class ExecChecker(object):
    """Class for measuring a for loop progress and estimation of completion time
    Args:
        collection_size (int): number of elements in the collection, >0
        start (float): timestamp of the start of the execution of the for loop
        elapsed (float): time spent in the loop so far
        iterations (int): number of completer iteration in the for loop
        status_bar (str): ASCII replresentation of a progress bar
        status (str): full output, containing status bas and estimated time of completion
    """
    def __init__(self, collection_size):
        self._collection_size = collection_size
        self.start = time()
        self.elapsed = 0.0
        self.iterations = 0
        self.status_bar = "Loop about to begin"
        self.status = self.status_bar
        print self

    def __str__(self):
        return self.status

    @property
    def collection_size(self):
        return self._collection_size

    @collection_size.setter
    def collection_size(self, v):
        """collection_size validation: must be a positive integer"""
        if not (v > 0):
            raise Exception("value must be greater than zero")
        self._collection_size = v

    def update(self):
        """ function to be called at the end of each iteration,
        updating elapsed time and prediction about completion time
        """
        iter_end = time()
        self.elapsed = iter_end - self.start
        self.iterations += 1
        elapsed_pct = int(float(self.iterations) * 100 / float(self.collection_size))
        remaining = self.elapsed*((float(self.collection_size) - float(self.iterations)) / float(self.iterations))
        self.statement(self.start, iter_end, elapsed_pct, remaining)
        print self

    def statement(self, start, end, elapsed_pct, remaining):
        """
        :param start: time at the beginning of the execution of the for loop
        :param end: end of latest completed iteration
        :param elapsed_pct: number in % of iterations completed
        :param remaining: predicted time until completion (in seconds)
        :return:
        """
        st = ' elapsed: {0}, completion in: {1}     '.format(int(end - start), int(remaining))
        self.status_bar = '|' + '.'*elapsed_pct + ' '*(100-elapsed_pct) + '|'
        self.status = self.status_bar + st + ' \r'
