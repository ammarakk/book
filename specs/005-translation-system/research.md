# Research: Translation System (English ↔ Urdu)

## Decision: Claude Code Subagent Architecture for Translation
**Rationale**: Using Claude Code Subagents with specialized agent skills to handle the translation between English and Urdu while preserving technical accuracy. This approach allows for rule-based, deterministic translations that maintain technical terminology and code blocks.

**Alternatives considered**:
- Google Cloud Translation API: Might not preserve technical terminology adequately
- OpenAI GPT models: Less control over deterministic output required for technical content
- Custom neural translation model: Would require extensive training data and maintenance

## Decision: Frontend Translation Component Architecture
**Rationale**: Creating a React-based translation toggle component that can be integrated into the Docusaurus documentation pages. This allows for dynamic content switching while maintaining visual distinction between original and translated content.

**Alternatives considered**:
- Server-side rendering: Would complicate caching and increase latency
- Static generation: Would not allow real-time toggling between languages
- Iframe embedding: Would create styling and integration challenges

## Decision: Session-Based Translation Caching
**Rationale**: Implementing translation as a session-based feature that caches results temporarily during the user's session. This reduces API calls to the Claude Code Subagent while ensuring original content remains immutable.

**Alternatives considered**:
- Permanent storage: Would violate the requirement to keep original content unchanged
- No caching: Would result in slower performance and higher API costs
- Browser storage only: Less secure and limited storage capacity

## Decision: Technical Term Preservation Strategy
**Rationale**: Using a combination of Claude Code Subagent prompting and post-processing to ensure technical terms (ROS 2, SLAM, URDF, Isaac Sim, etc.) remain unchanged during translation. This preserves the educational value of the content.

**Alternatives considered**:
- Regex replacement: Might miss context-dependent terms
- Dictionary lookup: Would require maintaining extensive technical term database
- Manual exclusion lists: Would be difficult to maintain and scale

## Decision: Code Block Protection Mechanism
**Rationale**: Implementing a system that identifies and protects code blocks from translation by passing them through unchanged. This ensures code examples remain functional regardless of the language of surrounding text.

**Alternatives considered**:
- Language detection: Would add complexity and potential errors
- Manual markup: Would require modifying original content, violating immutability requirement
- Post-translation restoration: Would be complex to match translated blocks with originals