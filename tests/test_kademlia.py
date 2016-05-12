from kademlia import Kademlia


def test_key_propagation():
    node1 = Kademlia("127.0.0.1", 5001)
    node2 = Kademlia("127.0.0.1", 5001, register_to=node1)

    node1["awesome-key"] = "cool-value"
    assert node2["awesome-key"] == "cool-value"
