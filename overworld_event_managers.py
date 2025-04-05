from collections import deque

class OverworldEventManager:
    def __init__(self,map_input_lock):
        self.event_queue = deque()
        self.map_input_lock=map_input_lock

    def add_event(self, event_func, event_args=[], event_kwargs={},persistent_condition=None, condition_args=[],condition_kwargs={}):
        """Adds an event to the queue. If persistent_condition is provided, it persists."""
        self.event_queue.append((event_func, event_args, event_kwargs, persistent_condition,condition_args,condition_kwargs))

    def run_next_event(self):
        """Runs the next event if available, blocking further events if persistent."""
        if self.event_queue:
            event_func, event_args, event_kwargs, persistent_condition, condition_args,condition_kwargs=self.event_queue.popleft()
            event_func(*event_args, **event_kwargs)
            if persistent_condition:
                if persistent_condition(*condition_args,**condition_kwargs):
                    self.event_queue.appendleft((event_func, event_args, event_kwargs, persistent_condition,condition_args,condition_kwargs))
                else:
                    self.run_next_event()