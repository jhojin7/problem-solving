import inspect
import json

class Solver:
    """ Leetcode Solver. 
    Runs the LAST METHOD in Solution class 
    and returns its return values.
    **TARGET METHOD MUST BE POSITIONED AT THE END** """
    # def __init__(self,input,method_name):
    #     print("solver called for {method_name}")
    #     self.input = input

    def solve(Solution, args):
        if Solution is None or args is None:
            return
        cl = Solution
        members = inspect.getmembers(cl)

        # target function MUST ALWAYS be the last one
        target_method = members[-1]
        (name, f) = target_method
        _output = f(cl,(args))

        ret = json.dumps({
            'name':name,
            'input':args,
            'output':_output
        })
        return ret