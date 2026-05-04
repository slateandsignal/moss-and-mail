# Moss & Mail — Session Starter
**Paste this at the start of every new Claude Code session.**
Last updated: 2026-05-03 (end of evening session)

---

## Who We Are
- **Raquel** — operations, edits in Canva + EDITS app, schedules all content, manages tools, runs Claude sessions. Creates all thumbnails (has template already built).
- **Kayli Angeleaux** — films footage, reviews/approves copy before it goes out. Hands off everything else. Email: kayli.angeleaux@mossandmail.com
- **Claude** — writes all captions, descriptions, hashtags, builds Shopify, manages API calls, edits website

## The Business
**Moss & Mail** — monthly handwritten letter subscription. Kayli writes a letter by hand, composes it in nature, seals it with wax, and mails it with: a handwritten letter (vulnerable, honest — like a letter from a friend), a curated Spotify playlist QR code, a "Letter to the Editor" Q&A from the community, a nature-inspired journaling prompt, a simple nourishing recipe, and a photo from the mountains OR an original watercolor from Kayli's children (one of a kind). The rest is a surprise — chosen for the season, the month, the mood. Some things come back. Some only come once.

**Launch date: June 8, 2026**
**Website:** mossandmail.com (live, hosted on GitHub Pages)
**GitHub repo:** github.com/slateandsignal/moss-and-mail (account: slateandsignal)
**Site files on Mac:** /Users/raquelcovey/Projects/MossAndMail-Site/ — main file is index.html

---

## Platform Status
| Platform | Status |
|----------|--------|
| Instagram | Live @mossandmail — connected to Publer |
| TikTok | Live @mossandmail — connected to Publer |
| YouTube | Live @mossandmail — connected to Publer |
| Facebook | Handle claimed — NOT connected to Publer yet |
| Pinterest | Handle claimed — connected to Metricool, not Publer |
| Linktree | Live — connected to all active platforms |
| Metricool | Connected: Instagram, TikTok, Pinterest |

---

