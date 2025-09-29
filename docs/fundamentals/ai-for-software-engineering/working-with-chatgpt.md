# Working with ChatGPT

ChatGPT is versatile for reasoning about code, generating documentation, and brainstorming. It excels at producing structured text outputs, explanations, and design drafts that you can refine.

## Responsible usage

- **Avoid exposing sensitive data**: Redact or abstract confidential code.
- **Test all suggestions**: Treat outputs as unverified drafts.
- **Use in combination with tooling**: Pair responses with linters, profilers, and CI tests.

## How to ask good questions

- Be specific: Provide context (language, framework, constraints).
- Break problems into smaller steps.
- Show your work (e.g., “Here’s my code + error message” rather than “It doesn’t work”).

💡 Example:

```text
I’m working in Python 3.11 with FastAPI. This async function throws "RuntimeError: event loop is closed."
Here’s the code: <snippet>. Can you suggest fixes and explain why it fails?
```

## Prompt strategies

#### Targeted improvements

```text
Act as a senior reviewer. Here is a function. Suggest minimal changes to improve readability and add type hints.
```

#### Explaining codebases

```text
Summarize this module in 6 bullet points. Identify assumptions, complexity hotspots, and missing test cases.
```

#### Review support

```text
Here is a diff. Review for correctness, performance, and security. Respond as a checklist.
```

#### Design assistance

```text
Draft a one-page design doc for <feature>. Include context, goals, trade-offs, and a basic test strategy.
```

## Best practices for developers

- Use ChatGPT to **learn patterns** (why something works) rather than just solutions.
- Pair it with your IDE’s IntelliSense, type checker, and debugger.
- Always keep a “scratchpad” or test repo for experimenting with generated code.

## When to limit usage

- **Critical algorithms**: AI cannot replace formal verification or proofs.
- **Compliance-heavy environments**: Code provenance must be clear.
- **Opaque suggestions**: If you cannot reason about the output, avoid adopting it.


