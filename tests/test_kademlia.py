import time

import pytest

from kademlia import Kademlia


@pytest.fixture
def nodes():
    node1 = Kademlia("127.0.0.1", 5001)
    node2 = Kademlia("127.0.0.1", 5002, register_to=node1)
    return node1, node2


def test_ping(nodes):
    node1, node2 = nodes

    node1.ping(node2)

    assert node1.received_jobs[-1] == {
            "job_type": "pong",
            "sender": node2.id,
    }

    assert node2.received_jobs[-1] == {
            "job_type": "ping",
            "sender": node1.id,
    }

    assert False

#def test_key_propagation(nodes):
#    node1, node2 = nodes
#
#    node1["awesome-key"] = "cool-value"
#    assert node2["awesome-key"] == "cool-value"
