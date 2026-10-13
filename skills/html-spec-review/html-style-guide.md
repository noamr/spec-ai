# HTML Standard — de-facto style guide

How the HTML Standard's `source` is actually written, distilled from the text itself, its recent
history, and recent review practice. Focused on common authoring and review patterns that are not
already enforced by Wattsi or automated lints.

Each rule has a short name (`PREFIX-NAME`), a title, a description, and a link or snippet from the
live specification (`https://html.spec.whatwg.org/`). Where the spec uses more than one style for
the same thing, a **Branch** side note lists the options in order of preference:

- **Modern** — use in new text.
- **Accepted** — fine to use; match the surrounding text.
- **Legacy** — do not introduce; rewriting is optional.
- **Obsolete** — fix when touching.

Rules that restate a convention of the [Infra Standard](https://infra.spec.whatwg.org/) — which
applies to every WHATWG specification, not just HTML — carry an **Infra:** line linking to the
relevant Infra section. For those rules, Infra is the normative source and this document only adds
HTML's preferred phrasing, markup, and known deviations; cite Infra when reviewing other specs.
Rules without an **Infra:** line are HTML house style.

**Scope.** Unless a rule says otherwise, it applies to *new or rewritten normative text*: algorithm
steps, state declarations, IDL member prose. It does not apply to notes, examples, `dl.domintro`, or
author-facing prose, and it does not turn carried-over text into a finding: a step that was merely
re-wrapped, text restored by a revert, or a single new step added inside an algorithm written in a
Legacy style all follow the surrounding style. Flag a Legacy form only when a PR introduces a new
algorithm, section, or several new steps in it. (Calibrated against merged PRs: nearly every rule hit
on a small merged fix was one of these cases, and no editor raised it.)

Companion documents:
[CONTRIBUTING.md](https://github.com/whatwg/html/blob/main/.github/CONTRIBUTING.md),
the [WHATWG style guide](https://whatwg.org/style-guide), and the spec's own guidance on
[realms, settings objects, and global objects](https://html.spec.whatwg.org/#realms-settings-objects-global-objects),
[parallelism](https://html.spec.whatwg.org/#parallelism),
and [the event loop](https://html.spec.whatwg.org/#event-loop-for-spec-authors).

| § | Section | Prefixes |
|---|---|---|
| 1 | Source layout and blocks | `SRC`, `BLK`, `DEV` |
| 2 | Headings, ids, and cross-references | `HDR`, `XREF` |
| 3 | Definitions (`<dfn>`) | `DFN`, `EVT` |
| 4 | Web IDL and element definitions | `IDL`, `ELEM` |
| 5 | Algorithm structure and control flow | `ALG`, `FLOW` |
| 6 | Variables, values, and state | `VAR`, `VAL`, `STATE` |
| 7 | Invoking algorithms and IDL member prose | `CALL`, `API` |
| 8 | Tasks, parallelism, and events | `TASK`, `PAR`, `EVT` |
| 9 | Exceptions and promises | `EXC`, `PROM` |
| 10 | Conformance, prose, and vocabulary | `CONF`, `PRS`, `VOC` |

---

## 1. Source layout and blocks (`SRC`, `BLK`, `DEV`)

### `SRC-WRAP-100` — Wrap at 100 columns
Wrap prose at 100 characters, breaking only at whitespace and filling each line before wrapping.
Do not rewrap `<pre>`, `<table>`, `<svg>`, `<script>`, `<style>`, comments, `<dt>`,
`<img>`/`<iframe>` tags, `ul.domTree`, Dependencies `<dfn>`s, or References `<dd>`s. Newlines
inside start tags and attribute values are fine. Only new or changed paragraphs need to comply.
In review, flag only prose that is clearly unwrapped (a line well over 100, or a whole paragraph on
one line); a 1–2 character overrun (≈900 such lines exist) or an under-filled line is not a review
comment — leave that to the author's editor. For `<dt>`s, match the sibling `<dt>`s in the same
`<dl>` (some wrap inside a long `for=""` value).
**Example:** [#parallelism](https://html.spec.whatwg.org/#parallelism)

### `SRC-INDENT-BLOCK` — One space of indentation per block; transparent wrappers do not indent
Indent one space for each block-level ancestor (`<ol>`, multi-line `<li>`, `<dl>`, `<dd>`,
`<div class="example">`, `<div class="note">`, `<div class="warning">`, `<div class="XXX">`, table
rows). A `<p>` inside a one-line `<li>` is not indented further. `<div algorithm>`, `<div w-nodev>`,
and `<div var-scope>` are transparent wrappers: their children stay at the surrounding indentation
level. The common slip is a multi-line `<li>` whose child `<p>`s sit at the same column as the
`<li>` (only 2 of ~1900 multi-line `<li>`s do this, so it is worth a comment).
**Example:** [#dom-track-track](https://html.spec.whatwg.org/#dom-track-track)
```html
  <div algorithm>
  <p>The <dfn attribute for="HTMLTrackElement"><code data-x="dom-track-track">track</code></dfn>
  getter steps are to return <span>this</span>'s <span>text track</span>.</p>
  </div>
```

### `SRC-LI-P` — Every `<li>` wraps its text in `<p>`, except in `ul.brief`
Write `<li><p>…</p></li>` even for one-liners. Items with several blocks put `<li>` on its own line
and indent the children. Separate sibling `<li>`s with a blank line. `<ul class="brief">` items are
bare. `<dd>` wraps prose sentences in `<p>`, while short phrases (`dl.element`, `dl.switch`) are bare.
**Example:** [#parallelism](https://html.spec.whatwg.org/#parallelism) · [#global-attributes](https://html.spec.whatwg.org/#global-attributes)

### `SRC-END-TAGS` — Close every `</p>`, `</li>`, `</dt>`, `</dd>`; double-quote attributes
Never rely on implied end tags: every `<p>`, `<li>`, `<dt>`, and `<dd>` is closed explicitly, and
a `<p>` is closed before a nested `<ol>`/`<ul>` starts (a stray `<p>` there breaks the build).
Attribute values are double-quoted. A missing end tag in a line the PR touches is fixed when
touching; the ≈550 unclosed `<dt>`s in older `dl.element`/struct blocks are Legacy and are not
cleaned up in passing.
**Example:** [#parallelism](https://html.spec.whatwg.org/#parallelism)
> **Branch**
> 1. **Modern** — all end tags present.
> 2. **Legacy** — `<dt>`/`<dd>` without end tags in old definition lists ([#the-html-element](https://html.spec.whatwg.org/#the-html-element)).

### `SRC-NO-EDGE-BLANK` — No blank line just inside a block's opening or closing tag
A `<div class="note">`, `<div class="example">`, `<li>`, `<ol>`, or `<dd>` starts its content on
the next line with no blank line after the opening tag and none before the closing tag. Blank lines
separate sibling blocks only. (Editors do ask for this: 53 of 61 `<div class="note">`s comply, and
the remainder are routinely pointed out in review.)
**Example:** [#ports-and-garbage-collection](https://html.spec.whatwg.org/#ports-and-garbage-collection)
```html
  <div class="note">
   <p>First paragraph.</p>

   <p>Second paragraph.</p>
  </div>
```

### `BLK-NOTE` — `<p class="note">` for one paragraph, `<div class="note">` for more
Notes are non-normative asides. They start with a capital letter and never with "Note:". Inside
algorithms, put the note in the `<li>` after the step's `<p>` (`ALG-NON-NORMATIVE-NOTES`); never
inside one condition bullet of an "any/all of the following" list — put it after the "then …"
paragraph. Contractions and "for example" asides are fine in notes.
**Example:** [#event-loop-for-spec-authors](https://html.spec.whatwg.org/#event-loop-for-spec-authors)

### `BLK-NOTE-STALE` — Re-read the notes next to a step you change
A note that explains *why* a step exists goes stale when the step's condition or effect changes.
When a PR edits a step, the adjacent notes, domintro text, and any "this is called again because…"
rationale must still be true for the new text; update or delete them in the same PR.
**Example:** [#check-popover-validity](https://html.spec.whatwg.org/#check-popover-validity)

### `BLK-EXAMPLE` — `<div class="example">` with an intro sentence and `<pre><code class="LANG">`
Examples are `<div class="example">` with an introductory `<p>` and `<pre><code class="html">`
(`js`, `css`), or `<p class="example">` for prose-only examples. Give an `id="example-…"` when
linked. Show discouraged code with `<pre class="bad"><code class="html">`, followed by the fix.
**Example:** [#example-cite-usage-correct-vs-incorrect](https://html.spec.whatwg.org/#example-cite-usage-correct-vs-incorrect)

### `DEV-W-NODEV` — Wrap implementer-only text in `w-nodev`; use `w-dev` for developer-only substitutes
Processing models, algorithms, IDL prose, and implementer notes go inside `<div w-nodev>`
(`<p w-nodev>`, `<span w-nodev>` for smaller units). `dl.domintro`, `dl.element`, examples, and
author conformance text stay visible. `<pre class="idl">` is omitted automatically; when the
Developer's Edition needs a replacement sentence (e.g. `<dd w-dev>Uses <code>HTMLHtmlElement</code>.</dd>`),
mark it `w-dev`.
**Example:** [#introduction](https://html.spec.whatwg.org/#introduction) · [#the-html-element](https://html.spec.whatwg.org/#the-html-element)

---

## 2. Headings, ids, and cross-references (`HDR`, `XREF`)

### `HDR-SENTENCE-CASE` — Headings are sentence case
Capitalize only the first word and proper nouns or IDL names.
**Example:** [#how-to-catch-mistakes-when-writing-html:-validators-and-conformance-checkers](https://html.spec.whatwg.org/#how-to-catch-mistakes-when-writing-html:-validators-and-conformance-checkers)
```html
  <h4>How to catch mistakes when writing HTML: validators and conformance checkers</h4>
```

### `HDR-EXPLICIT-ID` — Explicit lowercase-hyphen `id` when the derived one is fragile
Wattsi derives heading ids from the text, so headings containing code, punctuation, repeated titles
("Processing model"), or wording likely to change get a short explicit id (`<h4 id="mq">`,
`<h5 id="navigation-api-intro">`). Never introduce camelCase, dots, or underscores in ids.
**Example:** [#mq](https://html.spec.whatwg.org/#mq) · [#images-processing-model](https://html.spec.whatwg.org/#images-processing-model)

### `HDR-ALIAS-ANCHOR` — Preserve old anchors with `<span id="old-id">` or `<dfn id="old-id">`
When renaming or moving a heading or dfn, keep the old fragment working with `<span id="old-id"></span>`
as the first child of the heading or paragraph, or `<dfn id="old-id">` for dfns. This covers
headings, `export`ed dfns, and ids that other specs or MDN link to. Deleting a non-exported
internal algorithm dfn when its steps are inlined, or removing the ids of an unshipped feature, does
not need an alias.
**Example:** [#rel-alternate](https://html.spec.whatwg.org/#rel-alternate) · [#navigator.online](https://html.spec.whatwg.org/#navigator.online)
```html
  <h5 id="rel-alternate"><span id="link-type-alternate"></span>Link type "<code data-x="rel-alternate">alternate</code>"</h5>
```

### `XREF-SPAN-AUTOLINK` — `<span>` autolinks terms; add `data-x` only when the text differs
A bare `<span>term</span>` links to the `<dfn>` with the same text. Use
`<span data-x="dfn-key">visible text</span>` for conjugated or plural forms and `concept-*` keys.
Link a term on its first use in a paragraph; later uses in the same paragraph may be unlinked, and
re-linking them is not a finding. A redundant `data-x` equal to the text is harmless noise — mention
it only if the PR adds several. Link text should be the dfn's words (conjugated), not an invented
noun phrase for an algorithm; when an algorithm is a sentence subject, write "the
`<span>X</span>` algorithm".
**Example:** [#a-quick-introduction-to-html](https://html.spec.whatwg.org/#a-quick-introduction-to-html)

### `XREF-TEXT-MATCHES-TARGET` — Link text must name the dfn it links to
Flag `<span data-x="X">text</span>` whose visible text is the dfn text of a *different* dfn (e.g.
"queue a violation report for access to another window" keyed to the `…-to-opened` variant), and
`<span>X</span>` where `X` is not a dfn. Wattsi catches missing targets, not wrong ones.
**Example:** [#coop-violation-access-to-other](https://html.spec.whatwg.org/#coop-violation-access-to-other)

### `XREF-CODE-ELEMENT` — Element names are bare `<code>`
Element names autolink as `<code>a</code>`, `<code>div</code>`; never add `data-x` to an element
name. Pluralize outside the code: "`<code>div</code>` elements" (`PRS-MECHANICS`).
**Example:** [#the-a-element](https://html.spec.whatwg.org/#the-a-element)

### `XREF-CODE-ATTR` — Content attributes: `<code data-x="attr-ELEMENT-NAME">name</code>`
Keys are `attr-<element>-<name>` (`attr-img-src`), `attr-<name>` for global attributes
(`attr-translate`), `attr-<group>-<name>` for shared ones (`attr-hyperlink-href`, `attr-fe-name`,
`attr-dim-width`), `attr-…-<keyword>` for keyword values, and `attr-…-<keyword>-state` for states.
**Example:** [#document-base-url](https://html.spec.whatwg.org/#document-base-url)

### `XREF-CODE-DOM` — IDL members: `<code data-x="dom-INTERFACE-name">name()</code>`
Keys are `dom-<Interface>-<member>` (`dom-DOMStringList-item`), `dom-<element>-<member>` for
element interfaces (`dom-img-decode`), `dom-<name>` for Window/global members
(`dom-structuredClone`). Methods are written with empty parentheses, attributes without;
constructors are `dom-<Interface>` or `dom-<Interface>-constructor`.
**Example:** [#dom-structuredclone](https://html.spec.whatwg.org/#dom-structuredclone)

### `XREF-CODE-EVENT` — Events and handlers
Event names are `<code data-x="event-NAME">name</code>` (grouped keys like
`event-media-loadstart`); handler attributes are `<code data-x="handler-onNAME">onname</code>`
(`handler-window-onafterprint` for Window-only ones).
**Example:** [#the-body-element](https://html.spec.whatwg.org/#the-body-element)

### `XREF-CODE-HTTP` — HTTP headers and values in backticks
Header names are `` `<code data-x="http-NAME">Name</code>` `` wrapped in literal backticks; header
values and parameter names likewise `` `<code data-x="">require-corp</code>` ``.
**Example:** [#dom-document-lastmodified](https://html.spec.whatwg.org/#dom-document-lastmodified)
```html
  … from the `<code data-x="http-last-modified">Last-Modified</code>` header of the document …
```

### `XREF-STRING-LITERAL` — String literals: `"<code data-x="">text</code>"`
Literal strings are `<code data-x="">` with the quotation marks outside the code element. Compare
with "is" directly: `If <var>type</var> is "<code data-x="">module</code>"`, not "is the string …".
This is for Infra/IDL string values. Named parser states and token descriptions (`"ok"`/`"not ok"`,
`a "body" start tag token`) and other spec-internal enumerations stay as bare quoted words; sentinel
values returned by other specs (e.g. SRI's `no metadata`) follow that spec's markup.
**Example:** [#create-a-potential-cors-request](https://html.spec.whatwg.org/#create-a-potential-cors-request)
```html
   <li><p>Let <var>mode</var> be "<code data-x="">no-cors</code>" if <var>corsAttributeState</var> is
   <span data-x="attr-crossorigin-none">No CORS</span>, and "<code data-x="">cors</code>" otherwise.</p></li>
```

---

## 3. Definitions (`DFN`, `EVT`)

### `DFN-TYPED` — Use Wattsi's typed `<dfn>` attributes
Mark what is being defined so cross-spec linking works: `<dfn element>`, `<dfn interface>`,
`<dfn dictionary>`, `<dfn enum>`, `<dfn typedef>`, `<dfn callback>`, `<dfn attribute for="I">`,
`<dfn method for="I">`, `<dfn constructor for="I">`, `<dfn dict-member for="D">`,
`<dfn enum-value for="E">`, `<dfn element-attr for="el">`, `<dfn attr-value for="el/attr">`,
`<dfn element-state for="el/attr">`, `<dfn event for="I">`, `<dfn extended-attribute>`. Plain
`<dfn>` is for concepts and algorithms.
**Example:** [#the-track-element](https://html.spec.whatwg.org/#the-track-element) · [#event-media-loadstart](https://html.spec.whatwg.org/#event-media-loadstart)
```html
  <dfn event for="HTMLMediaElement"><code data-x="event-media-loadstart">loadstart</code></dfn>
```

### `DFN-DATA-X-PLACEMENT` — Where the `data-x` key goes on API and attribute dfns
In prose, put the key on the inner `<code>`:
`<dfn attribute for="HTMLImageElement"><code data-x="dom-img-decoding">decoding</code></dfn>`.
Inside IDL blocks, put it on the `<dfn>` itself with no `<code>`:
`<dfn attribute for="HTMLElement" data-x="dom-lang">lang</dfn>`.
**Example:** [#dom-img-decoding](https://html.spec.whatwg.org/#dom-img-decoding) · [#dom-lang](https://html.spec.whatwg.org/#dom-lang)
> **Branch**
> 1. **Modern** — key on the inner `<code>` (prose) or on the `<dfn>` (IDL), as above.
> 2. **Accepted** — key on the `<dfn>` with a bare `<code>` child in prose:
>    `<dfn attribute for="DOMStringList" data-x="dom-DOMStringList-length"><code>length</code></dfn>` ([#dom-domstringlist-length](https://html.spec.whatwg.org/#dom-domstringlist-length)).
> 3. **Obsolete** — untyped `<dfn><code data-x="…">…</code></dfn>` without `for`; add the type and
>    `for` when touching.

### `DFN-FOR-VALUES` — `for=""` syntax
`for` takes the interface or element name; several targets are comma-separated without spaces
(`for="a,area"`); attribute values use `element/attribute` pairs
(`for="img/loading,audio/loading,video/loading,iframe/loading"`); global attributes use
`html-global/translate`.
**Example:** [#attr-hyperlink-href](https://html.spec.whatwg.org/#attr-hyperlink-href) · [#attr-loading-lazy](https://html.spec.whatwg.org/#attr-loading-lazy)

### `DFN-EXPORT` — Export what other specs need
Add `export` to dfns consumed by other standards; `data-noexport=""` is the default and is written
only for emphasis. Use `data-lt="alt|alt2"` for alternative link texts instead of duplicate dfns.
**Example:** [#obtain-a-site](https://html.spec.whatwg.org/#obtain-a-site)

### `DFN-ALGORITHM-NAMES` — Algorithm names are lowercase imperative verb phrases
Name algorithms as what they do ("parse a URL", "obtain a site", "set the frozen base URL"). Hooks
defined for other specs end in "steps" ("get the text steps", "removing steps"); boolean predicates
are phrases used after a subject ("<var>element</var> <dfn>cannot navigate</dfn> if …"). No leading
article and no "algorithm" suffix in the dfn text. This governs the `<dfn>` text only; `data-x`
aliases and link text such as `<span>hide popover algorithm</span>` are out of scope.
**Example:** [#parse-a-url](https://html.spec.whatwg.org/#parse-a-url) · [#cannot-navigate](https://html.spec.whatwg.org/#cannot-navigate)

### `DFN-CONCEPT-NAMES` — Concept names are lowercase noun phrases; disambiguate with `data-x="concept-…"`
Define concepts in lowercase ("node document", "close watcher manager"). When the visible text
collides with another dfn ("origin", "URL", "document"), key the dfn
`data-x="concept-<owner>-<name>"` and link with the key. Capitalized dfn text is reserved for
IDL/ES names and struct items displayed in lists.
**Example:** [#concept-document-navigation-id](https://html.spec.whatwg.org/#concept-document-navigation-id) · [#close-watcher-manager](https://html.spec.whatwg.org/#close-watcher-manager)

### `DFN-NO-FLAGS` — Define booleans, not "flags"
New state is "a boolean, initially false", tested with "is true"/"is false" and mutated with "set …
to true/false" — never "a <dfn>… flag</dfn>, which is initially unset" or "set/unset the flag".
This applies to *new* `<dfn>`s. Using an existing flag (HTML has ~44 `… flag</dfn>`s, e.g. the
parser's `frameset-ok flag` with its "ok"/"not ok" states) or another spec's flag (Fetch's
`use-URL-credentials flag`) in new steps is fine; write "set the X flag to true" rather than "set
the flag", and do not ask for the flag to be renamed in a small edit.
**Example:** [#was-created-via-cross-origin-redirects](https://html.spec.whatwg.org/#was-created-via-cross-origin-redirects)
```html
  <p>A <code>Document</code> has a boolean <dfn export>was created via cross-origin redirects</dfn>,
  initially false.</p>
```
> **Branch**
> 1. **Modern** — boolean ("is true"/"is false", "set … to true"), as above.
> 2. **Legacy** — flag that is set/unset ([#click-in-progress-flag](https://html.spec.whatwg.org/#click-in-progress-flag)).

### `DFN-STRUCT` — "is a struct with the following items:" + `<ul>` of dfn items; tuples for small fixed-shape values
Define compound state as an Infra struct whose items are a `<ul>` of
`<li><p><dfn>Name</dfn>, a TYPE, initially VALUE.</p></li>`, accessed with the possessive
(`<var>manager</var>'s <span>groups</span>`). A tuple ("is a `<span>tuple</span>` consisting of a
`<dfn>`… and a `<dfn>`…") is equally fine for a small value of fixed shape, whatever its arity —
HTML has 2-tuples (insertion location), 3-tuples (sourced names), and 4-tuples (tuple origin). Prefer
a struct when items are mutable, optional, or likely to grow; do not ask for a struct just because a
tuple has more than two items.
**Infra:** [§structs](https://infra.spec.whatwg.org/#structs) · [§tuples](https://infra.spec.whatwg.org/#tuples)
**Example:** [#close-watcher-manager](https://html.spec.whatwg.org/#close-watcher-manager)
```html
  <p>Each <code>Window</code> has a <dfn>close watcher manager</dfn>, which is a <span>struct</span>
  with the following <span data-x="struct item">items</span>:</p>

  <ul>
   <li><p><dfn data-x="close watcher manager groups">Groups</dfn>, a <span>list</span> of
```
> **Branch**
> 1. **Modern** — "…, which is a `<span>struct</span>` with the following items:" + `<ul>` of
>    "Name, a TYPE, initially VALUE." (17 structs).
> 2. **Accepted** — "…is a `<span>struct</span>`. It has the following items:" + `<dl>` of
>    `<dt><dfn>name</dfn>` / `<dd>A TYPE` (4 structs, e.g. [#preload-entry](https://html.spec.whatwg.org/#preload-entry)),
>    and structs that are only ever built with explicit values via `<dl class="props">` and so carry
>    no "initially". Adding an item to such a struct follows its existing form.

### `EVT-DFN-EVENT` — Define events with `<dfn event for="…">` in `#events-2` (or a feature table), never duplicating external event dfns
Events fired by HTML are defined with `<dfn event for="Interface"><code data-x="event-…">name</code></dfn>`
directly in the `#events-2` Events index table (or in the dedicated media / drag-and-drop event tables).
Events defined and fired by another specification (e.g. `slotchange` in DOM) are imported in
`#dependencies` via `<dfn data-x="event-…" data-x-href="…"><code>…</code></dfn>` and must not be
redefined with `<dfn event>` in `#events-2`.
**Example:** [#event-media-loadstart](https://html.spec.whatwg.org/#event-media-loadstart) · [#events-2](https://html.spec.whatwg.org/#events-2) · [#dependencies](https://html.spec.whatwg.org/#dependencies)

---

## 4. Web IDL and element definitions (`IDL`, `ELEM`)

### `IDL-BLOCK` — IDL goes in `<pre><code class="idl">` right after the heading
Interface definitions follow the section heading (or `dl.element`'s "DOM interface" `<dd w-nodev>`)
as `<pre><code class="idl">`: extended attributes first (`[Exposed=Window]` on its own line), then
`interface <dfn interface>Name</dfn> : <span>Parent</span> {`.
**Example:** [#the-toggleevent-interface](https://html.spec.whatwg.org/#the-toggleevent-interface) · [#the-head-element](https://html.spec.whatwg.org/#the-head-element)
```html
  <pre><code class="idl">[Exposed=Window]
interface <dfn interface>HTMLHtmlElement</dfn> : <span>HTMLElement</span> {
  [<span>HTMLConstructor</span>] constructor();
```

### `IDL-XREF-SPAN` — Cross-references inside IDL use `<span>`, never `<code>`
Types, members, and extended attributes inside `<pre class="idl">` link via `<span>` or
`<span data-x>`; members defined in prose are `<span data-x="dom-document-hidden">hidden</span>`.
Escape `<` in generics (`<span data-x="idl-Promise">Promise</span>&lt;undefined>`).
**Example:** [#dom-document-hidden](https://html.spec.whatwg.org/#dom-document-hidden)

### `IDL-EXTENDED-ATTRS` — Link extended attributes that HTML defines; leave Web IDL's bare
`[<span>CEReactions</span>]`, `[<span>HTMLConstructor</span>]`,
`[<span data-x="xattr-Reflect">Reflect</span>]`, `<span>LegacyUnforgeable</span>`, and
`<span>LegacyUnenumerableNamedProperties</span>` are linked; `[Exposed=…]`, `[SameObject]`,
`[NewObject]`, `[EnforceRange]`, `[PutForwards=…]`, `[Replaceable]`, `[SecureContext]` are bare.
**Example:** [#htmlallcollection](https://html.spec.whatwg.org/#htmlallcollection) · [#dom-context-2d-gettransform](https://html.spec.whatwg.org/#dom-context-2d-gettransform)

### `IDL-REFLECT-IN-IDL` — Reflected attributes are declared with `[Reflect]` in the IDL
Attributes that reflect a content attribute carry their dfn in the IDL together with the
`Reflect*` extended attributes (`ReflectSetter`, `ReflectURL`, `ReflectDefault`, `ReflectRange`,
…), replacing the prose sentence.
**Example:** [#dom-lang](https://html.spec.whatwg.org/#dom-lang) · [#using-reflect-via-idl-extended-attributes](https://html.spec.whatwg.org/#using-reflect-via-idl-extended-attributes)
```html
  [<span>CEReactions</span>, <span data-x="xattr-Reflect">Reflect</span>] attribute DOMString <dfn attribute for="HTMLElement" data-x="dom-lang">lang</dfn>;
```
> **Branch**
> 1. **Modern** — `[Reflect]` plus dfn in the IDL, as above.
> 2. **Accepted** (when the extended attributes cannot express it, e.g. enumerated attributes) —
>    prose: "The `<dfn attribute for="HTMLImageElement"><code data-x="dom-img-decoding">decoding</code></dfn>`
>    IDL attribute must <span>reflect</span> the … content attribute, <span>limited to only known
>    values</span>." (Reflection is the one place where IDL-attribute prose keeps "must"; see
>    [#dom-img-decoding](https://html.spec.whatwg.org/#dom-img-decoding).)

### `IDL-DICTIONARY` — Members are defined inline; optional dictionary arguments default to `{}`
`dictionary <dfn dictionary>X</dfn> { boolean <dfn dict-member for="X" data-x="dom-X-y">y</dfn> = false; }`.
Boolean members get an explicit default unless absence is meaningful. Optional dictionary arguments
with no required members are `optional <span>X</span> options = {}`. Read members with `VAL-MAP-OPS`.
**Example:** [#dom-navigateeventinit-canintercept](https://html.spec.whatwg.org/#dom-navigateeventinit-canintercept)

### `IDL-ENUM-VALUES` — Where enum values are defined
Either keep plain strings in the IDL and define each value in a prose `<dl>` whose `<dt>` is
`"<dfn enum-value for="E"><code data-x="dom-E-value">value</code></dfn>"` (when values need
explanation), or put the `<dfn enum-value>` directly inside the IDL (when they are
self-explanatory).
**Example:** [#dom-navigationtype-push](https://html.spec.whatwg.org/#dom-navigationtype-push) · [#dom-navigationfocusreset-after-transition](https://html.spec.whatwg.org/#dom-navigationfocusreset-after-transition)
> **Branch**
> 1. **Accepted** — strings in IDL + prose `<dl>` of `enum-value` dfns.
> 2. **Accepted** — `<dfn enum-value>` inside the IDL.
> 3. **Legacy** — `<span data-x="dom-CanPlayTypeResult-maybe">maybe</span>` in the IDL plus an
>    untyped dfn ([#canplaytyperesult](https://html.spec.whatwg.org/#canplaytyperesult)).

### `ELEM-DL-ELEMENT` — The `dl.element` box
Every element section starts with `<dl class="element">` whose `<dt>`s are, in order: Categories ·
Contexts in which this element can be used · Content model · Tag omission in text/html · Content
attributes · Accessibility considerations · DOM interface. `<dt>` text is a
`<span data-x="concept-element-…">` link ending in a colon; `<dd>`s are bare phrases ending in a
period. Content attributes list `<dd><span>Global attributes</span></dd>` first, then one
`<dd><code data-x="attr-…">name</code></dd>` per attribute. "DOM interface" is `<dd w-nodev>` +
IDL followed by `<dd w-dev>Uses <code>HTMLHtmlElement</code>.</dd>`, or
`<dd>Uses <code>HTMLElement</code>.</dd>` when there is no dedicated interface.
**Example:** [#the-head-element](https://html.spec.whatwg.org/#the-head-element) · [#the-a-element](https://html.spec.whatwg.org/#the-a-element)

### `ELEM-ATTR-DEFINITION` — Content attribute definitions and enumerated attributes
Define content attributes with `<dfn element-attr for="source"><code data-x="attr-source-type">type</code></dfn>`,
stating author conformance ("must be a `<span>valid …</span>`") before the processing model.
Enumerated attributes use "is an `<span>enumerated attribute</span>` with the following keywords and
states:" followed by a Keyword (`<dfn attr-value for="…">`) | State (`<dfn data-x="attr-…-state">`) |
Brief description table, then sentences for the `<i data-x="missing value default">missing value
default</i>` and `<i data-x="invalid value default">invalid value default</i>`.
**Example:** [#attr-source-type](https://html.spec.whatwg.org/#attr-source-type) · [#lazy-loading-attributes](https://html.spec.whatwg.org/#lazy-loading-attributes)

### `ELEM-DOMINTRO` — The `dl.domintro` box
Developer summaries are `<dl class="domintro">`:
`<dt><code data-x=""><var>element</var>.<span subdfn data-x="dom-…">member</span>(<var>arg</var>[, <var>opt</var>])</code></dt>`;
promise-returning APIs as `<var>promise</var> = …` or `await …`; constructors as
`<var>audio</var> = new <span subdfn data-x="dom-Audio">Audio</span>([ <var>url</var> ])`; setters
as `… = <var>value</var>`. The `<dd>` is non-normative present tense ("Returns …", "Can be set,
to …", "Throws a <span>"<code>DataCloneError</code>"</span> <code>DOMException</code> if …") and
self-contained — no "see below".
**Example:** [#the-htmlformcontrolscollection-interface](https://html.spec.whatwg.org/#the-htmlformcontrolscollection-interface) · [#dom-structuredclone](https://html.spec.whatwg.org/#dom-structuredclone)
```html
  <dl class="domintro">
   <dt><code data-x=""><var>collection</var>.<span subdfn data-x="dom-HTMLCollection-length">length</span></code></dt>
   <dd><p>Returns the number of elements in <var>collection</var>.</p></dd>
```

### `ELEM-INDEX-TABLE` — Asterisks (`*`) in the `#elements-3` index table mean "see prose for constraints", not regex repetition
In the `#elements-3` Element Index table, a trailing `*` on an item in "Parents" or "Children"
(`<code>summary</code>*`, `<code>figcaption</code>*`, `<code>legend</code>*`,
`<span>transparent</span>*`) is a table footnote marker indicating additional prose constraints,
not regular-expression "zero or more" (truly singular unconditioned children use `one <code>img</code>`).
**Example:** [#elements-3](https://html.spec.whatwg.org/#elements-3)

---

## 5. Algorithm structure and control flow (`ALG`, `FLOW`)

### `ALG-PREAMBLE` — "To <dfn>name</dfn>, given a TYPE <var>x</var>…:"
Wrap the preamble `<p>` and its `<ol>` in `<div algorithm>`. The first paragraph names the algorithm
with a `<dfn>`, lists typed parameters after "given", and ends with a colon.
**Infra:** [§algorithm declaration](https://infra.spec.whatwg.org/#algorithm-declaration) (HTML adds the `<div algorithm>` wrapper and prefers the short colon form)
**Example:** [#light-dismiss-open-dialogs](https://html.spec.whatwg.org/#light-dismiss-open-dialogs)
```html
  <p>To <dfn>light dismiss open dialogs</dfn>, given a <code>PointerEvent</code> <var>event</var>:</p>
```
> **Branch**
> 1. **Modern** — direct colon, no verb phrase, as above. A comma before "given" is optional
>    (`</dfn>, given` 152 vs `</dfn> given` 165); do not comment on it.
> 2. **Accepted** — "…, perform the following steps:" ([#concept-get-all-named](https://html.spec.whatwg.org/#concept-get-all-named)),
>    "…, run these steps." ([#parse-a-url](https://html.spec.whatwg.org/#parse-a-url), usually
>    when a return sentence follows), and "…, run these steps:" (64 uses) — the usual form for hook
>    preambles that are not `To <dfn>` algorithms ("Whenever X's attribute is added or removed, run
>    these steps:"; "When X is popped off the stack of open elements, run these steps:").
> 3. **Legacy** — "…, run the following steps:", "the user agent must run the following steps",
>    "When the user agent is to <dfn>…</dfn>, it must…", "The steps … are as follows:"
>    ([#update-the-image-data](https://html.spec.whatwg.org/#update-the-image-data)).

### `ALG-PARAM-TYPES` — Parameters carry a type and a `<var>` name
"a string <var>url</var>", "a `<code>Document</code>` <var>document</var>", "a <span>list</span> of
<span data-x="URL">URLs</span> <var>urls</var>". Nullable types are "TYPE-or-null" ("a
<span>navigable</span>-or-null <var>parent</var>") and unions chain with "-or-"; for unions of IDL
interfaces "a `<code>Worker</code>` or `<code>SharedWorker</code>` object <var>worker</var>" is also
Accepted. Several parameters are joined with commas and a final "and". Per Infra, the type may be
omitted when the name makes it obvious or the algorithm is a thin wrapper — flag a missing type
only when a reader could not infer it.
**Infra:** [§algorithm declaration](https://infra.spec.whatwg.org/#algorithm-declaration) (the "-or-null" / "-or-" spelling is HTML's)
**Example:** [#parse-a-url](https://html.spec.whatwg.org/#parse-a-url) · [#insertion-target](https://html.spec.whatwg.org/#insertion-target)
```html
  <p>To <dfn export>parse a URL</dfn>, given a string <var>url</var>, relative to a
  <code>Document</code> object or <span>environment settings object</span> <var>environment</var>,
  run these steps. They return failure or a <span>URL</span>.</p>
```

### `ALG-OPTIONAL-ARGS` — "an optional TYPE <var>x</var> (default VALUE)"
Declare optional parameters inline, after the required ones, with their default in parentheses.
Optional booleans always default to false. Inside the steps test presence with "If <var>x</var> was
not given" / "is not given, then set it to …".
**Infra:** [§algorithm parameters](https://infra.spec.whatwg.org/#algorithm-params)
**Example:** [#beginning-navigation](https://html.spec.whatwg.org/#beginning-navigation)
```html
  null), and an optional boolean <var>initialInsertion</var> (default false):</p>
```

### `ALG-RETURN-SENTENCE` — State the return type: "They return X."
When the return type is not obvious from the steps, add a sentence to the preamble: "They return
failure or a <span>URL</span>." Infra allows the short colon form when the return type is easy to
infer (e.g. a boolean predicate); do not demand a return sentence there. Hooks that return nothing
say "returns nothing".
**Infra:** [§algorithm declaration](https://infra.spec.whatwg.org/#algorithm-declaration)
**Example:** [#parse-a-url](https://html.spec.whatwg.org/#parse-a-url)
> **Branch**
> 1. **Modern** — "They return X."
> 2. **Legacy** — "It returns X." ([#create-a-potential-cors-request](https://html.spec.whatwg.org/#create-a-potential-cors-request))

### `ALG-ASSERT` — `<span>Assert</span>: condition.`
State invariants as a linked "Assert:" step; never the bare unlinked word. Assertions describe
what is already true, not behavior. Add one where a nullable value is known to be non-null.
**Infra:** [§assertions](https://infra.spec.whatwg.org/#assertions) (linking the word is HTML's)
**Example:** [#light-dismiss-open-dialogs](https://html.spec.whatwg.org/#light-dismiss-open-dialogs) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/#starting-a-new-parallel-queue)

### `ALG-HOOKS` — "The <span>X steps</span> for the HTML Standard, given <var>y</var>, are defined as the following:"
Implementations of hooks defined by other standards (DOM insertion/removal steps, Fetch
callbacks, Web IDL hooks) link the hook name and do not create a new `<dfn>`; per-element hooks
read "The <span>HTML element insertion steps</span> for `<code>el</code>` elements, given
<var>insertedNode</var>, are:".
**Example:** [#dom-trees](https://html.spec.whatwg.org/#dom-trees)
```html
  <p>The <span data-x="concept-node-insert-ext">insertion steps</span> for the HTML Standard, given
  <var>insertedNode</var>, are defined as the following:</p>
```

### `ALG-ES-ABSTRACT-OPS` — ECMAScript abstract operations: `? <span>Name</span>(args)`
Call into ECMAScript with the JavaScript spec's notation verbatim: `Perform ? <span>Call</span>(…)`,
`Let <var>x</var> be ! <span>ToUint32</span>(<var>P</var>)`, `<var>record</var>.<span data-x="js-Link">Link</span>()`;
internal slots `[[Name]]` are unlinked; names that collide with HTML terms link via `data-x="js-Get"`.
The `?`/`!` prefixes are the only places where exceptions propagate implicitly (`EXC-THROW-DOMEXCEPTION`).
**Example:** [#structuredserializeinternal](https://html.spec.whatwg.org/#structuredserializeinternal)

### `ALG-NON-NORMATIVE-NOTES` — Explain *why* in a `<p class="note">`, never in the step
Rationale, implementation hints, and cross-references go in a note after the step or after the
algorithm, not in the normative sentence. A short parenthetical gloss that restates the effect
("(this delays the load event again)") is an established idiom in older sections and is not a
finding; a "because …" or multi-clause justification inside the step is.
**Example:** [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/#starting-a-new-parallel-queue)

### `ALG-VALIDATE-BEFORE-SIDE-EFFECTS` — A "validate first" pre-pass must cover every input that can fail
When an algorithm is split into a throwing validation loop followed by a side-effecting loop (e.g.
checking transfer data holders before running transfer-receiving steps), the pre-pass has to cover
*all* inputs that can still throw later, including nested records reached through a recursive call.
A partial pre-pass is worse than none: it implies atomicity that the algorithm does not provide.
If full coverage is impractical, say so in a note.
**Example:** [#structureddeserializewithtransfer](https://html.spec.whatwg.org/#structureddeserializewithtransfer)

### `FLOW-IF-THEN` — "If <condition>, then <action>." / "Otherwise, …"
Single-sentence conditionals always use ", then". When the consequent is multiple steps, end the
lead-in with a colon (`If <condition>:`) and nest an `<ol>`. Chains of alternatives use
"Otherwise, if …, then …" and end with "Otherwise, …" (never "Else").
**Infra:** [§conditional statements](https://infra.spec.whatwg.org/#algorithm-conditional-statements) (the colon + nested `<ol>` form is HTML's)
**Example:** [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/#starting-a-new-parallel-queue)
> **Branch**
> 1. **Modern** — `If <condition>:` + nested `<ol>`.
> 2. **Legacy** — `If <condition>, then:` (≈20 uses against thousands of the colon form) and
>    "do the following:". Do not introduce; worth a comment in new algorithms, not in a one-step edit.

### `FLOW-ANY-ALL` — "If any/all of the following are true:" + `<ul>` + "then …"
Several conditions become a bulleted list: lead-in `<p>If any of the following are
true:</p>` (or "all"), a `<ul>` of `<li><p>…;</p></li>` items with "; or" / "; and" on the
penultimate item and "," on the last, then a closing `<p>then …</p>` inside the same `<li>`. Each
item is a single `<li><p>…</p></li>`; notes go after the "then …" paragraph (`BLK-NOTE`). Three
short conditions on one subject that fit a two-line sentence ("If <var>x</var> is null,
<var>x</var>'s disabled is true, or <var>x</var> has a `multiple` attribute, then return.") are
Accepted inline; use the list when conditions are long, heterogeneous, or more than three.
**Example:** [#set-the-frozen-base-url](https://html.spec.whatwg.org/#set-the-frozen-base-url)

### `FLOW-RETURN` — "return" ends an algorithm; "abort these steps" ends a parallel or queued block
Early exits are "…, then return." / "return <var>x</var>." "Abort these steps" is the clearer
choice for leaving a set of steps that is not the algorithm itself — steps run <span>in
parallel</span>, a queued task, or a closure — but Infra permits "return" there too and the spec
uses both; do not flag "return" inside a closure when it is unambiguous. Prefer an early-return
guard as step 1 over deep nesting.
**Infra:** [§control flow](https://infra.spec.whatwg.org/#algorithm-control-flow) · [§conditional abort](https://infra.spec.whatwg.org/#algorithm-conditional-abort) (reserving "abort these steps" for non-algorithm blocks is HTML's)
**Example:** [#parallelism](https://html.spec.whatwg.org/#parallelism)

### `FLOW-SWITCH` — "Switch on <var>x</var>:" + `<dl class="switch">`
Multi-way branches on a value use a lead-in `<p>Switch on <var>x</var>:</p>` and a
`<dl class="switch">` whose `<dt>`s are the cases (only inside algorithms, never at section top
level). Condition-keyed switches write each `<dt>` as "If <var>element</var> is a `<code>bdi</code>`
element" and end with `<dt>Otherwise</dt>`.
**Example:** [#the-embed-element](https://html.spec.whatwg.org/#the-embed-element) · [#the-dir-attribute](https://html.spec.whatwg.org/#the-dir-attribute)
> **Branch**
> 1. **Modern** — "Switch on <var>x</var>:".
> 2. **Legacy** — "Run the appropriate steps from the following list:", "Follow these substeps:"
>    ([#Cue-Track-Parser](https://html.spec.whatwg.org/#text-track-model)).

### `FLOW-FOR-EACH` — "For each <var>item</var> of <var>list</var>:"
Iteration uses Infra's "For each" (`<span data-x="list iterate">For each</span>` when linked) with
"of" for lists and maps ("For each <var>key</var> → <var>value</var> of <var>map</var>").
**Infra:** [§iteration](https://infra.spec.whatwg.org/#algorithm-iteration) · [§lists](https://infra.spec.whatwg.org/#list-iterate)
**Example:** [#create-a-potential-cors-request](https://html.spec.whatwg.org/#create-a-potential-cors-request)
> **Branch**
> 1. **Modern** — "For each <var>x</var> of <var>y</var>".
> 2. **Legacy** — "For each <var>x</var> in <var>y</var>" ([#lazy-loading-attributes](https://html.spec.whatwg.org/#lazy-loading-attributes)).

### `FLOW-LABELS-LEGACY` — `<i>Label</i>:` steps and "jump to the step labeled <i>x</i>" are Legacy
Older parsers label steps (`<i>Loop</i>:`) and jump to them; new text uses `While <condition>:`,
nested steps, and early returns. Blocking with "Wait until <condition>." is legal only inside steps
that run `<span>in parallel</span>`.
**Example:** [#rules-for-parsing-floating-point-number-values](https://html.spec.whatwg.org/#rules-for-parsing-floating-point-number-values) · [#update-the-image-data](https://html.spec.whatwg.org/#update-the-image-data)

---

## 6. Variables, values, and state (`VAR`, `VAL`, `STATE`)

### `VAR-LET-SET` — "Let <var>x</var> be …" declares; "Set <var>x</var> to …" assigns
`Let` introduces a variable once in its scope; later mutations use `Set … to`. Values filled in
across branches start in the outer scope as "Let <var>x</var> be null" (or false) — this hoisting is
the required idiom (variables declared inside a nested `<ol>` are not visible outside it), not a
"dead initialization". Re-using one name for two different objects in the same algorithm (two
`Let <var>record</var>`s, even in exclusive branches) is a finding; a fresh `Let` inside a separate
closure (a fetch callback, queued task) is a new scope and is fine.
**Infra:** [§variables](https://infra.spec.whatwg.org/#variables)
**Example:** [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/#starting-a-new-parallel-queue)

### `VAR-BIND-THEN-TEST` — Bind a long expression once, then test and use the variable
When the same multi-link expression ("<var>moduleMap</var>[(<var>url</var>, <var>type</var>)]'s
fetch options's integrity metadata") appears in a condition and again in its consequent, first
"Let <var>x</var> be …", then test <var>x</var>. Conversely a `Let` that is used exactly once in the
very next step can usually be inlined. Editors ask for both in review.
**Example:** [#fetch-a-single-module-script](https://html.spec.whatwg.org/#fetch-a-single-module-script)

### `VAR-BOUND` — Every `<var>` in an algorithm is a parameter or was introduced with `Let`
A `<var>` that is neither a declared parameter nor `Let`-introduced in an enclosing scope is a bug
(typically a leftover from a rename, or copied from a sibling algorithm). The same goes for
pronouns: do not write "If <var>map</var>["x"] exists and it is a string" — repeat the expression,
or bind it. (`check_algorithms.py` catches only `Set` without `Let`; check reads by hand.)
**Example:** [#check-if-access-between-two-browsing-contexts-should-be-reported](https://html.spec.whatwg.org/#check-if-access-between-two-browsing-contexts-should-be-reported)

### `VAR-CAMELCASE` — Variable names are camelCase
`<var>parallelQueue</var>`, `<var>urlRecord</var>`. Names describe the value; type suffixes
(`…Flag`, `…List`) are avoided.
**Example:** [#set-the-frozen-base-url](https://html.spec.whatwg.org/#set-the-frozen-base-url)
> **Branch**
> 1. **Modern** — camelCase.
> 2. **Legacy** — space-separated multi-word names, `<var>date present</var>` ([#parse-a-date-or-time-string](https://html.spec.whatwg.org/#parse-a-date-or-time-string)).
> 3. **Obsolete** — hyphenated names ([#rules-for-parsing-floating-point-number-values](https://html.spec.whatwg.org/#rules-for-parsing-floating-point-number-values)).

### `VAR-THIS` — The receiver is `<span>this</span>`, not `<var>this</var>` or "this element"
In getter/setter/method steps the receiver is `<span>this</span>`, with possessives like
`<span>this</span>'s <span>node document</span>`. Bind a local (`Let <var>element</var> be
<span>this</span>`) only when passing it to closures or parallel steps.
**Example:** [#dom-domstringlist-length](https://html.spec.whatwg.org/#dom-domstringlist-length)
> **Branch**
> 1. **Modern** — `<span>this</span>` ([#dom-domstringlist-length](https://html.spec.whatwg.org/#dom-domstringlist-length)).
> 2. **Legacy** — "this element", "the element" ([#api-for-a-and-area-elements](https://html.spec.whatwg.org/#api-for-a-and-area-elements)).

### `VAL-LIST-OPS` — Infra lists (`« »`) and list verbs linked with `data-x="list …"`
List literals use guillemets with inner spaces (`« »`, `« <var>a</var>, <var>b</var> »`); empty
lists are "an empty <span>list</span>". Link operations to Infra: `<span data-x="list append">Append</span>`,
`<span data-x="list contains">contains</span>`, `<span data-x="list size">size</span>`, `list remove`,
`list extend`, `<span data-x="list is empty">is empty</span>`. In algorithm prose, never "array",
"push", "add to the list", or "length". ("Array" is fine in author-facing prose and examples that
describe JavaScript values.)
**Infra:** [§lists](https://infra.spec.whatwg.org/#lists) (the `data-x="list …"` linking is HTML's)
**Example:** [#parallelism](https://html.spec.whatwg.org/#parallelism) · [#HTMLAllCollection-call](https://html.spec.whatwg.org/#HTMLAllCollection-call)

### `VAL-MAP-OPS` — Maps (`«[ "key" → value ]»`, `<var>map</var>[<var>key</var>]`, `exists`) and dictionary access
Map lookup is bracket syntax; existence is `<span data-x="map exists">exists</span>`; assignment is
`<span data-x="map set">set</span> <var>map</var>[<var>k</var>] to <var>v</var>`. Web IDL
dictionary members use the same syntax with a linked member name:
`<var>options</var>["<code data-x="dom-X-y">y</code>"]`.
**Infra:** [§maps](https://infra.spec.whatwg.org/#maps)
**Example:** [#structuredserializeinternal](https://html.spec.whatwg.org/#structuredserializeinternal) · [#dom-structuredclone](https://html.spec.whatwg.org/#dom-structuredclone)
> **Branch** (dictionary member access)
> 1. **Modern** — `<var>options</var>["<code data-x="dom-StructuredSerializeOptions-transfer">transfer</code>"]` ([#dom-structuredclone](https://html.spec.whatwg.org/#dom-structuredclone)).
> 2. **Legacy** — "<var>options</var>'s `<code>foo</code>` member" ([#dom-window-postmessage-options](https://html.spec.whatwg.org/#dom-window-postmessage-options)).

### `VAL-NULL` — Null tests are "is null" / "is not null" / "is non-null"; never "exists", "is set", or "is undefined"
Test nullability with "If <var>x</var> is null" and "If <var>x</var> is not null" (≈240 uses) or "is
non-null" (≈110 uses, still being added in 2026) — both are fine; do not flag one for the other. What
to flag is a non-Infra idiom standing in for a null test: "exists" (that is a map/list operation),
"is set"/"is unset", "is defined", or "is undefined" for a non-IDL value. "non-null" as an adjective
("a non-null <span>navigable</span>") is also fine.
**Infra:** [§nulls](https://infra.spec.whatwg.org/#nulls)
**Example:** [#the-dir-attribute](https://html.spec.whatwg.org/#the-dir-attribute) · [#infrastructure](https://html.spec.whatwg.org/#infrastructure)
> **Branch**
> 1. **Accepted** — "is not null".
> 2. **Accepted** — "is non-null".

### `VAL-STRINGS` — "the empty string" and Infra string comparisons
Write "the empty string" (not `""` or "an empty string"). Equality is "is" / "is not" with a string
literal (`XREF-STRING-LITERAL`); case-insensitive comparison is "is an <span>ASCII
case-insensitive</span> match for"; prefix tests use `<span data-x="string starts with">starts
with</span>`. Values left to the UA are `<span>implementation-defined</span>` (linked to Infra).
**Infra:** [§strings](https://infra.spec.whatwg.org/#strings) · [§implementation-defined](https://infra.spec.whatwg.org/#implementation-defined)
**Example:** [#the-link-element](https://html.spec.whatwg.org/#the-link-element) · [#implementation-defined](https://infra.spec.whatwg.org/#implementation-defined)

### `STATE-DECLARATION` — "Each X has a TYPE <dfn>name</dfn>, initially VALUE."
Declare per-object state in one `<p>` with the owner ("Each `<code>input</code>` element", "A
`<code>Document</code>`", "Each <span>media element</span>"), the type, a `<dfn>` (with `for=""` and
`export` when needed across specs), and a trailing ", initially VALUE." clause — never a separate
"must" sentence. Several items of one owner may share a paragraph ("has a boolean <dfn>a</dfn>,
initially false; a <dfn>b</dfn>, a `<code>select</code>` element or null, initially null; …").
Reserve `[[Slot]]` internal slots for objects manipulated through ECMAScript internal methods
(`Window`, `Location`, `WindowProxy`). When the declaring sentence enumerates *when* the state
changes ("…set to true when X, and to false when Y"), a PR that adds a new transition must update
that sentence too (`STATE-DFN-SYNC`).
**Example:** [#was-created-via-cross-origin-redirects](https://html.spec.whatwg.org/#was-created-via-cross-origin-redirects) · [#insertion-target](https://html.spec.whatwg.org/#insertion-target)
> **Branch**
> 1. **Modern** — "Each X has a TYPE `<dfn>name</dfn>`, initially VALUE." ([#was-created-via-cross-origin-redirects](https://html.spec.whatwg.org/#was-created-via-cross-origin-redirects))
> 2. **Accepted** — "has an associated `<dfn>name</dfn>`, which is a TYPE or null, initially null."
>    ([#concept-document-internal-ancestor-origin-objects-list](https://html.spec.whatwg.org/#concept-document-internal-ancestor-origin-objects-list));
>    "a boolean `<dfn>name</dfn>`, which is initially false" when matching an adjacent declaration.
> 3. **Legacy** — "has a `<dfn>x flag</dfn>`, which is initially unset" / "must be initially unset"
>    (`DFN-NO-FLAGS`, [#click-in-progress-flag](https://html.spec.whatwg.org/#click-in-progress-flag)).

---

## 7. Invoking algorithms and IDL member prose (`CALL`, `API`)

### `CALL-CONJUGATED` — "the result of <span data-x="dfn">conjugated verb</span> …" and "given"
Call algorithms by conjugating the verb inside the link ("the result of
`<span data-x="dequeue">dequeuing</span>`") or "running `<span>X</span>`", with arguments introduced
by "given" ("run `<var>onComplete</var>` given `<var>moduleScript</var>`" — not "passing" or "with
… as the argument"). Closures are "Let `<var>steps</var>` be the following steps given
`<var>x</var>`:", run with "run `<var>steps</var>` given …". When an algorithm is the *subject* of a
sentence rather than being invoked, refer to it as a noun: "the `<span>X</span>` algorithm took care
of …" (≈140 uses), never a bare imperative ("fire a traverse navigate event took care of …").
**Example:** [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/#starting-a-new-parallel-queue)
> **Branch**
> 1. **Modern** — conjugated link ("`<span data-x="parse a URL">parsing</span>` `<var>url</var>`")
>    or "running `<span>X</span>` given …" ([#starting-a-new-parallel-queue](https://html.spec.whatwg.org/#starting-a-new-parallel-queue)).
>    "`</span>` given" (≈450) and "`</span>`, given" (≈50) are both fine.
> 2. **Accepted** — "invoking" for Web IDL callbacks; "Perform ? `<span>Op</span>`(…)" for
>    ECMAScript abstract operations (`ALG-ES-ABSTRACT-OPS`).
> 3. **Legacy** — "applying the `<span>URL parser</span>` to", "performing the `<span>X</span>`
>    algorithm" ([#parse-a-url](https://html.spec.whatwg.org/#parse-a-url)); bare "with" for
>    arguments ("`<span>X</span>` with `<var>a</var>`", ≈150) and "…, and let `<var>x</var>` be the
>    result."
> 4. **Obsolete** — an unconjugated verb after "the result of" ("the result of
>    `<span>update an option's nearest ancestor select</span>` given …", 7 uses): fix when touching,
>    including the siblings it was copied from.

### `CALL-ARGS-MATCH-DECL` — Call sites match the declaration's parameter count, order, and types
When invoking an algorithm, check the arguments against its preamble: same number, same order,
and each of the right type — in particular do not pass "<var>x</var>'s value" where <var>x</var> is
already the value, or an element where a `Document` is declared. This is the most common bug class
in "Editorial" fixes and is invisible to Wattsi.
**Example:** [#queue-a-violation-report-for-access-to-other](https://html.spec.whatwg.org/#queue-a-violation-report-for-access-to-other)

### `CALL-RELEVANT-OBJECTS` — "<span>this</span>'s <span>relevant global object</span>"
Obtain the JavaScript context through the possessive on the object being operated on:
"`<span>this</span>`'s `<span>relevant global object</span>`", "`<span>this</span>`'s
`<span data-x="concept-relevant-realm">relevant realm</span>`", "`<span>this</span>`'s
`<span>relevant settings object</span>`". Never introduce `entry` or `incumbent` in new
specifications ([whatwg/html#1430](https://github.com/whatwg/html/issues/1430),
[whatwg/html#1431](https://github.com/whatwg/html/issues/1431)).
**Example:** [#parallelism](https://html.spec.whatwg.org/#parallelism) · [#realms-settings-objects-global-objects](https://html.spec.whatwg.org/#realms-settings-objects-global-objects)

### `CALL-IMPERATIVE` — Steps are imperatives; no "the user agent must" inside algorithms
Within `<ol>` steps the subject is implicit ("Fire an event…", "Return <var>p</var>"). "the user
agent must …" is Legacy there; "The user agent should …" survives only for genuine UI latitude.
**Example:** [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/#starting-a-new-parallel-queue); Legacy: [#dom-document-cookie](https://html.spec.whatwg.org/#dom-document-cookie)

### `API-STEPS-FORM` — "The <dfn>x</dfn> getter/setter/method/constructor steps are …"
Give IDL member behavior as "The `<dfn attribute for=…><code data-x="dom-X-y">y</code></dfn>`
getter steps are to return …" (one-liner) or "The … getter steps are:" + `<ol>`; likewise "setter
steps", "method steps", and "The `<dfn constructor for="X"><code data-x="dom-X">new X(<var>a</var>)</code></dfn>`
constructor steps are:". Within a section, order is IDL block → `dl.domintro` → normative prose in
IDL member order.
**Example:** [#dom-domstringlist-item](https://html.spec.whatwg.org/#dom-domstringlist-item) · [#dom-offscreencanvas](https://html.spec.whatwg.org/#dom-offscreencanvas)
```html
  <p>The <dfn method for="DOMStringList" data-x="dom-DOMStringList-item"><code>item(<var>index</var>)</code></dfn> method steps are to
  return the <var>index</var>th item in <span>this</span>'s associated list, or null if
```
> **Branch**
> 1. **Modern** — "getter/setter/method/constructor steps are".
> 2. **Legacy** — "The `<code>x</code>` attribute must return …", "On getting, …", "On setting,
>    the … IDL attribute must run the following steps:", "The `<code>x()</code>` method, when
>    invoked, must …" ([#dom-radionodelist-value](https://html.spec.whatwg.org/#dom-radionodelist-value),
>    [#dom-document-cookie](https://html.spec.whatwg.org/#dom-document-cookie)).

### `API-ARGUMENTS` — Method arguments are `<var>` names from the IDL signature, read directly
Steps refer to arguments by their IDL names; optional arguments are tested with "If <var>x</var>
was not given" / "is not given" (`ALG-OPTIONAL-ARGS`), never "is undefined" unless the IDL type is
`any`.
**Example:** [#dom-structuredclone](https://html.spec.whatwg.org/#dom-structuredclone)

### `API-READ-INTERNAL-STATE` — Algorithms read internal state, not Web IDL attribute getters
Algorithm steps must reference underlying spec concepts (`<var>img</var>'s <span>current
request</span>'s <span data-x="img-req-url">current URL</span>`, `<var>element</var>'s <code
data-x="attr-…">…</code> content attribute) rather than reading another Web IDL attribute getter
(`<var>img</var>'s <code data-x="dom-img-currentSrc">currentSrc</code>`).
**Example:** [#dom-img-currentsrc](https://html.spec.whatwg.org/#dom-img-currentsrc)

---

## 8. Tasks, parallelism, and events (`TASK`, `PAR`, `EVT`)

### `TASK-QUEUE-GLOBAL` — "<span>queue a global task</span> on the <span>X task source</span> given <var>global</var> to …"
Returning from parallel steps to the event loop always names a task source (reusing an existing
`<dfn>… task source</dfn>` before minting one) and the global (or the element: "queue an element
task on the <span>networking task source</span> given <var>el</var> to …").
**Example:** [#parallelism](https://html.spec.whatwg.org/#parallelism) · [#queue-an-element-task](https://html.spec.whatwg.org/#queue-an-element-task)
```html
       then <span>queue a global task</span> on the <span>DOM manipulation task source</span> given
       <var>global</var> to reject <var>p</var> with a <code>TypeError</code>, and abort these
       steps.</p></li>
```
> **Branch**
> 1. **Modern** — "queue a global task" / "queue an element task", as above.
> 2. **Accepted** — "<span>queue a microtask</span> to …" for same-task continuations on the event loop.
> 3. **Legacy** — bare "<span>queue a task</span> to …" without source or global, and per-feature
>    wrappers such as "queue a media element task" ([#queue-a-media-element-task](https://html.spec.whatwg.org/#queue-a-media-element-task)).

### `PAR-IN-PARALLEL` — "Run the following steps <span>in parallel</span>:" and parallel queues
Introduce off-main-thread work with a nested block (or inline: "Otherwise, <span>in
parallel</span>, wait for …"). Inside it, touch no JavaScript objects or promises, throw nothing,
and hand results back via `TASK-QUEUE-GLOBAL`. When background work must not interleave,
"<span data-x="starting a new parallel queue">start a new parallel queue</span>" and
"<span data-x="enqueue the following steps">enqueue the following steps</span> to <var>queue</var>:".
**Example:** [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/#starting-a-new-parallel-queue) · [#enqueue-the-following-steps](https://html.spec.whatwg.org/#enqueue-the-following-steps)

### `PAR-EVENT-LOOP-LEGACY` — "spin the event loop", "await a stable state", and "synchronous section" are Legacy
These older primitives (and "⌛" step markers) remain in media and parser text and are not
introduced in new algorithms; use `PAR-IN-PARALLEL` + `TASK-QUEUE-GLOBAL`, "Wait until …" inside
parallel steps, or a promise. Editing or adding a ⌛ step inside an algorithm that already uses a
synchronous section is not a finding — the alternative would be rewriting the whole algorithm.
**Example:** [#spin-the-event-loop](https://html.spec.whatwg.org/#spin-the-event-loop) · [#await-a-stable-state](https://html.spec.whatwg.org/#await-a-stable-state)

### `EVT-FIRE` — "<span data-x="concept-event-fire">fire an event</span> named <code data-x="event-load">load</code> at <var>target</var>"
Always fire through DOM's "fire an event" with a linked name (`XREF-CODE-EVENT`), followed by
"using `<code>XEvent</code>`, with its `<code data-x="dom-XEvent-y">y</code>` attribute initialized
to …" when using a custom interface or attributes.
**Example:** [#event-media-addtrack](https://html.spec.whatwg.org/#event-media-addtrack)
```html
     <li><p>If <var>success</var> is true, <span data-x="concept-event-fire">fire an event</span>
     named <code data-x="event-load">load</code> at <var>element</var>.</p></li>
```
> **Branch** (attribute initialization)
> 1. **Modern** — "with its … attribute initialized to".
> 2. **Accepted** — "with the … attribute initialized to" ([#event-media-addtrack](https://html.spec.whatwg.org/#event-media-addtrack)).

---

## 9. Exceptions and promises (`EXC`, `PROM`)

### `EXC-THROW-DOMEXCEPTION` — `throw an <span>"<code>IndexSizeError</code>"</span> <code>DOMException</code>`
DOMException names are quoted, wrapped in a linking `<span>`, and followed by
`<code>DOMException</code>`; the article agrees with the name ("an "IndexSizeError"", "a
"SyntaxError""). JavaScript errors are "throw a `<code>TypeError</code>`". Make exception flow
explicit ("If this throws an exception, catch it, and …" / "rethrow"); `?` is the only implicit
propagation (`ALG-ES-ABSTRACT-OPS`).
**Example:** [#html-element-constructors](https://html.spec.whatwg.org/#html-element-constructors)
```html
     <span>"<code>IndexSizeError</code>"</span> <code>DOMException</code>.</p></li>
```
> **Branch**
> 1. **Modern** — "then throw a `<code>TypeError</code>`." / "throw a <span>"<code>NotSupportedError</code>"</span> <code>DOMException</code>."
> 2. **Legacy** — "throw a `<code>TypeError</code>` exception", "the user agent must throw a …"
>    ([#dom-document-cookie](https://html.spec.whatwg.org/#dom-document-cookie)).

### `PROM-CREATE` — "Let <var>p</var> be a new promise created in <span>this</span>'s <span>relevant realm</span>."
Create promises naming the realm. Short-circuit returns use Web IDL's linked phrases: "return
<span>a promise rejected with</span> a <span>"<code>NotSupportedError</code>"</span>
<code>DOMException</code>" / "<span>a promise resolved with</span> undefined".
**Example:** [#parallelism](https://html.spec.whatwg.org/#parallelism)
```html
    <li><p>Let <var>p</var> be a new promise created in <span>this</span>'s <span
    data-x="concept-relevant-realm">relevant realm</span>.</p></li>
```
> **Branch**
> 1. **Modern** — names the realm, as above.
> 2. **Accepted** — "Let <var>promise</var> be a new promise." when the realm is unambiguous ([#dom-img-decode](https://html.spec.whatwg.org/#dom-img-decode)).

### `PROM-SETTLE` — "resolve <var>p</var> with undefined" / "<span>Upon fulfillment</span> of <var>p</var>"
Settle with "resolve <var>p</var> with undefined" (never bare "resolve <var>p</var>") or "reject
<var>p</var> with …", always from a queued task when in parallel, and return `<var>p</var>` last.
Reactions use Web IDL's linked "<span>Upon fulfillment</span> of <var>p</var>" / "<span>Upon
rejection</span> of <var>p</var>".
**Example:** [#parallelism](https://html.spec.whatwg.org/#parallelism)

---

## 10. Conformance, prose, and vocabulary (`CONF`, `PRS`, `VOC`)

### `CONF-RFC2119` — Lowercase "must"/"should"/"may"; explicit conformance class; `<!-- NON-NORMATIVE SECTION -->`
Requirement keywords are ordinary lowercase words, never capitalized or emphasized, and each
conformance sentence names its conformance class as subject: "User agents must …", "Authors must
not …" (while algorithm `<ol>` steps are bare imperatives per `CALL-IMPERATIVE`). Syntax
constraints on attributes and headers ("The `foo` attribute's value must be a valid integer";
"a `Dictionary` whose value must be a `Token`", 7 uses) are author requirements and need no
explicit subject. "should" in an example or note is advice, not a requirement; leave it. Introductory
and informative sections put `<!-- NON-NORMATIVE SECTION -->` right after the heading.
**Infra:** [§conformance](https://infra.spec.whatwg.org/#conformance) (the `<!-- NON-NORMATIVE SECTION -->` marker and conformance-class phrasing are HTML's)
**Example:** [#conformance-requirements](https://html.spec.whatwg.org/#conformance-requirements) · [#semantics](https://html.spec.whatwg.org/#semantics)

### `PRS-MECHANICS` — Entities (`&mdash;`), plurals outside `<code>`, no contractions in normative text
Use `&mdash;` with spaces for asides (` &mdash; `, 89 uses vs 23 raw `—`) and `&minus;` for
negative numbers (`&minus;1`). Pluralize outside `<code>` ("`<code>img</code>` elements",
`<span data-x="URL">URLs</span>`, never "`<code>imgs</code>`"). Contractions ("can't", "doesn't")
and "we"/"you" appear only in notes, examples, and introductions; new normative text uses "cannot",
"does not", "is not" — a contraction in a re-wrapped parenthetical that the PR did not write is not
a finding. Name the object of a predicate ("scripting is disabled *for <var>document</var>*", not
"scripting is disabled"), and refer to the same thing by the same name within a step.
**Example:** [#typographic-conventions](https://html.spec.whatwg.org/#typographic-conventions) · [#parse-a-url](https://html.spec.whatwg.org/#parse-a-url)

### `VOC-NAVIGABLE` — "navigable" / "traversable", not "browsing context"
New text uses `<span>navigable</span>`, `<span>top-level traversable</span>`, and
`<span>child navigable</span>`. As the spec's own warning states, avoid the browsing context
concept unless dealing with browsing context group switches, agent clusters, opener relationships,
or `WindowProxy`.
**Example:** [#warning-avoid-using-bcs](https://html.spec.whatwg.org/#warning-avoid-using-bcs)
> **Branch**
> 1. **Modern** — `Document` and navigable / traversable concepts ([#navigables](https://html.spec.whatwg.org/#navigables)).
> 2. **Accepted** — browsing context, for browsing context groups, agent clusters, opener relationships, and `WindowProxy` ([#warning-avoid-using-bcs](https://html.spec.whatwg.org/#warning-avoid-using-bcs)).
> 3. **Legacy** — "browsing context" / "top-level browsing context" where a navigable or traversable is meant.

### `VOC-SAME-ORIGIN` — Predicate "is <span>same origin</span> with"; adjective "same-origin"
The relation is a linked predicate without hyphen: "<var>a</var> is <span>same origin</span> with
<var>b</var>", "same origin-domain". The hyphenated form is an adjective only ("same-origin
navigation", "cross-origin isolated").
**Example:** [#same-origin](https://html.spec.whatwg.org/#same-origin)

### `VOC-TERMS` — "authors" vs. "web developers"; "JavaScript" vs. "ECMAScript"
"Authors must not …" is the document conformance class; "web developers" is used in notes,
`dl.domintro`, and the Developer's Edition. Use "JavaScript" for the language (`<ref>JAVASCRIPT</ref>`),
and "ECMAScript" only when naming the ECMA-262 specification or its defined terms.
**Example:** [#semantics](https://html.spec.whatwg.org/#semantics) · [#dependencies](https://html.spec.whatwg.org/#dependencies)
