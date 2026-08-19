from langgraph.graph import StateGraph, START, END

from app.agent.state import AgentState
from app.agent.nodes import retrieve_node, generate_node


def create_graph():
    """
    Construit le workflow LangGraph.
    """

    # Création du graphe
    graph = StateGraph(AgentState)

    # Ajout des nodes
    graph.add_node("retrieve", retrieve_node)
    graph.add_node("generate", generate_node)

    # Définition du workflow

    # START → retrieve
    graph.add_edge(START, "retrieve")

    # retrieve → generate
    graph.add_edge("retrieve", "generate")

    # generate → END
    graph.add_edge("generate", END)

    # Compilation du graphe
    return graph.compile()
