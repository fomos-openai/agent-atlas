import assert from "node:assert/strict";
import test from "node:test";
import {decide, type ToolCall, type ToolSpec} from "../src/contracts.ts";

const base: ToolCall = {id: "c1", toolName: "submit", arguments: {proposalId: "p1"}, idempotencyKey: "k1"};

test("external commitment requires approval", () => {
  const spec: ToolSpec = {name: "submit", description: "submit proposal", required: ["proposalId"], sideEffect: "external_commitment"};
  assert.equal(decide(base, spec).kind, "require_approval");
});

test("missing required argument fails closed", () => {
  const spec: ToolSpec = {name: "submit", description: "submit proposal", required: ["owner"], sideEffect: "read"};
  assert.equal(decide(base, spec).kind, "deny");
});

test("high impact is not exposed as an approvable shortcut", () => {
  const spec: ToolSpec = {name: "modify", description: "modify production", required: [], sideEffect: "high_impact"};
  assert.equal(decide({...base, toolName: "modify"}, spec).reasonCode, "HIGH_IMPACT_FORBIDDEN");
});
