import json
from channels.generic.websocket import AsyncWebsocketConsumer


class GraphConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name = "graph_updates"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

 
    async def graph_update(self, event):
        await self.send(
            text_data=json.dumps(event["message"])
        )
