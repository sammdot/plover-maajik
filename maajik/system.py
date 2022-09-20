# fmt: off
#
#   # # # # #   # # # # #
#   H D B i *   * i B D H
#   S G a e *   * e a G S
#
#         g n   n g
#
KEYS = (
  "#",
  "H-", "S-", "D-", "G-", "B-", "a-", "i-", "e-", "*-", "g-", "n-",
  "-H", "-S", "-D", "-G", "-B", "-a", "-i", "-e", "-*", "-g", "-n",
)
# fmt: on

IMPLICIT_HYPHEN_KEYS = ()
SUFFIX_KEYS = ()
NUMBER_KEY = "#"
NUMBERS = {
  "H-": "1-",
  "D-": "2-",
  "B-": "3-",
  "i-": "4-",
  "*-": "5-",
  "-*": "-6",
  "-i": "-7",
  "-B": "-8",
  "-D": "-9",
  "-H": "-0",
}
FERAL_NUMBER_KEY = False

UNDO_STROKE_STENO = "*-*"

ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_RULES_ALIASES = {}
ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
  "Keyboard": {
    "#": ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"),
    "H-": "q",
    "S-": "a",
    "D-": "w",
    "G-": "s",
    "B-": "e",
    "a-": "d",
    "i-": "r",
    "e-": "f",
    "*-": ("t", "g"),
    "g-": "c",
    "n-": "v",
    "-H": "p",
    "-S": ";",
    "-D": "o",
    "-G": "l",
    "-B": "i",
    "-a": "k",
    "-i": "u",
    "-e": "j",
    "-*": ("y", "h"),
    "-g": "m",
    "-n": "n",
    "no-op": ("z", "x", "b", ",", ".", "/", "[", "'", "]", "\\"),
  },
  "Gemini PR": {
    # fmt: off
    "#": (
      "#1", "#2", "#3", "#4", "#5", "#6",
      "#7", "#8", "#9", "#A", "#B", "#C",
    ),
    # fmt: on
    "H-": "S1-",
    "S-": "S2-",
    "D-": "T-",
    "G-": "K-",
    "B-": "P-",
    "a-": "W-",
    "i-": "H-",
    "e-": "R-",
    "*-": ("*1", "*2"),
    "g-": "A-",
    "n-": "O-",
    "-H": "-T",
    "-S": "-S",
    "-D": "-L",
    "-G": "-G",
    "-B": "-P",
    "-a": "-B",
    "-i": "-F",
    "-e": "-R",
    "-*": ("*3", "*4"),
    "-g": "-U",
    "-n": "-E",
    "no-op": ("-D", "-Z", "Fn", "pwr", "res1", "res2"),
  },
}

DICTIONARIES_ROOT = "asset:maajik:dictionaries"
DEFAULT_DICTIONARIES = [
  "commands.json",
  "punctuation.json",
  "briefs.json",
  "main.json",
]
