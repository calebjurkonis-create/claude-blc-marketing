# Caleb & Moose — Seminar Marketing Workspace

## Working rule (always)
Before executing any request, play it back: what you plan to do, ideas to make it better, and a tightened version of the prompt. Wait for a go-ahead. Answers to your own questions count as the go-ahead for the plan already on the table.

**Standing permission: design edits (Caleb, 2026-10-26).** Once a design plan is approved, edit and save Canva designs without asking again: no separate "OK to save?" step. Show the finished result afterward. This covers editing and saving designs in the Caleb & Moose folder. It does not cover deleting designs, publishing ads, or spending money; those still need Caleb's OK.

## Who we are
- **Caleb Jurkonis** and **Mustaf "Moose" Grajqevci** — licensed insurance agents (Bankers Life), Clermont / The Villages, FL. In ads, use plain names: no "CLTC" or other designations.
- Put **Caleb & Moose's faces** on the ads (headshots now, event photos once they exist). They are the brand; the trust is in the two of them.
- "A local team with nearly 15 years of experience, serving more than 1,700 households right here in our community."
- Caleb: married to Emerson, 3 sons, from Franklin TN, former PGA Head Golf Professional. Moose: married to Dresha, 3 sons, born in Kosovo, raised in West Michigan, licensed investment advisor & fiduciary.

## The offer
**Free lunch or dinner workshop: "Medicare, Social Security, & Extended Care Workshop."** Complimentary meal for you + a guest. Always ask which meal and time; it changes every headline. Goal of every workshop: **book personal consultations (sales appointments).**

Agenda (from the deck `Caleb-Moose_Seminar_2027` in Google Drive):
1. Medicare made simple: Parts A, B, C, D and exactly when to sign up
2. Advantage vs. Supplement: which fits how you live, travel, see doctors
3. Social Security timing: the "Decade of Decisions" (62 / 65 / 67 / 70)
4. Extended care: protecting savings, home, and spouse

## Audience
- Primary: **turning 65 soon (T65)**, Central Florida, especially The Villages. Couples are common (the meal is for "you + a guest").
- Secondary: already on Medicare and re-thinking coverage; Social Security filers 62–70.
- Their worries: missing the sign-up window and lifetime penalties, Advantage networks/pre-approvals, surprise costs, long-term care draining savings, irreversible Social Security decisions.

## Voice
- Warm, neighborly, plain English. "Let's make Medicare simple." Teach, don't pitch.
- Light and a little playful ("Not-so-fun fun fact", "with some goodies too!") but never cute about money or health.
- Short sentences. Concrete numbers over adjectives. No jargon without a one-line explanation.
- Never: fear-mongering, "FREE!!!" spam energy, fake urgency, guarantees, "best plan" claims.

## Venues & logistics
- **The Grove House**, 810 Marilee Pl, The Villages, FL 32163 (formerly Sawgrass Tavern). Meal included. Formats used: two dinners at 6:00 PM (e.g. Tue + Fri) or two lunches at 12:00 PM (Nov 2026: Sat 11/14 + Mon 11/16).
- Past venues: Sawgrass Tavern, Giordano's, American Social, Harvest, Tampa.
- **RSVP: call 407-735-6371** (Google Voice). Seating is limited; "RSVP early to save your seats."
- Direct mail: 6x9 postcards via Panther Printing (Chad), ~1,000 pieces, ~$600–$780 per drop, plus a "Last Chance" follow-up card.

## Rules for every ad, mailer, email or text
- Always include: *"Not connected with or endorsed by the U.S. government or the federal Medicare program. Presented by licensed insurance agents. No obligation to enroll."*
- **Meta ads run under the Financial Products & Services special ad category** (insurance). That means: no age targeting (18–65+ fixed), 15-mile minimum radius, no ZIP targeting, no lookalikes, and instant forms can't ask age. **The creative and the location do the targeting**, not the audience settings.
- **Meta personal-attributes policy:** never assert or imply the reader's age, health, or finances. ✗ "Are you turning 65?" / "Your Medicare options" → ✓ "A free dinner workshop for anyone approaching 65" / "Medicare at 65, made simple."
- Never send emails or texts, publish ads, or spend money. Draft only; Caleb sends and launches.
- Never put client names, commissions, or mailing-list data into ad copy or this repo.

## Where things live
- `.claude/skills/` — reusable skills (`meta-seminar-ad`, `seminar-followup`).
- `seminars/<venue>/` — one folder per seminar: ads, follow-up, results.
- `MEMORY.md` — running log of results and decisions.
- **Seminar Tracker** (Google Sheet, ID `1bgtSi9PC-Ra-JDUYlSBvNZhKAB44R0B3PuuGyb7l_cg`) — one row per seminar on the Seminars tab (blue = typed inputs, yellow = still to fill in); Dashboard tab calculates cost per RSVP/appointment, commission payback and the Meta target. **Rates** tab holds Caleb's commission averages (from the Bankers Life FL schedule, agent-only). Sales go in as counts in the columns after Notes (F/M Plan N/G, MAPD new/switch, annuities, LTC/life); commission and policies sold calculate. Commission dollars and the schedule live **only in the Sheet**, never in this repo (the schedule is marked agent-only). After every seminar, add a row there.
- **Postcards** — `seminars/grove-house/mailer-nov/`: `postcard.template.html` + `build.py` → `postcard-A.pdf` / `postcard-B.pdf` (print-ready 9.25×6.25 in with bleed, same layout as the Oct card Panther printed; render with `node render.js`). Two headline versions, "CARD A/B" printed above the address panel, QR to the RSVP site. For the next seminar, change dates/meal in the template and rebuild.
- **Nov RSVPs tab** in the Seminar Tracker: one row per RSVP; checkboxes for each text; "Next step" column says who needs a text or call today; text scripts at the right.
- **Canva folder "Caleb & Moose Seminar Ads"** (`FAHZDvCn8w8`) — ad images; Caleb shares it with Moose to edit together.
- **RSVP website** (Canva design "Caleb & Moose RSVP website", `DAHZFAoyUAY`, in the folder above): 3 sections (ad hero, what we'll cover + RSVP buttons, meet your hosts). Call buttons link to `tel:+14077356371`; "RSVP Online" links to the Google Form https://forms.gle/CHd8XdhEEyJr5EU38 (spec in `seminars/grove-house/rsvp-form.md`). Caleb publishes it from Canva (free `.my.canva.site` address).
- `index.html` — the Claude Marketing course pack this setup is based on.

## Connectors (decided 2026-10-26)
- **Google Drive / Sheets / Docs / Gmail** — files, tracker, drafts (Gmail = drafts only).
- **Google Calendar** (`calebjurkonis@gmail.com`) — read open times for consultation offers; never create or change events without asking.
- **Canva** — ad creatives, built in the folder above. Dates stay as editable text.
- **Meta ads: shelved (Caleb, 2026-10-26).** November lunches go by mail. The website campaign was deleted, and the **"Caleb & Moose : Medicare & Retirement Workshops" Facebook page** (`1437082039478315`) is being **deactivated, not deleted**, so it can be switched back on. If Meta comes back: Adspirer, ad account `1399197117057223`, free tier 15 actions/month, any campaign it creates must be **PAUSED**; ad plan and copy in `seminars/grove-house/meta-ads.md`. The Page "Caleb Jurkonis - Bankers Life" (`465420126651073`) is not used for seminar ads.
- **RSVP website QR code:** `brand/rsvp-website-qr.png` (points to `https://otter-k66vr8.my.canva.site/`) for postcards.
- **Not used:** Calendly (Caleb's call), Supabase (the Google Sheet does that job), Zillow.
