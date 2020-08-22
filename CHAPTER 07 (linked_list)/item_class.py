class _Item:
    __slots__ = "_value", "_count"          # streamline memory usage
    def __init__(self,e):
        self._value = e                     # the user's element
        self.count = 0                      # access count initially zero
