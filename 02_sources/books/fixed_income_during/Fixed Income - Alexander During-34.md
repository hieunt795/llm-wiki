---
title: "Fixed Income - Alexander During-34"
type: raw_source
source_pdf: "Fixed Income - Alexander During-34.pdf"
extractor: docling
---

## PART Seven

## Risk Management

## CHAPTER 33

## Principal Component Analysis

P rincipal component analysis (PCA) is a useful statistical technique for dimension reduction of multivariate normally distributed data that can easily be implemented using standard statistics packages. A useful starting point are mean and standard deviation of a univariate normal random variable. While the mean is the centre of the distribution, the standard deviation provides a measure of how far the data is spread around the mean.

PCA is used throughout this book but presented here in the risk management section because it is particularly convenient for reducing the dimensionality of a complex system.

In 2 dimensions, standard deviation becomes a less well-defined concept. If one were to use a ruler to measure the extent of the distribution, it is clear that one point of the ruler should coincide with the mean, but it is not obvious in which direction the ruler should point. It turns out that if the standard deviation is measured and marked with the ruler in all possible directions, the resulting marks form an ellipse (cf. Figure 33.1).

This is related to a different problem which can be described in terms of the usual characters in cryptography: If Alice, after an initial transmission of some information, had to repeatedly describe to Bob a sample of a bivariate distribution ( x i , y i ) with a single number z i , how should she calculate that number? One possibility would be to choose 1 of the dimensions, e.g. z i = x i . For any given value of x , however, there is a range of likely values of y , and vice versa. Could there be a linear combination z i = /u1D6FC x i +/u1D6FD y i so that Bob has the lowest uncertainty about ( x , y ) whenreceiving only z i from Alice?

The relationship between the 2 problems is that the optimal /u1D6FC and /u1D6FD will reduce the standard deviation of the estimate ( x ′ , y ′ ) made from the value z to a minimum. As such, the problem of reducing dimensionality (here from 2 to 1) can be expressed as an estimation problem.

Before moving on, the next question is why it should be sufficient to consider linear models given the multitude of non-linear relationships discussed throughout this book. The answer is that one is often faced with risk analysis around a given point (usually the current set of market rates /u1D717 ), and risk is then the change in portfolio value for small changes ∆/u1D717 in these rates. One therefore has a problem that can be represented by a Taylor series:

FIGURE 33.1 Standard deviations of a highly correlated bivariate normal distribution of 2 variables x and y with the 2 eigenvectors of the covariance matrix (EV1 and EV2). The somewhat unusual chart format was chosen to preserve the right angle between the 2 orthogonal eigenvectors.

<!-- image -->

<!-- formula-not-decoded -->

Having a linear term therefore is valid as the first step in the approximation.

Conceptually, PCA can be explained as the process of extracting the single linear combination of variables ∑ i /u1D6FD 1 , i x i that explains most of the variance of the data set. In this case, /u1D6FD i would be the first PCA factor. The projection /u1D6FD 1 x = z 1 is known as the realisation of this factor. The next PCA factor is then the combination of variables that explains most of the variance of x -z 1 /u1D6FD 1 . The third PCA factor then explains most of the variance remaining after the first two factors x -z 1 /u1D6FD 1 -z 2 /u1D6FD 2 etc. In the communication problem above the best single variable for Alice to communicate to Bob is z 1 , if he could communicate 2 numbers, the optimal choices would be z 1 and z 2 , etc. For a hedger, the most important risk to hedge against is a change in z 1 , once this is hedged, the next most important risk is z 2 and so on.

Instead of using this iterative process, one can obtain all PCA factors in a single step because they are simply the eigenvectors of the covariance matrix of the observations x i . To recall, eigenvectors are the vectors /u1D6FD satisfying the equation:

<!-- formula-not-decoded -->

The eigenvector corresponding to the largest eigenvalue /u1D706 is the first PCA factor and so on. The eigenvalues /u1D706 measure the standard deviation of the data set in the direction of the corresponding eigenvector as shown in Figure 33.1. Most standard numerical libraries contain ready-made routines for the simultaneous calculation of eigenvectors and eigenvalues.

Two considerations need to be made when producing a PCA: whether to construct the covariance matrix from levels or changes, and whether to normalise the covariance matrix, i.e., use the correlation matrix.

The levels versus changes choice is essentially related to the unit root problem in ordinary least squares regression analyses. If the series under consideration is stationary, levels and changes will produce the same eigenvectors. If the series are not stationary, then taking first differences makes them stationary. On the face of it, therefore, one should always conduct PCA on levels rather than changes. That being said, if the series is not stationary, then some assumptions related to the use of PCA may not hold.

The choice between covariance and correlation matrix similarly depends on the problem at hand. When constructing yield curve hedges, there is no point in normalising volatility at different points of the curve because the point of the analysis is precisely to adjust to such variations in volatility. When considering performances of equity and bond indices, however, the index levels or changes depend largely on the scale of the index, and these are largely a function of when the index in question was established. Normalising away such historical artefacts is a useful first step.

## 33.1 PCAAS GENERALISED REGRESSION

As in other disciplines, it is often necessary in finance to relate 2 variables in a linear equation, i.e.,

<!-- formula-not-decoded -->

One can estimate /u1D6FC and /u1D6FD from N pairs of observed data ( x i , y i ) using standard regression equations:

<!-- formula-not-decoded -->

The problem with financial variables is that it is usually not obvious which variable is dependent or independent. For example, when estimating a hedge ratio between 2 different bond yields, none of the 2 is obviously the independent variable. The problem is that when Equation (33.3) is re-formulated as the inverse problem:

