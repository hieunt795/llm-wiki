# Research Dashboard: Bank Treasury Mechanics (ACI)

> [!NOTE]
> Bản đồ tư duy dạng **Whiteboard** bóc tách vi cấu trúc vận hành của bàn Dealing Treasury theo chuẩn ACI Dealing Certificate.

```mermaid
graph TD
    %% Classes Setup
    classDef startEnd fill:#00C853,stroke:#000,stroke-width:2px,color:#fff;
    classDef core fill:#2962FF,stroke:#fff,stroke-width:2px,color:#fff;
    classDef risk fill:#D50000,stroke:#fff,stroke-width:2px,color:#fff;
    classDef formula fill:#424242,stroke:#FFD600,stroke-width:2px,stroke-dasharray: 5 5,color:#FFD600;
    classDef process fill:#607D8B,stroke:#fff,stroke-width:1px,color:#fff;

    %% Nodes
    Inflow(["[1] Client FX/Deposit Request"])
    Quoting["[2] Two-way Pricing (BOB)"]
    Execution["[3] Deal Execution (Mine/Yours)"]
    
    subgraph Operations ["Quy trình Dealing"]
        Position["[4] Position Keeping (Open Position)"]
        Squaring["[5] Squaring & Hedging"]
        MtM[["[6] Mark-to-Market (Revaluation)"]]
    end
    
    subgraph RiskManagement ["Quản trị rủi ro"]
        Limit(["[7] Limit Checks (Intra-day/Overnight)"])
        Settlement["[8] Settlement (T+2/RTGS)"]
        Liquidity["[9] Liquidity Buffer (MRR/Prudential)"]
    end
    
    subgraph Formulas ["Toán học Treasury"]
        PointVal[["Value of One Point Rule"]]
        AvgRate[["Weighted Average Rate Formula"]]
    end

    %% Links
    Inflow ==> Quoting
    Quoting ==> Execution
    Execution ==> Position
    Position ==> Squaring
    Position ==> MtM
    
    Squaring -- "Hedge Market Risk" --> Limit
    MtM -- "P&L Calculation" --> Limit
    Execution -- "Delivery Risk" --> Settlement
    Inflow -- "Funding Needs" --> Liquidity
    
    PointVal -. "Định lượng P&L" .-> MtM
    AvgRate -. "Xác định điểm hòa vốn" .-> Position

    %% Apply Classes
    class Inflow startEnd
    class Quoting,Execution,Position,Squaring core
    class Limit,Settlement,Liquidity risk
    class MtM,PointVal,AvgRate formula
    class Operations process
```

### Chú thích luồng (Whiteboard Notes):
1.  **[1] -> [3]:** Luồng giao dịch bắt đầu từ yêu cầu khách hàng, Dealer báo giá dựa trên trạng thái hiện tại (Base currency) và thực hiện khớp lệnh.
2.  **[4] -> [6]:** Sau khi khớp, trạng thái (Position) được ghi nhận và revalue liên tục theo thị trường (Mark-to-Market) để kiểm soát P&L.
3.  **[7] -> [9]:** Các rào cản rủi ro (Hạn mức, Thanh khoản bắt buộc) đóng vai trò là "điểm dừng" kỹ thuật để bảo vệ vốn của Ngân hàng.

### Các Node liên quan:
*   [[FX_Spot_Trading_Mechanics]]
*   [[Bank_Risk_Environment]]
*   [[Bank_Treasury_Glossary]]
*   [[FX_Squaring_Workflow]]

---
*Cập nhật lần cuối: 2026-04-24 (ACI Ingestion Phase)*
