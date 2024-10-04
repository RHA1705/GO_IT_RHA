import asyncio
import logging
import platform
import websockets

logging.basicConfig(level=logging.INFO)


async def consumer(hostname: str, port: int):
    ws_resource_url = f"ws://{hostname}:{port}"
    async with websockets.connect(ws_resource_url) as ws:
        async for message in ws:
            logging.info("Message: %s", message)


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(consumer('localhost', 4000))
