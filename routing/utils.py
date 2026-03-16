from collections import deque
from network.models import Node, Edge


def shortest_path(start_node, end_node):

    queue = deque([[start_node]])
    visited = set()

    while queue:

        path = queue.popleft()
        node = path[-1]

        if node == end_node:
            return path

        edges = Edge.objects.filter(source=node)

        for edge in edges:

            next_node = edge.destination

            if next_node not in visited:

                visited.add(next_node)
                new_path = list(path)
                new_path.append(next_node)

                queue.append(new_path)

    return None