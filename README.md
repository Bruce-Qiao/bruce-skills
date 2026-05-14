# bruce-skills

A collection of [Claude Code](https://claude.com/claude-code) skills written by bruce.

## Skills

- **clarify** — Three-layer thought clarifier (Wittgenstein decomposition → Socratic questioning → Polanyi tacit-knowledge capture). Turns a vague intention into a precise statement plus an AI-ready prompt.

## Installation

```bash
git clone https://github.com/bruce-qiao/bruce-skills.git
cd bruce-skills
./install.sh
```

Then restart Claude Code so it picks up the new skills.

### Manual install

If you prefer to install only specific skills, copy their directories into `~/.claude/skills/`:

```bash
cp -r clarify ~/.claude/skills/
```

## Usage

Each skill is invoked via its slash command inside Claude Code, e.g. `/clarify`. See each skill's `SKILL.md` for details.
