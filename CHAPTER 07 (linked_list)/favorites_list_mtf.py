from favourites_list import *
from positional_list import *

class FavouritesListMTF(FavouritesList):
    """List of elements odered with move-to-front heuristic."""

    # we override _move_up provide move to front semantics.
    def _move_up(self,p):
        """Move accesses item at Position p to frony of the list."""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))  # delete/insert

    # we overide top because list is no longer sorted
    def top(self,k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1<=k<=len(self):
            raise ValueError("Illegal value for k")

        # we begin to make a copy of original list
        temp = PositionalList()
        for item in self._data:             # positional list supports iteration
            temp.add_last(item)

        # we repeatedly find, report and remove element with largest count
        for j in range(k):
            # find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            # we have found the element with highest count
            yield highPos.element()._value  # report element to user
            temp.delete(highPos)            # remove form temp list

