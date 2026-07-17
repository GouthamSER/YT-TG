"""
Minimal MongoDB layer — stores cookies.txt content only.
"""
import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.environ.get("MONGO_URI", "")

enabled = bool(MONGO_URI)
_client = AsyncIOMotorClient(MONGO_URI) if enabled else None
_db     = _client["ytbot"] if enabled else None
_config = _db["config"] if enabled else None


async def get_cookies():
    """Return stored cookies.txt content, or None."""
    if not enabled:
        return None
    doc = await _config.find_one({"_id": "cookies"})
    return doc["data"] if doc else None


async def save_cookies(data: str) -> bool:
    """Upsert cookies.txt content into MongoDB."""
    if not enabled:
        return False
    await _config.update_one(
        {"_id": "cookies"},
        {"$set": {"data": data}},
        upsert=True,
    )
    return True
