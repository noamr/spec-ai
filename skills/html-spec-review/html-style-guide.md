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
**Example:** [#parallelism](https://html.spec.whatwg.org/#parallelism)

### `SRC-INDENT-BLOCK` — One space of indentation per block; transparent wrappers do not indent
Indent one space for each block-level ancestor (`<ol>`, multi-line `<li>`, `<dl>`, `<dd>`,
`<div class="example">`, `<div class="note">`, `<div class="warning">`, `<div class="XXX">`, table
rows). A `<p>` inside a one-line `<li>` is not indented further. `<div algorithm>`, `<div w-nodev>`,
and `<div var-scope>` are transparent wrappers: their children stay at the surrounding indentation
level.
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

### `BLK-NOTE` — `<p class="note">` for one paragraph, `<div class="note">` for more
Notes are non-normative asides. They start with a capital letter and never with "Note:". Inside
algorithms, put the note in the `<li>` after the step's `<p>` (`ALG-NON-NORMATIVE-NOTES`).
**Example:** [#event-loop-for-spec-authors](https://html.spec.whatwg.org/#event-loop-for-spec-authors)

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
as the first child of the heading or paragraph, or `<dfn id="old-id">` for dfns.
**Example:** [#rel-alternate](https://html.spec.whatwg.org/#rel-alternate) · [#navigator.online](https://html.spec.whatwg.org/#navigator.online)
```html
  <h5 id="rel-alternate"><span id="link-type-alternate"></span>Link type "<code data-x="rel-alternate">alternate</code>"</h5>
```

### `XREF-SPAN-AUTOLINK` — `<span>` autolinks terms; add `data-x` only when the text differs
A bare `<span>term</span>` links to the `<dfn>` with the same text. Use
`<span data-x="dfn-key">visible text</span>` for conjugated or plural forms and `concept-*` keys.
Link a term on its first use in a paragraph; later uses in the same paragraph may be unlinked.
**Example:** [#a-quick-introduction-to-html](https://html.spec.whatwg.org/#a-quick-introduction-to-html)

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
article and no "algorithm" suffix in the dfn text.
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
**Example:** [#was-created-via-cross-origin-redirects](https://html.spec.whatwg.org/#was-created-via-cross-origin-redirects)
```html
  <p>A <code>Document</code> has a boolean <dfn export>was created via cross-origin redirects</dfn>,
  initially false.</p>
```
> **Branch**
> 1. **Modern** — boolean ("is true"/"is false", "set … to true"), as above.
> 2. **Legacy** — flag that is set/unset ([#click-in-progress-flag](https://html.spec.whatwg.org/#click-in-progress-flag)).

### `DFN-STRUCT` — "is a struct with the following items:" + `<ul>` of dfn items
Define compound state as an Infra struct whose items are a `<ul>` of
`<li><p><dfn>Name</dfn>, a TYPE, initially VALUE.</p></li>`, accessed with the possessive
(`<var>manager</var>'s <span>groups</span>`). Use a tuple only for two-element pairs.
**Example:** [#close-watcher-manager](https://html.spec.whatwg.org/#close-watcher-manager)
```html
  <p>Each <code>Window</code> has a <dfn>close watcher manager</dfn>, which is a <span>struct</span>
  with the following <span data-x="struct item">items</span>:</p>

  <ul>
   <li><p><dfn data-x="close watcher manager groups">Groups</dfn>, a <span>list</span> of
```

### `EVT-DFN-EVENT` — Define events in a table with `<dfn event for="…">` and list them in the index
Every event gets a `<dfn event for="Interface"><code data-x="event-…">name</code></dfn>` row in a
table with Interface / Fired when / Preconditions columns, plus a row in the Events index.
**Example:** [#event-media-loadstart](https://html.spec.whatwg.org/#event-media-loadstart) · [#events-2](https://html.spec.whatwg.org/#events-2)

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

---

## 5. Algorithm structure and control flow (`ALG`, `FLOW`)

### `ALG-PREAMBLE` — "To <dfn>name</dfn>, given a TYPE <var>x</var>…:"
Wrap the preamble `<p>` and its `<ol>` in `<div algorithm>`. The first paragraph names the algorithm
with a `<dfn>`, lists typed parameters after "given", and ends with a colon.
**Example:** [#light-dismiss-open-dialogs](https://html.spec.whatwg.org/#light-dismiss-open-dialogs)
```html
  <p>To <dfn>light dismiss open dialogs</dfn>, given a <code>PointerEvent</code> <var>event</var>:</p>
```
> **Branch**
> 1. **Modern** — direct colon, no verb phrase, as above.
> 2. **Accepted** — "…, perform the following steps:" ([#concept-get-all-named](https://html.spec.whatwg.org/#concept-get-all-named))
>    and "…, run these steps." ([#parse-a-url](https://html.spec.whatwg.org/#parse-a-url), usually
>    when a return sentence follows).
> 3. **Legacy** — "…, run the following steps:", "the user agent must run the following steps",
>    "When the user agent is to <dfn>…</dfn>, it must…", "The steps … are as follows:"
>    ([#update-the-image-data](https://html.spec.whatwg.org/#update-the-image-data)).

### `ALG-PARAM-TYPES` — Every parameter carries a type and a `<var>` name
"a string <var>url</var>", "a `<code>Document</code>` <var>document</var>", "a <span>list</span> of
<span data-x="URL">URLs</span> <var>urls</var>". Nullable types are "TYPE-or-null" ("a
<span>navigable</span>-or-null <var>parent</var>") and unions chain with "-or-". Several parameters
are joined with commas and a final "and".
**Example:** [#parse-a-url](https://html.spec.whatwg.org/#parse-a-url) · [#insertion-target](https://html.spec.whatwg.org/#insertion-target)
```html
  <p>To <dfn export>parse a URL</dfn>, given a string <var>url</var>, relative to a
  <code>Document</code> object or <span>environment settings object</span> <var>environment</var>,
  run these steps. They return failure or a <span>URL</span>.</p>
```

### `ALG-OPTIONAL-ARGS` — "an optional TYPE <var>x</var> (default VALUE)"
Declare optional parameters inline with their default in parentheses. Inside the steps test
presence with "If <var>x</var> was not given" / "is not given, then set it to …".
**Example:** [#beginning-navigation](https://html.spec.whatwg.org/#beginning-navigation)
```html
  null), and an optional boolean <var>initialInsertion</var> (default false):</p>
```

### `ALG-RETURN-SENTENCE` — State the return type: "They return X."
When an algorithm returns something, add a sentence to the preamble: "They return failure or a
<span>URL</span>." Hooks that return nothing say "returns nothing".
**Example:** [#parse-a-url](https://html.spec.whatwg.org/#parse-a-url)
> **Branch**
> 1. **Modern** — "They return X."
> 2. **Legacy** — "It returns X." ([#create-a-potential-cors-request](https://html.spec.whatwg.org/#create-a-potential-cors-request))

### `ALG-ASSERT` — `<span>Assert</span>: condition.`
State invariants as a linked "Assert:" step; never the bare unlinked word. Assertions describe
what is already true, not behavior. Add one where a nullable value is known to be non-null.
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
algorithm, not in the normative sentence.
**Example:** [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/#starting-a-new-parallel-queue)

### `FLOW-IF-THEN` — "If <condition>, then <action>." / "Otherwise, …"
Single-sentence conditionals always use ", then". When the consequent is multiple steps, end the
lead-in with a colon (`If <condition>:`) and nest an `<ol>` (never "then:" or "do the following:").
Chains of alternatives use "Otherwise, if …, then …" and end with "Otherwise, …" (never "Else").
**Example:** [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/#starting-a-new-parallel-queue)

### `FLOW-ANY-ALL` — "If any/all of the following are true:" + `<ul>` + "then …"
Three or more conditions become a bulleted list: lead-in `<p>If any of the following are
true:</p>` (or "all"), a `<ul>` of `<li><p>…;</p></li>` items with "; or" / "; and" on the
penultimate item and "," on the last, then a closing `<p>then …</p>` inside the same `<li>`.
**Example:** [#set-the-frozen-base-url](https://html.spec.whatwg.org/#set-the-frozen-base-url)

### `FLOW-RETURN` — "return" ends an algorithm; "abort these steps" ends a parallel or queued block
Early exits are "…, then return." / "return <var>x</var>." "Abort these steps" is reserved for
leaving a set of steps that is not the algorithm itself — steps run <span>in parallel</span>, a
queued task, or a closure — where "return" would be ambiguous. Prefer an early-return guard as
step 1 over deep nesting.
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
across branches start in the outer scope as "Let <var>x</var> be null" (or false).
**Example:** [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/#starting-a-new-parallel-queue)

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
`list extend`, `<span data-x="list is empty">is empty</span>`. Never "array", "push", "add to the
list", or "length".
**Example:** [#parallelism](https://html.spec.whatwg.org/#parallelism) · [#HTMLAllCollection-call](https://html.spec.whatwg.org/#HTMLAllCollection-call)

### `VAL-MAP-OPS` — Maps (`«[ "key" → value ]»`, `<var>map</var>[<var>key</var>]`, `exists`) and dictionary access
Map lookup is bracket syntax; existence is `<span data-x="map exists">exists</span>`; assignment is
`<span data-x="map set">set</span> <var>map</var>[<var>k</var>] to <var>v</var>`. Web IDL
dictionary members use the same syntax with a linked member name:
`<var>options</var>["<code data-x="dom-X-y">y</code>"]`.
**Example:** [#structuredserializeinternal](https://html.spec.whatwg.org/#structuredserializeinternal) · [#dom-structuredclone](https://html.spec.whatwg.org/#dom-structuredclone)
> **Branch** (dictionary member access)
> 1. **Modern** — `<var>options</var>["<code data-x="dom-StructuredSerializeOptions-transfer">transfer</code>"]` ([#dom-structuredclone](https://html.spec.whatwg.org/#dom-structuredclone)).
> 2. **Legacy** — "<var>options</var>'s `<code>foo</code>` member" ([#dom-window-postmessage-options](https://html.spec.whatwg.org/#dom-window-postmessage-options)).

### `VAL-NULL` — "is null" / "is not null" as predicates; "non-null" only as an adjective
Tests are "If <var>x</var> is not null, then …". "non-null" modifies a noun ("a non-null
<span>navigable</span>") and is never written "is non-null".
**Example:** [#the-dir-attribute](https://html.spec.whatwg.org/#the-dir-attribute) · [#infrastructure](https://html.spec.whatwg.org/#infrastructure)

### `VAL-STRINGS` — "the empty string" and Infra string comparisons
Write "the empty string" (not `""` or "an empty string"). Equality is "is" / "is not" with a string
literal (`XREF-STRING-LITERAL`); case-insensitive comparison is "is an <span>ASCII
case-insensitive</span> match for"; prefix tests use `<span data-x="string starts with">starts
with</span>`. Values left to the UA are `<span>implementation-defined</span>` (linked to Infra).
**Example:** [#the-link-element](https://html.spec.whatwg.org/#the-link-element) · [#implementation-defined](https://infra.spec.whatwg.org/#implementation-defined)

### `STATE-DECLARATION` — "Each X has a TYPE <dfn>name</dfn>, initially VALUE."
Declare per-object state in one `<p>` with the owner ("Each `<code>input</code>` element", "A
`<code>Document</code>`", "Each <span>media element</span>"), the type, a `<dfn>` (with `for=""` and
`export` when needed across specs), and a trailing ", initially VALUE." clause — never a separate
"must" sentence. Reserve `[[Slot]]` internal slots for objects manipulated through ECMAScript
internal methods (`Window`, `Location`, `WindowProxy`).
**Example:** [#was-created-via-cross-origin-redirects](https://html.spec.whatwg.org/#was-created-via-cross-origin-redirects) · [#insertion-target](https://html.spec.whatwg.org/#insertion-target)
> **Branch**
> 1. **Modern** — "Each X has a TYPE `<dfn>name</dfn>`, initially VALUE." ([#was-created-via-cross-origin-redirects](https://html.spec.whatwg.org/#was-created-via-cross-origin-redirects))
> 2. **Accepted** — "has an associated `<dfn>name</dfn>`, which is a TYPE or null, initially null."
>    ([#concept-document-internal-ancestor-origin-objects-list](https://html.spec.whatwg.org/#concept-document-internal-ancestor-origin-objects-list))
> 3. **Legacy** — "has a `<dfn>x flag</dfn>`, which is initially unset" / "must be initially unset"
>    (`DFN-NO-FLAGS`, [#click-in-progress-flag](https://html.spec.whatwg.org/#click-in-progress-flag)).

---

## 7. Invoking algorithms and IDL member prose (`CALL`, `API`)

### `CALL-CONJUGATED` — "the result of <span data-x="dfn">conjugated verb</span> …" and "given"
Call algorithms by conjugating the verb inside the link ("the result of
`<span data-x="dequeue">dequeuing</span>`") or "running `<span>X</span>`", with arguments introduced
by "given" ("run `<var>onComplete</var>` given `<var>moduleScript</var>`" — not "passing" or "with
… as the argument"). Closures are "Let `<var>steps</var>` be the following steps given
`<var>x</var>`:", run with "run `<var>steps</var>` given …".
**Example:** [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/#starting-a-new-parallel-queue)
> **Branch**
> 1. **Modern** — conjugated link ("`<span data-x="parse a URL">parsing</span>` `<var>url</var>`")
>    or "running `<span>X</span>` given …" ([#starting-a-new-parallel-queue](https://html.spec.whatwg.org/#starting-a-new-parallel-queue)).
> 2. **Accepted** — "invoking" for Web IDL callbacks; "Perform ? `<span>Op</span>`(…)" for
>    ECMAScript abstract operations (`ALG-ES-ABSTRACT-OPS`).
> 3. **Legacy** — "applying the `<span>URL parser</span>` to", "performing the `<span>X</span>`
>    algorithm" ([#parse-a-url](https://html.spec.whatwg.org/#parse-a-url)).

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
parallel steps, or a promise.
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
not …" (while algorithm `<ol>` steps are bare imperatives per `CALL-IMPERATIVE`). Introductory and
informative sections put `<!-- NON-NORMATIVE SECTION -->` right after the heading.
**Example:** [#conformance-requirements](https://html.spec.whatwg.org/#conformance-requirements) · [#semantics](https://html.spec.whatwg.org/#semantics)

### `PRS-MECHANICS` — Entities (`&mdash;`), plurals outside `<code>`, no contractions in normative text
Use `&mdash;` with spaces for asides (` &mdash; `) and `&minus;` for negative numbers (`&minus;1`).
Pluralize outside `<code>` ("`<code>img</code>` elements", `<span data-x="URL">URLs</span>`, never
"`<code>imgs</code>`"). Contractions ("can't", "doesn't") and "we"/"you" appear only in notes,
examples, and introductions; normative text uses "cannot", "does not", "is not".
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
