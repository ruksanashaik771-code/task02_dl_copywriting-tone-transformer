from pydantic import BaseModel

class MarketingCopy(BaseModel):
    product_name: str
    product_description: str
    platform: str
    tone: str
    content: str