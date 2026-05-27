# Google Stitch MCP (Cursor)

Stitch is configured in **global** Cursor MCP config: `~/.cursor/mcp.json`.

- Server: `stitch-mcp-server` (stdio via `npx`)
- Auth: `STITCH_API_KEY` in the server `env` block
- Official HTTP endpoint (used by the package): `https://stitch.googleapis.com/mcp`

## After changing config

1. **Cursor → Settings → MCP** (or Tools & MCP)
2. Enable **stitch** if it is off
3. **Reload** MCP servers or restart Cursor

## Verify

In MCP panel, **stitch** should show tools enabled (not “Needs authentication”).

## Security

- Do not commit API keys to this repo (see `.gitignore` for `.env`)
- If a key was shared in chat or committed, **rotate it** in [Stitch settings](https://stitch.withgoogle.com)

## Optional: project-only key via environment

```bash
export STITCH_API_KEY="your-key"
```

Then add `.cursor/mcp.json` with `"STITCH_API_KEY": "${env:STITCH_API_KEY}"` if you prefer not to use the global file.
