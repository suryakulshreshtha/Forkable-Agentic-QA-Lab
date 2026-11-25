# 🧠 "Prompt = test case": the philosophy behind the AI-agent layer

Traditional QA validates predefined logic. AI QA validates unpredictable, dynamic output. That shift changes
what "a test case" even means:

| Traditional QA | AI QA |
|---|---|
| Validates predefined logic | Validates unpredictable, dynamic output |
| A test case is written once | A prompt *is* a test case — it's versioned, evaluated, and refined like one |
| Pass/fail is exact-match | Pass/fail is often a graded judgment (relevance, faithfulness, hallucination rate) |
| Bugs are found reactively | Bugs can be predicted and flagged proactively from output patterns |

## The loop this repo mechanizes

```
Prompt → Output → Evaluate → Refine → Repeat
```

Concretely, in this repo:

1. **Prompt** — a versioned prompt template in `src/testgen/prompts/` turns a requirement/user story into a
   test-case-generation request.
2. **Output** — the LLM returns pytest-ready test cases, written into `tests/generated/`.
3. **Evaluate** — the *prompt itself* is evaluated with [DeepEval](https://deepeval.com/) / 
   [Ragas](https://docs.ragas.io/) / [Promptfoo](https://www.promptfoo.dev/) — not just the generated tests,
   but whether the generation prompt reliably produces correct, well-formed cases.
4. **Refine** — a failing evaluation is a signal to revise the prompt template, versioned alongside the code
   (`test_case_prompt.v1.md`, `v2.md`, ...), so the refinement is itself auditable.
5. **Repeat** — this loop runs in CI, the same way the rest of the test suite does.

## Why this matters more than "AI replacing QA"

AI isn't replacing QA engineers — it's shifting the job from writing every test case by hand to **designing
the validation strategy**: which prompts to trust, which outputs need a human-graded rubric versus a
deterministic assertion, and where the automation's own blind spots are. The bug-reporting agent
(`agents/bug_reporter/`) is the same idea applied to the other end of the cycle: automating the reporting
chore so the human time goes to root-cause analysis and exploratory testing instead of re-typing a Jira
ticket.