<!-- formula-not-decoded -->

one would expect that because changing x by 1, Equation (33.3) implies a change in y of /u1D6FD , that /u1D6FD ′ in Equation (33.5) would be equal to 1 ∕/u1D6FD . Running the regression Equation (33.4) given above with exchanged variables x and y will, however, not yield that result with real data.

The problem is that Equation (33.4) makes an implicit assumption, namely that x can be measured with certainty while y may be subject to noise, i.e.,

<!-- formula-not-decoded -->

The more realistic approach for financial variables is usually that there is an underlying factor z that drives the evolution of both x and y but both these 2 dependent variables are subject to additional, unknown noise:

<!-- formula-not-decoded -->

One can write this in matrix form if the 2 noise terms are correlated:

<!-- formula-not-decoded -->

where neither z nor /u1D700 are directly observable but z is assumed to be the signal while /u1D700 is noise. Under the additional assumption that the signal term z dominates the variance of x and y , one arrives at a PCA problem: The eigenvector of the covariance matrix of x and y corresponding to the largest eigenvalue, i.e. the ratio /u1D6FD y ∕/u1D6FD x will provide a better estimate for the regression coefficient between y and x than Equation (33.4), and trivially one finds that the inverse relationship holds true when swapping x and y . The evolution of z would then be interpreted as that of the common factor driving both x and y .

Because the characteristic polynomial of a 2x2 matrix is quadratic, there is a closed-form solution for this problem:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

so:

The required eigenvector is the one corresponding to the larger eigenvalue /u1D706 + . Without normalisation:

<!-- formula-not-decoded -->

The second component of v + , (/u1D706 + var x )∕ cov xy ) in this equation, is comparable to the /u1D6FD in Equation (33.3). The associated /u1D6FC is easily recovered from &lt; y &gt;= /u1D6FD &lt; x &gt; +/u1D6FC as:

<!-- formula-not-decoded -->

## 33.2 MEASURING DATA COMPLEXITY WITH PCA

Asomewhat unconventional but nevertheless edifying use of PCA is the measurement of the complexity of curve dynamics. To recall, the eigenvalues of the covariance matrix measure the contribution of the corresponding eigenvector to the total variance of the sample. This suggests two uses of these eigenvalues. The standard one is the measurement of curve volatility, which utilises the absolute values of these eigenvaues. An alternative use of eigenvalues is to consider their relative magnitudes. If a single eigenvalue dominates total sample volatility, then the dynamic of the entire curve is largely determined by a single factor. Independently of whether the curve is volatile or not, such a single-factor curve would be considered somewhat uninteresting. In contrast, finding several eigenvalues with higher values signals a more complex curve dynamic.

To use this approach, one conducts PCA on rolling data windows, as shown in Equation (33.2). The yields shown are the raw spline yields at various maturities that enter the PCA. Instead of using the complete sample, a rolling window is pulled across time and PCA is applied on the covariance of changes inside this window as it moves along the time axis. This means that the covariance matrix becomes a time series, as do derived quantities such as the eigenvalues.

Furnished with the time series of eigenvalus, one can proceed to construct complexity measures. The standard quantity to express the degree of dominance in economics is the Herfindahl index, which is the sum of squares of market shares of firms in a given market. One can easily apply the same ideas to PCA eigenvalues and construct the quantity:

<!-- formula-not-decoded -->

from the eigenvalues e i . Figure 33.3 shows the evolution of this quantity when calculated on a rolling basis for two different yield curves. The high volatility of the curve after the outbreak of the Corona crisis in 2020 is shown clearly in the drop in the German Herfindahl index which implies that curve movements became less dominated by a single factor.

Analternative interpretation of this quantity is that it gives guidance on the appropriate hedge strategy for a given portfolio. A high value of the index suggests dominance of a single PCA factor which implies that a single hedge instrument should suffice to cover the bulk of portfolio risk. A lower value means more complex dynamics and the requirement for more hedge instruments.

Instead of calculating this index for different points of a single curve, as done above, one can conduct the same PCA on the same points of multiple curves, for instance, the yields of multiple issuers. The resulting Herfindahl index would then help identify 'interesting' spread dynamics (bouts of name-specific risk aversion) that require complex hedge strategies.

FIGURE 33.2 Spline par yields of the US Treasury curve through time. Source: Data from treasurydirect.gov.

<!-- image -->

FIGURE 33.3 Herfindahl indices calculated from a rolling PCA of the US and German spline yields. History 2014-2020, rolling 90 business day window. Source: Data from treasurydirect.gov and Bundesbank.

<!-- image -->

This is done in Figure 33.4 for various Japanese issuer curves at two different maturity points (5- and 10-year) although the data shows that there is a fair degree of correlation between the spreads at these 2 points. Again, one would use such analyses as guidance to either the times when spread dynamics turn interesting, or to the required complexity of a hedge structure.

Relying on rolling correlation matrices is not without problems, however. Choosing long window lengths means that new data has a low weight in the estimation of the correlation matrix so it takes some time for structural changes in dynamics to be visible in the analysis. On the other hand, shorter windows usually lead to more volatility in the observed matrices. If the results are to be used for designing appropriate hedge strategies, such volatility could create unwarranted frequent adjustments.

FIGURE 33.4 Herfindahl indices calculated from a rolling PCA of Japanese government bond and other issuer spline yields (issuers are Tokyo Metropolis, Osaka Prefecture, Kanagawa, JFM, Japan Expressway, JR East, JR West, Tokyo Electric, Kansai Electric, Chubu Electric). Source: Data from JSDA.

<!-- image -->