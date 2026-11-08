# Outreach: getting paid for statistics and code reproducibility review

Research date: 2026-11-08 (all URLs below were loaded on that date unless marked otherwise).
Audience: Sahil, before contacting the ERROR team and the other outlets.
Wording rule for all correspondence and reports: describe discrepancies as "reported vs recomputed", never as misconduct.

Repo state (2026-11-08, 04:20 EST): pushed to https://github.com/SahilAujla/papercheck (origin main). The repository is private until Sahil makes it public; the email below links to it, so make it public before sending.

## 1. What ERROR says about reviewers

ERROR (University of Bern, Psychology of Digitalisation lab, Malte Elson) describes itself as a program to "systematically detect and report errors in scientific publications", "modelled after bug bounty programs in the technology industry". Funded by the University of Bern's "Humans in Digital Transformation" program; the homepage shows "250'000 CHF" under "Total Payouts". Initial rollout is in psychology ("journals of psychology and preprint servers"), with planned expansion to "other social sciences".
Sources: https://error.reviews (checked 2026-11-08), https://error.reviews/about/ (checked 2026-11-08).

### Eligibility and how reviewers are chosen

- Reviewers are invited, not self-appointed. The reviewer FAQ says reviewers are recruited for their technical or domain expertise, "similar to pre-publication peer review". Once authors agree, "the recommender finds a reviewer with suitable expertise". https://error.reviews/faq_reviewers/ (checked 2026-11-08), https://error.reviews/faq_general/ (checked 2026-11-08).
- There is no formal eligibility list (no degree or affiliation requirement is stated anywhere on the site). The route to express interest is the "Become a reviewer" page: "If you would like to participate in ERROR as a reviewer, let us know!" ERROR is building "a database of interested experts" to contact "when a suitable candidate paper is found". The page asks you to read the reviewer FAQ first. https://error.reviews/become-a-reviewer/ (checked 2026-11-08).
- The sign-up form is hosted on formr: https://errorsignup.formr.org/ (checked 2026-11-08, loads). Fields seen in the page source: your name, your email address, "The city and country in which you currently reside", "What's your highest attained education level?" (radio options: university bachelor, vocational or university master level, university master level, university doctorate, habilitation, other), disciplines, topic expertise, and further items that follow. The education question is informational; nothing on the site says a doctorate is required.
- Authors "can raise concerns about a potential reviewer's suitability", which the recommender weighs. https://error.reviews/faq_authors/ (checked 2026-11-08).
- Plain reading: you do not apply for a specific paper. You register in the expert database and wait to be matched. The realistic route for a non-academic is (a) fill in the formr sign-up with "statistics, computational reproducibility, code re-execution" as topic expertise, and (b) email the team directly offering to be on the roster for statistics and code checks, ideally paired with a domain expert. Science reported that ERROR cannot find enough reviewers (see below), so a credible, specific offer has a real chance.

### Payment structure

From https://error.reviews/participation/ (checked 2026-11-08):

- Base payment to the reviewer: "250-1,000 CHF, depending on expected effort". Base payment to authors: 250 CHF.
- Reviewer bonus, "depending on error severity", 250 to 2,500 CHF:

| Outcome | Recommended action | Indicative bonus |
|---|---|---|
| No errors | Publish report and reply | 250 CHF to author(s) |
| Minor errors | Authors acknowledge errors in future discussions | 250 CHF to author(s) and reviewer |
| Indeterminable | Authors acknowledge the lack of verifiability | 250 CHF to reviewer |
| Moderate errors | Minor correction notice | 500 CHF to reviewer |
| Major errors | Major correction notice, possible expression of concern | 1,000 CHF to reviewer |
| Severe errors | Retraction | 2,500 CHF to reviewer |

