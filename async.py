import asyncio
import httpx
from pydantic import BaseModel, Extra

LINK = "https://pokeapi.co/api/v2/pokemon/"


class Info_poke(BaseModel):
    name: str
    id: int

    class Config:
        extra: Extra.allow


async def func_httpx(id_: int) -> Info_poke:
    url: str = "".join([LINK, str(id_)])
    async with httpx.AsyncClient() as client:
        get_request = await client.get(url)
        get_json = get_request.json()
    return Info_poke(name=get_json["name"], id=get_json["id"])


def print_pokemon(amount) -> Info_poke:
    for i in range(amount):
        i += 1
        result = func_httpx(i)
        yield result


async def main():
    result = print_pokemon(10)
    async_work = await asyncio.gather(*result)
    print(f"{async_work}")


if __name__ == "__main__":
    asyncio.run(main())
