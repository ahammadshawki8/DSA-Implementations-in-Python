from euler_tour_class import *

class PreorderPrintIndentTour(EulerTour):
    def _hook_previsit(self,p,d,path):
        print(2*d*" "+str(p.element()))


class PreorderPrintIndentLabeledTour(EulerTour):
    def _hook_previsit(self,p,d,path):
        label = ".".join(str(j+1) for j in path)    # labels are one indexed
        print(2*d*" "+label,p.element())


class ParenthesizeTour(EulerTour):
    def _hook_previsit(self,p,d,path):
        if path and path[-1] > 0:       # p follows a sibling
            print(", ",end="")          # so preface with comma
        print(p.element(),end="")       # then print element
        if not self.tree().is_leaf(p):  # if p has children
            print(" (",end="")          # print opening parenthesis

    def _hook_postvisit(self,p,d,path,results):
        if not self.tree().is_leaf(p):  # if p has children
            print(")",end="")           # print closing paranthesis

class DiskSpaceTour(EulerTour):
    import sys
    space = sys.getsizeof
    def _hook_postvisit(self,p,d,path,results):
        # we simply add apace associated with p to that of its subtrees
        return p.element().space() + sum(results)
