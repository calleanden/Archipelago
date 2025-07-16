import asyncio
import Utils
import websockets
import functools
from copy import deepcopy
from typing import List, Any, Iterable
from NetUtils import decode, encode, JSONtoTextParser, JSONMessagePart, NetworkItem, NetworkPlayer
from MultiServer import Endpoint
from CommonClient import CommonContext, gui_enabled, ClientCommandProcessor, logger, get_base_parser

DEBUG = False

class DDJSONToTextParser(JSONtoTextParser):
    def _handle_color(self, node):
        return self._handle_text(node)
    
class DDCommandProcessor(ClientCommandProcessor):
    def _cmd_dd(self):
        if isinstance(self.ctx, DDContext):
            logger.info(f"DD Status : {self.ctx.get_DD_status()}")
    
class DDContext(CommonContext):
    command_processor = DDCommandProcessor
    game = "Darkest Dungeon"

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.proxy = None
        self.proxy_task = None
        self.gamejsontotext = DDJSONToTextParser(self)
        self.autoreconnect_task = None
        self.endpoint = None
        self.items_handling = 0b111
        self.room_info = None
        self.connected_msg = None
        self.game_connected = False
        self.awaiting_info = False
        self.full_inventory: List[Any] = []
        self.server_msgs: List[Any] = []

    async def server_auth(self, password_requested = False):
        if password_requested and not self.password:
            await super(DDContext, self).server_auth(password_requested)

        await self.get_username()
        await self.send_connect()

    def get_dd_status(self):
        if not self.is_proxy_connected():
            return "Not connected to Darkest Dungeon"
        return "Connected to Darkest Dungeon"
    
    async def send_msgs_proxy(self, msgs: Iterable[dict]):
        if not self.endpoint or not self.endpoint.socket.open or self.endpoint.socket.closed:
            return False
        if DEBUG:
            logger.info(f"Outgoing message: {msgs}")
        await self.endpoint.socket.send(msgs)
        return True
    
    async def disconnect(self, allow_autoreconnect = False):
        await super().disconnect(allow_autoreconnect)

    async def disconnect_proxy(self):
        if self.endpoint and not self.endpoint.socket.closed:
            await self.endpoint.socket.close()
        if self.proxy_task is not None:
            await self.proxy_task