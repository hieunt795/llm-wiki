# Writeback Queue
> File này dùng để gom các Writeback được đề xuất trong quá trình hội thoại. Khi kết thúc session, bạn có thể copy nội dung trong đây làm prompt (task list) cho AI chạy batch.
> 
> **Writeback types:** SPAWN | UPDATE | REPLACE | BRIDGE | CONTRADICTION | SYNTHESIS | PERSPECTIVE
> Xem Decision Tree đầy đủ tại `01_schema/workflows/W4_memory.md`.

## Session: 2026-04-22 (Lãi suất và UMP)
- [x] **BRIDGE** `03_wiki/concepts/Financial_Deepening.md` — Cần thêm liên kết hai chiều từ Financial Deepening sang `Unconventional_Monetary_Policy_Taxonomy.md` để nhấn mạnh rằng sự thiếu hụt độ sâu tài chính là một trong những nguyên nhân (bên cạnh ZLB) buộc NHTW phải dùng đến UMP.
- [x] **UPDATE** `03_wiki/mechanisms/Interbank_Money_Market_Mechanism.md` — Bổ sung chi tiết về "Broken Transmission" dưới dạng sơ đồ Flowchart (hoặc T-Shape) để trực quan hóa quá trình đứt gãy thanh khoản giữa Money Centers và Small Banks do rủi ro đối tác.
- [x] **UPDATE** `03_wiki/concepts/Financial_Deepening.md` — Bổ sung sơ đồ đối chiếu (ASCII) giữa Deep Market và Shallow Market, cùng với Worked Example về chênh lệch Term Premium để định lượng tác động của độ sâu tài chính.
- [x] **SPAWN** `03_wiki/mechanisms/Treasury_General_Account_Mechanism.md` (Đã hoàn thành)
- [x] **SPAWN** `03_wiki/mechanisms/Cross_Currency_Basis.md` (Đã hoàn thành)
- [ ] **SPAWN** `03_wiki/mechanisms/Central_Bank_Swap_Lines.md` (Data: `04_outputs/drafts/Central_Bank_Swap_Lines_draft.md`)

## Session: 2026-04-29 (Vietnam Monetary Policy + US Bond Yields + Fed Dilemma)

### Vietnam Monetary Policy
> URLs: https://vietnamnews.vn/economy/1764382/central-bank-s-first-2026-directive-prioritises-inflation-control-macro-stability.html | https://www.oecd.org/en/publications/oecd-economic-surveys-viet-nam-2025_fb37254b-en/full-report/strengthening-the-macroeconomic-foundations-for-growth_b6ed9c4e.html | https://theinvestor.vn/challenges-for-vietnams-monetary-policy-in-2026-d17806.html | https://fulcrum.sg/exchange-rate-stability-in-vietnam-navigating-the-conflicting-policy-demands/ | https://www.fastbull.com/news-detail/how-vietnam-stabilized-the-usdvnd-rate-through-targeted-4353240_0

- [ ] **SPAWN** `03_wiki/concepts/Vietnam_Monetary_Policy_Regime.md` — De jure ITF vs. de facto FX/credit target. Nội dung: 3-tầng mục tiêu (Ultimate/Intermediate/Operational), ITL classification (Warjiyo taxonomy), FX band ±5% mechanics, credit quota as primary instrument, gap giữa stated ITF và thực tế vận hành. Source: [WEB-2026-04-29: vietnamnews.vn; OECD Survey 2025] + [RAW-BOOK: Warjiyo (2019), Ch.8].
- [ ] **BRIDGE** `03_wiki/mechanisms/Monetary_Policy_Trilemma.md` ↔ `03_wiki/mechanisms/Exchange_Rate_Pass_Through.md` — Vietnam ERPT cao (~0.3–0.4) có nghĩa FX anchor không chỉ là chính sách mà còn là inflation control tool trực tiếp. Link 2 chiều chưa được map.
- [ ] **BRIDGE** `03_wiki/mechanisms/One-directional_Standing_Facility_Steering.md` ↔ Vietnam credit quota mechanism — hai hệ thống kiểm soát quantity khác nhau nhưng cùng logic: bypass price signal. Cần section so sánh trong một trong hai node.

### US Bond Yields & Fed
> URLs: https://www.advisorperspectives.com/dshort/updates/2026/04/24/treasury-yields-snapshot-april-24-2026 | https://www.morningstar.com/markets/bonds-tug-war-between-rising-inflation-slowing-growth | https://www.cfr.org/articles/trade-tariffs-and-treasuries-hidden-cost-trumps-protectionism | https://www.lpl.com/research/weekly-market-commentary/navigating-neutral-fed-policy-key-for-fixed-income-markets-in-2026.html | https://www.ishares.com/us/insights/fed-outlook-2026-interest-rate-forecast | https://www.federalreserve.gov/monetarypolicy/fomcminutes20260128.htm | https://www.cbo.gov/publication/62105 | https://streetstats.finance/rates/term-premiums | https://www.cnbc.com/2026/03/18/treasury-yields-move-lower-all-eyes-fed-meeting.html

- [ ] **SPAWN** `03_wiki/mechanisms/Term_Premium_Fiscal_Channel.md` — Cơ chế supply-driven yield tăng tách biệt với inflation expectations. Nội dung: TP = f(supply uncertainty, fiscal credibility, FX reserve recycling); reinforcing loop (yield → debt service → deficit → supply → TP); boundary conditions (QE collapse, risk-off). Source: [WEB-2026-04-29: CFR; streetstats.finance] + [RAW-BOOK: Tuckman & Serrat (2022)].
- [ ] **SPAWN** `03_wiki/mechanisms/Supply_Shock_Monetary_Policy_Dilemma.md` — Instrument mismatch: demand-side tool (FFR) vs. supply-side shock (tariff + oil). Nội dung: cost-push vs. demand-pull taxonomy, sacrifice ratio under stagflation, escape clause mechanics, second-round expectations effects. Source: [WEB-2026-04-29: Morningstar; CFR; iShares] + [RAW-BOOK: Warjiyo (2019), Ch.8].
- [ ] **BRIDGE** `03_wiki/mechanisms/Barro_Gordon_Model.md` ↔ `03_wiki/mechanisms/Term_Premium_Fiscal_Channel.md` (node chưa tồn tại — thực hiện sau khi SPAWN xong) — Credibility loss từ instrument mismatch amplifies term premium: market biết Fed không thể fix supply inflation → uncertainty premium tăng trên long-end.

### Ingest Candidates
- [ ] **[INGEST CANDIDATE]** CFR article "Trade, Tariffs, and Treasuries: The Hidden Cost of Trump's Protectionism" — phân tích tariff → yield spike mechanism (+34bps/7 ngày). Giá trị dài hạn cao. URL: https://www.cfr.org/articles/trade-tariffs-and-treasuries-hidden-cost-trumps-protectionism → W2 ingest khi có thời gian.
- [ ] **[INGEST CANDIDATE]** OECD Economic Survey Vietnam 2025 — khuyến nghị chuyển từ quantity-based sang price-based monetary policy. URL: https://www.oecd.org/en/publications/oecd-economic-surveys-viet-nam-2025_fb37254b-en/full-report/strengthening-the-macroeconomic-foundations-for-growth_b6ed9c4e.html → W2 ingest khi có thời gian.
- [ ] **[INGEST CANDIDATE]** CBO Budget & Economic Outlook 2026–2036 — fiscal deficit path, Treasury supply projection. URL: https://www.cbo.gov/publication/62105 → W2 ingest khi có thời gian.
