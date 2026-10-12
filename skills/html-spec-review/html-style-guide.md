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

## Files

The rules are split into three files by concern. Rule IDs are unique across all of them, so
`grep` this directory for an ID to find it.

| File | Covers | Prefixes |
|---|---|---|
| [html-style-formatting.md](html-style-formatting.md) | Source layout and Wattsi markup: wrapping, ids, cross-reference and `<dfn>` markup, blocks, IDL, element definitions, Developer's Edition | `SRC`, `HDR`, `XREF`, `DFN`, `BLK`, `CODE`, `IDL`, `ELEM`, `DEV`, `EVT` |
| [html-style-authoring.md](html-style-authoring.md) | How algorithms and prose are written: naming, steps, control flow, variables, values, IDL member prose, tasks and events, exceptions, promises, conformance language, vocabulary | `DFN`, `ALG`, `FLOW`, `VAR`, `VAL`, `STATE`, `CALL`, `API`, `TASK`, `EVT`, `EXC`, `PROM`, `CONF`, `PRS`, `VOC` |
| [html-semantics.md](html-semantics.md) | Which concept to use: documents, navigables, realms and settings objects, origins, the event loop, parallelism | `DOC`, `NAV`, `ENV`, `CALL`, `ORIGIN`, `TASK`, `PAR`, `VOC` |

## Rule index

