---
title: Tokenized Monetary System
aliases:
- Tokenization of Money
- Programmable Money
- CBDC and Tokenized Deposits
type: mechanism
tags:
- monetary-system
- technology
- cbdc
- tokenization
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: TBD
thesis: '**Tokenized Monetary System** là một kiến trúc hệ thống tiền tệ tương lai,
  dựa trên việc đại diện các quyền sở hữu dưới dạng "executable objects" (đối tượng
  có khả năng thực thi) trên các nền tảng lập trình được.'
source_refs: []
created: '2026-04-13'
updated: '2026-04-16'
source: https://www.bis.org/publ/arpdf/ar2023e3.htm
---

# Tokenized Monetary System

## Mechanism

**Tokenized Monetary System** là một kiến trúc hệ thống tiền tệ tương lai, dựa trên việc đại diện các quyền sở hữu dưới dạng "executable objects" (đối tượng có khả năng thực thi) trên các nền tảng lập trình được.

Hệ thống này tích hợp ba thành phần chính:
1. **Wholesale CBDC**: Đóng vai trò là tài sản quyết toán (settlement asset) cốt lõi, đảm bảo tính ổn định và sự duy nhất của tiền tệ (singleness of money).
2. **Tokenized Deposits**: Tiền gửi ngân hàng thương mại được mã hóa, cho phép thực hiện các giao dịch lập trình được trong khi vẫn duy trì cấu trúc nhị phân (two-tier) của hệ thống ngân hàng.
3. **Tokenized Assets**: Các tài sản tài chính (cổ phiếu, trái phiếu, nợ tư nhân) và tài sản thực được mã hóa để giao dịch đồng thời với tiền tệ (atomic settlement).

> [!TIP]
> Sự khác biệt cốt lõi: Trong hệ thống truyền thống, việc gửi tin nhắn (messaging) và quyết toán (settlement) là hai quy trình tách biệt. Trong hệ thống token hóa, chúng được hợp nhất thành một bước duy nhất. [extracted]

### Ưu điểm
- **Atomic Settlement (Quyết toán nguyên tử)**: Việc chuyển giao tài sản xảy ra đồng thời với việc chuyển tiền. Không có rủi ro đối tác trong quá trình settlement. [extracted]
- **Programmability (Tính lập trình)**: Cho phép tạo ra các hợp đồng thông minh (smart contracts) phức tạp, ví dụ: tự động giải ngân vốn cho doanh nghiệp khi đạt được các mốc KPI cụ thể. [inferred]
- **Composability (Tính kết hợp)**: Khả năng đóng gói nhiều giao dịch thành một gói thực thi duy nhất. [extracted]

### Hình ảnh minh họa (Idea)
> **Cỗ máy Hợp nhất**: Vẽ hai bánh răng cũ (Messaging và Settlement) đang rời rạc. Một cỗ máy mới (Tokenized Platform) hợp nhất chúng thành một băng chuyền liên tục, nơi hàng hóa và tiền tệ chạy song song và đổi chỗ cho nhau ngay lập tức.

## Evidence / Source Anchors
- [extracted] [BIS Annual Economic Report 2023, "Blueprint for the future monetary system", 2023](https://www.bis.org/publ/arpdf/ar2023e3.htm)
- [researched] [BIS Quarterly Review, March 2025](https://www.bis.org/publ/qtrpdf/r_qt2503b.htm)


## Related

- [[Project_Meridian]]
- [[Unified_Ledger_Concept]]
