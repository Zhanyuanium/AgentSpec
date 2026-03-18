# Rule Compiler (UCA -> AgentSpec DSL)

## Purpose
- Convert validated UCA entries into deterministic AgentSpec `.spec` rules.
- Keep generation stable for regression and golden-file testing.

## Input
- `UcaKnowledgeBase` from `src/agentspec_codegen/uca/models.py`.

## Output
- `CompilationArtifact` list:
  - `rule_id`
  - `uca_id`
  - `predicates`
  - `spec_text`

## Mapping Strategy
- Prefer `predicate_hints` from UCA entry.
- Fallback to risk-category defaults in `DEFAULT_PREDICATE_BY_RISK`.
- Rule ID normalization: `UCA-CODE-001` -> `uca_code_001`.

## Regression Safety
- Golden snapshot in `tests/golden/`.
- Generated rule must parse with existing `Rule.from_text`.
