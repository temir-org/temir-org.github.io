# Image Classification API – Specification v1.0

Every group implements this API exactly. The other groups' attacks, the course's
test tools, and your own HTML frontend all talk to your classifier only through
it, so field names, value ranges and error behavior must match this document.

A machine-readable version is available as `openapi.yaml`.

## Overview

| | |
|---|---|
| Protocol | HTTP, no TLS |
| Port | given via `--port` (default 8000) |
| Content type | `application/json` (requests and responses) |
| Endpoints | `POST /predict`, `GET /info` (at the root path, no prefix) |
| Cross-origin requests | must be allowed from any origin (see [CORS](#cors)) |

## `POST /predict`

Classifies an image into (1) a list of free-text classes given in the request
and (2) the fixed set of seven emotions.

### Request

```json
{
  "image": "<base64-encoded PNG>",
  "classes": ["cat", "dog", "a person at a desk"]
}
```

| Field | Type | Required | Constraints |
|---|---|---|---|
| `image` | string | yes | Base64 (RFC 4648, standard alphabet, **no** `data:image/png;base64,` prefix) of a PNG file, 1×1 to 1024×1024 px. Clients should send 8-bit RGB. Servers must accept any valid PNG (grayscale, palette, 16-bit, with or without alpha) and convert it to RGB themselves; the alpha channel is ignored. |
| `classes` | array of strings | yes | 0 to 50 entries, each 1 to 200 characters, no duplicates. Case-sensitive free text. May be empty (`[]`). |

Only PNG is accepted. Lossy formats such as JPEG would alter the pixel values
that attacks rely on. All resizing, cropping and normalization required by your
model happen inside your server.

### Response `200 OK`

```json
{
  "classes": {
    "cat": 0.71,
    "dog": 0.22,
    "a person at a desk": 0.07
  },
  "emotions": {
    "anger": 0.02,
    "disgust": 0.01,
    "fear": 0.03,
    "happiness": 0.81,
    "sadness": 0.04,
    "surprise": 0.05,
    "neutral": 0.04
  }
}
```

| Field | Semantics |
|---|---|
| `classes` | Exactly one key per requested class, spelled exactly as in the request. Values in [0, 1] that sum to 1 (± 1e-6), i.e. a probability distribution over the requested classes. If `classes` was empty, this is `{}`. |
| `emotions` | Always exactly these seven keys: `anger`, `disgust`, `fear`, `happiness`, `sadness`, `surprise`, `neutral`. Values in [0, 1] that sum to 1 (± 1e-6). |

The response contains no other fields.

### Behavioral requirements

- **No rounding.** Return probabilities as plain JSON numbers at full precision.
- **Determinism.** The same request must always produce the same response
  (no random augmentation, dropout or sampling at inference time).
- **Independence.** The emotion output must not depend on the `classes` list.
- **Statelessness.** A response must not depend on earlier requests.

## `GET /info`

Returns metadata about the running service.

### Response `200 OK`

```json
{
  "team": "team-03",
  "model_version": "a1b2c3d",
  "max_image_size": [1024, 1024],
  "max_classes": 50
}
```

| Field | Type | Semantics |
|---|---|---|
| `team` | string | Your group's name as registered in Moodle. |
| `model_version` | string | Identifier of the deployed model, e.g. a git commit hash. Must change whenever the model changes. |
| `max_image_size` | [int, int] | Always `[1024, 1024]`. |
| `max_classes` | int | Always `50`. |

## Errors

Every error response has the body

```json
{ "error": "<human-readable message>" }
```

| Status | When |
|---|---|
| `400 Bad Request` | Malformed JSON, missing or wrongly typed field, invalid base64, image is not a PNG, empty or duplicate class strings, class longer than 200 characters, more than 50 classes |
| `413 Payload Too Large` | Image larger than 1024×1024 px, or request body larger than 10 MB |
| `500 Internal Server Error` | Any unexpected failure inside your server |

## CORS

Your frontend is a standalone HTML file, and other groups' tools run from
different origins. The server must therefore allow cross-origin requests from
**any** origin:

- Every response, including error responses, carries the header
  `Access-Control-Allow-Origin: *`.
- The server answers CORS preflight requests (`OPTIONS /predict`,
  `OPTIONS /info`) with status `200` or `204` and the headers
  `Access-Control-Allow-Origin: *`,
  `Access-Control-Allow-Methods: GET, POST, OPTIONS`,
  `Access-Control-Allow-Headers: Content-Type`.

With FastAPI, this is:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)
```

## Deliverable and start command

You submit a single Python file `server.py`. Files your server needs that you
created yourself (e.g. the trained linear-probe weights) go in a directory
`weights/` next to it.

**Dependencies** are declared in the header of `server.py` as
[PEP 723](https://peps.python.org/pep-0723/) inline script metadata, with
pinned versions:

```python
# /// script
# requires-python = "==3.12.*"
# dependencies = [
#   "fastapi==0.115.6",
#   "uvicorn==0.34.0",
#   "open-clip-torch==2.29.0",
#   "torch==2.5.1",
#   "pillow==11.0.0",
# ]
# ///
```

**Start command**, used unchanged by us and by other groups:

```
uv run server.py --port 8000 --weights-dir ./weights
```

- The server listens on `0.0.0.0:<port>`.
- Publicly available pretrained models (e.g. CLIP checkpoints from the
  Hugging Face Hub) may be downloaded by name on first start. Everything you
  trained yourself must be in `weights/`.
- The server must answer `GET /info` within 120 seconds of starting
  (after the first download).
- It must run on a machine with one GPU and also on CPU only (slower, but
  with identical results up to floating-point tolerance).
- Any web framework and any ML framework are allowed, as long as they are
  listed in the header.

## Examples

### curl

```bash
curl -s http://localhost:8000/predict \
  -H 'Content-Type: application/json' \
  -d "{\"image\": \"$(base64 -w0 test.png)\", \"classes\": [\"cat\", \"dog\"]}"
```

### Python

```python
import base64
import requests

with open("test.png", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("ascii")

r = requests.post(
    "http://localhost:8000/predict",
    json={"image": image_b64, "classes": ["cat", "dog"]},
    timeout=30,
)
r.raise_for_status()
result = r.json()
top_emotion = max(result["emotions"], key=result["emotions"].get)
print(top_emotion, result["emotions"][top_emotion])
```

### JavaScript (browser)

```javascript
const res = await fetch("http://localhost:8000/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ image: imageB64, classes: ["cat", "dog"] }),
});
const result = await res.json();
```
