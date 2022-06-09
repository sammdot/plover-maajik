# fmt: off
#
#   H T P i *   * i P T H
#   S K a e *   * e a K S
#
#         m n   n m
#
KEYS = (
  "H-", "S-", "T-", "K-", "P-", "a-", "i-", "e-", "*-", "m-", "n-",
  "-H", "-S", "-T", "-K", "-P", "-a", "-i", "-e", "-*", "-m", "-n",
)
# fmt: on

IMPLICIT_HYPHEN_KEYS = ()
SUFFIX_KEYS = ()
NUMBER_KEY = None
NUMBERS = {}
FERAL_NUMBER_KEY = False

UNDO_STROKE_STENO = "*-*"

ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_RULES_ALIASES = {}
ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
  "Keyboard": {
    "H-": "q",
    "S-": "a",
    "T-": "w",
    "K-": "s",
    "P-": "e",
    "a-": "d",
    "i-": "r",
    "e-": "f",
    "*-": ("t", "g"),
    "m-": "c",
    "n-": "v",
    "-H": "p",
    "-S": ";",
    "-T": "o",
    "-K": "l",
    "-P": "i",
    "-a": "k",
    "-i": "u",
    "-e": "j",
    "-*": ("y", "h"),
    "-m": "m",
    "-n": "n",
    "no-op": ("z", "x", "b", ",", ".", "/", "[", "'", "]", "\\"),
  },
  "Gemini PR": {
    "H-": "S1-",
    "S-": "S2-",
    "T-": "T-",
    "K-": "K-",
    "P-": "P-",
    "a-": "W-",
    "i-": "H-",
    "e-": "R-",
    "*-": ("*1", "*2"),
    "m-": "A-",
    "n-": "O-",
    "-H": "-T",
    "-S": "-S",
    "-T": "-L",
    "-K": "-G",
    "-P": "-P",
    "-a": "-B",
    "-i": "-F",
    "-e": "-R",
    "-*": ("*3", "*4"),
    "-m": "-U",
    "-n": "-E",
    "no-op": ("-D", "-Z", "Fn", "pwr", "res1", "res2"),
  },
}
KEYMAPS["Plover HID"] = KEYMAPS["Gemini PR"]

DICTIONARIES_ROOT = None
DEFAULT_DICTIONARIES = ()
