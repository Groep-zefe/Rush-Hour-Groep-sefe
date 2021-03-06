import time

# Used source: https://realpython.com/python-timer/


class Timer:
    def __init__(self):
        """ Keeps track of the time your code is running."""
        
        self._start_time = None


    def start(self):
        """Start a new timer."""

        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()


    def stop(self):
        """Stop the timer, and report the runtime."""
        
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        # This part we add ourself
        minutes = elapsed_time / 60
        seconds = elapsed_time % 60
        self._start_time = None
        print(f"Runtime: {minutes:0.0f} minutes and {seconds:0.4f} seconds")
