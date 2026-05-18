from langgraph.graph import(
    StateGraph,#graph builder
    START,
    END
)
from app.graph.state import GraphState
from app.graph.nodes import(
    retrieval_node,
    generation_node
)
graph_builder = StateGraph(GraphState)

graph_builder.add_node(
    "retrieve",
    retrieval_node
)
graph_builder.add_node(
    "generate",
    generation_node
)

graph_builder.add_edge(
    START,
    "retrieve"
)

graph_builder.add_edge(
    "retrieve",
    "generate"
)

graph_builder.add_edge(
    "generate",
    END 
)

rag_graph = graph_builder.compile()