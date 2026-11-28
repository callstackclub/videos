"""Write catalog/public.json: the lessons from catalog/all.json whose video is public on YouTube right now.

A lesson is public when YouTube's oEmbed endpoint answers 200 for it (private and deleted videos don't)
and its release time has passed (a scheduled Premiere has a public countdown page before it airs).
If YouTube can't be reached for a video, that lesson keeps whatever state it had in the last public.json,
so a network hiccup never removes lessons from the app.
"""
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ALL, PUB = ROOT / "catalog" / "all.json", ROOT / "catalog" / "public.json"


def oembed(video_id: str):
    """True public, False not public, None unknown (network trouble)."""
    url = "https://www.youtube.com/oembed?format=json&url=" + urllib.parse.quote(f"https://www.youtube.com/watch?v={video_id}")
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "catalog-check"}), timeout=20) as r:
            return r.status == 200
    except urllib.error.HTTPError as e:
        return False if e.code in (401, 403, 404) else None
    except Exception:
        return None


def main() -> int:
    cat = json.loads(ALL.read_text(encoding="utf-8"))
    before = json.loads(PUB.read_text(encoding="utf-8")) if PUB.exists() else {"lessons": []}
    was = {l["youtubeId"] for l in before.get("lessons", [])}
    now = datetime.now(timezone.utc)
    keep = []
    for l in cat["lessons"]:
        released = datetime.fromisoformat(l["release"].replace("Z", "+00:00")) <= now
        state = oembed(l["youtubeId"]) if released else False
        if state is None:
            state = l["youtubeId"] in was
            print(f"{l['id']}: YouTube unreachable, keeping previous state ({state})")
        if state:
            keep.append(l)
    series = {l["series"] for l in keep}
    out = {k: v for k, v in cat.items() if k not in ("lessons", "series", "generated")}
    out["series"] = [s for s in cat["series"] if s["id"] in series]
    out["lessons"] = keep
    old = {k: v for k, v in before.items() if k != "checked"}
    if old == out:
        print(f"no change: {len(keep)} public lessons")
        return 0
    out["checked"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    PUB.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    added = sorted({l["id"] for l in keep} - {l["id"] for l in before.get("lessons", [])})
    print(f"public.json: {len(keep)} lessons" + (f", new: {', '.join(added)}" if added else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
