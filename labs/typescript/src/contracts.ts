export type SideEffect = "read" | "reversible_write" | "external_commitment" | "high_impact";
export type PolicyKind = "allow" | "deny" | "require_approval";

export interface ToolSpec { name: string; description: string; required: string[]; sideEffect: SideEffect }
export interface ToolCall { id: string; toolName: string; arguments: Record<string, unknown>; idempotencyKey: string }
export interface PolicyDecision { kind: PolicyKind; reasonCode: string }

export function decide(call: ToolCall, spec: ToolSpec): PolicyDecision {
  const missing = spec.required.filter((key) => !(key in call.arguments));
  if (missing.length) return {kind: "deny", reasonCode: "INVALID_ARGUMENTS"};
  if (spec.sideEffect === "high_impact") return {kind: "deny", reasonCode: "HIGH_IMPACT_FORBIDDEN"};
  if (spec.sideEffect === "external_commitment") return {kind: "require_approval", reasonCode: "EXTERNAL_COMMITMENT"};
  return {kind: "allow", reasonCode: "LOW_RISK"};
}
