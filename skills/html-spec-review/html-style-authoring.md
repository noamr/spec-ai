# HTML Standard style guide — authoring style

How algorithms and prose are written: naming definitions, preambles and step structure,
control flow, variables and values, state declarations, IDL member prose, tasks and events,
exceptions and promises, conformance language, prose mechanics, and vocabulary.

Part of the HTML house style guide. See [html-style-guide.md](html-style-guide.md) for the
Modern / Accepted / Legacy / Obsolete **Branch** tiers and an index of every rule ID across
files. Examples are pinned to whatwg/html commit [`877d614`](https://github.com/whatwg/html/commit/877d6146487f15b15bc8dd0e3c625063a37b456a).

| § | Section | Prefixes |
|---|---|---|
| 1 | Naming definitions | `DFN` |
| 2 | Algorithm structure | `ALG` |
| 3 | Control flow | `FLOW` |
| 4 | Variables | `VAR` |
| 5 | Values and data structures | `VAL` |
| 6 | State declarations | `STATE` |
| 7 | Invoking algorithms | `CALL` |
| 8 | IDL member prose | `API` |
| 9 | Tasks and events | `TASK`, `EVT` |
| 10 | Exceptions and promises | `EXC`, `PROM` |
| 11 | Conformance language | `CONF` |
| 12 | Prose mechanics | `PRS` |
| 13 | Vocabulary | `VOC` |

---

## 1. Naming definitions (`DFN`)

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

## 2. Algorithm structure (`ALG`)

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

## 3. Control flow (`FLOW`)

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

## 4. Variables (`VAR`)

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

## 5. Values and data structures (`VAL`)

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

## 6. State declarations (`STATE`)

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

## 7. Invoking algorithms (`CALL`)

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

### `CALL-IMPERATIVE` — Steps are imperatives; no "the user agent must" inside algorithms
Within `<ol>` steps the subject is implicit ("Fire an event…", "Return <var>p</var>"). "the user
agent must …" is Legacy there; "The user agent should …" survives only for genuine UI latitude.
See `CONF-RFC2119`.
**Example:** [source#L1599](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1599) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#starting-a-new-parallel-queue); Legacy: [source#L12094](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L12094) · [#dom-document-cookie](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-document-cookie); latitude: [source#L7861](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L7861)

---

## 8. IDL member prose (`API`)

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

## 9. Tasks and events (`TASK`, `EVT`)

This section covers how task and event steps are phrased. Which global to pass, when a
task can run, and what parallel steps may touch are in
[html-semantics.md](html-semantics.md) §5.

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

---

## 10. Exceptions and promises (`EXC`, `PROM`)

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

## 11. Conformance language (`CONF`)

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

## 12. Prose mechanics (`PRS`)

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

## 13. Vocabulary (`VOC`)

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
linked to Infra (`VAL-*`). Do not invent synonyms ("array", "dictionary" for maps, "add" for append,
"check whether").
**Example:** [source#L2256](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L2256) · [#dependencies](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dependencies); use: [source#L124882](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L124882)
