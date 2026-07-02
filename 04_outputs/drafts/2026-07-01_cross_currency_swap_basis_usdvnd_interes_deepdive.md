---
title: DeepDive — cross currency swap basis USDVND interest rate differential carry
date: 2026-07-01
query: "cross currency swap basis USDVND interest rate differential carry"
threshold: 2
wiki_hits: 8
thin_nodes: 1
raw_hits: 3
status: draft
---

# DeepDive: cross currency swap basis USDVND interest rate differential carry

## STAGE 1 — Wiki Coverage

- ⚠ THIN `Interest_Rate_Swap_Plain_Vanilla::wiki` conf=5
  - Issues: no source_refs section
  - Thesis: A plain vanilla interest rate swap is a bilateral agreement to exchange a
- ✓ SOLID `Swap_Market_Risk_DV01_Carry_Rolldown::Swap_Market_Risk_DV01_Carry_Rolldown` conf=4
  - Thesis: Swap market risk decomposes into fixed-rate bond risk minus FRN risk. DV01 (delta) and convexity (gamma) measure parallel shift sensitivity. Roll-down and carry decompose total P&L. Forward-starting s
- ✓ SOLID `Cross_Currency_Basis::Cross_Currency_Basis` conf=5
  - Thesis: Cross-Currency Basis là mức chênh lệch lãi suất (spread) cộng thêm vào chân ngoại tệ trong một giao dịch hoán đổi tiền tệ, phản ánh sự lệch pha giữa lý thuyết Covered Interest Parity (CIP) và thực tế 
- ✓ SOLID `Interest_Rate_Swap_Use_Cases::Interest_Rate_Swap_Use_Cases` conf=4
  - Thesis: Interest rate swaps are used either as leveraged duration instruments that change DV01 exposure without using cash principal, or as cash-flow transformers that convert fixed and floating obligations i
- ✓ SOLID `Swap_Rate_Conversion_Conventions::Swap_Rate_Conversion_Conventions` conf=5
  - Thesis: Swap rate conversion involves adjusting for different payment frequencies (compounding) and day count bases (bond vs. money), where minor technical errors in calculation can lead to significant presen
- ✓ SOLID `Crawling_Peg_and_Real_Exchange_Rate::Crawling_Peg_and_Real_Exchange_Rate` conf=4
  - Thesis: The crawling peg — a preannounced, periodic adjustment of the nominal exchange rate — resolves the fundamental tension between using the exchange rate as a nominal anchor against inflation and prevent
- ✓ SOLID `Currency_Substitution_Model::Currency_Substitution_Model` conf=5
  - Thesis: The Currency Substitution Model assumes that domestic and foreign money are imperfect substitutes, allowing investors to switch between them based on relative inflation rates, interest rates, and exch
- ✓ SOLID `Floating_vs_Fixed_Exchange_Rate_Regimes::Floating_vs_Fixed_Exchange_Rate_Regimes` conf=4
  - Thesis: The choice of exchange rate regime fundamentally determines fiscal and monetary policy autonomy. Floating rates preserve full policy space for domestic macro (unconstrained by foreign reserve accumula

## STAGE 2 — RAW Source Evidence

### RAW: Bondistan_Tourist_Guide::14.5 CROSS CURRENCY BASIS SWAP XCCY
- file: `02_sources\books\bondistan_tourist_guide\Bondistan_Tourist_Guide.md`
- score: 0.032
- thesis: 14.5 CROSS CURRENCY BASIS SWAP XCCY
- heatmap context:
```
L3: type: raw_source
          L4: source_pdf: "Bondistan_Tourist_Guide.pdf"
          L5: extractor: docling
          L6: ---
          L7: 
      >>> L8: Carry
          L9: 
          L10: ## The Ultimate Tourist Guide to Bondistan by Efficient Market Hype 1 st Ed. © 2022
          L11: 
          L12: <!-- image -->
          L13: 
      [... skip to next heatmap section ...]
          L906: 
          L907: - 1) the spread widens ahead of Fed lift-off
          L908: - 2) it tightens shortly after
          L909: - 3) it widens as Fed begins cutting
          L910: 
      >>> L911: Once 
```

### RAW: Weithers_Foreign_Exchange_Guide::CROSS-CURRENCY SWAPS OR FX CROSS-CURRENCY INTEREST RATE SWAPS OR FX BOND SWAPS
- file: `02_sources\books\weithers_fx_guide\Weithers_Foreign_Exchange_Guide.md`
- score: 0.032
- thesis: CROSS-CURRENCY SWAPS OR FX CROSS-CURRENCY INTEREST RATE SWAPS OR FX BOND SWAPS
- heatmap context:
```
L20: 
          L21: ## TIM WEITHERS
          L22: 
          L23: <!-- image -->
          L24: 
      >>> L25: Copyright © 2006 by Tim Weithers. All rights reserved. Published by John Wiley &amp; Sons, Inc., Hoboken, New Jersey. Published simultaneously in Canada. No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, electronic, mechanical, photocopying, recording, scanning, or otherwise, except as permitted under Section 107 or 108 of the 1976 United States Copyright Act, without either the prior written permission of the P
```

### RAW: Weithers_Foreign_Exchange_Guide::Foreign Exchange Swaps or Cross-Currency Swaps or Cross-Currency Interest Rate Swaps or . . .
- file: `02_sources\books\weithers_fx_guide\Weithers_Foreign_Exchange_Guide.md`
- score: 0.031
- thesis: Foreign Exchange Swaps or Cross-Currency Swaps or Cross-Currency Interest Rate Swaps or . . .
- heatmap context:
```
L20: 
          L21: ## TIM WEITHERS
          L22: 
          L23: <!-- image -->
          L24: 
      >>> L25: Copyright © 2006 by Tim Weithers. All rights reserved. Published by John Wiley &amp; Sons, Inc., Hoboken, New Jersey. Published simultaneously in Canada. No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, electronic, mechanical, photocopying, recording, scanning, or otherwise, except as permitted under Section 107 or 108 of the 1976 United States Copyright Act, without either the prior written permission of the P
```

## STAGE 3 — Expansion Proposal

> **Action required:** Review RAW evidence above, then:

- [ ] UPDATE `03_wiki/definitions/Interest_Rate_Swap_Plain_Vanilla.md` — address: no source_refs section
      Add source_refs from RAW hits above

---
*Generated by deepdive_search.py v2.1 on 2026-07-01*