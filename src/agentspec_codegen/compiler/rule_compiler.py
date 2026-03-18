from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from agentspec_codegen.uca.models import UcaEntry, UcaKnowledgeBase, UcaRiskType


DEFAULT_PREDICATE_BY_RISK = {
    UcaRiskType.UNTRUSTED_POST_REQUEST: ["submit_post_request", "request_untrusted_source"],
    UcaRiskType.NETWORK_EXFILTRATION: ["encode_data", "write_to_io"],
    UcaRiskType.SENSITIVE_DATA_LEAK: ["read_io", "write_to_io"],
    UcaRiskType.STARTUP_FILE_TAMPER: ["write_to_io", "involve_system_file"],
    UcaRiskType.BASHRC_ALIAS_BACKDOOR: ["write_to_io", "involve_bash_rc"],
    UcaRiskType.PRIVILEGE_RETENTION: ["execute_script", "involve_system_file"],
}


@dataclass(frozen=True)
class CompilationArtifact:
    rule_id: str
    uca_id: str
    spec_text: str
    predicates: list[str]


def _normalize_rule_id(uca_id: str) -> str:
    return uca_id.lower().replace("-", "_")


def _resolve_predicates(entry: UcaEntry) -> list[str]:
    if entry.predicate_hints:
        return entry.predicate_hints
    return DEFAULT_PREDICATE_BY_RISK[entry.risk_type]


def compile_entry(entry: UcaEntry) -> CompilationArtifact:
    rule_id = _normalize_rule_id(entry.uca_id)
    predicates = _resolve_predicates(entry)
    checks = "\n".join(f"    {name}" for name in predicates)
    spec_text = (
        f"rule @{rule_id}\n"
        f"trigger\n"
        f"    {entry.trigger_event}\n"
        f"check\n"
        f"{checks}\n"
        f"enforce\n"
        f"    {entry.enforcement}\n"
        f"end\n"
    )
    return CompilationArtifact(rule_id=rule_id, uca_id=entry.uca_id, spec_text=spec_text, predicates=predicates)


def compile_knowledge_base(knowledge_base: UcaKnowledgeBase) -> list[CompilationArtifact]:
    return [compile_entry(entry) for entry in knowledge_base.entries]


def write_compiled_rules(artifacts: list[CompilationArtifact], output_dir: str | Path) -> list[Path]:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for artifact in artifacts:
        path = output / f"{artifact.rule_id}.spec"
        path.write_text(artifact.spec_text, encoding="utf-8")
        written.append(path)
    return written
