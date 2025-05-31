import os
import urllib.request
from pathlib import Path
import shutil
import gzip
from gensim.models import KeyedVectors
from sklearn.metrics import accuracy_score, classification_report
import ssl

def extract_and_summary_gnews(
    output_dir: str = "."
):
    """
    Decompress the `GoogleNews-vectors-negative300.bin.gz` file to `GoogleNews-vectors-negative300.bin`, then print summary statistics:
       - Total number of word vectors (vocabulary size)
       - Vector dimensionality (should be 300)
       - A small sample of words + truncated vector snippets
    """

    output_dir = Path(output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    gz_path  = output_dir / "GoogleNews-vectors-negative300.bin.gz"
    bin_path = output_dir / "GoogleNews-vectors-negative300.bin"


    # -------------------------------------------------------------
    # Decompress .gz → .bin (if needed)
    # -------------------------------------------------------------
    if not bin_path.exists():
        print("Decompressing `.gz` → `.bin` (this may take a few minutes)…")
        with gzip.open(gz_path, "rb") as f_in, bin_path.open("wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
        print("Decompressed to:", bin_path)
    else:
        print("Uncompressed `.bin` already present:", bin_path)

    # -------------------------------------------------------------
    # Read header to get vocab size & vector dimension
    # -------------------------------------------------------------
    print("\n=== Summary Statistics ===")
    with open(bin_path, "rb") as f:
        header_bytes = b""
        # The very first line in a Word2Vec .bin is ASCII: "<vocab_size> <vector_dim>\n"
        while not header_bytes.endswith(b"\n"):
            header_bytes += f.read(1)

    vocab_size, vector_dim = map(int, header_bytes.decode("ascii").split())
    print(f"• Total vocabulary size: {vocab_size:,} words")
    print(f"• Vector dimensionality: {vector_dim}")

    # -------------------------------------------------------------
    # 4) Load a tiny sample (limit=10) via Gensim to show actual entries
    # -------------------------------------------------------------
    print("\nLoading a small sample (limit=10) to display a few word–vector snippets…")
    sample_kv = KeyedVectors.load_word2vec_format(str(bin_path), binary=True, limit=10)

    sample_words = list(sample_kv.key_to_index.keys())
    print("• Sample words loaded (first 10):", sample_words)

    print("\n• Vector snippets for the first 5 sample words:")
    for w in sample_words[:5]:
        vec = sample_kv[w]
        snippet = vec[:6]  # show only first 6 dimensions for brevity
        print(f"    {w:15s} → {snippet.tolist()} …")






def fetch_lexicons(pos_filename = "positive-words.txt", neg_filename = "negative-words.txt"):
    """
    Download positive-words.txt & negative-words.txt into the current directory
    if they do not already exist.
    """

    POS_URL = (
    "https://raw.githubusercontent.com/"
    "jeffreybreen/twitter-sentiment-analysis-tutorial-201107/"
    "master/data/opinion-lexicon-English/positive-words.txt"
    )
    NEG_URL = (
        "https://raw.githubusercontent.com/"
        "jeffreybreen/twitter-sentiment-analysis-tutorial-201107/"
        "master/data/opinion-lexicon-English/negative-words.txt"
    )
    for url, fname in [(POS_URL, pos_filename), (NEG_URL, neg_filename)]:
        path = Path(fname)
        if path.exists():
            print(f"[SKIP] {fname} already exists.")
            continue

        print(f"[DOWNLOAD] Fetching {url} → {fname}")
        # Bypass SSL verification if necessary
        ssl._create_default_https_context = ssl._create_unverified_context
        try:
            urllib.request.urlretrieve(url, fname)
            print(f"[OK] Saved {fname}.")
        except Exception as e:
            print(f"[ERROR] Could not download {url}: {e}")
            raise

def load_lexicon(path_to_file: Path) -> list[str]:
    """
    Reads a lexicon file (one word per line, with ';' comments) into a list.
    Uses latin-1 decoding so that no byte will fail. Ignores blank lines
    and any line that starts with ';'.
    """
    words: list[str] = []
    with path_to_file.open("r", encoding="latin-1") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(";"):
                continue
            words.append(line)
    return words


def load_lexicon_and_filter(loaded_model):

    fetch_lexicons()
    pos_path = Path("positive-words.txt")
    neg_path = Path("negative-words.txt")

    positive_words_raw = load_lexicon(pos_path)
    negative_words_raw = load_lexicon(neg_path)

    # print(f"Loaded (raw) {len(positive_words_raw)} positive words")
    # print(f"Loaded (raw) {len(negative_words_raw)} negative words")
    # print()

    model = loaded_model
    embedding_dim = model.vector_size
    # Filter raw lexicons so that only words in model.vocab remain
    vocab_set = set(model.key_to_index.keys())

    filtered_positive = [w for w in positive_words_raw if w in vocab_set]
    filtered_negative = [w for w in negative_words_raw if w in vocab_set]

    print(f"Filtered {len(positive_words_raw)} → {len(filtered_positive)} positive words kept")
    print(f"Filtered {len(negative_words_raw)} → {len(filtered_negative)} negative words kept")
    print()

    return filtered_positive, filtered_negative



def result_summary(y_test, y_pred, all_words, idx_test):
    acc_logreg = accuracy_score(y_test, y_pred)

    print("=== Logistic Regression (Sigmoid) Results ===")
    print(f"Accuracy: {acc_logreg:.4f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=["NEG", "POS"]))
    print()

        
    # ───────────────────────────────────────────────────────────────────────────
    # Inspect misclassified words for each classifier
    # ───────────────────────────────────────────────────────────────────────────
    print("Misclassified by Logistic Regression:")
    label_names = {0: "NEG", 1: "POS"}

    for i, (true_label, pred_label) in enumerate(zip(y_test, y_pred)):
        if true_label != pred_label:
            original_idx = idx_test[i]
            word = all_words[original_idx]
            true_name = label_names[true_label]
            pred_name = label_names[pred_label]
            print(f"  Word: {word:<15}   True={true_name:<3}   Pred={pred_name:<3}")
