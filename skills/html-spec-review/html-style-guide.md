# HTML Standard — de-facto style guide

How the HTML Standard's `source` is actually written, distilled from the text itself, its recent
history, and recent review practice. Pinned to whatwg/html commit
[`877d614`](https://github.com/whatwg/html/commit/877d6146487f15b15bc8dd0e3c625063a37b456a)
(`origin/main`, "Allow `style` in `body`"): every example links to that commit's source line on
GitHub and, where the term is rendered, to the matching
[commit snapshot](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/)
of the spec.

Each rule has a short name (`PREFIX-NAME`), a title, a description, and an example. Where the spec
uses more than one style for the same thing, a **Branch** side note lists the options in order of
preference:

- **Modern** — use in new text.
- **Accepted** — fine to use; match the surrounding text.
- **Legacy** — do not introduce; rewriting is optional.
- **Obsolete** — fix when touching.

Companion documents:
[CONTRIBUTING.md](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/.github/CONTRIBUTING.md),
the [WHATWG style guide](https://whatwg.org/style-guide), and the spec's own guidance on
[parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism)
and [the event loop](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#event-loop-for-spec-authors).

| § | Section | Prefixes |
|---|---|---|
| 1 | Source layout and markup | `SRC` |
| 2 | Headings, ids, cross-references | `HDR`, `XREF` |
| 3 | Definitions | `DFN` |
| 4 | Blocks: notes, examples, warnings, issues | `BLK` |
| 5 | Code and IDL blocks | `CODE`, `IDL` |
| 6 | Element definitions | `ELEM` |
| 7 | Developer's Edition annotations | `DEV` |
| 8 | Algorithm structure | `ALG` |
| 9 | Control flow | `FLOW` |
| 10 | Variables | `VAR` |
| 11 | Values and data structures | `VAL` |
| 12 | State declarations | `STATE` |
| 13 | Invoking algorithms | `CALL` |
| 14 | IDL member prose | `API` |
| 15 | Tasks, parallelism, events | `TASK`, `PAR`, `EVT` |
| 16 | Exceptions and promises | `EXC`, `PROM` |
| 17 | Conformance language | `CONF` |
| 18 | Prose mechanics | `PRS` |
| 19 | Vocabulary | `VOC` |

---

## 1. Source layout and markup (`SRC`)

### `SRC-WRAP-100` — Wrap at 100 columns
Wrap prose at 100 characters, breaking only at whitespace and filling each line before wrapping.
Do not rewrap `<pre>`, `<table>`, `<svg>`, `<script>`, `<style>`, comments, `<dt>`,
`<img>`/`<iframe>` tags, `ul.domTree`, Dependencies `<dfn>`s, or References `<dd>`s. Newlines
inside start tags and attribute values are fine. Only new or changed paragraphs need to comply.
**Example:** [source#L1595](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1595) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism)

### `SRC-INDENT-BLOCK` — One space of indentation per block
Indent one space for each block-level ancestor (`<ol>`, multi-line `<li>`, `<dl>`, `<dd>`,
`<div class="example">`, `<div class="note">`, table rows). A `<p>` inside a one-line `<li>` is not
indented further.
**Example:** [source#L1598](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1598) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism)
```html
  <ol>
   <li><p>Let <var>parallelQueue</var> be a new <span>parallel queue</span>.</p></li>

   <li>
    <p>Run the following steps <span>in parallel</span>:</p>

    <ol>
```

### `SRC-WRAPPER-NO-INDENT` — `<div algorithm>`, `<div w-nodev>`, `<div var-scope>` do not indent
These wrappers are transparent: their children stay at the surrounding indentation level.
`<div class="example">`, `<div class="note">`, `<div class="warning">`, and `<div class="XXX">`
do indent their contents.
**Example:** [source#L38087](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L38087) · [#dom-track-track](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-track-track)
```html
  <div algorithm>
  <p>The <dfn attribute for="HTMLTrackElement"><code data-x="dom-track-track">track</code></dfn>
  getter steps are to return <span>this</span>'s <span>text track</span>.</p>
  </div>
```

### `SRC-LI-P` — Every `<li>` wraps its text in `<p>`, except in `ul.brief`
Write `<li><p>…</p></li>` even for one-liners. Items with several blocks put `<li>` on its own line
and indent the children. Separate sibling `<li>`s with a blank line. `<ul class="brief">` items are
bare.
**Example:** [source#L1599](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1599) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism); brief list: [source#L14342](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L14342) · [#global-attributes](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#global-attributes)

### `SRC-DD-P` — `<dd>` wraps prose in `<p>`; short phrases may be bare
Definition-list values containing sentences use `<dd><p>…</p></dd>` or a multi-line `<dd>`. Bare
`<dd>` is for short phrases: `dl.element` boxes, Dependencies lists, `dl.switch` values.
**Example:** prose [source#L9792](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L9792); bare [source#L16155](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L16155) · [#the-head-element](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-head-element)

### `SRC-BLANK-BEFORE-HEADING` — Two blank lines before a heading
Leave two blank lines before `<h3>`–`<h6>` (one is tolerated when a wrapper `</div>` closes right
before it) and one blank line after, or follow the heading directly with
`<!-- NON-NORMATIVE SECTION -->`.
**Example:** [source#L100449](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L100449) · [#navigation-api](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#navigation-api)

### `SRC-END-TAGS` — Never omit end tags, except consistently inside tables
Write every end tag. The one conventional exception is table cells, where a whole table may use
implied `</th>`/`</td>`/`</tr>`.
**Example:** [source#L27939](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L27939) · [#linkTypes](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#linkTypes)
> **Branch** (table cells)
> 1. **Accepted** — explicit `</th>`/`</td>`/`</tr>`; dominant in new tables. [source#L27939](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L27939)
> 2. **Accepted** — compact rows with implied end tags, `<tr> <th>Keyword <th>State …`; standard in
>    keyword/state tables. Never mix the two in one table. [source#L8052](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8052) · [#referrer-policy-attribute](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#referrer-policy-attribute)

### `SRC-ATTR-QUOTES` — Double-quoted attribute values
Quote attribute values with double quotes (`colspan="2"`). Boolean Wattsi attributes are bare
(`<dfn export>`, `<div algorithm>`, `<var ignore>`, `<span subdfn>`, `<p w-nodev>`); `data-x=""`
and `data-noexport=""` use an explicit empty value.
**Example:** [source#L38087](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L38087) · [#dom-track-track](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-track-track)

### `SRC-WATTSI-ATTRS` — Wattsi-specific attributes
| Attribute | Purpose | Example |
|---|---|---|
| `data-x="key"` | link a `<span>`/`<code>` to a `<dfn>` whose text differs; `data-x=""` suppresses autolinking | [source#L680](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L680) |
| `data-x-href="url"` on `<dfn>` | import a term from another spec (Dependencies section) | [source#L2264](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L2264) |
| `data-lt="a\|b"` | alternative link texts; `data-lt=""` for IDL names redefined elsewhere | [source#L11778](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11778) |
| `export` / `data-noexport=""` | control export of a dfn to other specs | [source#L13047](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L13047) |
| `subdfn` | the `domintro` mention that gets the dfn panel | [source#L8153](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8153) |
| `w-nodev` / `w-dev` | omit from / include only in the Developer's Edition | [source#L175](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L175) |
| `algorithm`, `var-scope`, `ignore` | algorithm and variable scoping (§8) | [source#L618](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L618) |
| `split-filename="…"` on `<h2>` | multipage file name | [source#L173](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L173) |

### `SRC-COMMENTS` — Editorial comments
Editor notes are HTML comments, never visible text: `<!-- NON-NORMATIVE SECTION -->` after an
informative heading; `<!--INSERT TRACKING-->` before text documenting a fingerprinting vector;
`<!--en-GB-->` before a `<dfn id>` that preserves a British-spelled anchor; `<!-- v2: … -->` for
parked ideas; `<!-- TODO: … -->`; `<!-- algo-declaration -->` on a `<div var-scope>` that only
declares an algorithm.
**Example:** [source#L214](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L214); [source#L1983](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1983)

### `SRC-ENTITIES` — Characters and entities
Use named entities for typographic characters that are hard to see in source: `&mdash;`, `&nbsp;`,
`&le;`/`&ge;`, `&middot;`, `&times;`, `&minus;`. Infra list and map literals use literal `« »` and
`→`. Code points in prose are written `U+0041`. Quotes are straight ASCII (`PRS-QUOTES`).
**Example:** [source#L100682](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L100682) · [#navigation-current-entry-index](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#navigation-current-entry-index)
```html
  entry index</dfn>, an integer, initially &minus;1.</p>
```

### `SRC-REF-PLACEMENT` — `<ref>` goes after the final period of the paragraph
Bibliographic references are `<ref>KEY</ref>` placed after the sentence-ending period at the end of
the paragraph, several separated by spaces. Spec names in prose are `<cite>`.
**Example:** [source#L798](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L798) · [#writing-secure-applications-with-html](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#writing-secure-applications-with-html); multiple: [source#L3256](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L3256)
```html
  <p>In particular, the following features are defined in <cite>DOM</cite>: <ref>DOM</ref></p>
```

### `SRC-REFERENCES-ENTRY` — References section entries
`<dt id="refsKEY">[KEY]</dt>` followed by `<dd><cite><a href="…">Title</a></cite>, Authors.
Org.</dd>`; `<dd w-nodev>` for implementer-only references. Entries are alphabetical by key.
**Example:** [source#L161720](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L161720) · [#refsABNF](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#refsABNF)

### `SRC-DEPENDENCIES-ENTRY` — Dependencies section entries
Imported terms are one `<dfn data-x-href="…">term</dfn>` per `<li>` of a `<ul class="brief">`,
introduced by "The following terms are defined in `<cite>X</cite>`: `<ref>X</ref>`". Add `data-x`
when HTML's local name differs from the text, and `id` when preserving an old anchor.
**Example:** [source#L2524](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L2524) · [#dependencies](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dependencies)

---

## 2. Headings, ids, and cross-references (`HDR`, `XREF`)

### `HDR-SENTENCE-CASE` — Headings are sentence case
Capitalize only the first word and proper nouns or IDL names.
**Example:** [source#L961](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L961)
```html
  <h4>How to catch mistakes when writing HTML: validators and conformance checkers</h4>
```

### `HDR-ELEMENT-HEADING` — "The `<dfn element><code>x</code></dfn>` element"
Element sections are headed `The <dfn element><code>base</code></dfn> element`, with the defining
instance in the heading. Interfaces: "The `<code>X</code>` interface"; attributes: "The
`<code data-x="attr-…">x</code>` attribute". Later mentions in headings are plain `<code>`.
**Example:** [source#L16321](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L16321) · [#the-base-element](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-base-element); [source#L86143](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L86143) · [#the-toggleevent-interface](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-toggleevent-interface)

### `HDR-SECTION-NAMES` — Conventional subsection names
Reuse "Introduction" (with `<!-- NON-NORMATIVE SECTION -->`), "Processing model" (with an explicit
id such as `images-processing-model`, since the text repeats), "Security and privacy
considerations", "Examples", "X infrastructure", "Supporting concepts", "Definitions",
"Terminology".
**Example:** [source#L32793](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L32793) · [#images-processing-model](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#images-processing-model); [source#L116784](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L116784) · [#speculative-loading-security](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#speculative-loading-security)

### `HDR-EXPLICIT-ID` — Explicit lowercase-hyphen `id` when the derived one is fragile
Wattsi derives heading ids from the text, so headings containing code, punctuation, or wording
likely to change get a short explicit id (`<h4 id="mq">`, `<h4 id="origin">`,
`<h5 id="navigation-api-intro">`). All `<h2>`s have an explicit id plus `split-filename`. Never
introduce camelCase, dots, or underscores in ids.
**Example:** [source#L7614](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7614) · [#mq](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#mq); [source#L100451](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L100451) · [#navigation-api](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#navigation-api)

### `HDR-ALIAS-ANCHOR` — Preserve old anchors with an empty `<span id>`
When renaming a heading or dfn, keep the old fragment working with `<span id="old-id"></span>` as
the first child of the heading or paragraph, or `<dfn id="old-id">` for dfns.
**Example:** [source#L28174](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L28174) · [#rel-alternate](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#rel-alternate); [source#L131331](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L131331) · [#navigator.online](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#navigator.online)
```html
  <h5 id="rel-alternate"><span id="link-type-alternate"></span>Link type "<code data-x="rel-alternate">alternate</code>"</h5>
```

### `HDR-EN-GB-ALIAS` — British-spelled anchors are kept via `<!--en-GB-->`
Text uses American spelling; historical ids with British spelling survive as
`<!--en-GB--><dfn id="…isation…">` or an explicit heading id, with the comment marking the
exception.
**Example:** [source#L3375](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L3375) · [#activation-behaviour](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#activation-behaviour); [source#L77612](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L77612) · [#serialising-bitmaps-to-a-file](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#serialising-bitmaps-to-a-file)

### `HDR-PARAGRAPH-IDS` — Ids on paragraphs and list items for linkable concepts
Give an `id` to a `<p>`, `<li>`, note, or example that other specs or notes link to without a dfn
(`<p id="html-namespace">`, `<li id="node-remove-focus-fixup">`,
`<div class="example" id="example-…">`).
**Example:** [source#L1752](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1752) · [#html-namespace](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#html-namespace); [source#L23848](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L23848) · [#example-cite-usage-correct-vs-incorrect](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#example-cite-usage-correct-vs-incorrect)

### `HDR-ABSTRACT-OP-HEADING` — ECMAScript-style headings for internal methods
Internal methods of exotic objects use ECMA-262's heading format with an explicit id:
`[[Call]] ( <var>thisArgument</var>, <var>argumentsList</var> )`.
**Example:** [source#L9745](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L9745) · [#HTMLAllCollection-call](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#HTMLAllCollection-call)

### `XREF-SPAN-AUTOLINK` — `<span>` autolinks terms; add `data-x` only when the text differs
A bare `<span>term</span>` links to the `<dfn>` with the same text. Use
`<span data-x="dfn-key">visible text</span>` for conjugated or plural forms and `concept-*` keys.
Link a term on its first use in a paragraph; later uses in the same paragraph may be unlinked.
**Example:** [source#L680](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L680) · [#a-quick-introduction-to-html](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#a-quick-introduction-to-html)

### `XREF-CODE-ELEMENT` — Element names are bare `<code>`
Element names autolink as `<code>a</code>`, `<code>div</code>`; never add `data-x` to an element
name. Pluralize outside the code: "`<code>div</code>` elements" (`PRS-PLURALS`).
**Example:** [source#L675](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L675) · [#the-a-element](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-a-element)

### `XREF-CODE-ATTR` — Content attributes: `<code data-x="attr-ELEMENT-NAME">name</code>`
Keys are `attr-<element>-<name>` (`attr-img-src`), `attr-<name>` for global attributes
(`attr-translate`), `attr-<group>-<name>` for shared ones (`attr-hyperlink-href`, `attr-fe-name`,
`attr-dim-width`), `attr-…-<keyword>` for keyword values, and `attr-…-<keyword>-state` for states.
**Example:** [source#L7803](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7803) · [#document-base-url](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#document-base-url)

### `XREF-CODE-DOM` — IDL members: `<code data-x="dom-INTERFACE-name">name()</code>`
Keys are `dom-<Interface>-<member>` (`dom-DOMStringList-item`), `dom-<element>-<member>` for
element interfaces (`dom-img-decode`), `dom-<name>` for Window/global members
(`dom-structuredClone`). Methods are written with empty parentheses, attributes without;
constructors are `dom-<Interface>` or `dom-<Interface>-constructor`.
**Example:** [source#L10261](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L10261) · [#dom-structuredclone](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-structuredclone)

### `XREF-CODE-EVENT` — Events and handlers
Event names are `<code data-x="event-NAME">name</code>` (grouped keys like
`event-media-loadstart`); handler attributes are `<code data-x="handler-onNAME">onname</code>`
(`handler-window-onafterprint` for Window-only ones).
**Example:** [source#L19527](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L19527) · [#the-body-element](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-body-element)

### `XREF-CODE-HTTP` — HTTP headers and values in backticks
Header names are `` `<code data-x="http-NAME">Name</code>` `` wrapped in literal backticks; header
values and parameter names likewise `` `<code data-x="">require-corp</code>` ``.
**Example:** [source#L12176](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L12176) · [#dom-document-lastmodified](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-document-lastmodified)
```html
  … from the `<code data-x="http-last-modified">Last-Modified</code>` header of the document …
```

### `XREF-CODE-IDL-JS` — IDL types and JavaScript names
Web IDL types link as `<code data-x="idl-DOMString">DOMString</code>`; JavaScript built-ins and
errors as `<code data-x="js-RangeError">RangeError</code>`; abstract operations as bare
`<span>CreateByteDataBlock</span>(…)` (`ALG-ES-ABSTRACT-OPS`).
**Example:** [source#L9472](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L9472) · [#reflecting-content-attributes-in-idl-attributes](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#reflecting-content-attributes-in-idl-attributes)

### `XREF-STRING-LITERAL` — String literals: `"<code data-x="">text</code>"`
Literal strings are `<code data-x="">` with the quotation marks outside the code element. MIME
types follow the same rule when used as values, but are bare `<code>text/plain</code>` when used as
nouns. Compare with "is" directly: `If <var>type</var> is "<code data-x="">module</code>"`, not
"is the string …".
**Example:** [source#L7940](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7940) · [#create-a-potential-cors-request](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#create-a-potential-cors-request)
```html
   <li><p>Let <var>mode</var> be "<code data-x="">no-cors</code>" if <var>corsAttributeState</var> is
   <span data-x="attr-crossorigin-none">No CORS</span>, and "<code data-x="">cors</code>" otherwise.</p></li>
```

### `XREF-I-STATES` — `<i data-x>` for attribute-state concepts; `<i>` for labels
Named defaults of enumerated attributes are `<i data-x="missing value default">missing value
default</i>` / `invalid value default`. Bare `<i>` marks terms-as-terms, step labels, and legacy
flag names; it is not emphasis (`PRS-EMPHASIS`).
**Example:** [source#L5499](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L5499) · [#enumerated-attribute](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#enumerated-attribute)

### `XREF-THIS` — `<span>this</span>` for the receiver
In IDL member prose the receiver is `<span>this</span>`, with possessives like
`<span>this</span>'s <span>node document</span>`.
**Example:** [source#L10230](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L10230) · [#dom-domstringlist-length](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-domstringlist-length)
> **Branch**
> 1. **Modern** — `<span>this</span>`. [source#L10230](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L10230)
> 2. **Legacy** — "this element", "the element". [source#L27246](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L27246) · [#api-for-a-and-area-elements](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#api-for-a-and-area-elements)

### `XREF-INTERNAL-LINK` — `<a href="#id">` for section links; external links sparingly
Link to sections (not dfns) with `<a href="#id">descriptive text</a>`. External `<a href>` in
normative prose is rare and mostly GitHub issue references written as `org/repo#123`.
**Example:** [source#L1575](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1575) · [#event-loop-for-spec-authors](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#event-loop-for-spec-authors); issue link: [source#L67819](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L67819)

---

## 3. Definitions (`DFN`)

### `DFN-TYPED` — Use Wattsi's typed `<dfn>` attributes
Mark what is being defined so cross-spec linking works: `<dfn element>`, `<dfn interface>`,
`<dfn dictionary>`, `<dfn enum>`, `<dfn typedef>`, `<dfn callback>`, `<dfn attribute for="I">`,
`<dfn method for="I">`, `<dfn constructor for="I">`, `<dfn dict-member for="D">`,
`<dfn enum-value for="E">`, `<dfn element-attr for="el">`, `<dfn attr-value for="el/attr">`,
`<dfn element-state for="el/attr">`, `<dfn event for="I">`, `<dfn extended-attribute>`. Plain
`<dfn>` is for concepts and algorithms.
**Example:** [source#L38089](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L38089) · [#the-track-element](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-track-element); [source#L44148](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L44148) · [#event-media-loadstart](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#event-media-loadstart)
```html
  <dfn event for="HTMLMediaElement"><code data-x="event-media-loadstart">loadstart</code></dfn>
```

### `DFN-DATA-X-PLACEMENT` — Where the `data-x` key goes on API and attribute dfns
In prose, put the key on the inner `<code>`:
`<dfn attribute for="HTMLImageElement"><code data-x="dom-img-decoding">decoding</code></dfn>`.
Inside IDL blocks, put it on the `<dfn>` itself with no `<code>`:
`<dfn attribute for="HTMLElement" data-x="dom-lang">lang</dfn>`.
**Example:** [source#L31620](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L31620) · [#dom-img-decoding](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-img-decoding); in IDL: [source#L13047](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L13047) · [#dom-lang](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-lang)
> **Branch**
> 1. **Modern** — key on the inner `<code>` (prose) or on the `<dfn>` (IDL), as above.
> 2. **Accepted** — key on the `<dfn>` with a bare `<code>` child in prose:
>    `<dfn attribute for="DOMStringList" data-x="dom-DOMStringList-length"><code>length</code></dfn>`. [source#L10230](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L10230)
> 3. **Obsolete** — untyped `<dfn><code data-x="dom-media-bufferingRate">…</code></dfn>` without
>    `for`; add the type and `for` when touching. [source#L40018](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L40018)

### `DFN-FOR-VALUES` — `for=""` syntax
`for` takes the interface or element name; several targets are comma-separated without spaces
(`for="a,area"`); attribute values use `element/attribute` pairs
(`for="img/loading,audio/loading,video/loading,iframe/loading"`); global attributes use
`html-global/translate`.
**Example:** [source#L26451](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L26451) · [#attr-hyperlink-href](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#attr-hyperlink-href); [source#L8246](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8246) · [#attr-loading-lazy](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#attr-loading-lazy)

### `DFN-EXPORT` — Export what other specs need
Add `export` to dfns consumed by other standards; `data-noexport=""` is the default and is written
only for emphasis. Use `data-lt="alt|alt2"` for alternative link texts instead of duplicate dfns.
**Example:** [source#L94123](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L94123) · [#obtain-a-site](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#obtain-a-site)

### `DFN-ALGORITHM-NAMES` — Algorithm names are lowercase imperative verb phrases
Name algorithms as what they do ("parse a URL", "obtain a site", "set the frozen base URL"). Hooks
defined for other specs end in "steps" ("get the text steps", "removing steps"); boolean predicates
are phrases used after a subject ("<var>element</var> <dfn>cannot navigate</dfn> if …"). No leading
article and no "algorithm" suffix in the dfn text.
**Example:** [source#L7730](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7730) · [#parse-a-url](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parse-a-url); [source#L27254](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L27254) · [#cannot-navigate](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#cannot-navigate)

### `DFN-CONCEPT-NAMES` — Concept names are lowercase noun phrases; disambiguate with `data-x="concept-…"`
Define concepts in lowercase ("node document", "close watcher manager"). When the visible text
collides with another dfn ("origin", "URL", "document"), key the dfn
`data-x="concept-<owner>-<name>"` and link with the key. Capitalized dfn text is reserved for
IDL/ES names and struct items displayed in lists.
**Example:** [source#L11747](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11747) · [#concept-document-navigation-id](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#concept-document-navigation-id); [source#L89674](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L89674) · [#close-watcher-manager](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#close-watcher-manager)

### `DFN-EXPLICIT-ID` — `id=""` on a dfn only for anchor stability
Let Wattsi derive dfn ids; add `id` only when renaming a term whose old anchor is referenced.
**Example:** [source#L8951](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8951) · [#limited-to-only-non-negative-numbers-greater-than-zero-with-fallback](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#limited-to-only-non-negative-numbers-greater-than-zero-with-fallback)

### `DFN-NO-FLAGS` — Define booleans, not "flags"
New state is "a boolean, initially false", never "a <dfn>… flag</dfn>, which is initially unset".
**Example:** [source#L12274](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L12274) · [#was-created-via-cross-origin-redirects](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#was-created-via-cross-origin-redirects)
```html
  <p>A <code>Document</code> has a boolean <dfn export>was created via cross-origin redirects</dfn>,
  initially false.</p>
```
> **Branch**
> 1. **Modern** — boolean, as above.
> 2. **Legacy** — flag that is set/unset. [source#L86120](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L86120) · [#click-in-progress-flag](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#click-in-progress-flag)

### `DFN-STRUCT` — "is a struct with the following items:" + `<ul>` of dfn items
Define compound state as an Infra struct whose items are a `<ul>` of
`<li><p><dfn>Name</dfn>, a TYPE, initially VALUE.</p></li>`, accessed with the possessive
(`<var>manager</var>'s <span>groups</span>`). Use a tuple only for two-element pairs.
**Example:** [source#L89676](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L89676) · [#close-watcher-manager](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#close-watcher-manager)
```html
  <p>Each <code>Window</code> has a <dfn>close watcher manager</dfn>, which is a <span>struct</span>
  with the following <span data-x="struct item">items</span>:</p>

  <ul>
   <li><p><dfn data-x="close watcher manager groups">Groups</dfn>, a <span>list</span> of
```

### `DFN-WORD-AS-WORD` — Mark non-linked terms with `data-x=""`
When introducing ordinary words as terminology without a linkable concept, write
`<dfn data-x="">shown</dfn>` so Wattsi does not create a colliding link target.
**Example:** [source#L1558](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1558) · [#terminology](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#terminology)

---

## 4. Blocks: notes, examples, warnings, issues (`BLK`)

### `BLK-NOTE` — `<p class="note">` for one paragraph, `<div class="note">` for more
Notes are non-normative asides. They start with a capital letter and never with "Note:". Inside
algorithms, put the note in the `<li>` after the step's `<p>`.
**Example:** [source#L1575](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1575) · [#event-loop-for-spec-authors](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#event-loop-for-spec-authors); [source#L8122](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8122)

### `BLK-EXAMPLE` — `<div class="example">` with an intro sentence and `<pre>`
Examples are `<div class="example">` with an introductory `<p>` and the code, or
`<p class="example">` for prose-only examples. Give an `id="example-…"` when linked. Usual
openers: "Here, …", "In this example, …", "For example, …", "The following example …", "Consider …".
Show bad code first (`<pre class="bad">`), then the fix.
**Example:** [source#L23848](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L23848) · [#example-cite-usage-correct-vs-incorrect](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#example-cite-usage-correct-vs-incorrect)

### `BLK-WARNING` — `<p class="warning">` for security and safety advice
Reserve warnings for security, privacy, or data-loss hazards; `<div class="warning">` for several
blocks.
**Example:** [source#L1977](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1977) · [#interactive](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#interactive)

### `BLK-CRITICAL` — `<p class="critical">` for known spec gaps affecting interoperability
Used only for "this specification does not currently say …" notices. Ordinary open questions use
`BLK-XXX`.
**Example:** [source#L42919](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L42919)

### `BLK-XXX` — `<p class="XXX">` marks open issues in the text
Open issues are `<p class="XXX">` (inline `<span class="XXX">`), usually linking the tracking
issue. Never write "TODO" in visible text.
**Example:** [source#L1743](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1743)

### `BLK-SWITCH` — `<dl class="switch">` only inside algorithms
Case analysis uses `<dl class="switch">` with `<dt>` conditions and `<dd>` steps, inside an
algorithm step — never at the top level of a section.
**Example:** [source#L36491](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L36491) · [#the-embed-element](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-embed-element); condition-keyed: [source#L14993](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L14993) · [#the-dir-attribute](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-dir-attribute)

### `BLK-BRIEF-LIST` — `<ul class="brief">` for short enumerations
Use `ul.brief` with bare `<li>`s for lists of names or terms without sentences (attribute lists,
Dependencies terms). Prose lists keep `<li><p>`.
**Example:** [source#L14342](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L14342) · [#global-attributes](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#global-attributes)

### `BLK-HR` — `<hr>` separates topics inside one section
A bare `<hr>` splits a long section into topics without adding a heading.
**Example:** [source#L12042](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L12042) · [#dom-document-lastmodified](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-document-lastmodified)

### `BLK-DOMTREE` — `<ul class="domTree">` for DOM diagrams
DOM trees in examples are a single-line `<ul class="domTree">` with `class="t1"` (element) and
`t3` (text) items; not rewrapped.
**Example:** [source#L1122](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1122) · [#syntax-errors](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#syntax-errors)

### `BLK-FIGURE` — Inline accessible `<svg>` or `<img class="darkmode-aware">`
Diagrams are inline `<svg role="img" aria-label="…">` or
`<img src="/images/…" alt="…" class="darkmode-aware">`, optionally inside `<figure>`.
**Example:** [source#L32098](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L32098); [source#L20912](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L20912)

### `BLK-TABLE` — Tables have `<thead>`/`<tbody>` and `<th>` headers; `<caption>` only in examples
Data tables use `<table>` → `<thead><tr><th>…` → `<tbody>`. Author-facing tables inside examples
carry `<caption>` and `scope`; normative tables do not. Table-wide ids go on `<table id="…">`.
**Example:** [source#L8052](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8052) · [#referrer-policy-attribute](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#referrer-policy-attribute); [source#L48091](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L48091) · [#table-examples](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#table-examples)

---

## 5. Code and IDL blocks (`CODE`, `IDL`)

### `CODE-PRE-CLASS` — `<pre><code class="LANG">` on one line
Code blocks are `<pre><code class="html">` (`js`, `css`, `idl`, `abnf`), with the opening tags and
the first code line on the same line and `</code></pre>` right after the last line. Bare `<pre>`
is for non-highlighted text such as HTTP messages.
**Example:** [source#L669](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L669) · [#a-quick-introduction-to-html](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#a-quick-introduction-to-html); HTTP: [source#L17563](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L17563) · [#early-hints](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#early-hints)

### `CODE-ESCAPE` — Escape `<` and `&`, leave `>` raw
Inside `<pre>`/`<code>`, write `&lt;` and `&amp;` but keep `>` literal.
**Example:** [source#L12876](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L12876) · [#semantics](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#semantics)

### `CODE-EXAMPLE-DOC` — Complete documents start with `<!DOCTYPE html>` and `<html lang="en">`
Full-document examples use the modern doctype and a language-tagged root; omit
`<html>`/`<head>`/`<body>` only when the example is about tag omission.
**Example:** [source#L764](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L764) · [#a-quick-introduction-to-html](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#a-quick-introduction-to-html)

### `CODE-HIGHLIGHT` — `<strong>` highlights the relevant part of an example
Use `<strong>` to call out the lines or tokens an example is about; `<em>` only inside code
comments. Keep highlights out of normative `<pre class="idl">`.
**Example:** [source#L14899](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L14899) · [#the-dir-attribute](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-dir-attribute)

### `CODE-BAD` — `<pre class="bad">` for non-conforming or discouraged code
Anti-examples are `<pre class="bad"><code class="html">`, usually followed by the corrected
version.
**Example:** [source#L948](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L948) · [#common-pitfalls-to-avoid-when-using-the-scripting-apis](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#common-pitfalls-to-avoid-when-using-the-scripting-apis)

### `IDL-BLOCK` — IDL goes in `<pre><code class="idl">` right after the heading
Interface definitions follow the section heading (or `dl.element`'s "DOM interface" `<dd w-nodev>`)
as `<pre><code class="idl">`: extended attributes first (`[Exposed=Window]` on its own line), then
`interface <dfn interface>Name</dfn> : <span>Parent</span> {`.
**Example:** [source#L86143](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L86143) · [#the-toggleevent-interface](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-toggleevent-interface); [source#L16112](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L16112) · [#the-head-element](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-head-element)
```html
  <pre><code class="idl">[Exposed=Window]
interface <dfn interface>HTMLHtmlElement</dfn> : <span>HTMLElement</span> {
  [<span>HTMLConstructor</span>] constructor();
```

### `IDL-XREF-SPAN` — Cross-references inside IDL use `<span>`, never `<code>`
Types, members, and extended attributes inside `<pre class="idl">` link via `<span>` or
`<span data-x>`; members defined in prose are `<span data-x="dom-document-hidden">hidden</span>`.
**Example:** [source#L11718](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11718) · [#dom-document-hidden](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-document-hidden)

### `IDL-EXTENDED-ATTRS` — Link extended attributes that HTML defines; leave Web IDL's bare
`[<span>CEReactions</span>]`, `[<span>HTMLConstructor</span>]`,
`[<span data-x="xattr-Reflect">Reflect</span>]`, `<span>LegacyUnforgeable</span>`, and
`<span>LegacyUnenumerableNamedProperties</span>` are linked; `[Exposed=…]`, `[SameObject]`,
`[NewObject]`, `[EnforceRange]`, `[PutForwards=…]`, `[Replaceable]`, `[SecureContext]` are bare.
Single space after `optional` and types.
**Example:** [source#L9608](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L9608) · [#htmlallcollection](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#htmlallcollection); [source#L71012](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L71012) · [#dom-context-2d-gettransform](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-context-2d-gettransform)

### `IDL-REFLECT-IN-IDL` — Reflected attributes are declared with `[Reflect]` in the IDL
Attributes that reflect a content attribute carry their dfn in the IDL together with the
`Reflect*` extended attributes (`ReflectSetter`, `ReflectURL`, `ReflectDefault`, `ReflectRange`,
…), replacing the prose sentence.
**Example:** [source#L13047](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L13047) · [#dom-lang](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-lang); definitions: [source#L9427](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L9427) · [#using-reflect-via-idl-extended-attributes](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#using-reflect-via-idl-extended-attributes)
```html
  [<span>CEReactions</span>, <span data-x="xattr-Reflect">Reflect</span>] attribute DOMString <dfn attribute for="HTMLElement" data-x="dom-lang">lang</dfn>;
```
> **Branch**
> 1. **Modern** — `[Reflect]` plus dfn in the IDL, as above.
> 2. **Accepted** (only when the extended attributes cannot express it) — prose: "The
>    `<dfn attribute for="HTMLImageElement"><code data-x="dom-img-decoding">decoding</code></dfn>`
>    IDL attribute must <span>reflect</span> the … content attribute, <span>limited to only known
>    values</span>." [source#L31620](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L31620) · [#dom-img-decoding](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-img-decoding)

### `IDL-GENERICS` — Escape `<` in generics, keep `>`
`sequence&lt;Node>`, `<span data-x="idl-Promise">Promise</span>&lt;undefined>`,
`FrozenArray&lt;<var>T</var>>`; `Promise` links to `idl-Promise`.
**Example:** [source#L31233](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L31233) · [#dom-img-decode](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-img-decode); [source#L70217](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L70217)

### `IDL-DICTIONARY` — Members are defined inline; optional dictionary arguments default to `{}`
`dictionary <dfn dictionary>X</dfn> { boolean <dfn dict-member for="X" data-x="dom-X-y">y</dfn> = false; }`.
Boolean members get an explicit default unless absence is meaningful. Dictionary arguments are
`optional <span>X</span> options = {}`. Read members with `VAL-DICT-ACCESS`.
**Example:** [source#L102791](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L102791) · [#dom-navigateeventinit-canintercept](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-navigateeventinit-canintercept)

### `IDL-ENUM-VALUES` — Where enum values are defined
Either keep plain strings in the IDL and define each value in a prose `<dl>` whose `<dt>` is
`"<dfn enum-value for="E"><code data-x="dom-E-value">value</code></dfn>"` (when values need
explanation), or put the `<dfn enum-value>` directly inside the IDL (when they are
self-explanatory).
**Example:** [source#L100766](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L100766) · [#dom-navigationtype-push](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-navigationtype-push); in IDL: [source#L102809](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L102809) · [#dom-navigationfocusreset-after-transition](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-navigationfocusreset-after-transition)
> **Branch**
> 1. **Accepted** — strings in IDL + prose `<dl>` of `enum-value` dfns.
> 2. **Accepted** — `<dfn enum-value>` inside the IDL.
> 3. **Legacy** — `<span data-x="dom-CanPlayTypeResult-maybe">maybe</span>` in the IDL plus an
>    untyped dfn. [source#L38124](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L38124) · [#canplaytyperesult](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#canplaytyperesult)

### `IDL-CONSTRUCTOR` — Constructor declarations
In IDL: `constructor(DOMString type, optional <span>ErrorEventInit</span> eventInitDict = {});` or
`[<span>HTMLConstructor</span>] constructor();` for elements. In prose the dfn carries the full
signature: `<dfn constructor for="OffscreenCanvas"><code data-x="dom-OffscreenCanvas">new
OffscreenCanvas(<var>width</var>, <var>height</var>)</code></dfn>` (`API-CONSTRUCTOR-STEPS`).
**Example:** [source#L77037](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L77037) · [#dom-offscreencanvas](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-offscreencanvas)

### `IDL-COMMENTS` — Comments inside IDL
Use `// ` comments to note inherited members
(`// inherits <span data-x="dom-HTMLCollection-length">length</span>`) and to point to obsolete
partials (`// <a href="#HTMLImageElement-partial">also has obsolete members</a>`).
**Example:** [source#L9779](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L9779) · [#the-htmloptionscollection-interface](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-htmloptionscollection-interface); [source#L11725](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11725)

### `IDL-PARTIAL-OBSOLETE` — Obsolete members live in `partial interface` blocks in "Obsolete features"
`partial interface <span id="HTMLImageElement-partial">HTMLImageElement</span> { … }`, each with
an explicit `Interface-partial` id referenced from the main IDL comment.
**Example:** [source#L86010](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L86010) · [#NavigatorUserActivation-partial](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#NavigatorUserActivation-partial)

### `IDL-EVENT-HANDLERS` — Event handler IDL attributes
`attribute <span>EventHandler</span> <span data-x="handler-onvisibilitychange">onvisibilitychange</span>;`
in the IDL; the dfn lives in the event-handler tables
(`<dfn attribute for="GlobalEventHandlers"><code data-x="handler-onabort">onabort</code></dfn>`)
with the event name in the second column.
**Example:** [source#L11723](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11723)

---

## 6. Element definitions (`ELEM`)

### `ELEM-DL-ELEMENT` — The `dl.element` box
Every element section starts with `<dl class="element">` whose `<dt>`s are, in order: Categories ·
Contexts in which this element can be used · Content model · Tag omission in text/html · Content
attributes · Accessibility considerations · DOM interface. `<dt>` text is a
`<span data-x="concept-element-…">` link ending in a colon; `<dd>`s are bare phrases ending in a
period. Content attributes list `<dd><span>Global attributes</span></dd>` first, then one
`<dd><code data-x="attr-…">name</code></dd>` per attribute. "DOM interface" is `<dd w-nodev>` +
IDL followed by `<dd w-dev>Uses <code>HTMLHtmlElement</code>.</dd>`, or
`<dd>Uses <code>HTMLElement</code>.</dd>` when there is no dedicated interface.
**Example:** [source#L16155](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L16155) · [#the-head-element](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-head-element); [source#L23270](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L23270) · [#the-a-element](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-a-element)

### `ELEM-REPRESENTS` — First sentence: "The `<code>x</code>` element <span>represents</span> …"
State the element's meaning with the linked verb "represents".
**Example:** [source#L16250](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L16250) · [#the-title-element](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-title-element)

### `ELEM-ATTR-DEFINITION` — Attribute definition sentence
"The `<dfn element-attr for="source" data-x="attr-source-type"><code>type</code></dfn>` attribute
may be present. If present, the value must be a <span>valid MIME type string</span>." or "The
`<code>x</code>` attribute, if specified, must have a value that is a <span>valid …</span>."
Author requirements use "must"; the processing model follows separately.
**Example:** [source#L30895](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L30895) · [#attr-source-type](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#attr-source-type); [source#L52452](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L52452)

### `ELEM-BOOLEAN-ATTR` — "The `x` attribute is a <span>boolean attribute</span>."
**Example:** [source#L20776](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L20776)

### `ELEM-ENUMERATED-ATTR` — Enumerated attributes use the keyword/state table
"The `x` attribute is an <span>enumerated attribute</span> with the following keywords and
states:" followed by a Keyword | State | Brief description table — keyword cells
`<dfn attr-value for="…"><code data-x="attr-…-keyword">kw</code></dfn>`, state cells
`<dfn data-x="attr-…-kw-state">Kw</dfn>` — then sentences for the
`<i data-x="missing value default">missing value default</i>` and
`<i data-x="invalid value default">invalid value default</i>`.
**Example:** [source#L8240](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8240) · [#lazy-loading-attributes](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#lazy-loading-attributes)

### `ELEM-DOMINTRO` — The `dl.domintro` box
Developer summaries are `<dl class="domintro">`:
`<dt><code data-x=""><var>element</var>.<span subdfn data-x="dom-…">member</span>(<var>arg</var>[, <var>opt</var>])</code></dt>`;
promise-returning APIs as `<var>promise</var> = …` or `await …`; constructors as
`<var>audio</var> = new <span subdfn data-x="dom-Audio">Audio</span>([ <var>url</var> ])`; setters
as `… = <var>value</var>`. The `<dd>` is non-normative present tense ("Returns …", "Can be set,
to …", "Throws a <span>"<code>DataCloneError</code>"</span> <code>DOMException</code> if …") and
self-contained — no "see below".
**Example:** [source#L9791](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L9791) · [#the-htmlformcontrolscollection-interface](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-htmlformcontrolscollection-interface); [source#L11587](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11587) · [#dom-structuredclone](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-structuredclone)
```html
  <dl class="domintro">
   <dt><code data-x=""><var>collection</var>.<span subdfn data-x="dom-HTMLCollection-length">length</span></code></dt>
   <dd><p>Returns the number of elements in <var>collection</var>.</p></dd>
```

---

## 7. Developer's Edition annotations (`DEV`)

### `DEV-W-NODEV` — Wrap implementer-only text in `w-nodev`
Processing models, algorithms, IDL prose, and implementer notes go inside `<div w-nodev>`
(`<p w-nodev>`, `<span w-nodev>` for smaller units). `dl.domintro`, `dl.element`, examples, and
author conformance text stay visible. `<pre class="idl">` is omitted automatically.
**Example:** [source#L175](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L175) · [#introduction](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#introduction); [source#L9576](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L9576)

### `DEV-W-DEV` — `w-dev` for developer-only substitutes
When the Developer's Edition needs a replacement sentence (e.g. "Uses `HTMLHtmlElement`." in place
of IDL), add it with `w-dev` (`<dd w-dev>`, `<span w-dev>`, `<p w-dev>`).
**Example:** [source#L16119](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L16119) · [#the-html-element](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-html-element); [source#L46474](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L46474)

---

## 8. Algorithm structure (`ALG`)

### `ALG-DIV-ALGORITHM` — Wrap every algorithm in `<div algorithm>`
The preamble `<p>` and its `<ol>` live inside one `<div algorithm>`, which scopes `<var>` names so
the build can flag unused or undeclared variables. One algorithm per `<div>`.
**Example:** [source#L1595](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1595) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#starting-a-new-parallel-queue)
```html
  <div algorithm>
  <p>To <dfn data-x="starting a new parallel queue" export>start a new parallel queue</dfn>, run the following steps:</p>

  <ol>
   <li><p>Let <var>parallelQueue</var> be a new <span>parallel queue</span>.</p></li>
```

### `ALG-PREAMBLE` — "To <dfn>name</dfn>, given a TYPE <var>x</var>…:"
The first paragraph names the algorithm with a `<dfn>`, lists typed parameters after "given", and
ends with a colon.
**Example:** [source#L67331](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L67331) · [#light-dismiss-open-dialogs](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#light-dismiss-open-dialogs)
```html
  <p>To <dfn>light dismiss open dialogs</dfn>, given a <code>PointerEvent</code> <var>event</var>:</p>
```
> **Branch**
> 1. **Modern** — direct colon, no verb phrase, as above.
> 2. **Accepted** — "…, perform the following steps:" and "…, run these steps." (the latter usually
>    when a return sentence follows). [source#L9700](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L9700) · [#concept-get-all-named](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#concept-get-all-named); [source#L7730](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7730) · [#parse-a-url](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parse-a-url)
> 3. **Legacy** — "…, run the following steps:", "the user agent must run the following steps",
>    "When the user agent is to <dfn>…</dfn>, it must…", "The steps … are as follows:". [source#L33135](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L33135) · [#update-the-image-data](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#update-the-image-data)

### `ALG-PARAM-TYPES` — Every parameter carries a type and a `<var>` name
"a string <var>url</var>", "a `<code>Document</code>` <var>document</var>", "a <span>list</span> of
<span data-x="URL">URLs</span> <var>urls</var>". Nullable types are "TYPE-or-null" ("a
<span>navigable</span>-or-null <var>parent</var>") and unions chain with "-or-". Several parameters
are joined with commas and a final "and".
**Example:** [source#L7730](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7730) · [#parse-a-url](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parse-a-url); or-null: [source#L105494](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105494); union: [source#L69804](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L69804) · [#insertion-target](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#insertion-target)
```html
  <p>To <dfn export>parse a URL</dfn>, given a string <var>url</var>, relative to a
  <code>Document</code> object or <span>environment settings object</span> <var>environment</var>,
  run these steps. They return failure or a <span>URL</span>.</p>
```

### `ALG-OPTIONAL-ARGS` — "an optional TYPE <var>x</var> (default VALUE)"
Declare optional parameters inline with their default in parentheses. Inside the steps test
presence with "If <var>x</var> was not given" / "is not given, then set it to …".
**Example:** [source#L35740](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L35740); [source#L102389](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L102389); [source#L66720](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L66720)
```html
  null), and an optional boolean <var>initialInsertion</var> (default false):</p>
```

### `ALG-RETURN-SENTENCE` — State the return type: "They return X."
When an algorithm returns something, add a sentence to the preamble: "They return failure or a
<span>URL</span>." Hooks that return nothing say "returns nothing".
**Example:** [source#L7732](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7732) · [#parse-a-url](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parse-a-url); [source#L87569](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L87569)
> **Branch**
> 1. **Modern** — "They return X."
> 2. **Legacy** — "It returns X." [source#L7993](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7993)

### `ALG-ASSERT` — `<span>Assert</span>: condition.`
State invariants as a linked "Assert:" step; never the bare unlinked word. Assertions describe
what is already true, not behavior. Add one where a nullable value is known to be non-null.
**Example:** [source#L67334](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L67334) · [#light-dismiss-open-dialogs](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#light-dismiss-open-dialogs); [source#L1614](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1614) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#starting-a-new-parallel-queue)
```html
   <li><p><span>Assert</span>: <var>event</var>'s <code
   data-x="dom-Event-isTrusted">isTrusted</code> attribute is true.</p></li>
```

### `ALG-VAR-SCOPE` — `<var ignore>` and `var-scope` for variables outside an algorithm
A `<var>` used outside a `<div algorithm>` (prose, notes, tables, hook signatures) is
`<var ignore>`; a block that introduces its own variables (examples, closures) gets `var-scope`
(`<div class="example" var-scope>`).
**Example:** [source#L8597](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8597) · [#set-the-content-attribute](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#set-the-content-attribute); [source#L1633](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1633) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism)
```html
   <li><dfn>set the content attribute</dfn>: takes a string <var ignore>value</var>; returns nothing.</li>
```

### `ALG-NESTED-STEPS` — A step with sub-steps is `<li><p>Lead-in:</p><ol>…</ol></li>`
When a step opens a block ("Run the following steps <span>in parallel</span>:", "While true:",
"Otherwise:", "If <var>x</var> is <var>y</var>:"), the lead-in ends with a colon and the nested
`<ol>` follows inside the same `<li>`, indented one more space. Notes and comments about a step go
inside that `<li>` after its `<p>`.
**Example:** [source#L1601](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1601) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#starting-a-new-parallel-queue); note in a step: [source#L119518](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L119518)

### `ALG-HOOKS` — "The <span>X steps</span> for the HTML Standard, given <var>y</var>, are defined as the following:"
Implementations of hooks defined by other standards (DOM insertion/removal steps, Fetch
callbacks, Web IDL hooks) link the hook name and do not create a new `<dfn>`; per-element hooks
read "The <span>HTML element insertion steps</span> for `<code>el</code>` elements, given
<var>insertedNode</var>, are:".
**Example:** [source#L1789](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1789) · [#dom-trees](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-trees)
```html
  <p>The <span data-x="concept-node-insert-ext">insertion steps</span> for the HTML Standard, given
  <var>insertedNode</var>, are defined as the following:</p>
```

### `ALG-ES-ABSTRACT-OPS` — ECMAScript abstract operations: `? <span>Name</span>(args)`
Call into ECMAScript with the JavaScript spec's notation verbatim: `Perform ? <span>Call</span>(…)`,
`Let <var>x</var> be ! <span>ToUint32</span>(<var>P</var>)`, `<var>record</var>.<span data-x="js-Link">Link</span>()`;
internal slots `[[Name]]` are unlinked; names that collide with HTML terms link via `data-x="js-Get"`.
The `?`/`!` prefixes are the only places where exceptions propagate implicitly (`EXC-RETHROW`).
**Example:** [source#L10575](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L10575) · [#structuredserializeinternal](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#structuredserializeinternal); [source#L11365](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11365); [source#L98726](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L98726)
```html
        <p>Let <var>dataCopy</var> be ? <span>CreateByteDataBlock</span>(<var>size</var>).</p>
```

### `ALG-NON-NORMATIVE-NOTES` — Explain *why* in a `<p class="note">`, never in the step
Rationale, implementation hints, and cross-references go in a note after the step or after the
algorithm, not in the normative sentence.
**Example:** [source#L1618](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1618) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#starting-a-new-parallel-queue)

---

## 9. Control flow (`FLOW`)

### `FLOW-IF-THEN` — "If <condition>, then <action>."
Single-sentence conditionals always use ", then". Join conditions with "and"/"or"; negate with
"is not". The form without "then" is Legacy and only tolerated inside the older micro-syntax
parsers.
**Example:** [source#L1612](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1612) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#starting-a-new-parallel-queue); Legacy: [source#L5572](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L5572)
```html
       <li><p>If <var>steps</var> is not nothing, then run <var>steps</var>.</p></li>
```

### `FLOW-IF-BLOCK` — "If <condition>:" + nested steps; "Otherwise:" + nested steps
When the consequent is more than one step, end the lead-in with a colon and nest an `<ol>`. Do not
write "then:" or "do the following:".
**Example:** [source#L5822](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L5822) · [#rules-for-parsing-floating-point-number-values](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#rules-for-parsing-floating-point-number-values); "Otherwise:": [source#L7250](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7250)

### `FLOW-OTHERWISE` — "Otherwise, if …, then …" / "Otherwise, …"; never "Else"
Chains of alternatives use "Otherwise, if …, then …" and end with "Otherwise, …", each alternative
in its own `<li>`. "Else", "Else if", and "Otherwise if" (without the comma) do not occur.
**Example:** [source#L6131](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L6131); [source#L19309](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L19309)
```html
     <li><p>Otherwise, <span data-x="concept-event-fire">fire an event</span> named <code
     data-x="event-error">error</code> at <var>element</var>.</p></li>
```

### `FLOW-TERNARY` — "Let <var>x</var> be A if <condition>; otherwise B."
A two-way value choice is one sentence with "; otherwise", not two steps.
**Example:** [source#L7735](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7735) · [#parse-a-url](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parse-a-url)
```html
   <li><p>Let <var>baseURL</var> be <var>environment</var>'s <span data-x="document base URL">base
   URL</span>, if <var>environment</var> is a <code>Document</code> object; otherwise
   <var>environment</var>'s <span>API base URL</span>.</p></li>
```

### `FLOW-ANY-ALL` — "If any/all of the following are true:" + `<ul>` + "then …"
Three or more conditions become a bulleted list: lead-in `<p>If any of the following are
true:</p>` (or "all"), a `<ul>` of `<li><p>…;</p></li>` items with "; or" / "; and" on the
penultimate item and "," on the last, then a closing `<p>then …</p>` inside the same `<li>`.
**Example:** [source#L16454](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L16454) · [#set-the-frozen-base-url](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#set-the-frozen-base-url); "all": [source#L28503](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L28503)
```html
    <p>If any of the following are true:</p>

    <ul>
     <li><p><var>urlRecord</var> is failure;</p></li>

     <li><p><var>urlRecord</var>'s <span data-x="concept-url-scheme">scheme</span> is "<code
     data-x="">data</code>" or "<code data-x="">javascript</code>"; or</p></li>

     <li><p>running <span>Is base allowed for Document?</span> on <var>urlRecord</var> and
     <var>document</var> returns "<code data-x="">Blocked</code>",</p></li>
    </ul>

    <p>then set <var>element</var>'s <span>frozen base URL</span> to <var>document</var>'s
    <span>fallback base URL</span> and return.</p>
```

### `FLOW-RETURN` — "return" ends an algorithm; "abort these steps" ends a parallel or queued block
Early exits are "…, then return." / "return <var>x</var>." "Abort these steps" is reserved for
leaving a set of steps that is not the algorithm itself — steps run <span>in parallel</span>, a
queued task, or a closure — where "return" would be ambiguous. Prefer an early-return guard as
step 1 over deep nesting.
**Example:** [source#L36152](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L36152); abort: [source#L1654](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1654) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism)
```html
    <li><p>If <var>document</var> is not <span>fully active</span>, then return false.</p></li>
```

### `FLOW-SWITCH` — "Switch on <var>x</var>:" + `<dl class="switch">`
Multi-way branches on a value use a lead-in `<p>Switch on <var>x</var>:</p>` and a
`<dl class="switch">` whose `<dt>`s are the cases. Condition-keyed switches write each `<dt>` as
"If <var>element</var> is a `<code>bdi</code>` element" and end with `<dt>Otherwise</dt>`. Cases
that compute a value should return it rather than set an outer variable.
**Example:** [source#L36491](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L36491) · [#the-embed-element](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-embed-element); condition-keyed: [source#L14993](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L14993) · [#the-dir-attribute](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-dir-attribute)
```html
        <p>Switch on <var>type</var>:</p>

        <dl class="switch">
         <dt>null</dt>
         <dd>
```
> **Branch**
> 1. **Modern** — "Switch on <var>x</var>:".
> 2. **Legacy** — "Run the appropriate steps from the following list:", "Follow these substeps:". [source#L38931](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L38931)

### `FLOW-FOR-EACH` — "For each <var>item</var> of <var>list</var>:"
Iteration is Infra's "For each" (`<span data-x="list iterate">For each</span>` when linked) with
"of" for lists and maps ("For each <var>key</var> → <var>value</var> of <var>map</var>").
Single-step bodies stay inline after the colon; longer bodies nest an `<ol>`. Ordered traversals
add "in <span>tree order</span>" / "in reverse order". There is no "continue" or "break":
restructure with conditions, early returns, or a `while`.
**Example:** [source#L58808](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L58808); linked: [source#L7873](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7873)
> **Branch**
> 1. **Modern** — "For each <var>x</var> of <var>y</var>".
> 2. **Legacy** — "For each <var>x</var> in <var>y</var>". [source#L8335](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8335)

### `FLOW-WHILE` — "While <condition>:" and "While true:"
Loops are "While <condition>:" lead-ins with nested steps; infinite loops are "While true:" and
exit via return.
**Example:** [source#L1606](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1606) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#starting-a-new-parallel-queue); [source#L6025](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L6025)

### `FLOW-LABELS-LEGACY` — `<i>Label</i>:` steps and "jump to the step labeled <i>x</i>" are Legacy
Older parsers label steps (`<i>Loop</i>:`) and jump to them. New text expresses this with
`while`, nested steps, and early returns.
**Example:** [source#L5778](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L5778) · [#rules-for-parsing-floating-point-number-values](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#rules-for-parsing-floating-point-number-values); [source#L47904](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L47904)

### `FLOW-WAIT` — "Wait until <condition>." only in parallel steps
Blocking is "Wait until <var>eventsFired</var> is true." or "Wait for <thing>" and is legal only
inside steps that run <span>in parallel</span>.
**Example:** [source#L33146](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L33146) · [#update-the-image-data](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#update-the-image-data); [source#L109998](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L109998)

### `FLOW-INCREMENT` — "Increment <var>x</var>."
Counters are changed with "Increment"/"Decrement <var>x</var>" when the step is one, or with an
explicit amount.
**Example:** [source#L109542](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L109542); [source#L92968](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L92968)
> **Branch**
> 1. **Modern** — "Increment <var>scriptHistoryIndex</var>."
> 2. **Accepted** — "Increment <var>i</var> by 1." [source#L22262](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L22262) and "by one" [source#L24514](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L24514); match the surrounding algorithm.

---

## 10. Variables (`VAR`)

### `VAR-LET-SET` — "Let <var>x</var> be …" declares; "Set <var>x</var> to …" assigns
`Let` introduces a variable exactly once; later changes use `Set … to`. Values filled in later
start as "be null" / "be false". Never "Let … equal", "Define", or "Create".
**Example:** [source#L1599](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1599) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#starting-a-new-parallel-queue); set: [source#L63694](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L63694)

### `VAR-CAMELCASE` — Variable names are camelCase
`<var>parallelQueue</var>`, `<var>urlRecord</var>`. Names describe the value; type suffixes
(`…Flag`, `…List`) are avoided.
**Example:** [source#L16457](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L16457) · [#set-the-frozen-base-url](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#set-the-frozen-base-url)
> **Branch**
> 1. **Modern** — camelCase.
> 2. **Legacy** — space-separated multi-word names, `<var>date present</var>`. [source#L7381](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7381) · [#parse-a-date-or-time-string](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parse-a-date-or-time-string)
> 3. **Obsolete** — hyphenated names. [source#L5868](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L5868)

### `VAR-SHORT-NAMES` — Short names for short scopes, descriptive names for long ones
`<var>p</var>` for the promise an API returns, `<var>i</var>`/`<var>n</var>` for indices,
`<var>el</var>`/`<var>element</var>`, `<var>document</var>`, `<var>global</var>`, `<var>event</var>`.
**Example:** [source#L1642](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1642) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism); [source#L22262](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L22262)

### `VAR-POSSESSIVE` — "<var>x</var>'s <span>field</span>" for state access
Fields and associated concepts are read with the possessive, chained freely
("<var>element</var>'s <span>node document</span>'s <span>relevant global object</span>"). The
genitive "the <span>field</span> of <var>x</var>" is used only where the possessive reads badly.
**Example:** [source#L1610](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1610) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#starting-a-new-parallel-queue); genitive: [source#L7491](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7491)

### `VAR-THIS` — The receiver is `<span>this</span>`, not `<var>this</var>` or "the element"
In getter/setter/method steps the object is `<span>this</span>` (`XREF-THIS`); name a local
(`Let <var>element</var> be <span>this</span>`) only when it is passed on repeatedly.
**Example:** [source#L1645](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1645) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism)

### `VAR-MARKUP` — Variables are `<var>`; never `<i>`, `<em>`, or backticks
Every occurrence, including inside `<code>` for API signatures and inside IDL comments, uses
`<var>`. Variables are not pluralized or inflected ("<var>nodes</var>' items", not
"<var>node</var>s").
**Example:** [source#L618](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L618) · [#typographic-conventions](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#typographic-conventions)

---

## 11. Values and data structures (`VAL`)

### `VAL-LIST-LITERAL` — `« »` for list literals; "an empty <span>list</span>"
Infra list literals use guillemets with inner spaces: `« »`, `« <var>a</var>, <var>b</var> »`.
Declarations say "an empty <span>list</span>" or "a new <span>list</span>"; "an empty array" is
Legacy.
**Example:** [source#L9248](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L9248); [source#L9261](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L9261); with items: [source#L124882](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L124882)

### `VAL-LIST-OPS` — Infra list verbs, linked with `data-x="list …"`
`<span data-x="list append">Append</span>`, `<span data-x="list contains">contains</span>`,
`<span data-x="list size">size</span>`, `list remove`, `list extend`,
`<span data-x="list is empty">is empty</span>`, `list iterate`; indexing is `<var>list</var>[0]`.
"Add … to the list", "push", and "length" are not used for lists.
**Example:** [source#L1659](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1659) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism); [source#L1635](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1635); size/index: [source#L9748](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L9748)

### `VAL-MAP-OPS` — Maps: `«[ "key" → value ]»`, `<var>map</var>[<var>key</var>]`, `exists`
Map literals are `«[ "<code data-x="">a</code>" → 1 ]»`; lookup is bracket syntax; existence is
`<span data-x="map exists">exists</span>`; assignment is `<span data-x="map set">set</span>
<var>map</var>[<var>k</var>] to <var>v</var>`.
**Example:** [source#L10489](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L10489) · [#structuredserializeinternal](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#structuredserializeinternal); literal: [source#L8394](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8394)
```html
   <li><p>If <var>memory</var>[<var>value</var>] <span data-x="map exists">exists</span>, then
```

### `VAL-DICT-ACCESS` — Dictionary members: `<var>options</var>["<code data-x="dom-X-y">y</code>"]`
Read Web IDL dictionary members with Infra map syntax and a linked member name; presence is
`<span data-x="map exists">exists</span>`.
**Example:** [source#L11601](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11601) · [#dom-structuredclone](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-structuredclone)
> **Branch**
> 1. **Modern** — `<var>options</var>["<code data-x="dom-StructuredSerializeOptions-transfer">transfer</code>"]`.
> 2. **Legacy** — "<var>options</var>'s `<code>foo</code>` member". [source#L126393](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L126393)

### `VAL-STRUCT-ITEMS` — Structs are declared once; items are accessed possessively
Declare per `DFN-STRUCT`; items may carry "(default 0)". Access is "<var>timing</var>'s
<span>navigation start time</span>"; construction is "a new <span>document load timing
info</span>" optionally followed by "whose <span>x</span> is <var>y</var>".
**Example:** [source#L12277](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L12277) · [#document-load-timing-info](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#document-load-timing-info); `<ul>` form: [source#L44008](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L44008)

### `VAL-BOOLEANS` — Booleans "are true"/"false"; never "set"/"unset"
Test with "is true"/"is false"; change with "set … to true/false". The "flag is set / unset the
flag" vocabulary is Legacy (`DFN-NO-FLAGS`).
**Example:** [source#L109998](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L109998); Legacy: [source#L41541](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L41541)

### `VAL-NULL` — "is null" / "is not null" as predicates; "non-null" only as an adjective
Tests are "If <var>x</var> is not null, then …". "non-null" modifies a noun ("a non-null
<span>navigable</span>") and is never written "is non-null". Nullable types are "TYPE-or-null".
**Example:** [source#L15152](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L15152); adjective: [source#L1862](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1862)

### `VAL-EMPTY-STRING` — "the empty string", not "an empty string" or `""`
Emptiness of lists is "is empty" (`VAL-LIST-OPS`).
**Example:** [source#L38967](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L38967)

### `VAL-CODE-POINTS` — "U+0065 (e)" in new text; "U+002D HYPHEN-MINUS (-)" when naming matters
Use "code point" for units of a string; "character" remains the parser's and author-facing term.
Named sets link to Infra: `<span>ASCII whitespace</span>`, `<span>ASCII digits</span>`,
`<span>ASCII alpha</span>`.
**Example:** [source#L5822](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L5822) · [#rules-for-parsing-floating-point-number-values](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#rules-for-parsing-floating-point-number-values)
> **Branch**
> 1. **Modern** — short form `U+0065 (e)`.
> 2. **Accepted** — full form `U+002D HYPHEN-MINUS (-)` in micro-syntax definitions and wherever
>    the glyph is ambiguous (hyphen vs minus, spaces, quotes). [source#L5548](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L5548) · [#valid-integer](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#valid-integer)
> 3. **Accepted in the parser only** — bare name `U+0060 GRAVE ACCENT`; Legacy elsewhere. [source#L1176](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1176)

### `VAL-STRINGS` — String comparison vocabulary
Equality is "is" / "is not" with a string literal (`XREF-STRING-LITERAL`); case-insensitive
comparison is "is an <span>ASCII case-insensitive</span> match for"; prefix tests are
`<span data-x="string starts with">starts with</span>`; whitespace handling is
`<span data-x="strip leading and trailing ASCII whitespace">strip…</span>` and
`<span>split on ASCII whitespace</span>`. Never "equals (ignoring case)" or "compare".
**Example:** [source#L17490](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L17490)

### `VAL-COMPARISONS` — Spell out comparisons; `&le;`/`&ge;` only in ranges
"is less than", "is greater than or equal to"; numeric equality is "equals" or "is equal to",
identity is "is". Ranges in micro-syntaxes use entities with `&nbsp;`:
`1&nbsp;&le;&nbsp;<var>month</var>&nbsp;&le;&nbsp;12`.
**Example:** [source#L5642](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L5642) · [#rules-for-parsing-integers](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#rules-for-parsing-integers); range: [source#L6201](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L6201) · [#parse-a-month-component](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parse-a-month-component); equals: [source#L114661](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L114661)
> **Branch** (minus sign)
> 1. **Modern** — `&minus;`. [source#L10030](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L10030)
> 2. **Legacy** — `&#x2212;`. [source#L5757](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L5757)

### `VAL-NUMBERS` — Digits in algorithms, words in prose; "implementation-defined" is linked
Steps use digits ("by 1", "index 0"); prose uses words up to ten. Values left to the UA are
`<span>implementation-defined</span>` (linked to Infra), not "UA-defined", "undefined", or
"unspecified".
**Example:** [source#L1944](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1944); [source#L22262](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L22262)

### `VAL-ENUM-STATES` — Internal enumerations are string values
Declare as "one of "…", "…", or "…", initially "…"" with `"<code data-x="">pending</code>"`
literals. Attribute *states* of enumerated attributes are a different thing:
`<span data-x="attr-…-state">Eager</span>`, capitalized (`ELEM-ENUMERATED-ATTR`).
**Example:** [source#L107391](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L107391)
> **Branch**
> 1. **Modern** — string values.
> 2. **Accepted** — italic labels `<i>years</i>`, `<i>object</i>` for states never observable as
>    strings. [source#L7180](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7180) · [#parse-a-duration-string](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parse-a-duration-string); [source#L38896](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L38896)

---

## 12. State declarations (`STATE`)

### `STATE-DECLARATION` — "Each X has a TYPE <dfn>name</dfn>, initially VALUE."
Declare per-object state in its own `<p>` with the owner, the type, a `<dfn>`, and the initial
value in one sentence.
**Example:** [source#L12274](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L12274) · [#was-created-via-cross-origin-redirects](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#was-created-via-cross-origin-redirects); union type: [source#L69804](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L69804) · [#insertion-target](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#insertion-target)
```html
  <p>A <code>Document</code> has a boolean <dfn export>was created via cross-origin redirects</dfn>,
  initially false.</p>
```
> **Branch**
> 1. **Modern** — type before the name, as above.
> 2. **Accepted** — "has an associated <dfn>name</dfn>, which is a TYPE or null, initially null."
>    [source#L11785](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11785) · [#concept-document-internal-ancestor-origin-objects-list](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#concept-document-internal-ancestor-origin-objects-list)
> 3. **Legacy** — "has a <dfn>x flag</dfn>, which is initially unset" / "must be initially unset"
>    / "which must initially be" (`DFN-NO-FLAGS`). [source#L86120](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L86120) · [#click-in-progress-flag](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#click-in-progress-flag); [source#L42456](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L42456)

### `STATE-INITIAL-VALUE` — Trailing ", initially VALUE."
The initial value is a trailing clause, never a separate "must" sentence: ", initially false.",
", initially null.", ", initially empty", ", initially « »", `initially "<code data-x="">pending</code>"`
for string enums. "which is initially X" is fine when a relative clause is already open.
**Example:** [source#L8295](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8295) · [#lazy-load-resumption-steps](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#lazy-load-resumption-steps); [source#L1585](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1585) · [#algorithm-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#algorithm-queue); enum: [source#L107391](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L107391)
```html
  <p>Each <span>parallel queue</span> has an <dfn>algorithm queue</dfn> (a <span>queue</span>),
  initially empty.</p>
```

### `STATE-OWNER-PHRASE` — "Each `<code>X</code>` element" / "A `<code>Document</code>`" / "Each <span>concept</span>"
The owner is "Each `<code>input</code>` element" or "Every … element" for elements, "A
`<code>Document</code>`" / "Each `<code>Document</code>`" for interfaces, "Each <span>media
element</span>" for spec concepts, and "Each object implementing the `<code>X</code>` mixin" for
mixins. Do not write "The X has a…" or "X objects have a…".
**Example:** [source#L60719](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L60719); [source#L8307](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8307); [source#L38318](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L38318)

### `STATE-INTERNAL-SLOT` — `[[Name]]` internal slots only on JavaScript-facing objects
`<dfn>[[CrossOriginPropertyDescriptorMap]]</dfn> internal slot` is used only where the object is
manipulated through ECMAScript internal methods (`Window`, `Location`, module records,
`WindowProxy`). Ordinary platform objects use `STATE-DECLARATION` concepts, not slots.
**Example:** [source#L97075](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L97075)

### `STATE-DFN-FOR` — Give state dfns `for=""` and `export` when other specs need them
State owned by an interface is `<dfn export for="Document">…</dfn>`; element-owned state uses
`data-x="concept-…"` or a bare `<dfn>` when the name is unique.
**Example:** [source#L11785](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11785) · [#concept-document-internal-ancestor-origin-objects-list](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#concept-document-internal-ancestor-origin-objects-list)

---

## 13. Invoking algorithms (`CALL`)

### `CALL-CONJUGATED` — "the result of <span data-x="dfn">conjugated verb</span> …"
Algorithm names are verb phrases (`DFN-ALGORITHM-NAMES`); call them by conjugating the verb inside
the link and keying `data-x` to the dfn: "the result of <span data-x="dequeue">dequeuing</span>",
"<span data-x="parse a URL">parsing</span> <var>url</var>".
**Example:** [source#L1609](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1609) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#starting-a-new-parallel-queue); [source#L7779](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7779)
```html
       <li><p>Let <var>steps</var> be the result of <span data-x="dequeue">dequeuing</span> from
       <var>parallelQueue</var>'s <span>algorithm queue</span>.</p></li>
```
> **Branch**
> 1. **Modern** — conjugated link, as above.
> 2. **Accepted** — "the result of running <span>X</span>" when the dfn is a noun phrase or an
>    abstract-op name. [source#L8710](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8710)
> 3. **Accepted** — "the result of invoking" for Web IDL callbacks and JavaScript functions;
>    "Perform ? <span>Op</span>(…)" for ECMAScript abstract operations (`ALG-ES-ABSTRACT-OPS`). [source#L36250](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L36250)
> 4. **Legacy** — "the result of applying the <span>URL parser</span> to", "calling", "performing
>    the <span>X</span> algorithm". [source#L7739](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7739) · [#parse-a-url](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parse-a-url)

### `CALL-GIVEN` — Arguments follow "given"
"run <span>X</span> given <var>a</var> and <var>b</var>", "<span>fetch</span> <var>request</var>
given <var>client</var>". "with <var>x</var> as the argument", "passing <var>x</var>", and "using
<var>x</var>" are not used in new text. Named arguments are "with <var>flag</var> set to true"
only when the callee defines them that way.
**Example:** [source#L1797](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1797) · [#dom-trees](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-trees); callback: [source#L119527](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L119527)
```html
   <li><p>Run <var>onComplete</var> given <var>moduleScript</var>.</p></li>
```

### `CALL-STEPS-AS-VALUES` — "the following steps given <var>x</var>:" for closures
An algorithm passed as an argument is introduced as "Let <var>steps</var> be the following steps
given <var>x</var>:" or inline "…, with <var>processResponse</var> set to the following steps given
<var>response</var>:", and later executed with "run <var>steps</var> given …". Use `<var ignore>`
/ `var-scope` when the closure is declared outside a `<div algorithm>`.
**Example:** [source#L1612](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1612) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#starting-a-new-parallel-queue); [source#L1633](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1633)

### `CALL-RELEVANT-OBJECTS` — "<span>this</span>'s <span>relevant global object</span>"
Obtain the JavaScript context through the possessive: "<span>this</span>'s <span>relevant global
object</span>", "<var>element</var>'s <span>node document</span>'s <span>relevant global
object</span>", "<span>this</span>'s <span data-x="concept-relevant-realm">relevant realm</span>".
"the <span>relevant global object</span> of <var>x</var>" is Legacy; "current realm", "entry
settings object", and "incumbent" are only for the JavaScript-embedding machinery, never for new
APIs.
**Example:** [source#L1645](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1645) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism)
```html
    <li><p>Let <var>global</var> be <span>this</span>'s <span>relevant global
    object</span>.</p></li>
```

### `CALL-IMPERATIVE` — Steps are imperatives; no "the user agent must" inside algorithms
Within `<ol>` steps the subject is implicit ("Fire an event…", "Return <var>p</var>"). "the user
agent must …" is Legacy there; "The user agent should …" survives only for genuine UI latitude.
See `CONF-RFC2119`.
**Example:** [source#L1599](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1599) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#starting-a-new-parallel-queue); Legacy: [source#L12094](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L12094) · [#dom-document-cookie](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-document-cookie); latitude: [source#L7861](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7861)

---

## 14. IDL member prose (`API`)

### `API-STEPS-FORM` — "The <dfn>x</dfn> getter steps are …" / "setter steps are …" / "method steps are …"
Give IDL member behavior as "The `<dfn attribute for=…><code data-x="dom-X-y">y</code></dfn>`
getter steps are to return …" (one-liner) or "The getter steps are:" + `<ol>`; likewise "setter
steps" and "The `<dfn method …>…</dfn>` method steps are:". The `<dfn>` sits inside this sentence
(`DFN-DATA-X-PLACEMENT`) and the receiver is `<span>this</span>` (`XREF-THIS`).
**Example:** [source#L10237](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L10237) · [#dom-domstringlist-item](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-domstringlist-item); multi-step: [source#L8707](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8707); [source#L45783](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L45783) · [#dom-table-deletecaption](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-table-deletecaption)
```html
  <p>The <dfn method for="DOMStringList" data-x="dom-DOMStringList-item"><code>item(<var>index</var>)</code></dfn> method steps are to
  return the <var>index</var>th item in <span>this</span>'s associated list, or null if
```
> **Branch**
> 1. **Modern** — "getter/setter/method steps are".
> 2. **Legacy** — "The `<code>x</code>` attribute must return …", "On getting, …", "On setting,
>    the … IDL attribute must run the following steps:", "The `<code>x()</code>` method must …" /
>    ", when invoked, must …". [source#L9892](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L9892) · [#dom-radionodelist-value](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-radionodelist-value); [source#L12091](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L12091) · [#dom-document-cookie](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-document-cookie); [source#L9643](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L9643)

### `API-CONSTRUCTOR-STEPS` — "The <dfn>new X(args)</dfn> constructor steps are:"
Constructors follow the same pattern with the full signature in the dfn; the IDL block carries
`constructor(...)` (`IDL-CONSTRUCTOR`). "The `<code>X()</code>` constructor, when invoked, must …"
is Legacy.
**Example:** [source#L77037](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L77037) · [#dom-offscreencanvas](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-offscreencanvas); one-liner: [source#L94581](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L94581) · [#dom-origin-constructor](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-origin-constructor)
```html
  <p>The <dfn constructor for="OffscreenCanvas"><code data-x="dom-OffscreenCanvas">new OffscreenCanvas(<var>width</var>,
  <var>height</var>)</code></dfn> constructor steps are:</p>
```

### `API-REFLECT-SENTENCE` — "The `x` IDL attribute must <span>reflect</span> the `x` content attribute"
Reflection is the one place where IDL-attribute prose keeps "must", with the variants "limited to
only known values", "limited to only non-negative numbers", "with a default value of …". Prefer
`IDL-REFLECT-IN-IDL` whenever the extended attributes can express it.
**Example:** [source#L16946](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L16946); [source#L15276](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L15276)

### `API-MEMBER-DFN-ORDER` — IDL block → domintro → normative prose, member by member
Within a section: the `<pre class="idl">` block first, the `<dl class="domintro">` summary
(`ELEM-DOMINTRO`), then one normative paragraph or algorithm per member in IDL order, each
starting with the `API-STEPS-FORM` sentence. Shared helper algorithms follow the members that use
them.
**Example:** [source#L10191](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L10191) · [#the-domstringlist-interface](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-domstringlist-interface)

### `API-ARGUMENTS` — Method arguments are `<var>` names from the IDL signature, read directly
Steps refer to arguments by their IDL names ("If <var>options</var>["<code data-x="…">transfer</code>"] …",
`VAL-DICT-ACCESS`); optional arguments are tested with "If <var>x</var> was not given" / "is not
given" (`ALG-OPTIONAL-ARGS`), never "is undefined" unless the IDL type is `any`.
**Example:** [source#L11597](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11597) · [#dom-structuredclone](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-structuredclone); [source#L63694](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L63694)

---

## 15. Tasks, parallelism, and events (`TASK`, `PAR`, `EVT`)

### `TASK-QUEUE-GLOBAL` — "<span>queue a global task</span> on the <span>X task source</span> given <var>global</var> to …"
Returning from parallel steps to the event loop always names the task source and the global (or
the element: "queue an element task on the <span>networking task source</span> given
<var>el</var> to …").
**Example:** [source#L1653](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1653) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism); element task: [source#L29035](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L29035) · [#queue-an-element-task](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#queue-an-element-task)
```html
       then <span>queue a global task</span> on the <span>DOM manipulation task source</span> given
       <var>global</var> to reject <var>p</var> with a <code>TypeError</code>, and abort these
       steps.</p></li>
```
> **Branch**
> 1. **Modern** — "queue a global task" / "queue an element task", as above.
> 2. **Accepted** — "<span>queue a microtask</span> to …" for same-task continuations. [source#L58808](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L58808)
> 3. **Legacy** — bare "<span>queue a task</span> to …" without source or global, and per-feature
>    wrappers such as "queue a media element task". [source#L91288](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L91288)

### `TASK-SOURCES` — Task sources are `<dfn>…task source</dfn>` noun phrases
Generic sources live in the event loop's `<dl>` ("The <dfn export>DOM manipulation task
source</dfn>"); feature-specific ones are defined inline where first queued ("on the <dfn>embed
task source</dfn>") or per object. Reuse an existing source before minting one.
**Example:** [source#L124195](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L124195) · [#dom-manipulation-task-source](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-manipulation-task-source); [source#L36439](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L36439) · [#embed-task-source](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#embed-task-source)

### `PAR-IN-PARALLEL` — "Run the following steps <span>in parallel</span>:" and the rules inside
Introduce off-main-thread work with a nested block (or inline: "Otherwise, <span>in
parallel</span>, wait for …"). Inside it, touch no JavaScript objects or promises, throw nothing,
and hand results back via `TASK-QUEUE-GLOBAL`.
**Example:** [source#L1602](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1602) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#starting-a-new-parallel-queue); inline: [source#L31825](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L31825) · [#dom-img-decode](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-img-decode)

### `PAR-PARALLEL-QUEUE` — Ordered background work uses a <span>parallel queue</span>
When parallel steps must not interleave, "<span data-x="starting a new parallel queue">start a new
parallel queue</span>" and "<span data-x="enqueue the following steps">enqueue the following
steps</span> to <var>queue</var>:", instead of ad-hoc locks or "in order".
**Example:** [source#L1581](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1581) · [#parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallel-queue); [source#L1588](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1588) · [#enqueue-the-following-steps](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#enqueue-the-following-steps)

### `PAR-EVENT-LOOP-LEGACY` — "spin the event loop", "await a stable state", and "synchronous section" are Legacy
These older primitives (and "⌛" step markers) remain in media and parser text and are not
introduced in new algorithms; use `PAR-IN-PARALLEL` + `TASK-QUEUE-GLOBAL`, "Wait until …" inside
parallel steps (`FLOW-WAIT`), or a promise.
**Example:** [source#L148184](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L148184) · [#spin-the-event-loop](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#spin-the-event-loop); [source#L34275](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L34275) · [#await-a-stable-state](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#await-a-stable-state); [source#L123949](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L123949)

### `EVT-FIRE` — "<span data-x="concept-event-fire">fire an event</span> named <code data-x="event-load">load</code> at <var>target</var>"
Always fire through DOM's "fire an event" with a linked name (`XREF-CODE-EVENT`); "dispatch" is
used only when a pre-built event object is dispatched.
**Example:** [source#L19306](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L19306); from a task: [source#L29036](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L29036)
```html
     <li><p>If <var>success</var> is true, <span data-x="concept-event-fire">fire an event</span>
     named <code data-x="event-load">load</code> at <var>element</var>.</p></li>
```

### `EVT-INIT-ATTRS` — "using `<code>XEvent</code>`, with its … attribute initialized to …"
Event interface and init-dictionary values follow the name: "using `<code>TrackEvent</code>`, with
its `<code data-x="dom-TrackEvent-track">track</code>` attribute initialized to …"; booleans are
"with its `bubbles` attribute initialized to true". Several attributes chain with commas and
"and".
**Example:** [source#L57053](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L57053)
> **Branch**
> 1. **Modern** — "with its … attribute initialized to".
> 2. **Accepted** — "with the … attribute initialized to" (the historical majority). [source#L39611](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L39611) · [#event-media-addtrack](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#event-media-addtrack); [source#L54000](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L54000) · [#event-change](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#event-change)

### `EVT-DFN-EVENT` — Define events in a table with `<dfn event for="…">` and list them in the index
Every event gets a `<dfn event for="Interface"><code data-x="event-…">name</code></dfn>` row in a
table with Interface / Fired when / Preconditions columns, plus a row in the Events index. Handler
IDL attributes go in the `IDL-EVENT-HANDLERS` table.
**Example:** [source#L44148](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L44148) · [#event-media-loadstart](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#event-media-loadstart); index: [source#L161281](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L161281)

---

## 16. Exceptions and promises (`EXC`, `PROM`)

### `EXC-THROW-DOMEXCEPTION` — `throw an <span>"<code>IndexSizeError</code>"</span> <code>DOMException</code>`
DOMException names are quoted, wrapped in a linking `<span>`, and followed by
`<code>DOMException</code>`; the article agrees with the name ("an "IndexSizeError"", "a
"SyntaxError""). JavaScript errors are "throw a `<code>TypeError</code>`".
**Example:** [source#L13221](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L13221) · [#html-element-constructors](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#html-element-constructors); [source#L8936](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8936)
```html
     <span>"<code>IndexSizeError</code>"</span> <code>DOMException</code>.</p></li>
```
> **Branch**
> 1. **Modern** — "then throw a `<code>TypeError</code>`." / "throw a <span>"<code>NotSupportedError</code>"</span> <code>DOMException</code>."
> 2. **Legacy** — "throw a `<code>TypeError</code>` exception", "the user agent must throw a …".
>    [source#L56341](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L56341); [source#L12094](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L12094) · [#dom-document-cookie](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-document-cookie)

### `EXC-RETHROW` — "If this throws an exception, then …" / "catch it, and …" / "rethrow"
Make exception flow explicit: "…, catching any exceptions. If this threw an exception, then set
<var>result</var>'s … to that exception." or "If this throws an exception, then return/abort …".
Propagation is "rethrow that exception" or, for ECMAScript operations, the `?` prefix
(`ALG-ES-ABSTRACT-OPS`). Never leave an exception implicit in a parallel block.
**Example:** [source#L101661](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L101661); [source#L120731](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L120731); [source#L119523](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L119523)
```html
   <li><p>Run <var>onComplete</var> given <var>moduleScript</var>. If this throws an exception,
   catch it, and set <var>moduleScript</var>'s <span>error to rethrow</span> to that exception.</p></li>
```

### `PROM-CREATE` — "Let <var>p</var> be a new promise created in <span>this</span>'s <span>relevant realm</span>."
Create promises naming the realm. Short-circuit returns use Web IDL's linked phrases: "return
<span>a promise rejected with</span> a <span>"<code>NotSupportedError</code>"</span>
<code>DOMException</code>" / "<span>a promise resolved with</span> undefined".
**Example:** [source#L1642](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1642) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism); rejected: [source#L124334](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L124334); resolved: [source#L104059](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L104059)
```html
    <li><p>Let <var>p</var> be a new promise created in <span>this</span>'s <span
    data-x="concept-relevant-realm">relevant realm</span>.</p></li>
```
> **Branch**
> 1. **Modern** — names the realm, as above.
> 2. **Accepted** — "Let <var>promise</var> be a new promise." when the realm is unambiguous. [source#L31789](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L31789) · [#dom-img-decode](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-img-decode)
> 3. **Obsolete** — "a new promise object"; "Let <var>promise</var> be a new <code>Promise</code>".

### `PROM-SETTLE` — "resolve <var>p</var> with undefined" / "reject <var>p</var> with a `<code>TypeError</code>`"
Settle with the bare verbs and "with", always from a queued task when the algorithm is in
parallel, and return the promise as the last step ("Return <var>p</var>."). Spell out the
fulfillment value "undefined"; never "resolve <var>p</var>" alone.
**Example:** [source#L1663](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1663) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism); [source#L1654](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1654); [source#L1667](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1667)

### `PROM-REACT` — "<span>Upon fulfillment</span> of <var>p</var>, run the following steps:" (or "with <var>v</var>")
Reactions use Web IDL's linked "Upon fulfillment"/"Upon rejection" phrases followed by a nested
`<ol>`. Promises awaited in bulk use "<span>wait for all</span>"; rejections that must not be
reported use "<span>mark as handled</span>".
**Example:** [source#L119514](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L119514); [source#L119532](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L119532); imports: [source#L2967](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L2967) · [#dependencies](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dependencies)
```html
    <p><span>Upon fulfillment</span> of <var>loadingPromise</var>, run the following steps:</p>
```

---

## 17. Conformance language (`CONF`)

### `CONF-RFC2119` — Lowercase "must"/"should"/"may"; one requirement per sentence
Requirement keywords are ordinary lowercase words, never capitalized or emphasized, and each
conformance sentence names its conformance class as subject: "User agents must …", "Authors must
not …". Negatives are "must not" / "should not"; "may not" is Legacy because it is ambiguous.
Where there is no normative content, use the plain indicative ("is", "returns"), not "will" or
"shall".
**Example:** UA: [source#L5255](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L5255); authors: [source#L12858](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L12858); [source#L15480](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L15480)
```html
  <p>Authors must not use elements, attributes, or attribute values for purposes other than their
  appropriate intended semantic purpose, as doing so prevents software from correctly processing the
  page.</p>
```

### `CONF-IMPERATIVE-STEPS` — Requirements live in the preamble; steps are imperative
The "must" attaches once, to the algorithm's trigger (or is implied by the caller in the Modern
"To X, given …:" form), and the steps themselves are plain imperatives (`ALG-PREAMBLE`,
`CALL-IMPERATIVE`). The one exception is "should" for UI latitude inside a step.
**Example:** [source#L7730](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7730) · [#parse-a-url](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parse-a-url); Legacy: [source#L33135](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L33135) · [#update-the-image-data](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#update-the-image-data)

### `CONF-NON-NORMATIVE-MARKER` — `<!-- NON-NORMATIVE SECTION -->` right after the heading
Introductory and informative sections carry this comment as the first line after the heading;
Wattsi renders the "This section is non-normative." sentence. Notes and examples are
non-normative by class; do not add "(non-normative)" to prose.
**Example:** [source#L202](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L202) · [#abstract](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#abstract); [source#L214](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L214)
```html
  <h3>Where does this specification fit?</h3>

  <!-- NON-NORMATIVE SECTION -->
```

### `CONF-EXPECTED` — The Rendering section says "is expected to", not "must"
Rendering requirements are "User agents are <span>expected</span> to …", using the `<dfn>expected</dfn>`
term that the section defines as equivalent to "should". Do not use "expected" outside Rendering.
**Example:** [source#L151319](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L151319) · [#expected](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#expected); use: [source#L152457](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L152457)

### `CONF-WILLFUL-VIOLATION` — Deviations from other specs are declared "willful violations"
A requirement that contradicts another standard is followed by a note "This is a <span>willful
violation</span> of <cite>X</cite>, motivated by …". Never hide a known contradiction in a comment.
**Example:** [source#L5351](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L5351) · [#willful-violation](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#willful-violation)

### `CONF-TRACKING-VECTOR` — `<!--INSERT TRACKING-->` on features that enable tracking
Start the paragraph that defines the observable behavior with `<!--INSERT TRACKING-->`; Wattsi
replaces it with the tracking-vector badge. Not in the domintro.
**Example:** [source#L1983](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1983) · [#tracking-vector](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#tracking-vector)

### `CONF-SECURITY-PRIVACY` — Security and privacy text goes in `<p class="warning">` or a dedicated subsection
Normative mitigations stay in the algorithm; advice to authors or implementers is a
`<p class="warning">` (`BLK-WARNING`) or a "Security and privacy considerations" subsection beside
the feature (`HDR-SECTION-NAMES`), never an inline aside in the steps.
**Example:** [source#L44606](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L44606); [source#L131651](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L131651)

---

## 18. Prose mechanics (`PRS`)

### `PRS-QUOTES` — Straight ASCII quotes; double for strings, single only for CSS values
Source uses `"` and `'` exclusively; curly quotes appear only inside author examples. String
literals are `"<code data-x="">…</code>"` with the quotes outside the `<code>`
(`XREF-STRING-LITERAL`); CSS property and keyword names use single quotes inside the link:
`<span>'display'</span>`. Apostrophes are straight: `<var>el</var>'s`.
**Example:** [source#L15778](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L15778) · [#the-dir-attribute](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#the-dir-attribute); stray curly to avoid: [source#L98626](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L98626)

### `PRS-DASH` — `&mdash;` with spaces for asides; hyphens for compounds
Write asides with the `&mdash;` entity and a space on each side. Compound modifiers are hyphenated
with U+002D ("same-origin", "case-insensitive", "non-null", "top-level"); `&ndash;` is only for
numeric ranges.
**Example:** [source#L504](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L504)
> **Branch**
> 1. **Modern** — `&mdash;` entity, spaced.
> 2. **Accepted** — literal "—"; harmless but inconsistent with `SRC-ENTITIES`. [source#L150960](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L150960)
> 3. **Obsolete** — `--` as a dash.

### `PRS-LATIN-ABBREV` — "e.g." and "i.e." are allowed, with or without the comma
Always followed by a lowercase word; never "eg", "ie", or "etc..". Match the paragraph you are
editing.
**Example:** [source#L699](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L699); [source#L924](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L924)
> **Branch**
> 1. **Accepted** — "(e.g., web browsers)". [source#L699](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L699)
> 2. **Accepted** — "(e.g. `<code>img</code>` elements)". [source#L924](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L924)

### `PRS-SERIAL-COMMA` — Oxford comma in lists of three or more
"elements, attributes, or attribute values". Lists inside a step that would need commas inside
items become `FLOW-ANY-ALL` bullet lists.
**Example:** [source#L12858](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L12858)

### `PRS-AMERICAN` — American spelling, except in preserved anchors
"behavior", "color", "canceled", "serialize", "center", "license". British spellings survive only
as hidden anchor aliases (`HDR-EN-GB-ALIAS`) and in quoted external names. "email" not "e-mail";
"website" / "web page", not "webpage".
**Example:** [source#L372](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L372); [source#L27541](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L27541)

### `PRS-CONTRACTIONS` — Contractions and first/second person only in non-normative text
"can't", "doesn't", "we", and "you" occur in notes, examples, and the introduction; normative
sentences and algorithm steps use "cannot", "does not", "is not" and no personal pronouns.
**Example:** note: [source#L150033](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L150033); [source#L17618](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L17618); normative "cannot": [source#L33156](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L33156)

### `PRS-EMPHASIS` — `<em>` for contrastive stress; `<i>` for labels and terms; `<strong>` never in prose
`<em>` marks genuine spoken emphasis ("does <em>not</em>") and is rare in normative steps. `<i>`
is semantic: step labels, state names, terms-as-terms (`XREF-I-STATES`, `VAL-ENUM-STATES`).
`<strong>` appears only in the header boilerplate and inside author examples; use
`<p class="warning">` for weight. Never use all caps, bold, or exclamation marks for requirements.
**Example:** [source#L571](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L571); in a note: [source#L1849](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1849)
```html
   <p class="note">This does <em>not</em> perform the <span>unfocusing steps</span>,
```

### `PRS-PLURALS` — Pluralize outside the code or map the plural with `data-x`
Element and interface names stay singular inside `<code>`: "`<code>img</code>` elements",
"`<code>Document</code>` objects". Concept plurals are linked with the singular key:
`<span data-x="URL">URLs</span>`. Never "`<code>imgs</code>`" or "`<code>Document</code>s`".
**Example:** [source#L12580](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L12580); concept plural: [source#L7730](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7730) · [#parse-a-url](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parse-a-url)

### `PRS-CITE-SPEC` — Name other specs with `<cite>` and a `<ref>`
Write `<cite>Infra</cite>` (title, not acronym) and append `<ref>INFRA</ref>` after the
paragraph's final punctuation (`SRC-REF-PLACEMENT`). Never "[URL]" or raw links.
**Example:** [source#L1523](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1523) · [#dependencies](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dependencies); [source#L2256](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L2256)

### `PRS-PARENTHETICAL` — Parentheses for defaults and asides; no nested parentheses
"(default false)", "(if any)", "(e.g., …)" are fine; multi-sentence asides become a
`<p class="note">`. Do not nest parentheses or put a full sentence in parentheses inside a step.
**Example:** [source#L35740](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L35740); [source#L31547](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L31547)

---

## 19. Vocabulary (`VOC`)

### `VOC-NAVIGABLE` — "navigable" / "traversable", not "browsing context"
New text speaks of `<span>navigable</span>`, `<span>top-level traversable</span>`, and
`<span>child navigable</span>`. "browsing context" is reserved for the remaining
browsing-context concepts (agent clusters, `window.open`'s auxiliary browsing context, browsing
context groups) and historical anchors.
**Example:** [source#L105494](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105494); [source#L29175](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L29175)
> **Branch**
> 1. **Modern** — navigable / traversable.
> 2. **Legacy** — "browsing context" where a navigable is meant; rewrite when touching.

### `VOC-FULLY-ACTIVE` — Check "<span>fully active</span>" before touching a Document
APIs that must not run for bfcached or detached documents begin with "If <span>this</span>'s
<span>relevant global object</span>'s <span>associated <code>Document</code></span> is not
<span>fully active</span>, then …". Use this exact predicate, not "is not active" or "is not
shown".
**Example:** [source#L36152](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L36152); [source#L11801](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11801)

### `VOC-SAME-ORIGIN` — Predicate "is <span>same origin</span> with"; adjective "same-origin"
The relation is a linked predicate without hyphen: "<var>a</var> is <span>same origin</span> with
<var>b</var>", "same origin-domain". The hyphenated form is an adjective only ("same-origin
navigation", "cross-origin isolated").
**Example:** [source#L11841](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11841); adjective: [source#L117794](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L117794)

### `VOC-AUTHORS-DEVELOPERS` — "authors" in conformance text; "web developers" in notes and domintro
"Authors must not …" is the conformance class for documents; "web developers" (lowercase) is the
audience of notes, domintro, and the Developer's Edition.
**Example:** [source#L89699](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L89699); [source#L18361](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L18361); normative: [source#L12858](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L12858)
> **Branch**
> 1. **Modern** (informative voice) — "web developers".
> 2. **Accepted** (normative voice) — "authors".
> 3. **Obsolete** — "web authors", "page authors", "content authors".

### `VOC-USER-AGENT` — "user agent" spelled out; "UA" only in comments and CSS
"user agent" is the implementation conformance class; "UA" occurs only in source comments and the
rendering section's "UA style sheet" context. "browser" only in non-normative prose when the point
is specifically about browsers; "implementers" (never "implementors") for people.
**Example:** [source#L5255](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L5255); implementers: [source#L27717](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L27717)

### `VOC-JAVASCRIPT` — "JavaScript", not "ECMAScript", except when naming the spec or its terms
Use "JavaScript" for the language and `JAVASCRIPT` as the reference key; "ECMAScript" only in
"the ECMAScript specification" / "ECMAScript module" where that is the defined term.
Abstract-operation names and `[[InternalSlots]]` are spelled exactly as in ECMA-262.
**Example:** [source#L132302](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L132302); [source#L2256](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L2256) · [#dependencies](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dependencies)

### `VOC-WEB-CASING` — "the web", "web page", "web platform" lowercase; "Web IDL" as a proper name
Common nouns are lowercase; proper names keep their casing: "Web IDL" (never "WebIDL"), "World
Wide Web", "HTML Standard", "Fetch".
**Example:** [source#L18361](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L18361)

### `VOC-IS-SAID-TO` — "is said to be <i>x</i>" / "is said to <dfn>verb</dfn>" for defining predicates
A predicate or adjective is introduced with "is said to", the term in `<i>` when it is not
linkable or `<dfn>` when it is. New text prefers a direct dfn sentence ("An element is <dfn>being
rendered</dfn> if …"); "is said to" remains Accepted.
**Example:** [source#L1775](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1775); [source#L1719](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1719)

### `VOC-INFRA-TERMS` — Use Infra's names for data types and operations
Lists ("list", "append", "remove", "contains", "size", "is empty"), ordered sets, maps ("map",
"exists", "set the value", "keys"), strings ("code point", "ASCII lowercase", "strip leading and
trailing ASCII whitespace"), booleans and null, structs/tuples, and "implementation-defined" are
linked to Infra (§11). Do not invent synonyms ("array", "dictionary" for maps, "add" for append,
"check whether").
**Example:** [source#L2256](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L2256) · [#dependencies](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dependencies); use: [source#L124882](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L124882)

---

## About this guide

Rules were derived from the full `source` text, weighted toward the forms that dominate text
added or edited in the last two years and that editors ask for in review; branch ordering follows
that weighting. Links are pinned to commit `877d6146487f15b15bc8dd0e3c625063a37b456a`; to
refresh them, re-derive the line numbers against a newer commit and swap the SHA in the
`github.com/whatwg/html/blob/…` and `commit-snapshots/…` URLs.

