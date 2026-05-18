from typing import TypedDict, List
#GraphState is a dictionary with fixed keys.TypeDict add rules

class GraphState(TypedDict):
    question :str
    chunks : List
    answer : str