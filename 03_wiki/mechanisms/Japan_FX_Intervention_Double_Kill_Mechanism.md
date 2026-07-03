---
title: Japan FX Intervention — Double Kill Mechanism (TQN Perspective)
type: mechanism
status: verified
confidence: 5
expert_lens: [Trần Quang Nghĩa — Operational Mechanics, Ulrich Bindseil — Central Bank Operations]
tags: [monetary-policy, fx-intervention, japan, liquidity-management]
source_refs: [RAW-CLIP: Trần Quang Nghĩa (2026-05-07) — PY: 160 Yentervention]
---

## Thesis
Cơ chế "Double Kill" trong can thiệp tỷ giá của Nhật Bản là sự phối hợp tinh vi giữa Bộ Tài chính (MoF) và NHTW (BoJ), sử dụng **độ trễ thời gian (time lag)** trong hoạt động hoàn trả thanh khoản (Redemption) để tạo ra áp lực thắt chặt kép lên đồng Yên, trực tiếp "tiêu diệt" các vị thế bán khống (Short Yen).

## Mechanism (RCL Skeleton)

### 1. REGIME: Tactical Sterilization Lag
Trong trạng thái can thiệp thông thường, MoF đặt mục tiêu **Sterilized Intervention** (delta MB = 0) để không làm xáo trộn mục tiêu lãi suất của BoJ. Tuy nhiên, trong regime "Double Kill", MoF và BoJ chủ động tạo ra một trạng thái **"Thắt chặt tạm thời"** bằng cách kéo dài quá trình hoàn trả JPY vào hệ thống ngân hàng.

### 2. CAUSAL CHAIN: T-Account Logic & Redemption Delay

Chuỗi truyền dẫn vận hành qua 4 giai đoạn:

1.  **Giai đoạn Huy động (Financing):** MoF (thông qua FEFSA) phát hành **Financing Bills (FBs)** để huy động JPY hoặc sử dụng dự trữ USD có sẵn.
2.  **Giai đoạn Can thiệp (The Hit):** MoF bán USD, mua JPY trên thị trường.
    *   **Bảng CĐKT MoF/FEFSA:** Asset [-USD, +TGA (Yen Account)]; Liab [Unchanged FB].
    *   **Bảng CĐKT Hệ thống Ngân hàng:** Asset [-JPY reserves]; Liab [Unchanged].
    *   **Kết quả:** Thanh khoản JPY trong hệ thống bị hút về tài khoản TGA tại BoJ → **MB giảm (Thắt chặt).**
3.  **Giai đoạn "Nghệ thuật Timing" (The Delay):** Theo quy trình chuẩn, MoF sẽ dùng JPY trong TGA để mua lại (Redeem) FBs, trả lại JPY cho các ngân hàng (MB quay về 0). Nhưng trong "Double Kill", MoF **trì hoãn** hoặc làm chậm quá trình này.
4.  **Hệ quả "Double Kill":** 
    *   **Kill 1 (Price Action):** Cú sốc trực tiếp từ việc bán USD làm giá UJ giảm mạnh.
    *   **Kill 2 (Liquidity Squeeze):** MB vẫn ở trạng thái âm (-delta MB) lâu hơn dự kiến → Lãi suất thị trường tiền tệ (Money market rates) tăng vọt → Chi phí duy trì vị thế Short Yen tăng (Negative Carry) → Buộc speculators phải đóng vị thế (Short squeeze).

### 3. T-Account Visualization

| Entity | Action: Intervention (Sell U, Buy J) | Action: Redemption Delay | Final (After Redemption) |
| :--- | :--- | :--- | :--- |
| **MoF (FEFSA)** | Assets: -USD, +TGA; Liab: FB | Asset: +TGA (Hold); Liab: FB | Asset: -USD; Liab: -FB |
| **BoJ** | Asset: -USD (Hold for MoF); Liab: -Reserves, +TGA | Asset: Unchanged; Liab: -Reserves, +TGA | Asset: Unchanged; Liab: Unchanged |
| **Banks** | Asset: -Reserves (JPY); Liab: Unchanged | **Liquidity Squeeze** | Asset: Unchanged (after RO) |

## Worked Example: 30-Apr-2024 (and May 2026)
*   **Scale:** MoF bán USD mua JPY lượng tương đương **5.4 nghìn tỷ Yên**.
*   **Tactics:** Kết hợp **Intensified Verbal Intervention** (OMO - Open Mouth Operation) để gây sốc tâm lý, sau đó trì hoãn Redemption để tạo áp lực thắt chặt thanh khoản kéo dài (Time lag timing art).

## Failure Conditions
*   **Sterilization Reversal:** Nếu BoJ thực hiện OMO bơm tiền quá sớm để cứu thị trường trái phiếu, hiệu ứng "Double Kill" về thanh khoản sẽ bị triệt tiêu.
*   **Scale Exhaustion:** Nếu lượng FBs cần mua lại quá lớn vượt quá khả năng điều tiết của TGA, MoF buộc phải hoàn tất Redemption sớm.

## Related
- [[Japan_FX_Intervention_MOF_BOJ_Framework]]
- [[FX_Sterilization_Mechanism]]
- [[Financing_Bills_FB]]
- [[Money_Base_MB_Dynamics]]
- [[Japan_FX_Intervention_May_2026_Event]]
- [[JP_Domain]]
- [[Japanese_Premium_Synthetic_Loans]]
- [[FX_Intervention_Ambush_Tactic]]
- [[BOJ_June_2026_Rate_Hike_Ueda_Absence]]
