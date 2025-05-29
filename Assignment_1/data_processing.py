"""berp_summary.py

Download Berkeley Restaurant Project transcripts, clean the file in place, and print summary stats.

"""

from __future__ import annotations

import collections
import json
import re
import urllib.request
from pathlib import Path
from typing import List, Tuple

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
URL = "https://raw.githubusercontent.com/wooters/berp-trans/master/transcript.txt"
LOCAL_TXT = Path("berp_dataset.txt")

# ---------------------------------------------------------------------------
# Regular expressions
# ---------------------------------------------------------------------------

# Square‑bracket tags to drop entirely (e.g. [uh])
_SQUARE_RE = re.compile(r"\[[^\]]+?\]")
# Angle‑bracket tokens to unwrap (e.g. <(te)-ll>, <me>)
_ANGLE_RE = re.compile(r"<[^>]+?>")
# Leading utterance ID (letters/numbers/underscores) followed by whitespace
_PREFIX_RE = re.compile(r"^[A-Za-z0-9_]+\s+")
# Special symbols to delete entirely once angle tokens are unwrapped
_SYMBOL_RE = re.compile(r"[.*\-\_]")
# Collapse ≥2 spaces to 1
_SPACE_RE = re.compile(r"\s{2,}")

# ---------------------------------------------------------------------------
# Download & cleaning helpers
# ---------------------------------------------------------------------------

def download(url: str = URL, dest: Path | str = LOCAL_TXT) -> Path:
    dest = Path(dest)
    urllib.request.urlretrieve(url, dest)
    return dest


def _unwrap_angle(match: re.Match) -> str:
    """Return only the alphabetic/apostrophe content inside <...>."""
    inner = match.group(0)[1:-1]  # strip < >
    # Keep letters and apostrophes; drop dashes, parentheses, etc.
    return re.sub(r"[^A-Za-z' ]", "", inner)


def _clean_line(line: str) -> str:
    """Clean one raw transcript line and return it (or "" if empty)."""
    # Drop leading ID
    text = _PREFIX_RE.sub("", line.strip())
    # Remove square‑bracket disfluencies
    text = _SQUARE_RE.sub("", text)
    # Unwrap angle‑bracket tokens, preserving letters
    text = _ANGLE_RE.sub(_unwrap_angle, text)
    # Remove selected symbols * . -
    text = _SYMBOL_RE.sub("", text)
    # Collapse whitespace and trim
    text = _SPACE_RE.sub(" ", text).strip()
    return text


def clean_file(path: Path) -> None:
    """Rewrite *path* in place, leaving only cleaned utterances (no blank lines),
    and wrap each sentence with <s> and </s>."""
    with path.open(encoding="utf-8") as fh:
        cleaned_lines: List[str] = [
            f"<s> {cl} </s>" for raw in fh if (cl := _clean_line(raw))
        ]

    # Overwrite file with cleaned content
    with path.open("w", encoding="utf-8") as fh:
        fh.write("\n".join(cleaned_lines))


    

def load_sentences(path: Path | str):
    """Return list[list[str]] of tokens assuming *path* is already cleaned."""
    sentences: List[List[str]] = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            parts = line.strip().split()
            if parts:
                sentences.append(parts)
    return sentences


def compute_stats(sentences: List[List[str]]):
    words = [token.lower() for sent in sentences for token in sent]
    vocab = collections.Counter(words)
    return {
        "num_sentences": len(sentences),
        "num_tokens": len(words),
        "vocab_size": len(vocab)
    }


def download_berp() -> None:
    path = download()
    clean_file(path)
    stats = compute_stats(load_sentences(path))
    print("download complete")
    print(json.dumps(stats, indent=2))



def load_data(path: str = LOCAL_TXT, train_frac: float = 0.8
                   ) -> Tuple[List[List[str]], List[List[str]]]:
    """Load cleaned corpus from path, strip <s> tags, and split into training/dev sets."""
    sentences = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            # remove sentence boundary markers
            tokens = [tok for tok in parts if tok not in ('<s>', '</s>')]
            if tokens:
                sentences.append(tokens)
    return sentences
