---
title: Scatter Plot Density Visualization
aliases:
- Density Scatter Plot
- Probability Density Scatter Plot
type: mechanism
tags:
- data-visualization
- chart-design
- analysis
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch01.md"
thesis: To prevent outliers from optically dominating a chart, data points are augmented
  with probability density information using 2D Gaussians and isolines, revealing
  the true concentration of observations.
source_refs:
- file: Fixed_Income_Alexander_During_Ch01.md
  page: 8
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

The human eye tends to perceive multiple overlapping data points as a single point, which can lead to the visual overvaluation of outliers in a standard scatter plot. To mitigate this effect, a specific form of scatter plot is used throughout this analysis that represents the actual observations alongside their calculated probability density.

## Mechanism

The visualization method follows a multi-step process to reveal the underlying concentration of data:

1. **Calculate individual Gaussians:** For each individual data point, a two-dimensional Gaussian distribution is calculated.
2. **Determine Variance:** The variance in the $x$ and $y$ directions for the entire set of observed data points is used as the basis for these Gaussians.
3. **Evaluate on a Grid:** These individual Gaussians are evaluated on a regular grid and then summed across all data points to create a composite **Probability Density Function (PDF)**.
4. **Represent via Greyscale:** The resulting PDF is represented as a greyscale background behind the standard dots of the scatter plot.
5. **Add Isolines:** Topographic-style isolines are added to provide further visual depth and clarity to the resulting density shape.

### Key Benefits
- **Corrects for Overlap:** Prevents densely packed points from appearing as a single observation.
- **Accurately Weights Outliers:** Places outliers in the context of the main data mass.
- **Topographic Context:** Isolines provide a clear "map" of the data distribution.

## Convention

This method is particularly effective for datasets where:
- The number of observations is high (thousands of points).
- Data tends to cluster heavily in specific regions.
- Visualizing "hotspots" is more important than identifying every individual point.

[extracted] [[Fixed_Income_Alexander_During_Ch01.md#page=8]]

## Evidence / Source Anchors

- Discussion on visual overvaluation of outliers: [[Fixed_Income_Alexander_During_Ch01.md#page=8]]
- Technical steps of Gaussian summation and grid evaluation: [[Fixed_Income_Alexander_During_Ch01.md#page=8]]
- Visual description of greyscale and isoline usage: [[Fixed_Income_Alexander_During_Ch01.md#page=8]]

## Related

- [[Yield_Curve_Sectoral_Analysis]] — Where this visualization is frequently applied to show bond richness/cheapness clusters.
- [[ACM_Curve_Decomposition]] — Another area where high-density data visualization is utilized.
