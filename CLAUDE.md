# Moss & Mail — Claude Code Standing Rules

---

## ⚠️ MANDATORY SESSION START — DO THIS BEFORE ANYTHING ELSE

Every single session, before responding to any request, Claude MUST run all of these in order:

### Step 1 — Read the source of truth files
- Read `SESSION_STARTER.md`
- Read `MASTER_TASK_LIST.md`
- Read `MOSS_AND_MAIL_MASTER.html` — this is where ALL captions live. Never rewrite captions. Never suggest rewriting captions. They were written by Claude and edited and approved by Kayli. They are final.

### Step 2 — Check live Publer schedule
Run this EVERY session before touching anything in Publer:
```
curl -s "https://app.publer.com/api/v1/posts?limit=100" -H "Authorization: Bearer-API d2b0ecf66cecf5ab91cb4bfb28fe95a3d9c60bac9f675f5b" -H "Publer-Workspace-Id: 69ee4e131454f4622d3ef523"
```
Parse the `posts` key (not `data`). Sort by `scheduled_at`. Show Raquel what's live before doing anything.

### Step 3 — Report discrepancies only
Compare live Publer schedule against the CSVs. Report what's missing, what's extra, what's wrong. Do NOT fix anything until Raquel approves each change one at a time.

---

## ⚠️ CAPTIONS — NEVER REWRITE

ALL captions for ALL videos are in `MOSS_AND_MAIL_MASTER.html`. They were written by Claude, edited by Kayli, and approved. They are final.

- NEVER write new captions for existing videos
- NEVER suggest rewriting existing captions
- NEVER say "I'll write the caption for this" — instead, read the HTML and find it
- If a caption is missing from the HTML, say so and ask Raquel — do not invent one

---

## ⚠️ PUBLER — NEVER TOUCH WITHOUT APPROVAL

- NEVER add, delete, or edit a Publer post without Raquel saying yes to that specific post
- NEVER delete a post because it "looks like a duplicate" without showing Raquel both posts first
- NEVER schedule from memory — always read the live schedule first
- If something looks wrong, describe it and ask. Do not fix it unilaterally.

---

## CONTENT FOLDER — SOURCE OF TRUTH FOR VIDEO FILES

All finished video content is in:
`/Users/raquelcovey/Projects/MossAndMail/Moss & Mail Content FINAL  copy/`
Subfolder with newer content: `more finished content added 5:2/`
Processed/clipped versions: `/Users/raquelcovey/Projects/MossAndMail/clips/`
Book review clips specifically: `/Users/raquelcovey/Projects/MossAndMail/clips/book-review/`

Both iced matcha videos are intentional — schedule both, spaced apart. Do not treat as duplicates.

---

## ⚠️ CSV VERSIONING — MANDATORY EVERY TIME A CSV CHANGES

Every time any Publer CSV is created or updated, Claude MUST:
1. Copy the OLD csv into `/Users/raquelcovey/Projects/MossAndMail/csv-archive/` with the date appended — e.g. `MossAndMail_Publer_Instagram_2026-05-05.csv`
2. Save the NEW csv as the standard filename — e.g. `MossAndMail_Publer_Instagram.csv`
3. Note in SESSION_STARTER.md what changed and when

This allows Publer to be fully restored from the archive if the schedule is ever corrupted.
Archive folder: `/Users/raquelcovey/Projects/MossAndMail/csv-archive/`

---

## BULK SCHEDULING WORKFLOW — HOW IT ACTUALLY WORKS

Claude does NOT upload videos via API. The workflow is:
1. Claude updates the CSV files with new posts (captions from HTML, filenames, dates, alt text)
2. Raquel goes to Publer → Bulk Schedule → uploads the CSV + selects the video files
3. Publer matches filenames and schedules everything automatically

API parse key: responses use `posts` key, not `data`.

---

## SEO: Instagram Alt Text + First 125 Characters

Every Instagram post MUST include:

1. **Alt text on every video/image** — must be added manually in Publer: Edit post → Advanced Settings → Write Alt Text.
   - Formula: `[What is in the video/image] — [keyword phrase] — Moss & Mail`

2. **First 125 characters must contain a keyword**
   - slow living / slow morning / slow recipe
   - matcha / hot chocolate / recipe
   - handwritten letter / snail mail / letter subscription
   - Moss & Mail / mossandmail
   - Charlotte Mason / homeschool
   - intentional living / intentional motherhood

3. **Alt text goes in the CSV** — always populate the `Alt text(s)` column.

---

## END OF EVERY SESSION — REQUIRED CHECKLIST

Before Raquel closes Claude Code or restarts her computer, Claude MUST:
1. Update `MASTER_TASK_LIST.md` — mark completed ✅, add new pending items
2. Update `SESSION_STARTER.md` — reflect current state of everything
3. Update `MOSS_AND_MAIL_MASTER.html` — add any new schedule changes as a log entry
4. Commit all changed files to git
5. Tell Raquel: "Safe to close"

If Raquel says "I'm shutting down" or "should I save anything" — STOP everything and run this immediately.

---

## SCHEDULING RULE — ALWAYS CHECK BEFORE TOUCHING PUBLER

NEVER schedule without first running the Publer API check above and comparing against CSVs.

---

## API Keys

### Publer
Key: d2b0ecf66cecf5ab91cb4bfb28fe95a3d9c60bac9f675f5b
Workspace ID: 69ee4e131454f4622d3ef523
IG Account ID: 69ee548a578cfba22c490081
TikTok Account ID: 69ee5498b7b333b553b35bb2
YouTube Account ID: 69ee5b1ea8efaa444defd05b
Note: Key resets when Publer subscription renews — regenerate from Settings → Access & Login → Manage API Keys

### YouTube Data API
Key: AIzaSyC_ET2j0RKNo-Sr8sHO9hRYQLqP1dKrUxY

### Mailchimp
Key: 4eb88764e24c19d6240b51c94651ca2f-us7
Data center: us7

### Shopify
Shop: moss-mail.myshopify.com
Access token: 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
Product: Snail Mail Club — ID: 8821049327794, Variant ID: 47383030825138, Price: $12.99, Status: draft

---

## Posting Workflow — Alt Text Step
Before any Instagram post publishes:
1. Open Publer → find the post → Edit → Advanced Settings → paste alt text from CSV → Save
