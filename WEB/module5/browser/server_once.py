import asyncio
import websockets
import platform


async def handler(websocket):
    data = await websocket.recv()
    reply = f"Data recieved as:  {data}!"
    print(reply)
    await websocket.send(reply)


async def main():
    async with websockets.serve(handler, "localhost", 8000):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