- Caveats on the page: values are "indicative" and decided case by case; a sliding schedule applies by complexity; amounts "will be scaled for regional differences"; "numerous 'minor' errors might constitute a moderate error in aggregate"; most published research is expected to land in the minor-errors category.
- Non-cash benefit: project leadership will write "meta" papers summarising findings, and all participating authors and reviewers are invited to co-author them as a consortium, listed alphabetically. The reviewer FAQ also frames being listed as "a visible commitment to scientific rigour".

### Process (who nominates, timeline, what the reviewer delivers)

From https://error.reviews/faq_general/ and https://error.reviews/faq_reviewers/ and https://error.reviews/faq_authors/ (all checked 2026-11-08):

1. A recommender (works "like an editor in peer review") selects an article. Articles are chosen for their importance in their field. Authors can also self-nominate by contacting ERROR.
2. Authors are invited; the process continues only if they agree. Authors must share "data, code, and other materials with the recommender and the reviewer" and answer reasonable questions.
3. The recommender finds a reviewer with suitable expertise. Reviewers have broad latitude to check any error type they consider appropriate.
4. The reviewer writes a report with two mandatory sections: "Error checking" and "Other critique". The report "must document the checks performed and the results, so that others can verify them", and the reviewer must supply the data, code and materials needed for that. "Candidate errors must be verifiable by others, and reviewers must be able to substantiate their claims." The recommender's error assessment is based only on the "Error checking" section.
5. Reviewers copy the recommender on all author correspondence; the recommender decides what counts as a reasonable request.
6. The report is licensed CC-BY 4.0 and hosted on error.reviews; reviewers keep copyright and may republish (journal commentary, blog, PubPeer). Reviewers are named, not anonymous; exceptions are rare and need advance approval.
7. Authors reply (two sections: "Responses to error checking", "Responses to other critiques"). The recommender writes a summary with an error category and recommended action. Further discussion moves to PubPeer or similar.

