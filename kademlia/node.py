import sha


class Node(object):
    @staticmethod
    def hash_it(value):
        return sha.new(value).hexdigest()
