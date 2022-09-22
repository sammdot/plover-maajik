STARTER = "HSDG"
ENDER = "gn"

LETTERS = {
  "H": "手",
  "D": "田",
  "B": "水",
  "i": "口",
  "i*": "廿",
  "-i*": "卜",
  "-i": "山",
  "-B": "戈",
  "-D": "人",
  "-H": "心",
  "S": "日",
  "G": "尸",
  "a": "木",
  "e": "火",
  "e*": "土",
  "-e*": "竹",
  "-e": "十",
  "-a": "大",
  "-G": "中",
  "-S": "難",
  "g": "金",
  "n": "女",
  "-n": "月",
  "-gn": "弓",
  "-g": "一",
}

MAX_LETTERS = 5
LONGEST_KEY = MAX_LETTERS + 2


def lookup(outline):
  """
    >>> lookup(("HSDG",))
    '{&(倉:)}'

    >>> lookup(("HSDG", "H", "D", "B"))
    '{&(倉:手田水)}'

    >>> lookup(("HSDG", "H", "D", "gn"))
    '{&(倉:手田)}'

    >>> lookup(("HSDG", "H", "D", "gn", "-e"))
    Traceback (most recent call last):
      ...
    KeyError
    """

  assert len(outline) <= LONGEST_KEY

  starter, *letters = outline
  if starter != STARTER:
    raise KeyError

  if not letters:
    return "{&(倉:)}"

  if ENDER in letters:
    if letters[-1] != ENDER:
      raise KeyError
    *letters, _ = letters

  letters = "".join(LETTERS[l] for l in letters)
  return f"{{&(倉:{letters})}}"


if __name__ == "__main__":
  import doctest

  doctest.testmod()
