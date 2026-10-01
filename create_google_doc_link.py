#!/usr/bin/env python3
import json, sys
sys.path.append("/home/louis/.hermes/skills/productivity/google-workspace/scripts")
from google_api import build_service

def main():
    docs_service = build_service("docs", "v1")
    drive_service = build_service("drive", "v3")

    # 1. Create document
    title = "The Sift in Minecraft: 4th Dimension Complete Guide & Wiki"
    doc = docs_service.documents().create(body={"title": title}).execute()
    doc_id = doc.get("documentId")
    print(f"Created doc ID: {doc_id}")

    # 2. Build structured text with hyperlinks
    full_text = (
        "The Sift in Minecraft: Everything Confirmed About the 4th Official Dimension\n\n"
        "Official Live Guide & Interactive Wiki: https://thesiftguide.com\n\n"
        "During Minecraft Live 2026, Mojang officially announced The Sift, marking the first time in over 14 years that a new official dimension has been added to Minecraft (joining the Overworld, the Nether, and The End).\n\n"
        "Key Highlights & Mechanics:\n"
        "- Dimension Type: Official Vanilla Dimension #4 (first new realm since The End in 2012)\n"
        "- Release Window: Full vanilla release scheduled for 2027 on both Java and Bedrock editions\n"
        "- Early Access: Playable starting September 29, 2026 via Minecraft Dungeons II dimensional rift events\n"
        "- Confirmed Biomes: The Meadow (bioluminescent flora and soul pools) and The Carapace (ancient skeletal desert)\n"
        "- Native Fauna: New amphibious frog-like soul creature native to The Meadow\n\n"
        "Explore full biome breakdowns, crafting recipes, and live tracker updates at the official guide website:\n"
        "https://thesiftguide.com\n"
    )

    # Insert text
    insert_req = {
        "insertText": {
            "location": {"index": 1},
            "text": full_text
        }
    }
    docs_service.documents().batchUpdate(
        documentId=doc_id,
        body={"requests": [insert_req]}
    ).execute()

    # Find link positions and add actual clickable hyperlink styling
    link_url = "https://thesiftguide.com"
    requests = []
    
    start = 0
    while True:
        pos = full_text.find(link_url, start)
        if pos == -1:
            break
        # Google Docs API indexes are 1-based offset from start of body
        req = {
            "updateTextStyle": {
                "range": {
                    "startIndex": pos + 1,
                    "endIndex": pos + len(link_url) + 1
                },
                "textStyle": {
                    "link": {"url": link_url},
                    "underline": True
                },
                "fields": "link,underline"
            }
        }
        requests.append(req)
        start = pos + len(link_url)

    if requests:
        docs_service.documents().batchUpdate(
            documentId=doc_id,
            body={"requests": requests}
        ).execute()

    # 3. Set public permission (anyone with link can view)
    perm_body = {
        "role": "reader",
        "type": "anyone"
    }
    perm = drive_service.permissions().create(
        fileId=doc_id,
        body=perm_body
    ).execute()
    print("Permission updated:", perm)

    doc_info = drive_service.files().get(
        fileId=doc_id,
        fields="id, name, webViewLink"
    ).execute()

    print("Document URL:", doc_info.get("webViewLink"))

if __name__ == "__main__":
    main()