| Prefix | File | Rules |
|---|---|---|
| `SRC` | [html-style-formatting.md](html-style-formatting.md) | `SRC-WRAP-100`, `SRC-INDENT-BLOCK`, `SRC-WRAPPER-NO-INDENT`, `SRC-LI-P`, `SRC-DD-P`, `SRC-BLANK-BEFORE-HEADING`, `SRC-END-TAGS`, `SRC-ATTR-QUOTES`, `SRC-WATTSI-ATTRS`, `SRC-COMMENTS`, `SRC-ENTITIES`, `SRC-REF-PLACEMENT`, `SRC-REFERENCES-ENTRY`, `SRC-DEPENDENCIES-ENTRY` |
| `HDR` | [html-style-formatting.md](html-style-formatting.md) | `HDR-SENTENCE-CASE`, `HDR-ELEMENT-HEADING`, `HDR-SECTION-NAMES`, `HDR-EXPLICIT-ID`, `HDR-ALIAS-ANCHOR`, `HDR-EN-GB-ALIAS`, `HDR-PARAGRAPH-IDS`, `HDR-ABSTRACT-OP-HEADING` |
| `XREF` | [html-style-formatting.md](html-style-formatting.md) | `XREF-SPAN-AUTOLINK`, `XREF-CODE-ELEMENT`, `XREF-CODE-ATTR`, `XREF-CODE-DOM`, `XREF-CODE-EVENT`, `XREF-CODE-HTTP`, `XREF-CODE-IDL-JS`, `XREF-STRING-LITERAL`, `XREF-I-STATES`, `XREF-THIS`, `XREF-INTERNAL-LINK` |
| `DFN` | [html-style-formatting.md](html-style-formatting.md) | `DFN-TYPED`, `DFN-DATA-X-PLACEMENT`, `DFN-FOR-VALUES`, `DFN-EXPORT`, `DFN-EXPLICIT-ID` |
| `DFN` | [html-style-authoring.md](html-style-authoring.md) | `DFN-ALGORITHM-NAMES`, `DFN-CONCEPT-NAMES`, `DFN-NO-FLAGS`, `DFN-STRUCT`, `DFN-WORD-AS-WORD` |
| `BLK` | [html-style-formatting.md](html-style-formatting.md) | `BLK-NOTE`, `BLK-EXAMPLE`, `BLK-WARNING`, `BLK-CRITICAL`, `BLK-XXX`, `BLK-SWITCH`, `BLK-BRIEF-LIST`, `BLK-HR`, `BLK-DOMTREE`, `BLK-FIGURE`, `BLK-TABLE` |
| `CODE` | [html-style-formatting.md](html-style-formatting.md) | `CODE-PRE-CLASS`, `CODE-ESCAPE`, `CODE-EXAMPLE-DOC`, `CODE-HIGHLIGHT`, `CODE-BAD` |
| `IDL` | [html-style-formatting.md](html-style-formatting.md) | `IDL-BLOCK`, `IDL-XREF-SPAN`, `IDL-EXTENDED-ATTRS`, `IDL-REFLECT-IN-IDL`, `IDL-GENERICS`, `IDL-DICTIONARY`, `IDL-ENUM-VALUES`, `IDL-CONSTRUCTOR`, `IDL-COMMENTS`, `IDL-PARTIAL-OBSOLETE`, `IDL-EVENT-HANDLERS` |
| `ELEM` | [html-style-formatting.md](html-style-formatting.md) | `ELEM-DL-ELEMENT`, `ELEM-REPRESENTS`, `ELEM-ATTR-DEFINITION`, `ELEM-BOOLEAN-ATTR`, `ELEM-ENUMERATED-ATTR`, `ELEM-DOMINTRO` |
| `DEV` | [html-style-formatting.md](html-style-formatting.md) | `DEV-W-NODEV`, `DEV-W-DEV` |
| `ALG` | [html-style-authoring.md](html-style-authoring.md) | `ALG-DIV-ALGORITHM`, `ALG-PREAMBLE`, `ALG-PARAM-TYPES`, `ALG-OPTIONAL-ARGS`, `ALG-RETURN-SENTENCE`, `ALG-ASSERT`, `ALG-VAR-SCOPE`, `ALG-NESTED-STEPS`, `ALG-HOOKS`, `ALG-ES-ABSTRACT-OPS`, `ALG-NON-NORMATIVE-NOTES` |
| `FLOW` | [html-style-authoring.md](html-style-authoring.md) | `FLOW-IF-THEN`, `FLOW-IF-BLOCK`, `FLOW-OTHERWISE`, `FLOW-TERNARY`, `FLOW-ANY-ALL`, `FLOW-RETURN`, `FLOW-SWITCH`, `FLOW-FOR-EACH`, `FLOW-WHILE`, `FLOW-LABELS-LEGACY`, `FLOW-WAIT`, `FLOW-INCREMENT` |
| `VAR` | [html-style-authoring.md](html-style-authoring.md) | `VAR-LET-SET`, `VAR-CAMELCASE`, `VAR-SHORT-NAMES`, `VAR-POSSESSIVE`, `VAR-THIS`, `VAR-MARKUP` |
| `VAL` | [html-style-authoring.md](html-style-authoring.md) | `VAL-LIST-LITERAL`, `VAL-LIST-OPS`, `VAL-MAP-OPS`, `VAL-DICT-ACCESS`, `VAL-STRUCT-ITEMS`, `VAL-BOOLEANS`, `VAL-NULL`, `VAL-EMPTY-STRING`, `VAL-CODE-POINTS`, `VAL-STRINGS`, `VAL-COMPARISONS`, `VAL-NUMBERS`, `VAL-ENUM-STATES` |
| `STATE` | [html-style-authoring.md](html-style-authoring.md) | `STATE-DECLARATION`, `STATE-INITIAL-VALUE`, `STATE-OWNER-PHRASE`, `STATE-INTERNAL-SLOT`, `STATE-DFN-FOR` |
| `CALL` | [html-style-authoring.md](html-style-authoring.md) | `CALL-CONJUGATED`, `CALL-GIVEN`, `CALL-STEPS-AS-VALUES`, `CALL-IMPERATIVE` |
| `CALL` | [html-semantics.md](html-semantics.md) | `CALL-RELEVANT-OBJECTS` |
| `API` | [html-style-authoring.md](html-style-authoring.md) | `API-STEPS-FORM`, `API-CONSTRUCTOR-STEPS`, `API-REFLECT-SENTENCE`, `API-MEMBER-DFN-ORDER`, `API-ARGUMENTS` |
| `TASK` | [html-style-authoring.md](html-style-authoring.md) | `TASK-QUEUE-GLOBAL`, `TASK-SOURCES` |
| `TASK` | [html-semantics.md](html-semantics.md) | `TASK-RUNNABLE`, `TASK-ELEMENT-OR-GLOBAL`, `TASK-NO-IMPLIED`, `TASK-MICROTASK` |
| `PAR` | [html-semantics.md](html-semantics.md) | `PAR-IN-PARALLEL`, `PAR-PARALLEL-QUEUE`, `PAR-EVENT-LOOP-LEGACY`, `PAR-REALM-AGNOSTIC` |
| `EVT` | [html-style-authoring.md](html-style-authoring.md) | `EVT-FIRE`, `EVT-INIT-ATTRS` |
| `EVT` | [html-style-formatting.md](html-style-formatting.md) | `EVT-DFN-EVENT` |
| `EXC` | [html-style-authoring.md](html-style-authoring.md) | `EXC-THROW-DOMEXCEPTION`, `EXC-RETHROW` |
| `PROM` | [html-style-authoring.md](html-style-authoring.md) | `PROM-CREATE`, `PROM-SETTLE`, `PROM-REACT` |
| `CONF` | [html-style-authoring.md](html-style-authoring.md) | `CONF-RFC2119`, `CONF-IMPERATIVE-STEPS`, `CONF-NON-NORMATIVE-MARKER`, `CONF-EXPECTED`, `CONF-WILLFUL-VIOLATION`, `CONF-TRACKING-VECTOR`, `CONF-SECURITY-PRIVACY` |
| `PRS` | [html-style-authoring.md](html-style-authoring.md) | `PRS-QUOTES`, `PRS-DASH`, `PRS-LATIN-ABBREV`, `PRS-SERIAL-COMMA`, `PRS-AMERICAN`, `PRS-CONTRACTIONS`, `PRS-EMPHASIS`, `PRS-PLURALS`, `PRS-CITE-SPEC`, `PRS-PARENTHETICAL` |
| `VOC` | [html-semantics.md](html-semantics.md) | `VOC-NAVIGABLE`, `VOC-FULLY-ACTIVE`, `VOC-SAME-ORIGIN` |
| `VOC` | [html-style-authoring.md](html-style-authoring.md) | `VOC-AUTHORS-DEVELOPERS`, `VOC-USER-AGENT`, `VOC-JAVASCRIPT`, `VOC-WEB-CASING`, `VOC-IS-SAID-TO`, `VOC-INFRA-TERMS` |
| `DOC` | [html-semantics.md](html-semantics.md) | `DOC-ACTIVE-VS-FULLY-ACTIVE`, `DOC-WHICH-DOCUMENT`, `DOC-NULL-BROWSING-CONTEXT`, `DOC-CONNECTED`, `DOC-ORIGIN-NOT-URL`, `DOC-WINDOW-REUSE` |
| `NAV` | [html-semantics.md](html-semantics.md) | `NAV-AVOID-BROWSING-CONTEXT`, `NAV-DEFINED-ACCESSORS`, `NAV-SESSION-ENTRIES`, `NAV-TOP-LEVEL` |
| `ENV` | [html-semantics.md](html-semantics.md) | `ENV-PICK-BY-PURPOSE`, `ENV-RELEVANT-BY-DEFAULT`, `ENV-NO-ENTRY-INCUMBENT`, `ENV-WINDOW-ONLY`, `ENV-URL-BASE`, `ENV-SECURE-CONTEXT` |
| `ORIGIN` | [html-semantics.md](html-semantics.md) | `ORIGIN-WHICH-ORIGIN`, `ORIGIN-COMPARE-ORIGINS`, `ORIGIN-SAME-ORIGIN-DOMAIN`, `ORIGIN-AVOID-SITE` |

---

## About this guide

Rules were derived from the full `source` text, weighted toward the forms that dominate text
added or edited in the last two years and that editors ask for in review; branch ordering follows
that weighting. Links are pinned to commit `877d6146487f15b15bc8dd0e3c625063a37b456a`; to
refresh them, re-derive the line numbers against a newer commit and swap the SHA in the
`github.com/whatwg/html/blob/…` and `commit-snapshots/…` URLs.
