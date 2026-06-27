import asyncio
from app.services.groq_service import generate_copy

sem = asyncio.Semaphore(3)

async def generate_platform_copy(
    product_name,
    platform,
    tone,
    build_prompt
):
    async with sem:

        prompt = build_prompt(
            product_name,
            platform,
            tone
        )

        return await asyncio.to_thread(
            generate_copy,
            prompt
        )