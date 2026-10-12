# HTML Standard style guide — semantics of core concepts

Which concept to use: picking the right `Document`, navigable, realm, global object, settings
object, origin, and task primitive. Text that gets these wrong can read fine and still
specify the wrong behavior (for bfcached or detached documents, cross-realm calls, opaque
origins, workers).

Part of the HTML house style guide. See [html-style-guide.md](html-style-guide.md) for the
Modern / Accepted / Legacy / Obsolete **Branch** tiers and an index of every rule ID across
files. Examples are pinned to whatwg/html commit [`877d614`](https://github.com/whatwg/html/commit/877d6146487f15b15bc8dd0e3c625063a37b456a).

| § | Section | Prefixes |
|---|---|---|
| 1 | Documents | `DOC` |
| 2 | Navigables and browsing contexts | `NAV` |
| 3 | Realms, global objects, and settings objects | `ENV` |
| 4 | Origins and sites | `ORIGIN` |
| 5 | Event loop and parallelism | `TASK`, `PAR` |

---

## 1. Documents (`DOC`)

### `DOC-ACTIVE-VS-FULLY-ACTIVE` — "active document" belongs to a navigable; "fully active" is the check on a `Document`
A navigable's active document is its active session history entry's document. A `Document` can be
the active document of its node navigable and still not be fully active, because "fully active"
also requires the navigable to be a top-level traversable or its container document to be fully
active. Guards on a `Document` use "is not <span>fully active</span>"; "is the active document of
<var>navigable</var>" is only for statements about a specific navigable.
**Example:** [source#L107223](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L107223) · [#fully-active](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#fully-active); navigable's active document: [source#L105439](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105439) · [#nav-document](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#nav-document); active but not fully active: [source#L107238](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L107238)
```html
  <p>A <code>Document</code> <var>d</var> is said to be <dfn export for="Document">fully
  active</dfn> when <var>d</var> is the <span data-x="nav-document">active document</span> of a
  <span>navigable</span> <var>navigable</var>, and either <var>navigable</var> is a <span>top-level
  traversable</span> or <var>navigable</var>'s <span data-x="nav-container-document">container
  document</span> is <span>fully active</span>.</p>
```
> **Branch**
> 1. **Modern** — "is (not) <span>fully active</span>".
> 2. **Legacy** — "is active", "is the active document" with no navigable named, "is shown"; rewrite when touching.

### `VOC-FULLY-ACTIVE` — Check "<span>fully active</span>" before touching a Document
APIs that must not run for bfcached or detached documents begin with "If <span>this</span>'s
<span>relevant global object</span>'s <span>associated <code>Document</code></span> is not
<span>fully active</span>, then …". Use this exact predicate, not "is not active" or "is not
shown".
**Example:** [source#L36152](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L36152); [source#L11801](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11801)

### `DOC-WHICH-DOCUMENT` — Reach the `Document` through the object you have
Pick the `Document` from the receiver:
- a node: its <span>node document</span> ("<span>this</span>'s <span>node document</span> is not <span>fully active</span>");
- a `Document`: <span>this</span> itself;
- a `Window`: its <span data-x="concept-document-window">associated `Document`</span>;
- any other platform object: <span>this</span>'s <span>relevant global object</span>'s associated
  `Document`, after checking that the global is a `Window` (`ENV-WINDOW-ONLY`).

For a node, do not detour through its relevant global object: the node document and the global's
associated `Document` can differ (for example for nodes in a `template` element's contents, whose
node document is a separate inert `Document`).
**Example:** node: [source#L31813](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L31813) · [#dom-img-decode](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-img-decode); `Document`: [source#L125944](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L125944) · [#dom-document-open-window](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-document-open-window); `Window`: [source#L97437](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L97437) · [#concept-document-window](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#concept-document-window); other object: [source#L36152](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L36152)

### `DOC-NULL-BROWSING-CONTEXT` — A `Document` may have no browsing context and no navigable
A `Document` created by `createDocument()`, one used by a data-mining tool, and the `Document` of
an `iframe` that has been removed all have a null browsing context. "node navigable" returns null
when no navigable has the node document as its active document. Any step that goes from a
`Document` or node to a navigable, `WindowProxy`, or browsing context handles null first
("If <var>document</var>'s <span>node navigable</span> is null, then return …"). Scripting is
disabled for nodes whose node document's browsing context is null.
**Example:** [source#L106694](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L106694) · [#concept-document-bc](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#concept-document-bc); [source#L105483](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105483) · [#node-navigable](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#node-navigable); null check: [source#L19429](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L19429); [source#L105743](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105743); scripting: [source#L118507](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L118507)
```html
   <li><p>If <var>document</var>'s <span>node navigable</span> is null, then return false.</p></li>
```

### `DOC-CONNECTED` — "connected" vs. "browsing-context connected"
"<span>connected</span>" (DOM) means the node's shadow-including root is a `Document`.
"<span>browsing-context connected</span>" also requires that `Document`'s browsing context to be
non-null. Use the hook that matches the condition you mean ("<span>becomes connected</span>" /
"<span>becomes browsing-context connected</span>" and their "disconnected" pairs). Behavior that
only makes sense in a document with a browsing context uses the browsing-context variant.
**Example:** [source#L1905](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1905) · [#becomes-connected](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#becomes-connected); [source#L1914](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1914) · [#browsing-context-connected](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#browsing-context-connected); use: [source#L8200](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L8200)

### `DOC-ORIGIN-NOT-URL` — A `Document`'s origin is not derived from its URL
A `Document`'s origin is set when it is created and changes only through `document.domain`. It can
differ from its URL's origin, for example when an initial `about:blank` `Document` inherits its
creator's origin. Security decisions use the `Document`'s
<span data-x="concept-document-origin">origin</span>, never "the origin of <var>document</var>'s
URL".
**Example:** [source#L11639](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11639)

### `DOC-WINDOW-REUSE` — `Window` and `Document` are not always 1-to-1
A `Window`'s associated `Document` is set when the `Window` is created. It changes only once: when
a navigation from the initial `about:blank` `Document` reuses the `Window` for the new
`Document`. State keyed on a `Window` is therefore not always per-`Document`, and state keyed on a
`Document` is not always per-`Window`; consider this case when choosing where state lives.
**Example:** [source#L97437](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L97437) · [#concept-document-window](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#concept-document-window); [source#L106703](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L106703)

---

## 2. Navigables and browsing contexts (`NAV`)

### `VOC-NAVIGABLE` — "navigable" / "traversable", not "browsing context"
New text speaks of `<span>navigable</span>`, `<span>top-level traversable</span>`, and
`<span>child navigable</span>`. "browsing context" is reserved for the remaining
browsing-context concepts (agent clusters, `window.open`'s auxiliary browsing context, browsing
context groups) and historical anchors.
**Example:** [source#L105494](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105494); [source#L29175](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L29175)
> **Branch**
> 1. **Modern** — navigable / traversable.
> 2. **Legacy** — "browsing context" where a navigable is meant; rewrite when touching.

### `NAV-AVOID-BROWSING-CONTEXT` — Use browsing contexts only for group switches and agent clusters
The spec warns that modern specifications should avoid the browsing context concept unless they
deal with browsing context group switches or agent cluster allocation. Otherwise the `Document`
and navigable concepts are usually more appropriate.
**Example:** [source#L106682](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L106682) · [#warning-avoid-using-bcs](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#warning-avoid-using-bcs)
> **Branch**
> 1. **Modern** — `Document` and navigable concepts.
> 2. **Accepted** — browsing context, for browsing context groups, agent clusters, opener relationships, and `WindowProxy`.
> 3. **Legacy** — browsing context where a navigable or `Document` is meant.

### `NAV-DEFINED-ACCESSORS` — Move between concepts with the defined accessors
Use the defined terms rather than inventing chains such as "the navigable of <var>x</var>" or
"<var>x</var>'s browsing context's …":

| From | To | Term |
|---|---|---|
| navigable | `Document` | <span data-x="nav-document">active document</span> |
| navigable | `Window` | <span data-x="nav-window">active window</span> (always the active document's relevant global object) |
| node | navigable | <span>node navigable</span> (may be null) |
| `Window` | navigable | <span data-x="window navigable">navigable</span> (may be null) |
| navigable | element / `Document` | <span data-x="nav-container">container</span> / <span data-x="nav-container-document">container document</span> (null for traversables) |
| navigable container | navigable | <span>content navigable</span> (may be null) |
| navigable | top | <span data-x="nav-top">top-level traversable</span> |

**Example:** [source#L105439](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105439) · [#nav-document](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#nav-document); [source#L105464](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105464) · [#nav-window](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#nav-window) and its note [source#L105469](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105469); [source#L105483](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105483) · [#node-navigable](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#node-navigable); [source#L97451](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L97451) · [#window-navigable](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#window-navigable); [source#L105707](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105707) · [#content-navigable](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#content-navigable); [source#L105712](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105712) · [#nav-container](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#nav-container); [source#L105718](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105718) · [#nav-container-document](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#nav-container-document)

### `NAV-SESSION-ENTRIES` — Say whether you mean the current or the active session history entry
A navigable's current session history entry can be modified only within the session history
traversal queue. Its active session history entry can be modified only from the event loop of
that entry's document. The two diverge during synchronous navigations and when a non-displayable
response is received. Session history algorithms say which entry they read and run where that
entry may be accessed.
**Example:** [source#L105379](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105379) · [#nav-current-history-entry](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#nav-current-history-entry); [source#L105388](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105388) · [#nav-active-history-entry](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#nav-active-history-entry); divergence: [source#L105421](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105421)

### `NAV-TOP-LEVEL` — "top-level traversable", not "top-level browsing context"
A navigable's <span data-x="nav-top">top-level traversable</span> is the modern way to reach the
top of a frame tree. A browsing context also has a
<span data-x="bc-traversable">top-level traversable</span>.
**Example:** [source#L105598](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L105598) · [#nav-top](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#nav-top); [source#L106666](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L106666) · [#bc-traversable](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#bc-traversable)
> **Branch**
> 1. **Modern** — "top-level traversable".
> 2. **Accepted** — "top-level browsing context" in browsing-context-group and opener logic (`NAV-AVOID-BROWSING-CONTEXT`).
> 3. **Legacy** — "top-level browsing context" elsewhere. [source#L11894](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11894)

---

## 3. Realms, global objects, and settings objects (`ENV`)

### `ENV-PICK-BY-PURPOSE` — Realm, global object, and settings object map 1-to-1-to-1; name the one whose property you need
Each realm has exactly one global object and one environment settings object, and the spec
defines how to get from each to the others. Name the one that owns what you need:
- **realm**: creating JavaScript objects ("a new promise created in <span>this</span>'s relevant
  realm", `PROM-CREATE`);
- **global object**: queuing tasks (`TASK-QUEUE-GLOBAL`), firing events at the `Window`, reaching
  the associated `Document`;
- **settings object**: origin, policy container, API base URL, secure context, cross-origin
  isolated capability.

**Example:** [source#L117857](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L117857) · [#realms-settings-objects-global-objects](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#realms-settings-objects-global-objects); realm: [source#L1642](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1642) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism); settings object: [source#L125648](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L125648) · [#dom-issecurecontext](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-issecurecontext); [source#L125654](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L125654) · [#dom-origin](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-origin)

### `CALL-RELEVANT-OBJECTS` — "<span>this</span>'s <span>relevant global object</span>"
Obtain the JavaScript context through the possessive: "<span>this</span>'s <span>relevant global
object</span>", "<var>element</var>'s <span>node document</span>'s <span>relevant global
object</span>", "<span>this</span>'s <span data-x="concept-relevant-realm">relevant realm</span>".
"the <span>relevant global object</span> of <var>x</var>" is Legacy. For when "current" is
acceptable, see `ENV-RELEVANT-BY-DEFAULT`; "entry" and "incumbent" are never introduced in new
text (`ENV-NO-ENTRY-INCUMBENT`).
**Example:** [source#L1645](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1645) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism)
```html
    <li><p>Let <var>global</var> be <span>this</span>'s <span>relevant global
    object</span>.</p></li>
```

### `ENV-RELEVANT-BY-DEFAULT` — Use "relevant", applied to the object being operated on
"In general, web platform specifications should use the relevant concept, applied to the object
being operated on (usually the this value of the current method)." This differs from JavaScript,
where "current" is the default, and the spec accepts the inconsistency. "Current" stays correct
where the caller is what matters: `IsPlatformObjectSameOrigin` compares the current settings
object's origin, and the spec's own template for asynchronous algorithms parses URLs relative to
the current settings object and creates results in the current realm.
**Example:** [source#L117999](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L117999) · [#realms-settings-objects-global-objects](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#realms-settings-objects-global-objects); current, caller-sensitive: [source#L97171](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L97171) · [#isplatformobjectsameorigin](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#isplatformobjectsameorigin); template: [source#L124331](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L124331) · [#example-event-loop-using-algorithm](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#example-event-loop-using-algorithm)
> **Branch**
> 1. **Modern** — relevant realm / global object / settings object of <span>this</span> (or of an argument).
> 2. **Accepted** — current realm / global object / settings object, for caller-sensitive checks and argument processing.
> 3. **Legacy** — entry or incumbent (`ENV-NO-ENTRY-INCUMBENT`).

### `ENV-NO-ENTRY-INCUMBENT` — Do not introduce "entry" or "incumbent"
"The incumbent and entry concepts should not be used by new specifications, as they are
excessively complicated and unintuitive to work with." Removal of existing uses is tracked in
[whatwg/html#1430](https://github.com/whatwg/html/issues/1430) (incumbent) and
[whatwg/html#1431](https://github.com/whatwg/html/issues/1431) (entry). The spec's example notes
that choosing the source `Document` for `Location`-object navigation is "perhaps the only
justifiable use" of incumbent.
**Example:** [source#L117990](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L117990) · [#realms-settings-objects-global-objects](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#realms-settings-objects-global-objects); Legacy use: [source#L99198](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L99198) · [#dom-location-href](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-location-href); [source#L118412](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L118412)

### `ENV-WINDOW-ONLY` — Check that the global is a `Window` before reaching for a `Document`
Global objects can be `Window`, `WorkerGlobalScope`, or `WorkletGlobalScope` objects. "queue a
global task" itself uses "<var>global</var>'s associated `Document`, if <var>global</var> is a
`Window` object; otherwise null". Algorithms that can run in workers or worklets branch the same
way before they use the associated `Document`.
**Example:** [source#L117819](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L117819); [source#L123256](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L123256) · [#queue-a-global-task](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#queue-a-global-task); [source#L118478](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L118478)
```html
   <li><p>Let <var>document</var> be <var>global</var>'s <span
   data-x="concept-document-window">associated <code>Document</code></span>, if <var>global</var> is
   a <code>Window</code> object; otherwise null.</p>
```

### `ENV-URL-BASE` — Parse URLs relative to the node document for elements, and to a settings object otherwise
Element attributes and element methods parse URLs "relative to <span>this</span>'s <span>node
document</span>" (or "relative to the element's node document"). APIs that are not on nodes use a
settings object, normally <span>this</span>'s relevant settings object.
**Example:** element: [source#L61596](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L61596); [source#L35706](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L35706); settings object: [source#L131449](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L131449) · [#dom-navigator-registerprotocolhandler](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-navigator-registerprotocolhandler); current: [source#L124331](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L124331) · [#example-event-loop-using-algorithm](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#example-event-loop-using-algorithm)
> **Branch**
> 1. **Modern** — the node document (nodes) / <span>this</span>'s relevant settings object (other objects).
> 2. **Accepted** — the current settings object (`ENV-RELEVANT-BY-DEFAULT`).
> 3. **Legacy** — the entry settings object. [source#L99216](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L99216) · [#dom-location-href](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-location-href)

### `ENV-SECURE-CONTEXT` — "secure context" is a property of an environment
Test "<span>this</span>'s <span>relevant settings object</span> is a <span>secure
context</span>" (or the same of another environment). Do not test a URL's scheme or an origin as
a proxy.
**Example:** [source#L118525](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L118525) · [#secure-context](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#secure-context); [source#L125648](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L125648) · [#dom-issecurecontext](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-issecurecontext)

---

## 4. Origins and sites (`ORIGIN`)

### `VOC-SAME-ORIGIN` — Predicate "is <span>same origin</span> with"; adjective "same-origin"
The relation is a linked predicate without hyphen: "<var>a</var> is <span>same origin</span> with
<var>b</var>", "same origin-domain". The hyphenated form is an adjective only ("same-origin
navigation", "cross-origin isolated").
**Example:** [source#L11841](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11841); adjective: [source#L117794](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L117794)

### `ORIGIN-WHICH-ORIGIN` — The `Document`'s origin for a `Document`; the relevant settings object's origin otherwise
A `Document` has its own <span data-x="concept-document-origin">origin</span> (`DOC-ORIGIN-NOT-URL`).
For other objects, use "<span>this</span>'s <span>relevant settings object</span>'s
<span data-x="concept-settings-object-origin">origin</span>". A request's origin is a separate
Fetch concept; do not substitute one for another.
**Example:** [source#L11639](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L11639); [source#L56499](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L56499) · [#dom-input-showpicker](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-input-showpicker); [source#L125654](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L125654) · [#dom-origin](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-origin)
```html
    <p>If <span>this</span>'s <span>relevant settings object</span>'s <span
    data-x="concept-settings-object-origin">origin</span> is not <span>same origin</span> with
    <span>this</span>'s <span>relevant settings object</span>'s <span>top-level origin</span>, and
```

### `ORIGIN-COMPARE-ORIGINS` — Compare origins with "same origin", not their serializations
Every opaque origin serializes to "`null`", so comparing serialized strings conflates distinct
opaque origins. "same origin" treats two opaque origins as equal only when they are the same
opaque origin. The serialization of a site has the same problem, plus a site and an origin can
serialize identically. Serialize only to expose a string (for example `self.origin`).
**Example:** [source#L93993](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L93993) · [#ascii-serialisation-of-an-origin](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#ascii-serialisation-of-an-origin); [source#L94027](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L94027) · [#same-origin](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#same-origin); sites: [source#L94183](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L94183); exposing a string: [source#L125654](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L125654) · [#dom-origin](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-origin)

### `ORIGIN-SAME-ORIGIN-DOMAIN` — "same origin-domain" only for `document.domain`-sensitive access checks
"same origin-domain" takes `document.domain` into account. It is used by cross-origin object
access checks (`IsPlatformObjectSameOrigin`, `Location`); everything else uses "same origin".
**Example:** [source#L94045](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L94045) · [#same-origin-domain](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#same-origin-domain); table: [source#L94071](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L94071); uses: [source#L97171](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L97171) · [#isplatformobjectsameorigin](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#isplatformobjectsameorigin); [source#L99198](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L99198) · [#dom-location-href](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-location-href)

### `ORIGIN-AVOID-SITE` — Prefer "same origin" over "same site"
"the same site and schemelessly same site concepts should be avoided when possible, in favor of
same origin checks." When a site really is needed, "obtain a site" from the origin and compare
with "same site". Port and domain are ignored by both site concepts.
**Example:** [source#L94244](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L94244); [source#L94123](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L94123) · [#obtain-a-site](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#obtain-a-site); [source#L94220](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L94220) · [#same-site](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#same-site); [source#L94239](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L94239)

---

## 5. Event loop and parallelism (`TASK`, `PAR`)

### `TASK-RUNNABLE` — The global or element you pass decides when the task can run
A task is runnable if its document is null or fully active. "queue a global task" sets the task's
document to the global's associated `Document` (for a `Window`). So the task does not run while
that `Document` is not fully active ("if that global object is inactive, the task does not run").
Pass the global whose `Document`'s lifecycle should gate the work, usually <span>this</span>'s
relevant global object, captured before going in parallel.
**Example:** [source#L123155](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L123155) · [#concept-task-runnable](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#concept-task-runnable); [source#L123256](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L123256) · [#queue-a-global-task](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#queue-a-global-task); [source#L124288](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L124288) · [#event-loop-for-spec-authors](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#event-loop-for-spec-authors)

### `TASK-ELEMENT-OR-GLOBAL` — "queue an element task" for work on an element; "queue a global task" otherwise
"queue an element task" is "queue a global task" with the element's relevant global object. Use
it when the steps act on an element (for example firing an event at it); use "queue a global
task" with an explicit global otherwise.
**Example:** [source#L123266](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L123266) · [#queue-an-element-task](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#queue-an-element-task); [source#L123249](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L123249) · [#queue-a-global-task](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#queue-a-global-task)

### `TASK-NO-IMPLIED` — Always supply an event loop and document, or use the wrappers
"Failing to pass an event loop and document to queue a task means relying on the ambiguous and
poorly-specified implied event loop and implied document concepts." Use "queue a global task" or
"queue an element task"; call "queue a task" directly only with both values. This is why bare
"queue a task" is Legacy in `TASK-QUEUE-GLOBAL`.
**Example:** [source#L123242](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L123242) · [#queue-a-task](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#queue-a-task); [source#L124292](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L124292) · [#event-loop-for-spec-authors](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#event-loop-for-spec-authors)

### `TASK-MICROTASK` — Queue microtasks only from the event loop
"queue a microtask" asserts that there is a surrounding agent, that is, that it is not called
from parallel steps. Use a microtask to continue within the current task; from parallel steps,
queue a global task instead.
**Example:** [source#L123279](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L123279) · [#queue-a-microtask](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#queue-a-microtask); [source#L123186](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L123186) · [#microtask](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#microtask)

### `PAR-IN-PARALLEL` — "Run the following steps <span>in parallel</span>:" and the rules inside
Introduce off-main-thread work with a nested block (or inline: "Otherwise, <span>in
parallel</span>, wait for …"). Inside it, touch no JavaScript objects or promises, throw nothing,
and hand results back via `TASK-QUEUE-GLOBAL`.
**Example:** [source#L1602](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1602) · [#starting-a-new-parallel-queue](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#starting-a-new-parallel-queue); inline: [source#L31825](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L31825) · [#dom-img-decode](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#dom-img-decode)

### `PAR-REALM-AGNOSTIC` — Parallel steps operate on realm-agnostic values only
Steps running in parallel cannot access JavaScript objects or Web IDL's <span>this</span>. They
can manipulate Infra values, which are realm-agnostic. Convert inputs to Infra values and capture
the relevant global object before going in parallel. Convert results back inside a queued global
task.
**Example:** [source#L124273](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L124273) · [#event-loop-for-spec-authors](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#event-loop-for-spec-authors); [source#L124277](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L124277); template: [source#L124300](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L124300); capture: [source#L1645](https://github.com/whatwg/html/blob/877d6146487f15b15bc8dd0e3c625063a37b456a/source#L1645) · [#parallelism](https://html.spec.whatwg.org/commit-snapshots/877d6146487f15b15bc8dd0e3c625063a37b456a/#parallelism)

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