No deadlines or durations are published anywhere on the site. The "Tools" page (https://error.reviews/tools/, checked 2026-11-08) is a placeholder that "will publish tools and guides for error detection work"; it names no tools, so there is room to offer papercheck there.

Completed reviews listed on https://error.reviews/reviews-completed/ (checked 2026-11-08): six papers (Fernbach et al. 2019; Lades et al. 2020; Hehman et al. 2018; Cikara et al. 2014; Joel et al. 2017; Wessel 2018). Reading two or three of these before writing is the fastest way to match the expected report format.

### Contact

- Contact page: https://error.reviews/contact/ (checked 2026-11-08). The text reads "In case of any requests, queries, or questions, please email" followed by an address that is obfuscated by a WordPress email-encoder plugin, so it could not be read without a browser. Open the page in a browser to copy it. The page also gives: Psychology of Digitalisation Lab, University of Bern, Fabrikstrasse 8, 3012 Bern, Switzerland, phone +41 31 68 44095. Responsible: Malte Elson.
- Reviewer sign-up form: https://errorsignup.formr.org/ (checked 2026-11-08).
- Team and board page: https://error.reviews/advisory-board/ (linked from the homepage; not fetched separately).

### What the press says (context for the pitch)

- Science, "Offering scientists cash to spot errors in published papers doesn't work" (https://www.science.org/content/article/offering-scientists-cash-spot-errors-published-papers-doesn-t-work). Direct fetch returned HTTP 403 on 2026-11-08, so the following comes from search-result snippets, not the full article: the project "can't find enough reviewers to do the work"; Elson is quoted that "money itself is not enough of an incentive"; candidates decline immediately, agree and then do not follow up, or stop replying after a few emails; of nine studies examined so far, only one had no errors, and several had "minor" errors that did not affect conclusions; the founders hope a new journal for publishing critiques will attract reviewers; funding exceeds 300,000 USD and ERROR ends in 2028. Verify these against the article in a browser before quoting them to anyone.
- Nature news (https://www.nature.com/articles/d41586-024-02681-2) redirected to a login wall on 2026-11-08 and was not read. Search snippets attribute the project to Elson, Ian Hussey (Bern) and Ruben Arslan (Leipzig), with the 250,000 CHF intended to cover roughly 100 papers over four years, and say Hussey teaches a master's course on error detection at Bern to grow the reviewer pool.

## 2. Draft email to the ERROR organizers

Send to the address on https://error.reviews/contact/ (copy it from a browser), after also submitting the formr sign-up. Attach nothing; link instead.

Subject: Offer to review statistics and code reproducibility for ERROR

Dear Dr. Elson and the ERROR team,

I am a software developer, not an academic, and I would like to join your database of interested reviewers for statistics and computational reproducibility checks. I have read the reviewer FAQ and the participation page, and I understand that a report must document every check so that others can verify it.

What I can offer on a paper that has agreed to be checked: recomputing p values from the reported test statistics and degrees of freedom, checking degrees of freedom against the reported sample sizes, GRIM and GRIMMER checks on reported means and standard deviations, flagging duplicated statistics across tables, and rerunning the authors' analysis code against their data to confirm that the reported numbers reproduce. Every discrepancy is reported as "reported vs recomputed", with the inputs and code that produced it.

I have built an open-source Python pipeline for the first part, papercheck (https://github.com/SahilAujla/papercheck). The repository includes thirteen example reports and hand-verified write-ups under docs/findings/ on published papers so you can judge the format and the care taken.

I do not have domain expertise in psychology, so I would be glad to pair with a domain expert, handling the statistical and computational checks while they judge measurement, design and interpretation. Could you tell me what you would accept from a non-academic reviewer, and whether such a pairing fits your process?

Best regards,
Sahil Aujla
https://github.com/SahilAujla

(Body is about 230 words.)

## 3. Three other outlets

### Institute for Replication (I4R)

- What it is: "an international organization dedicated to improving the credibility of science" that coordinates reproductions and replications of empirical social science research, mostly economics and political science. Chair Abel Brodeur (University of Ottawa), co-chair Jörg Ankel-Peters (RWI). Lists 198 fellows. https://i4replication.org (checked 2026-11-08), https://i4replication.org/about (checked 2026-11-08).
- What it pays or builds: the website does not state compensation. A 2024 Brodeur presentation found by search lists "payments to replicators (USD 5,000)" for one stream only (admin data, non-public data and lab experiments), not for standard reports; treat that figure as unconfirmed until I4R says so in writing. The reliable return is reputation: replication reports are published as I4R discussion papers (232+ so far), and replication-games participants are typically co-authors on the resulting meta-paper (not stated on the games page; confirm by email).
- How to participate: Replication Games are "one-day hackathons where researchers collaborate to reproduce and verify the results of published studies"; participants "run the code, detect coding errors, and reanalyze data". Participants are "typically PhD students, faculty, and researchers with a PhD", so a developer should ask first. Upcoming: ASTMH (Maryland, Nov 18 2026), Marburg (Nov 27 2026, registration deadline Nov 11 2026), Toulouse (Dec 8), Montpellier and Poitiers (Dec 10), Cologne (Jan 21 2027). No virtual games are listed. https://i4replication.org/games (checked 2026-11-08). Contact: instituteforreplication@gmail.com or the form at https://i4replication.org/contact (checked 2026-11-08).
- Pitch angle: offer to handle the code re-execution and statistical consistency checks on a team at a game, or to run papercheck over new I4R target papers as a service.

### Black Spatula Project

- What it is: "an open initiative to investigate the potential of large language models (LLMs) to identify errors in scientific papers", started by Steve Newman after the black-plastic-utensils arithmetic error. Volunteer run; search snippets (heise, 2025) describe about eight active developers, hundreds of volunteer advisers, roughly 500 papers analysed and about a ten percent false-alarm rate, with human verification of flagged errors as the main bottleneck. https://the-black-spatula-project.github.io/ (checked 2026-11-08), https://github.com/The-Black-Spatula-Project (checked 2026-11-08 via the GitHub API; the repos were last pushed Dec 2024 and Aug 2025, so activity may have moved to chat). The domain blackspatula.org does not resolve (checked 2026-11-08).
- What it pays or builds: no payment. Reputation value is direct: a deterministic checker (statcheck-style recomputation, GRIM, GRIMMER, df vs N) is exactly the human-verification layer they say they lack, and the project is well known in the error-detection community that ERROR draws from.
- How to participate: join the Discord (https://discord.gg/Zxf9p7hAnG) or WhatsApp group (https://chat.whatsapp.com/DRkjqk1pwTu1pDXC9oeC0q); open an issue on the main repo with the model name in the title and the PDF attached to trigger an analysis; add yourself to the Volunteer Evaluators sheet (linked from the site) with "statistics recomputation, code re-execution" as expertise. Propose papercheck as a non-LLM pre-filter and verification step.

### PubPeer

- What it is: "The online Journal club", a post-publication commenting database covering "all publications in all fields" with a DOI, PubMed ID or arXiv ID. ERROR's own FAQ names PubPeer as where discussion continues after a report, and allows reviewers to republish reports there. https://pubpeer.com (checked 2026-11-08; the site warned it is moving to a new version on 9 November 2026 and may be briefly unavailable), https://pubpeer.com/static/faq (checked 2026-11-08).
- What it pays or builds: nothing paid. It builds a public, citable track record under a signed account. Comments must rest on "publicly verifiable information"; "Allegations of misconduct are forbidden on PubPeer"; tone must be "Polite, neutral and factual". Authors are notified automatically. This matches the "reported vs recomputed" style exactly.
- How to participate: create an account (signed accounts avoid the moderation delay that new pseudonymous accounts get; moderation can take up to a week), paste the DOI in the search bar to open the first comment, post the recomputation with inputs and method so anyone can reproduce it. Each papercheck example report should end up as a PubPeer comment under Sahil's name, which gives the ERROR email something public to point at.

### Considered and set aside

- AEA Data Editor internship (https://aeadataeditor.github.io/projects/project7, checked 2026-11-08): paid (16.25 USD per hour, up to 20 hours per week, remote) but only for "current students at a participating institution, residing in the United States"; 2026 sign-up closed. Cornell LDI replication lab supervisor posting: filled, in-person, US citizens or residents only.
- Psychological Science STAR (Statistics, Transparency, and Rigor) editors: appointed by the editor-in-chief for their expertise; no open call found.
- AJPS verification policy (https://ajps.org/ajps-verification-policy/, checked 2026-11-08): verification is done for the journal; the page does not name the verifier or offer outside participation. Contact ajps@ajps.org only if a specific opening appears.
- Economic Journal and Econometric Society data editors: appointed editorial roles, not hiring calls.

## 4. Next actions

- [x] Example reports exist (13 papers under `examples/`, hand-verified write-ups under `docs/findings/`), pushed to https://github.com/SahilAujla/papercheck as a private repo. Remaining: make the repo public before sending the email.
- [ ] Read two completed ERROR reports on https://error.reviews/reviews-completed/ and format the example reports with "Error checking" and "Other critique" sections.
- [ ] Post each example report as a PubPeer comment under a signed account, using "reported vs recomputed" wording and no interpretation of motive.
- [ ] Fill in https://errorsignup.formr.org/ (topic expertise: statistics recomputation, computational reproducibility, R and Python code re-execution).
- [ ] Open https://error.reviews/contact/ in a browser, copy the email address, and send the draft email from section 2 with the three PubPeer links added.
- [ ] Email instituteforreplication@gmail.com offering code re-execution help at a game or on new target papers; ask whether non-PhD team members are accepted and whether any stream pays.
- [ ] Join the Black Spatula Discord, add yourself to the Volunteer Evaluators sheet, and offer papercheck as a verification pre-filter.
- [ ] In a browser, read the Science article and confirm the quotes in section 1 before repeating them.
