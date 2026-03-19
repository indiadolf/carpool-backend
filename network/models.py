from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Edge(models.Model):
    from_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="out_edges")
    to_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="in_edges")

    def __str__(self):
        return f"{self.from_node} -> {self.to_node}"