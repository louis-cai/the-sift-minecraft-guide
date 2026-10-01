#!/usr/bin/env python3
import urllib.request, json

token = "71e10afa6e52c00104a33ad40d8c00fd1d0481033d977ccdaaf53588a744"

# Content as DOM nodes for Telegraph API
content = [
    {
        "tag": "p",
        "children": [
            "Announced during ",
            {"tag": "strong", "children": ["Minecraft Live 2026"]},
            ", ",
            {"tag": "strong", "children": ["The Sift"]},
            " marks Minecraft's first official new dimension in over 14 years, joining the Overworld, the Nether, and The End."
        ]
    },
    {
        "tag": "p",
        "children": [
            "For full interactive biome guides, release schedules, and updates, visit the official community wiki: ",
            {
                "tag": "a",
                "attrs": {"href": "https://thesiftguide.com"},
                "children": ["The Sift Minecraft Guide (thesiftguide.com)"]
            },
            "."
        ]
    },
    {
        "tag": "h3",
        "children": ["Confirmed Biomes & Early Playable Access"]
    },
    {
        "tag": "p",
        "children": [
            "1. ",
            {"tag": "strong", "children": ["The Meadow"]},
            ": A bioluminescent landscape featuring alien flora and a new amphibious frog-like soul creature.\n",
            "2. ",
            {"tag": "strong", "children": ["The Carapace"]},
            ": A desert wasteland of ancient colossal skeletal structures."
        ]
    },
    {
        "tag": "p",
        "children": [
            "Players can experience The Sift ahead of the 2027 vanilla survival update starting September 29, 2026 via dimensional rift events in ",
            {"tag": "strong", "children": ["Minecraft Dungeons II"]},
            "."
        ]
    },
    {
        "tag": "p",
        "children": [
            "Explore detailed dimension mechanics and updates at ",
            {
                "tag": "a",
                "attrs": {"href": "https://thesiftguide.com"},
                "children": ["https://thesiftguide.com"]
            },
            "."
        ]
    }
]

page_data = {
    "access_token": token,
    "title": "Minecraft The Sift Dimension Guide & Wiki",
    "author_name": "Minecraft Lore Hub",
    "author_url": "https://thesiftguide.com",
    "content": json.dumps(content),
    "return_content": True
}

req = urllib.request.Request(
    "https://api.telegra.ph/createPage",
    data=json.dumps(page_data).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read().decode())
    print("Page creation result:", res.get("ok"))
    if res.get("ok"):
        print("URL:", res["result"]["url"])
