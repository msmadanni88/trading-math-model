"""The team. To add an agent: write a class with the Agent interface and list
it here. Nothing else in the code base needs to change - the orchestrator
starts weighting a new forecast agent as soon as it produces forecasts."""
from .baseline import Empirical
from .learners import Lgbm, OnlineQR
from .regime import BocpdAgent, Hmm
from .shape import WickAgent
from .volatility import Ewma, Garch, Har


def forecast_agents(d):
    """d: length of the feature vector."""
    return [Empirical(), Ewma(), Garch(), Har(), BocpdAgent(), Hmm(), OnlineQR(d), Lgbm()]


def shape_agents(d):
    return [WickAgent(d)]


def signal_agents():
    """Reserved for agents that publish signals on the blackboard
    (cross-asset lead, trend state, volume profile, ...). See ARCHITECTURE.md."""
    return []
