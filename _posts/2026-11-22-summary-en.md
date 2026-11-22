---
layout: default
title: "Horizon Summary: 2026-11-22 (EN)"
date: 2026-11-22
lang: en
---

> From 24 items, 8 important content pieces were selected

---

**Technology News**
1. [Lean community post claims a Riemann Hypothesis formal verification](#item-tech-news-1) ⭐️ 9.0/10
2. [OpenRouter Discloses Data-Processing Incidents Among Inference Providers](#item-tech-news-2) ⭐️ 7.0/10
3. [Linebender&\#x27;s Advice for the Next 100 Rust GUIs](#item-tech-news-3) ⭐️ 7.0/10
4. [Analysis projects Anthropic’s 2028 power mix at 87% gas, 11% coal](#item-tech-news-4) ⭐️ 7.0/10
5. [Graham Dumpleton&\#x27;s Muru: AI-Assisted Rust Server for ASGI/WSGI Python](#item-tech-news-5) ⭐️ 7.0/10
6. [Tesla starts FSD v15 rollout with Reality View and speed-control changes](#item-tech-news-6) ⭐️ 7.0/10
7. [FT Alleges Nvidia Smuggling Network Tied to Cambodia&\#x27;s Prince Group](#item-tech-news-7) ⭐️ 7.0/10

**Technology Blog**
1. [To Code Well, Avoid Catastrophic Blunders](#item-tech-blog-1) ⭐️ 6.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Lean community post claims a Riemann Hypothesis formal verification](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) ⭐️ 9.0/10

A post on the Lean Prover community blog announces a Lean verification of the Riemann Hypothesis, according to the item&\#x27;s title and link. The supplied material contains no statement of exactly which conjecture was formalized — the Riemann Hypothesis or its generalization, GRH — no list of axioms or admitted lemmas, and no description of the proof&\#x27;s size or the checker configuration, so the scope and strength of the claim cannot be assessed from what is available here. Hacker News discussion characterizes the work as AI-assisted, with commenters saying the proof was produced using Claude alongside a human expert, but those details come from comments rather than from the source itself.

hackernews · g-b-r · Nov 21, 14:36 · [Discussion](https://news.ycombinator.com/item?id=50589618)

**「Background」** The Riemann Hypothesis is a long-standing conjecture about the zeros of the Riemann zeta function, and Lean is an interactive theorem prover that checks a proof against a small trusted kernel, so a formalization can in principle be verified mechanically rather than by peer review alone. According to press reports, Levent Alpöge, a mathematician at Anthropic, released a 17-million-line Lean library on November 20, 2026 that he said encodes the argument he found while working with Claude, and the Lean FRO and Mathlib Initiative issued a joint statement the next day certifying that the library&\#x27;s statement and proof match the Riemann Hypothesis.

**「Practical verification」** Teams relying on Lean for verified mathematics should plan to re-check the claimed proof with independent kernels before depending on it: commenters point to con-leche and con-ron as alternate checkers with their own consistency proofs, and note that a fake Collatz refutation reportedly slipped past one checker. With no theorem statement, Lean version, or artifact details in the item, that cross-checking step—not the “verified” label alone—is the practical gate.

**「Community discussion」** Commenters split on how much the verification establishes by itself: one argued that a bug-exploiting proof is now vanishingly unlikely because several independent kernels, which they named as con-leche and con-ron, each carry consistency proofs, while another countered that a fake Collatz refutation previously passed one such checker and noted that the write-up&\#x27;s claims do not all depend on human oversight. Others credited the human collaborator referred to as Levent for drawing the result out of Claude, and one commenter said that, whatever happens with RH, the work formalized a large chunk of modern mathematics.

<details><summary>References</summary>
<ul>
<li><a href="https://www.unite.ai/lean-and-mathlib-communities-certify-claude-assisted-riemann-proof/">Lean and Mathlib Communities Certify Claude-Assisted Riemann ...</a></li>
<li><a href="https://www.datastudios.org/post/claude-riemann-hypothesis-proof-lean-community-certifies-levent-alpoge">Claude-assisted Riemann hypothesis proof certified by Lean ...</a></li>
<li><a href="https://officechai.com/ai/lean-community-certifies-levent-alpoges-claude-assisted-proof-of-the-riemann-hypothesis-as-correct/">Lean Community Certifies Levent Alpöge’s Claude-Assisted ...</a></li>

</ul>
</details>

**Tags**: `#formal verification`, `#Lean`, `#Riemann Hypothesis`, `#mathematics`, `#AI-assisted proof`

---

<a id="item-tech-news-2"></a>
### [OpenRouter Discloses Data-Processing Incidents Among Inference Providers](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/) ⭐️ 7.0/10

OpenRouter published an announcement about data-processing incidents involving inference providers, making the issue public for teams that route AI prompts through its aggregation service. The supplied material does not give the number of incidents, identify the providers or affected users, or describe remediation commitments. Because the upstream provider handling a request can determine its data-retention terms, customers cannot assume the same privacy conditions apply to every request.

hackernews · sdko · Nov 22, 02:14 · [Discussion](https://news.ycombinator.com/item?id=50595554)

**「Background」** OpenRouter is an aggregator that routes a request for a given model to one of several third-party inference providers, so the same model can be served by different hosts with different characteristics. It also supports a \`provider: \{&quot;zdr&quot;: true\}\` request setting that restricts routing to endpoints with a zero-data-retention policy, according to a shared tip about the service.

**「Impact」** For teams using OpenRouter, the immediate operational concern is provider selection: one commenter reported being affected by a single prompt and said they now restrict OpenRouter routing to a shortlist of trusted providers. That makes allow-listing upstream providers, rather than relying on default routing, a concrete safeguard when prompts may be forwarded beyond the aggregator.

**「Community discussion」** Commenters split on whether OpenRouter&\#x27;s response is adequate: one said the incident ended their consideration of the platform, citing what they described as a lack of provider vetting, while another welcomed the response but argued that the strongest zero-data-retention protection is a direct agreement with each inference provider. A user who said one prompt was affected reported switching to a provider allowlist instead of accepting default routing.

<details><summary>References</summary>
<ul>
<li>The same model on OpenRouter is five different products and nobody treats it that way</li>
<li>Kenny Rogers on X: &quot; @OpenRouter tip #7 Add &quot;provider&quot;: {&quot;zdr&quot;: true} to a request and ...</li>

</ul>
</details>

**Tags**: `#OpenRouter`, `#AI inference privacy`, `#data processing incidents`, `#zero data retention`, `#provider trust`

---

<a id="item-tech-news-3"></a>
### [Linebender&\#x27;s Advice for the Next 100 Rust GUIs](https://linebender.org/blog/next-100-guis/) ⭐️ 7.0/10

Linebender&\#x27;s raphlinus has published &quot;Advice for the next 100 Rust GUIs,&quot; a blog essay offering guidance to developers building GUI frameworks and applications in Rust. It is a practitioner essay about Rust GUI architecture and lessons learned, not a framework release; the supplied material does not enumerate its specific recommendations. The post also drew a sizable Hacker News discussion focused on framework choices and implementation tradeoffs.

hackernews · raphlinus · Nov 21, 21:17 · [Discussion](https://news.ycombinator.com/item?id=50593737)

**「Background」** Linebender&\#x27;s Raph Levien has been developing Xilem, a Rust-native UI architecture; a May 2023 Bay Area Rust talk presented it as a refinement of Xilem&\#x27;s medium-grained reactive model. Rust developers have also sought GUI-library recommendations in forum and Reddit threads dating back to 2016.

**「Community discussion」** Commenters highlighted framework coverage gaps: one praised Slint for its ex-Qt team, fast performance, DSL-based layout and data binding, and Skia rendering, while another noted that a 2026 Rust GUI library survey omitted the retained-mode Native Shell. A developer building a custom Rust GUI reported that text selection, text wrapping, and input-cursor placement are slow to get right, illustrating the cost of a bespoke stack.

<details><summary>References</summary>
<ul>
<li>What GUI libs are out there and good to use? : r/rust - Reddit</li>
<li>GUI framework for rust - help - The Rust Programming Language Forum</li>
<li>Bay Area Rust May 2023: Raph Levien on Xilem Vector Graphics - YouTube</li>

</ul>
</details>

**Tags**: `#Rust GUI`, `#GUI frameworks`, `#software architecture`, `#rendering`, `#developer experience`

---

<a id="item-tech-news-4"></a>
### [Analysis projects Anthropic’s 2028 power mix at 87% gas, 11% coal](https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/) ⭐️ 7.0/10

An analysis published by the Better Data Center Project projects that 87% of Anthropic’s power in 2028 will come from natural gas and 11% from coal. The figure is a forecast from an advocacy-oriented source, not a confirmed Anthropic disclosure, and the supplied item includes no methodology or source text to verify it. It nonetheless focuses attention on the fossil-fuel share of electricity for AI data centers.

hackernews · happosai · Nov 22, 08:57 · [Discussion](https://news.ycombinator.com/item?id=50597612)

**「BYOP and grid power」** The analysis separates data-center electricity into “bring your own power” \(BYOP\) on-site generation and utility grid supply. Earthjustice describes proposed gas BYOP projects as at least 4.5 gigawatts each, roughly enough to power 3.7 million homes, and says AI data-center developers plan to build far more gas than renewables.

**「Impact」** If the projection is used for planning, Anthropic’s 2028 electricity demand would remain overwhelmingly tied to fossil fuels, making grid capacity and emissions key constraints for siting and power procurement.

**「Community Discussion」** Commenters criticized the projected reliance on fossil fuels, with one arguing that if rooftop solar can supply renewable power for a model, Anthropic could do more, and another saying AI is accelerating climate change. Others focused on scale and affordability: one said data-center energy use is far larger than most people visualize, while another asked whether the U.S. grid and consumers can afford the added load.

<details><summary>References</summary>
<ul>
<li><a href="https://earthjustice.org/experts/mandy-deroche/the-ai-gas-rush-how-bring-your-own-power-evades-regulation-and-drives-deadly-pollution">The AI Gas Rush: How “Bring Your Own Power ” Evades... - Earthjustice</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data center energy`, `#Anthropic`, `#electricity grid`, `#sustainability`

---

<a id="item-tech-news-5"></a>
### [Graham Dumpleton&\#x27;s Muru: AI-Assisted Rust Server for ASGI/WSGI Python](https://simonwillison.net/2026/Nov/21/muru/) ⭐️ 7.0/10

Graham Dumpleton, the creator of mod\_wsgi, is developing Muru, an AI-assisted Rust server intended to run ASGI and WSGI Python applications in both development and production. In the three weeks before Simon Willison&\#x27;s November 21, 2026 link post, Dumpleton published 18 posts documenting the project, covering worker architecture, import once and fork many, HTTPS in development, releases without restarts, canaries, Kubernetes integration, scaling to zero, and a tracing toolbar. The source gives no release version, installation instructions, benchmarks, or compatibility guarantees; Dumpleton describes AI as doing much of the surface work while he judges what is good enough, drawing on two decades of mod\_wsgi experience.

rss · Simon Willison · Nov 21, 23:56

**「Background」** Graham Dumpleton started mod\_wsgi 20 years ago and has been thinking about the ideal way to serve Python web applications ever since. Muru is his new, AI-assisted Rust server for running ASGI and WSGI Python apps in development and production, and he is publishing detailed accounts of its design and progress as he builds it.

**「Impact」** Python web teams have another ASGI and WSGI server to evaluate, but the absence of a release version, performance measurements, and compatibility guarantees means Muru should not yet be treated as a drop-in production replacement; evaluating it would require checking the GitHub repository and the detailed design writeups rather than relying on a production-readiness claim.

**Tags**: `#Python web servers`, `#ASGI/WSGI`, `#Rust`, `#mod\_wsgi`, `#open source`

---

<a id="item-tech-news-6"></a>
### [Tesla starts FSD v15 rollout with Reality View and speed-control changes](https://x.com/Tesla/status/2124222447855743019) ⭐️ 7.0/10

Tesla has begun rolling out FSD v15 in overseas markets, adding a &quot;Tesla Reality View&quot; interface that overlays camera feeds and FSD driving plans on the vehicle screen in full-screen, map, or split-screen views, plus a quiet mode. The update also adds navigation overlays for turns, makes the turn-signal chime softer and gradually fading, and adjusts driving through potholes and debris as well as speed control near schools and in bad weather. Tesla claims the update improves handling of safety-critical scenarios by 25 times, but the source provides no technical detail or independent evidence for that figure.

telegram · zaihuapd · Nov 22, 00:03

**「Context: what FSD v15 is built on」** FSD is Tesla&\#x27;s supervised driver-assistance system, and coverage of this rollout describes v15 as upgrading every part of its end-to-end driving network. That same reporting frames the release as Tesla&\#x27;s attempt to close FSD&\#x27;s most-cited weak spots — reading signs, handling potholes and debris, and controlling speed in school zones and bad weather — rather than as a change to the system&\#x27;s overall operating domain.

<details><summary>References</summary>
<ul>
<li><a href="https://electrek.co/2026/11/21/tesla-fsd-v15-rollout-25x-safety-reality-view/">Tesla launches FSD v15, targets its biggest weaknesses, from ...</a></li>
<li><a href="https://elonexplained.com/news/2026/11/tesla-fsd-v15-rollout-reality-view/">Tesla FSD V15 Starts Rolling Out With 25x Better Handling of ...</a></li>

</ul>
</details>

**Tags**: `#Tesla FSD`, `#autonomous driving`, `#AI`, `#software update`, `#vehicle UI`

---

<a id="item-tech-news-7"></a>
### [FT Alleges Nvidia Smuggling Network Tied to Cambodia&\#x27;s Prince Group](https://www.ft.com/content/f3ad8a81-3890-4a8a-8853-ff0a94b08ba9?syn-25a6b1a6=1) ⭐️ 7.0/10

The Financial Times, citing people familiar with the matter, reported that Hu Xiaowei—identified by the U.S. Treasury as a &quot;number two&quot; figure in Cambodia&\#x27;s Prince Group—is alleged to have helped move Nvidia chips into China. The report cites trade data showing about $4.6 billion in declared imports between December 2024 and December 2025 by Megaspeed&\#x27;s Malaysian subsidiary, with some chips reportedly reaching China&\#x27;s black market. It also describes shell companies, underground financing channels, and private jets used to smuggle goods. Prince Group denied that Hu worked for it and said the allegations of an illegal network and private-jet smuggling lacked factual basis.

telegram · zaihuapd · Nov 22, 04:34

**「Background」** The allegation follows earlier reporting that placed Megaspeed, a Singapore-based cloud provider, at the center of the Nvidia chip-smuggling controversy; the FT traced the network through its Malaysia-based subsidiary Speedmatrix and hundreds of shell companies. Coverage of that investigation also notes that the US Treasury has designated Prince Group a transnational criminal organization.

**「Enforcement pressure would land on re-export paperwork」** The likely consequence is procedural rather than technical: after an earlier alleged diversion scheme that shipped 400 Nvidia A100 GPUs to China via Malaysia, U.S. officials called for chip-tracking measures \(tool-3-2\), and Taiwan later detained suspects while Nvidia publicly warned server maker Super Micro in a separate supply case \(tool-3-3\). For distributors and cloud operators handling Nvidia hardware in Southeast Asia, that precedent points toward tighter end-use verification and documentation on onward sales — though Prince Group denies the FT allegations, which rest on unnamed sources and declared import values rather than independently audited shipments.

<details><summary>References</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/ft-ties-huangs-75b-nvidia-chip-route-to-prince-group">FT Ties Huang&#x27;s $7.5B Nvidia Chip Route to Prince Group</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/megaspeed-built-network-singapore-malaysia-024836098.html?fr=sycsrp_catchall">How Megaspeed built a network in Singapore and Malaysia to ...</a></li>
<li>Alleged AI chip smuggling to China leads to US calls for chip tracking - Yahoo</li>
<li>Taiwan Launched a Crackdown on AI Chip Smuggling after a High-Profile Statement by Nvidia&#x27;s CEO - Incrypted</li>

</ul>
</details>

**Tags**: `#Nvidia`, `#export controls`, `#AI chips`, `#smuggling`, `#supply chain`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [To Code Well, Avoid Catastrophic Blunders](https://seangoedecke.com/to-code-well-avoid-blunders/) ⭐️ 6.0/10

rss · Sean Goedecke · Nov 22, 00:00

**「Background」** Many engineers treat good programming as a search for brilliant insights or elegant abstractions, but Sean Goedecke argues that the main skill is avoiding catastrophic mistakes. Unlike basketball, where a large lead survives a blunder, programming offers no durable advantage: one bad design choice can turn an elegant codebase into a janky one.

**「Solution」** Goedecke identifies inconsistency and unnecessary requirements as the cardinal sins. Typical blunders include introducing a parallel system for the same task, creating a second source of truth, turning a safe synchronous operation into a delicate asynchronous one, adding subtle failure points, or complicating a key interface. Even slight inconsistency is dangerous because it destroys trust: engineers can no longer assume code behaves sensibly and must hunt for surprises. Unnecessary requirements are sticky, since later engineers lack the context to remove them and must assume they are needed, and they interact combinatorially with every new feature. The author therefore advises fitting each task as normally as possible into the existing codebase and trimming it to the smallest set of requirements. Thinking “I could implement this with a clever pattern” is a warning sign of distraction, and he notes that coding agents currently handle consistency about as well as humans but are worse at avoiding unnecessary requirements.

**「Takeaway」** Goedecke’s thesis is that great programming does not require cleverness and can even be harmed by it; what matters is attention to detail and a laser focus on preserving consistency while skipping unnecessary requirements.

**Tags**: `#software engineering`, `#code quality`, `#complexity management`, `#consistency`, `#maintainability`

---