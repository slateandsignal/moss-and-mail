import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

TOKEN_FILE = "/Users/raquelcovey/Projects/MossAndMail/youtube_token.json"

with open(TOKEN_FILE) as f:
    data = json.load(f)

creds = Credentials(
    token=data['token'],
    refresh_token=data['refresh_token'],
    token_uri=data['token_uri'],
    client_id=data['client_id'],
    client_secret=data['client_secret']
)

if creds.expired:
    creds.refresh(Request())
    with open(TOKEN_FILE, 'w') as f:
        json.dump({
            'token': creds.token,
            'refresh_token': creds.refresh_token,
            'token_uri': creds.token_uri,
            'client_id': creds.client_id,
            'client_secret': creds.client_secret
        }, f)

youtube = build('youtube', 'v3', credentials=creds)

SHARED_DESCRIPTION_FOOTER = """
✉️ Moss & Mail — a monthly handwritten letter, sealed in wax and sent to your door.
mossandmail.com

---
Moss & Mail is a monthly handwritten letter subscription for people who still believe in slow living, real mail, and the magic of opening an envelope."""

SHARED_TAGS = ["walnut hill", "moss and mail", "slow living", "intentional living",
               "life update", "youtube shorts", "mossandmail", "intentional motherhood"]

PARTS = [
    {
        "label": "Part 1/4",
        "file": "/Users/raquelcovey/Desktop/Walnut Hill Part 1 all platforms/Walnut Hill Part 1 (YT Short) (1).mp4",
        "title": "We poured everything into it. (Part 1/4) #Shorts",
        "description": """Three years. Every penny. Every ounce of effort. And it hurt deeply to let it go.

This is Part 1 of 4 — the story of how we got here and why we left.""" + SHARED_DESCRIPTION_FOOTER,
        "tags": SHARED_TAGS + ["selling our home", "historic home", "homestead", "ohio home"],
        "publishAt": "2026-05-14T14:00:00Z",
        "scheduleLabel": "May 14 at 8am MDT"
    },
    {
        "label": "Part 2/4",
        "file": "/Users/raquelcovey/Desktop/Walnut Hill Part 2/Walnut Hill Part 2 (YT short).mp4",
        "title": "The beginning was an end. (Part 2/4) #Shorts",
        "description": """The beginning was an end. The end of trying to be something they weren't built for.

This is Part 2 of 4 — what they really wanted, and what it cost to get there.""" + SHARED_DESCRIPTION_FOOTER,
        "tags": SHARED_TAGS + ["mountains", "community", "utah", "mountain living", "sacrifice"],
        "publishAt": "2026-05-16T15:00:00Z",
        "scheduleLabel": "May 16 at 9am MDT"
    },
    {
        "label": "Part 3/4",
        "file": "/Users/raquelcovey/Desktop/Walnut Hill Part 3/Walnut Hill Part 3 YT short.mp4",
        "title": "She changed my life. (Part 3/4) #Shorts",
        "description": """She changed my life.

This is Part 3 of 4 — the podcast, the friendship, and the moment that changed everything.""" + SHARED_DESCRIPTION_FOOTER,
        "tags": SHARED_TAGS + ["1000 hours outside", "nature mom", "friendship", "outdoor school"],
        "publishAt": "2026-05-17T15:00:00Z",
        "scheduleLabel": "May 17 at 9am MDT"
    },
    {
        "label": "Part 4/4",
        "file": "/Users/raquelcovey/Desktop/Walnut Hill Part 4/Walnut Hill Part 4 YT Short.mp4",
        "title": "Welcome. I'm so glad you're here. (Part 4/4) #Shorts",
        "description": """There's a gap. In knowledge, confidence, and community — for mamas who want to get outside with their kids and don't know where to start.

This is Part 4 of 4 — the gap, and an invitation to fill it together.

Letters open June 8 → mossandmail.com""" + SHARED_DESCRIPTION_FOOTER,
        "tags": SHARED_TAGS + ["nature moms", "1000 hours outside", "gap in community", "welcome", "letters open"],
        "publishAt": "2026-05-18T14:00:00Z",
        "scheduleLabel": "May 18 at 8am MDT"
    }
]

# Create the Walnut Hill playlist once
print("Creating 'Walnut Hill' playlist...")
playlist = youtube.playlists().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "Walnut Hill",
            "description": "The story of our 1807 Ohio home — why we bought it, what we poured into it, and why we let it go."
        },
        "status": {"privacyStatus": "public"}
    }
).execute()
playlist_id = playlist["id"]
print(f"✅ Playlist created: {playlist_id}\n")

video_ids = []

for part in PARTS:
    print(f"Uploading {part['label']} — {part['title']}")
    body = {
        "snippet": {
            "title": part["title"],
            "description": part["description"],
            "tags": part["tags"],
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "private",
            "publishAt": part["publishAt"],
            "selfDeclaredMadeForKids": False
        }
    }
    media = MediaFileUpload(part["file"], mimetype="video/mp4", resumable=True, chunksize=10*1024*1024)
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"  Progress: {int(status.progress() * 100)}%", end="\r")

    video_id = response["id"]
    video_ids.append(video_id)
    print(f"\n✅ {part['label']} uploaded → https://youtube.com/watch?v={video_id} | scheduled: {part['scheduleLabel']}")

    youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {"kind": "youtube#video", "videoId": video_id}
            }
        }
    ).execute()
    print(f"   Added to Walnut Hill playlist\n")

    if part != PARTS[-1]:
        time.sleep(2)

print("=" * 50)
print("ALL DONE")
print(f"Playlist ID: {playlist_id}")
for i, vid_id in enumerate(video_ids):
    print(f"Part {i+1}: https://youtube.com/watch?v={vid_id}")
