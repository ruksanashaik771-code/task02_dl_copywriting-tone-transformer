import json
import asyncio
from pathlib import Path

from app.prompts.template import build_prompt
from app.services.async_service import (
    generate_platform_copy
)

async def main():
    products_file = Path(__file__).parent.parent / "products.json"

    with open(products_file, "r") as file:
        products = json.load(file)

    
    tasks = []

    for product in products:

        tasks.append(

            generate_platform_copy(
                product,
                "Instagram",
                "Funny",
                build_prompt
            )

        )

    results = await asyncio.gather(
        *tasks
    )

    for product, result in zip(
        products,
        results
    ):

        print("\n")
        print(product)
        print(result)

asyncio.run(main())