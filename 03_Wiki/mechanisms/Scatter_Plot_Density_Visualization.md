---
type: mechanism
trigger: "Cần trực quan hóa scatter plot có nhiều điểm trùng nhau"
output: "Scatter plot có probability density background dạng greyscale + isolines"
constraints: ["Sử dụng Gaussian 2D cho mỗi data point", "Variance theo x và y direction"]
sources: ["Fixed Income - Alexander During-2.pdf"]
confidence: low
provenance: extracted
created: 2026-04-13
chapter: 1
---

# Scatter Plot Density Visualization

## Cơ chế

Phương pháp trực quan hóa scatter plot đặc biệt được Düring sử dụng xuyên suốt sách. Giải quyết vấn đề: khi nhiều điểm rơi gần nhau, mắt người chỉ thấy **một điểm** → **optically overvalues outliers**. [extracted] [[Fixed Income - Alexander During-2.pdf#page=8]]

### Quy trình

1. Cho mỗi data point, tính một **2D Gaussian** sử dụng observed variance theo chiều $x$ và $y$
2. Evaluate các Gaussians riêng lẻ trên **regular grid**
3. Cộng tất cả Gaussians → **probability density function**
4. Hiển thị PDF dưới dạng **greyscale** phía sau các dots thông thường
5. Thêm **isolines** (đường đồng mức) theo kiểu bản đồ địa hình

[extracted] [[Fixed Income - Alexander During-2.pdf#page=8]]

## Điều kiện

- Cần đủ data points để density có ý nghĩa
- Giả định Gaussian distribution cho mỗi data point (có thể không phù hợp với dữ liệu multimodal)

## Ví dụ số

Düring cho biết phương pháp này được sử dụng xuyên suốt sách cho các scatter plot. [extracted] [[Fixed Income - Alexander During-2.pdf#page=8]]

## Nguồn

- [[Fixed Income - Alexander During-2.pdf#page=8]] — "A quick word on charts"
