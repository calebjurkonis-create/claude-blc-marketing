---
name: meta-seminar-ad
description: Write a ready-to-load Meta (Facebook/Instagram) ad campaign that fills a Caleb & Moose dinner workshop. Use when Caleb says "make seminar ads", "Meta ads for [venue]", "Facebook ads for the workshop", or gives new seminar dates/venue.
---

# Meta seminar ad

Turns one set of workshop details into a campaign Caleb can paste into Ads Manager. Read `CLAUDE.md` first: voice, disclaimer, and the special-ad-category rules there are mandatory.

## 1. Collect the details
Ask only for what's missing, all at once:
- Venue + address, and the two dates/times (use `[DATE 1]` / `[DATE 2]` placeholders if TBD)
- Meal included? Seat cap?
- Daily budget and how many days before the first night ads should run (default: $25–$40/day, 10–14 days)
- RSVP path: phone call (default, 407-735-6371) and/or Meta instant form

## 2. Campaign setup (write it out as a checklist)
- **Special ad category:** Financial Products & Services. Say so first; it can't be changed after launch.
- **Objective:** Leads → conversion location **Calls** (call button to the RSVP number). Optional second ad set: **Instant form** (name + phone + which night; no age questions; custom question "Which night works best?").
- **Location:** 15-mile radius around the venue (minimum allowed). Note which nearby 55+ communities that radius covers; that's the real age filter.
- **Audience:** Advantage+ / broad. No interests needed; age is locked 18–65+.
- **Placements:** Advantage+ placements. Facebook Feed does the work for this crowd.
- **Schedule:** start 10–14 days out, end at 3 PM on night two. Raise budget ~30% for the final 4 days ("last chance" window).
- **Tracking:** ad name convention `venue_angle_format` (e.g. `grovehouse_penalty_image`) so results map back.

## 3. Write three angles
For each angle give: **primary text** (≤125 chars before "See more", full version ≤500), **headline** (≤40 chars), **description** (≤30 chars), **CTA button** (Call Now / Sign Up), and the disclaimer at the end of primary text.

Default angles (swap if Caleb asks):
1. **The deadline**: the sign-up window opens 3 months before the 65th-birthday month; missing it can mean lifelong penalties.
2. **The choice**: Advantage vs. Supplement, and which fits how you live, travel and see doctors.
3. **The dinner**: a relaxed evening, a local team, bring a guest, no obligation.

Check every line against Meta's personal-attributes policy: no "you're turning 65", "your Medicare", "seniors like you". Talk about the topic, not the reader's traits.

## 4. Creative briefs
For each angle, one image brief and one short-video brief (≤20s, captions on, vertical 4:5). Use real photos of Caleb & Moose and the venue over stock. Big readable type; this audience reads on phones held at arm's length. Reuse mailer look: "FREE DINNER WORKSHOP", venue, dates, "CALL TO RSVP".

## 5. Save + summarize
Save to `seminars/<venue-slug>/meta-ads.md`. End with: what Caleb must do in Ads Manager (in order), the total planned spend, and the break-even math vs. a ~$700 postcard drop (cost per RSVP call to beat).

Never publish, launch or spend. Draft only.
