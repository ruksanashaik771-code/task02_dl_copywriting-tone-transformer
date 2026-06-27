from app.prompts.template import build_prompt
from app.services.groq_service import generate_copy
from app.models.marketing_copy import MarketingCopy

product_name = input("Enter Product Name: ")

product_description = input(
    "Enter Product Description: "
)

platform = input("Enter Platform: ")

tone = input("Enter Tone: ")

prompt = build_prompt(
    product_name,
    product_description,
    platform,
    tone
)

result = generate_copy(prompt)

marketing_copy = MarketingCopy(
    product_name=product_name,
    product_description=product_description,
    platform=platform,
    tone=tone,
    content=result
)

print(marketing_copy.model_dump_json(indent=4))