## Content Schedule — DONE, DO NOT REDO
All posts scheduled in Publer: **May 6 — June 12, 2026**
- Instagram: 19 posts (Reels + Photos)
- TikTok: posts scheduled (May 21 TikTok needs manual add — mason jar clip)
- YouTube Shorts: scheduled manually in Publer UI (API quirk — jobs succeed but don't appear in API list)
- YouTube Long-form: 8 entries in CSV — some need manual upload (838MB unboxing file too large for API)
- CSVs saved at: MossAndMail_Publer_Instagram.csv, MossAndMail_Publer_TikTok.csv, MossAndMail_Publer_YouTube.csv, MossAndMail_Publer_Facebook.csv

**3 Book Review clips scheduled:**
- TikTok: May 21 (mason jar clip) — **NEEDS MANUAL ADD in Publer** (clip1-mason-jar-vertical.mp4)
- Instagram Reel: May 23 (screen realization clip) ✅
- YouTube Short: May 24 (1917 book clip) ✅ — scheduled manually

**YouTube videos updated (May 3 session):**
- Beaver Hike (live): description, tags, affiliate links, cross-link to Book Review, pinned comment with book links ✅
- Book Review (private, scheduled May 27): description, tags, affiliate links, cross-link to Beaver Hike ✅

---

## API Keys & Tools
| Tool | Key / ID |
|------|----------|
| Publer API | 6059e2530c0d00aaf78201d76f970fdf8938eca21d8a01d2 |
| Publer Workspace ID | 69ee4e131454f4622d3ef523 |
| Publer IG Account ID | 69ee548a578cfba22c490081 |
| Publer TikTok Account ID | 69ee5498b7b333b553b35bb2 |
| Publer YouTube Account ID | 69ee5b1ea8efaa444defd05b |
| YouTube Data API | AIzaSyC_ET2j0RKNo-Sr8sHO9hRYQLqP1dKrUxY |
| YouTube OAuth token | /Users/raquelcovey/Projects/MossAndMail/youtube_token.json |
| Mailchimp API | 4eb88764e24c19d6240b51c94651ca2f-us7 (data center: us7) |
| Mailchimp list u= | 0ced347425816f6636ddecf11 |
| Mailchimp list id= | ab002c9324 |
| GitHub token | /Users/raquelcovey/Projects/MossAndMail/.github_token — rotates July 21, 2026 |
| Shopify Admin Token | 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 |
| Shopify Shop | moss-mail.myshopify.com |
| Shopify Product ID | 8821049327794 (Snail Mail Club, $12.99, Draft) |
| Shopify Variant ID | 47383030825138 |

**Note:** Publer API key resets when subscription renews — regenerate from Settings → Access & Login → Manage API Keys

---

## Mailchimp — WORKING
- Account: Standard plan ($13/mo)
- Welcome automation active — subject: "You're on the list — thank you for being here"
- Domain authenticated via GoDaddy (SPF + DKIM) — emails go to inbox, not junk
- Waitlist form on mossandmail.com: **CONFIRMED WORKING** — direct POST to Mailchimp, opens confirmation in new tab. Emails arrive in Mailchimp (tested and confirmed with green checkmark). UX improvement (no new tab) is next session with Formspree.

---

## Shopify — WAITING ON KAYLI
- Store: Moss & Mail (moss-mail.myshopify.com)
- Seal Subscriptions app: installed
- Product created: "Snail Mail Club" — $12.99/month — Status: DRAFT — ID: 8821049327794
- **BLOCKED:** Need Kayli to confirm name ("Snail Mail Club") and price ($12.99/month)
- When confirmed: say "Shopify confirmed" → Claude sets up Seal Subscriptions billing rule, activates Shopify Payments, changes Draft→Active, adds photos

---

## Thumbnails
**Raquel creates all thumbnails** — she has a Canva template already built. Claude does NOT write thumbnail briefs or create thumbnails.

---

## Roles Reminder for Claude
- Write captions, descriptions, hashtags, YouTube titles/tags
- Make Publer API calls to schedule posts
- Edit website (index.html) locally — provide git commands for Raquel to push
- Build Shopify product via API when token is received
- Do NOT upload large video files (838MB+ must be done manually via Publer web UI)
- YouTube Shorts: always schedule manually via Publer Create button (API quirk)
- ALWAYS check Publer before scheduling — run GET /api/v1/posts first to avoid duplicates

---

## Pending — What's Left To Do

### Do first next session:
- [ ] **May 23 Instagram Reel** — add manually in Publer: clip3-screen-realization-vertical.mp4, caption + alt text in MASTER_TASK_LIST.md, 8:00 AM
- [ ] **May 21 TikTok** — confirm video file is actually attached in Publer (caption is there)
- [ ] **Schedule 13 unscheduled videos** — Claude updates CSVs, Raquel bulk imports in Publer (see MASTER_TASK_LIST.md for full list)
- [ ] **Fix email form UX** — Claude replaces Mailchimp POST with Formspree (no new tab)

### Waiting on Kayli:
- [ ] Shopify: confirm name + price → say "Shopify confirmed" → Claude finishes
- [ ] Google Business verification: Kayli films 3-minute video
- [ ] Launch day video (June 8): needs to be filmed
- [ ] Review video (June 12): needs to be filmed

### Raquel manual:
- [ ] Alt text: add to all scheduled Publer posts (text is in CSVs)
- [ ] Delete 2 test posts in Publer (June 30 dates)
- [ ] Facebook: connect to Publer when ready
- [ ] YouTube long-form unboxing (838MB): upload manually via Publer Media Library
- [ ] Frame.io: set up (~$15/mo) for Raquel + Kayli footage sharing

---

## Brand Colors
Moss #889063 | Plum #481827 | Ivory #EBE2CF | Blush #E0A399 | Daffodil #FFDE7A | Coral #81666B

## CRITICAL — Before Every Publer Scheduling Session
Check what already exists in Publer BEFORE scheduling anything. Run:
`curl -s "https://app.publer.com/api/v1/posts?limit=100" -H "Authorization: Bearer-API 6059e2530c0d00aaf78201d76f970fdf8938eca21d8a01d2" -H "Publer-Workspace-Id: 69ee4e131454f4622d3ef523"`
Compare against CSV before adding anything. Duplicates require manual cleanup.

## Notes for Claude
- Raquel is non-technical — walk through new tools completely, step by step
- Always use Kayli's voice and language for copy — never generic subscription box language
- First 125 chars of every Instagram caption must contain a searchable keyword (see CLAUDE.md)
- Publer API auth format: `Authorization: Bearer-API {key}` — NOT standard Bearer
- GitHub API is network-blocked from Claude's sandbox — edit files locally, give Raquel git commands to run
- Canva connected: R.C Designs account (Apple private relay email)
- Competitor: "Moss & Moon Mail" by Maureen Miller on Facebook (~300 followers, not a major threat)
