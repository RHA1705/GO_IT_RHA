# from http import client


# h1 = client.HTTPConnection('localhost', 8001)
# print("Client start")
# h1.request("POST", "/")

# res = h1.getresponse()
# print(res.status, res.reason)

# data = res.read()
# print(data)
import asyncio


async def baz() -> str:
    print('Before Sleep')
    await asyncio.sleep(1)
    print('After Sleep')
    return 'Hello world'


async def main():
    r = baz()
    print(r)
    result = await r
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
