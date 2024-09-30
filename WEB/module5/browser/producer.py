import asyncio
import websockets
import sys
import platform


async def producer(message: str, host: str, port: int):
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        await ws.send(message)


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(producer(message=sys.argv[1], host='localhost', port=4000))
