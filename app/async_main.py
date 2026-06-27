import asyncio

from app.prompts.template import build_prompt
from app.services.async_service import (
    generate_platform_copy
)

async def main():

    product = input(
        "Enter Product Name: "
    )

    tone = input(
        "Enter Tone: "
    )

    platforms = [
        "Instagram",
        "LinkedIn",
        "Email"
    ]

    tasks = [

        generate_platform_copy(
            product,
            platform,
            tone,
            build_prompt
        )

        for platform in platforms
    ]

    results = await asyncio.gather(
        *tasks
    )

    for platform, result in zip(
        platforms,
        results
    ):
        print("\n")
        print("=" * 40)
        print(platform)
        print("=" * 40)
        print(result)

asyncio.run(main())