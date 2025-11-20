import datetime
import time
from typing import Literal

import requests

from mcp.server.fastmcp import FastMCP

# Create server
mcp = FastMCP("Weather Recommendation Bot")

@mcp.prompt(title="Outfit Choice Assistant")
def choose_outfit(style: str, time: Literal["today", "tomorrow"]) -> str:
    """
    Generate agent instructions for weather-dependent recommendations.

    :arg str style: The desired style of the outfit.
    :arg str time: The day to plan the outfit for.
    """
    return f"""
You are a helpful weather advisor providing personalized clothing recommendations.

INSTRUCTIONS:
- Use available tools to determine current location, time and weather to determine the appropriate clothing
- Use the users clothing inventory to give specific recommendations. 
- Only propose outfits the user has in their inventory; take into account their preference ratings!
- Plan the for this date: {time}
- Plan the in this style: {style}

Always base your advice on real-time weather data from the tools. Be succinct and minimal, and provide a to-the-point recommendation.
"""

@mcp.tool()
def get_clothing_inventory() -> list[tuple[str, str, str, int]]:
    """Get the clothing inventory of the user. Returns tuples of (category, item, color, preference rating)"""
    data = [
        ("jackets", "wool jacket", "charcoal gray", 5),
        ("jackets", "rain jacket", "navy blue", 4),
        ("jackets", "winter coat", "forest green", 4),
        ("jackets", "blazer", "midnight blue", 2),
        ("jackets", "denim jacket", "faded blue", 3),
        ("jackets", "windbreaker", "bright red", 4),
        ("jackets", "leather jacket", "black", 3),
        ("jackets", "puffer jacket", "olive green", 5),

        ("upper_layers", "t-shirt (short sleeve)", "white", 5),
        ("upper_layers", "t-shirt (long sleeve)", "heather gray", 4),
        ("upper_layers", "polo shirt", "cobalt blue", 3),
        ("upper_layers", "flannel shirt", "red plaid", 4),
        ("upper_layers", "dress shirt", "light blue", 2),
        ("upper_layers", "hoodie (lightweight)", "charcoal", 5),
        ("upper_layers", "hoodie (heavyweight)", "dark green", 4),
        ("upper_layers", "sweater (thin)", "cream", 4),
        ("upper_layers", "sweater (thick wool)", "oatmeal", 5),
        ("upper_layers", "cardigan", "burgundy", 3),
        ("upper_layers", "thermal base layer", "black", 4),

        ("lower_layers", "jeans (regular)", "indigo", 5),
        ("lower_layers", "jeans (thermal lined)", "dark wash", 4),
        ("lower_layers", "chinos", "khaki", 3),
        ("lower_layers", "cargo pants", "olive drab", 4),
        ("lower_layers", "shorts", "light gray", 5),
        ("lower_layers", "sweatpants", "charcoal", 4),
        ("lower_layers", "dress pants", "navy", 2),
        ("lower_layers", "leggings/base layer", "black", 3),

        ("footwear", "sneakers", "white", 5),
        ("footwear", "running shoes", "neon green", 4),
        ("footwear", "boots (waterproof)", "brown", 5),
        ("footwear", "boots (winter insulated)", "black", 4),
        ("footwear", "sandals", "tan", 3),
        ("footwear", "dress shoes", "oxblood", 2),
        ("footwear", "hiking boots", "dark brown", 4),

        ("accessories", "umbrella", "black", 5),
        ("accessories", "sunglasses", "matte black", 4),
        ("accessories", "baseball cap", "navy", 4),
        ("accessories", "beanie", "charcoal", 5),
        ("accessories", "sun hat (wide brim)", "beige", 3),
        ("accessories", "scarf (light)", "sky blue", 3),
        ("accessories", "scarf (wool)", "dark gray", 4),
        ("accessories", "gloves (light)", "black", 3),
        ("accessories", "gloves (winter insulated)", "navy", 4),
        ("accessories", "mittens", "red", 3),
        ("accessories", "neck gaiter", "dark green", 4),

        ("specialized", "rain pants", "black", 3),
        ("specialized", "snow pants", "charcoal", 4),
        ("specialized", "vest (puffer)", "navy", 4),
        ("specialized", "vest (fleece)", "gray", 3),
        ("specialized", "rain poncho", "yellow", 2),
        ("specialized", "ear muffs", "black", 3),
        ("specialized", "face mask (cold weather)", "dark gray", 4),
    ]
    return data

@mcp.tool()
def get_weather(city: str) -> list[dict[str, str | float | int]]:
    """Get weather forecast for a given city."""
    endpoint = "https://wttr.in"
    response = requests.get(f"{endpoint}/{city}?format=j1&2").json()
    data = []
    for day in response.get("weather", {}):
        date_str = day.get("date")
        for hr in day.get("hourly", []):
            dt = datetime.datetime.strptime(
                day.get("date")+" "+hr.get("time", "0").zfill(4),
                "%Y-%m-%d %H%M"
            )
            data.append({
                "datetime": dt.isoformat(),
                "temp": int(hr.get("tempC")),
                "feelsLike": int(hr.get("FeelsLikeC")),
                "precipChance": max(
                    int(hr.get("chanceofrain", 0)),
                    int(hr.get("chanceofsnow", 0))
                ),
                "uvIndex": int(hr.get("uvIndex", 0)),
                "windKmph": int(hr.get("windspeedKmph", 0)),
                "windGustKmph": int(hr.get("WindGustKmph", 0)),
                "cloudCover": int(hr.get("cloudcover", 0)),
                "weather": hr.get("weatherDesc", [{"value": ""}])[0]["value"].strip()
            })
    return data

@mcp.tool()
def get_current_time() -> str:
    """Get current time."""
    return time.strftime("%I:%M:%S %p")

@mcp.tool()
def get_location() -> str:
    """Get current location."""
    endpoint = "https://ipinfo.io"
    response = requests.get(f"{endpoint}")
    return response.json()["city"]


if __name__ == "__main__":
    mcp.run(transport="streamable-http")