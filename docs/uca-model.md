# UCA Model (Code Domain)

## File Layout
- Sample knowledge base: `data/uca/code/sample_kb.json`
- Model code: `src/agentspec_codegen/uca/models.py`
- ATT&CK mapping: `src/agentspec_codegen/uca/mitre.py`

## Core Fields
- `uca_id`: stable unique identifier.
- `risk_type`: normalized code-domain risk category.
- `mitre_tactic`: normalized ATT&CK tactic (`exfiltration` or `persistence` in this phase).
- `trigger_event`: AgentSpec trigger event (default code domain uses `PythonREPL`).
- `predicate_hints`: predicate candidates used by the compiler.
- `enforcement`: target enforcement strategy (`stop`, `user_inspection`, etc.).

## Validation Rules
- `domain` must be `code`.
- `uca_id` must be unique in one knowledge-base file.
- `risk_type` and `mitre_tactic` must satisfy the mapping table.

## Extension Rules
- Add new risk categories in `UcaRiskType`.
- Extend `ATTACK_TACTIC_TO_RISKS` for new ATT&CK tactics.
- Add corresponding compiler mapping and tests before enabling in experiments.
