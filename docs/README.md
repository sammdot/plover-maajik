# MaaJik Theory Manual

- **Basics** _(this page)_
- [Phonetics](phonetics.md)
- [Cangjie](cangjie.md)
- [Phrasing](phrasing.md)
- [Punctuation](punctuation.md)

## Layout

The MaaJik keyboard has a symmetrical layout, with 12 keys on each side, and a single number key. Each side contains enough keys to be able to write one syllable.

![MaaJik keyboard layout](https://raw.githubusercontent.com/sammdot/plover-maajik/main/assets/layout.png)

The order of the steno keys is as follows:

```
# H- S- D- G- B- a- i- e- *- g- n- -H -S -D -G -B -a -i -e -* -g -n
```

Note that the order of the keys on the right-hand side is the exact same as on the left side, despite it being mirrored. This is to allow for easier dictionary generation and readback.

## Fundamentals

Because the Cantonese language is not written with spaces, all outlines for words must be defined without spaces. We have standardized on the glue operator (`{& }`), and you should do the same when defining new outlines.

To write words and phrases, MaaJik uses a phonetic base derived from the Jyutping romanization system, with a secondary layer of Cangjie/Congkit (倉頡) input. Most words and phrases can be written phonetically, but the Cangjie base exists to resolve conflicts between homophones, and to write singular characters, especially rare characters.

In addition to the phonetic base, MaaJik has a briefing and phrasing system for the most common words, including verbs, pronouns, and sentence-final particles.

### Example

In the example on the repository's README:

![MaaJik writing demo](https://raw.githubusercontent.com/sammdot/plover-maajik/main/assets/demo.png)

The outlines can be broken down as follows:

- 你哋 `DB-D` (_n-d_) is a [phrase brief](phrasing.md);
- 想唔想 `S-HD` (_s-m_) is a phrase brief using the X-唔-X pattern;
- 去 `Hie` (_heoi_) is a [phonetic](phonetics.md);
- 尖沙咀 `DGign-Sa/DGaiegn-gn` (_zim-saa/zeoi-2_) is a trisyllabic phonetic;
- 買嘢 `HDaign-HDBe` (_maai-je_) is a disyllabic phonetic; and
- ？ `Ga-DB` is an arbitrary [punctuation](punctuation.md) outline.
