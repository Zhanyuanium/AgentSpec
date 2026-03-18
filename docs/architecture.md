# AgentSpec Code Domain Architecture

## Scope
- This stage targets only the code domain.
- Pipeline: STPA/UCA knowledge -> DSL compilation -> runtime enforcement -> evaluation.

## Layered Modules
- `src/agentspec_codegen/uca/`: UCA schema and ATT&CK mapping.
- `src/agentspec_codegen/compiler/`: UCA to AgentSpec rule compiler.
- `src/agentspec_codegen/runtime/`: Runtime context helpers and audit records.
- `scripts/`: dataset and experiment entrypoints.

## Runtime Integration Points
- Existing executor: `src/controlled_agent_excector.py`
- Existing interpreter: `src/interpreter.py`
- Existing enforcement: `src/enforcement.py`
- Predicate registry: `src/rules/manual/table.py`
