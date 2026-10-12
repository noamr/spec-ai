# HTML Standard style guide — formatting and Wattsi markup

How `source` is laid out and marked up for Wattsi: wrapping and indentation, ids and
cross-reference markup, `<dfn>` attributes, note/example/warning blocks, IDL and code blocks,
element definitions, and Developer's Edition annotations.

Part of the HTML house style guide. See [html-style-guide.md](html-style-guide.md) for the
Modern / Accepted / Legacy / Obsolete **Branch** tiers and an index of every rule ID across
files. Examples are pinned to whatwg/html commit [`877d614`](https://github.com/whatwg/html/commit/877d6146487f15b15bc8dd0e3c625063a37b456a).

| § | Section | Prefixes |
|---|---|---|
| 1 | Source layout and markup | `SRC` |
| 2 | Headings, ids, cross-references | `HDR`, `XREF` |
| 3 | Definition markup | `DFN`, `EVT` |
| 4 | Blocks: notes, examples, warnings, issues | `BLK` |
| 5 | Code and IDL blocks | `CODE`, `IDL` |
| 6 | Element definitions | `ELEM` |
| 7 | Developer's Edition annotations | `DEV` |

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
| `algorithm`, `var-scope`, `ignore` | algorithm and variable scoping (`ALG-*` in [html-style-authoring.md](html-style-authoring.md)) | [source#L618](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L618) |
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

## 2. Headings, ids, cross-references (`HDR`, `XREF`)

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

## 3. Definition markup (`DFN`, `EVT`)

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

### `DFN-EXPLICIT-ID` — `id=""` on a dfn only for anchor stability
Let Wattsi derive dfn ids; add `id` only when renaming a term whose old anchor is referenced.
**Example:** [source#L8951](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8951) · [#limited-to-only-non-negative-numbers-greater-than-zero-with-fallback](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#limited-to-only-non-negative-numbers-greater-than-zero-with-fallback)

### `EVT-DFN-EVENT` — Define events in a table with `<dfn event for="…">` and list them in the index
Every event gets a `<dfn event for="Interface"><code data-x="event-…">name</code></dfn>` row in a
table with Interface / Fired when / Preconditions columns, plus a row in the Events index. Handler
IDL attributes go in the `IDL-EVENT-HANDLERS` table.
**Example:** [source#L44148](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L44148) · [#event-media-loadstart](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#event-media-loadstart); index: [source#L161281](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L161281)

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
