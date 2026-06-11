from langgraph.graph import StateGraph,END

from graph.state import AgentState
from graph.router import router
from nodes.SupervisorAgent import supervisor
from nodes.bank_node import banking_node
from nodes.search_node import search_node

graph = StateGraph(AgentState)

graph.add_node(
    'supervisor',supervisor
)
graph.add_node(
    'banking',banking_node
)
graph.add_node(
    'search',search_node
)

graph.set_entry_point(
    'supervisor'
)

graph.add_conditional_edges(
    'supervisor',
    router,
    {
        'banking':'banking',
        'search':'search',
        'end':END
    }
)

graph.add_edge(
    'banking',
    'supervisor'
)

graph.add_edge(
    'search',
    END
)

app = graph.compile()