
# Abstract observer class
class Observer(object):
    def __init__(self, subject):
        subject.push_handlers(self)

class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state
