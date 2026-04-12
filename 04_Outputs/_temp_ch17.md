

--- [PAGE 1] ---

CHAPTER17
Floating-Rate Notes

F
loating-rate notes (FRNs) may appear to sit oddly in a book of fixed income instru-
ments. They are bonds where the coupon is not fixed but is reset, usually at the start
of each interest period. However, as will be discussed below, under some circumstances
this feature stabilises the value of the bonds compared to other securities. The term
variable-rate note is used almost interchangeably with the term FRN but has slight con-
notation of a coupon structure that is linked to something else than benchmark interest
rates.
The cashflow structure of an FRN is shown in Figure 17.1. The specific features of
an FRN are the choices for the reference index used to calculate the coupon rate, the
coupon frequency, and the timing of the resets. In the majority of FRNs, coupons reset to
a ‘natural’ index at the begining of each coupon period. However, more complex FRNs
exist and the full spectrum of FRNs ends at highly structured products. In essence, if
one thinks of a bond coupon as a function of some inputs:

C = f(something)
(17.1)

then the standard bullet bonds discussed so far are the most simple manifestation of
this equation, namely:
f(something) = const
(17.2)

Floating-rate notes are bonds where f takes a more interesting form. Although the vast
bulk of FRNs has a very natural structure for f, some can be very complex.
The typical investor in a floating rate bond is the treasury of a deposit-taking institu-
tion, for instance a retail bank. Banks compete against other banks and other products
for deposit money. The deposit rate each bank offers is therefore a compromise between
wishing to pay a low rate (to save costs) and a high rate (to attract money). At the same
time, deposit funding competes with other funding sources that may be available to the
bank. As a result, deposit interest rates tend to follow interbank market funding interest
rates, albeit usually with a spread that reflects the higher cost of deposits. This extra cost
is linked to the need to advertise, retain customer service staff, and maintain buildings
that impress the saving public. Although deposit interest rates fluctuate, the deposits
themselves tend to remain at a bank for longer periods. Customers do not frequently
move deposit money between different banks, and for this reasons deposits are said to
be ‘sticky’.

169



--- [PAGE 2] ---

170
CASH INSTRUMENTS

FIGURE 17.1
Simple floating rate note. The bond repays its par amount at the maturity date.
The bond has regular accrual periods but coupons are reset at the beginning of each coupon
period in accordance with some pre-defined index.

As a result of this economic setting, the liability side of a bank tends to be linked to
short-term rates in the interbank market. Banks therefore are natural investors in assets
that also pay the variable interbank rates, or use derivatives to transform the cashflow
structure of other instruments into a variable-rate structure.
By the same logic, some retail investors purchase FRNs as an alternative to
holding term deposits at a bank that roll over periodically. The advantage of doing
so can be a higher coupon, but also that a FRN can be sold at any time while a
term deposit can usually only be terminated at maturity without incurring extra
penalties. Also, only banks can offer term deposits while FRN can be issued by other
entities.

17.1
COUPON RESET MECHANICS

FRNs usually reset the coupon at the beginning of the coupon period. There can be a
lag between the observation of the benchmark and the reset date. For instance, because
money market deposits settle T + 2 in most markets, the coupon used for a coupon
period starting at T will usually be the reference rate taken at T −2. Some FRNs, par-
ticularly more structured ones, have longer lags which sometimes reach 20 business
days, i.e., almost a month.
It is possible to fix the coupon later than at the start of the accrual period. Such
in-arrears structures can delay the coupon fixing to as late as the payment date. It is
meaningless to calculate an accrued interest when the accrual rate is not fixed and
in-arrears structures therefore trade on dirty, rather than clean price.
Coupons only rarely set to the benchmark itself, and instead a spread is set at
issuance, and then applied at every reset date. This spread is called the quoted margin,
called here 𝜇. The coupon on a standard FRN payable over the period starting at ti
would therefore be:
Ci = R(ti −2) + 𝜇
(17.3)

where as usual all rates are quoted in annualised terms even though FRN coupon
periods are frequently shorter than one year. Note that other formulas are possible.



--- [PAGE 3] ---

Floating-Rate Notes
171

A so-called inverse floater for instance uses a formula like:

Ci = max(0, 𝜇−R(ti −2))
(17.4)

so the coupon moves in the opposite direction of the benchmark.
Most jurisdictions do not allow negative coupons which would be payment obliga-
tions from the investor to the issuer. In addition, many CSDs are unable to process such
payments. Implicitly, therefore, Equation (17.3) is to be read as:

Ci = max(0, R(ti −2) + 𝜇)
(17.5)

This implicit coupon floor is now standard in bond documentation because there have
been frequent instances where the simple formula Equation (17.3) would have led
to negative resets. Again, nothing prevents issuers from setting the floor to any other
non-negative value and some FRNs have floors above zero. In the same vein, issuers
can furnish coupons with a cap.

17.2
LIBOR AND OIS-LINKED NOTES

The ‘natural’ coupon of a floating rate note is the interbank benchmark rate applying to
the period between two coupon resets, as pertaining at the start of the accrual period,
and the coupon formula Equation (17.3). A quarterly FRN would therefore have coupon
resets linked to the 3M Libor rate applicable in that currency.
If that is the case, then the present value of the FRN at the time of its last coupon
reset (i.e., one coupon period before maturity) would be:

P = 100 + C ∗DCF

1 + rDCF
(17.6)

where r is the appropriate discount rate applicable to liabilities of the FRN issuer. This
discount rate should be the market rate plus an appropriate spread. A quick comparison
with Equation (17.3) shows that if that spread happens to be 𝜇, then P = 100 in this
equation. At the beginning of the last coupon period, the FRN is therefore worth exactly
par if the quoted margin is equal to the credit spread of the issuer. One can now consider
the beginning of second-to-last coupon period. At the end of that period, the bond will
be worth par (as has just been shown), and an additional coupon will be paid on the
end of that period. Equation (17.6) wherefore applies again, only that in this instance
the 100 in the numerator refers to the value of the bond, not its redemption amount. It
follows that also at the start of the second-to-last coupon period the bond has a value of
par. This induction can be continued all the way to the first coupon period. The result
is that the value of an FRN is equal to par at the time of each coupon reset if the quoted
margin is the correct risk premium for the issuer.
Between coupon resets the FRN value can fluctuate because the market discount
rate applicable between the settlement date of any trade, and the market rate when the
coupon was fixed can differ. For instance, if the central bank makes a surprise rate cut



--- [PAGE 4] ---

172
CASH INSTRUMENTS

after a coupon has been fixed, the next coupon payment will reference the older, higher
central bank rate, and so the FRN price will increase to reflect the lower discount rate.
However, the effect of this mismatch between the coupon fixing and the market rate will
end with the next coupon payment. In total therefore, FRNs have a very stable market
price as long as the risk premium of the issuer remains constant.
As mentioned in the section on Libor, Section 13.6, unsecured term benchmark
rates are being phased out globally because regulators have taken the view that bench-
marks based on an economically irrelevant subset of transactions are open to abuse.
FRN issuers have therefore switched to coupons that follow overnight benchmark rates.
In principle, the coupon payment (not the annualised coupon rate) should amount to
the compounded interest on a money market account:

t1
∏

c(t −1) =

t=t0
[1 + (r(t −2) + 𝜇)DCF(t, t + 1)] −1
(17.7)

where r(t −2) is the overnight rate observed for each day t applicable to the relevant
overnight rate (note that money markets settle T+2) within the coupon period, and
DCF(t, t + 1) is the applicable daycount fraction1. This formula, however, has a struc-
tural disadvantage and therefore is not how interest is calculated on actual bonds. The
total interest amount is only known at the end of the coupon period and so it would
be difficult to define accrued interest during the accrual period. Inconveniently for the
issuer, the spread 𝜇would also be compounded, and so be not directly comparable to
the quoted margin of a standard Libor FRN.
Instead, Equation (17.7) is used to construct an intermediate term rate which is the
annualised compound interest between the last coupon payment and any settlement
date within the coupon period, including the next payment date:

d∏

t=t0
[1 + (r(t −l))DCF(t, t + 1)] −1

𝜌(t −1) =

DCF(t0, d)
(17.8)

𝜌(t) is then used in the same way as R(t) in Equation (17.3) to calculate the coupon
fixing. In this way, the quoted margin 𝜇is not compounded, and the formula can be
used to calculate interim accrued interest. This accrued interest is in effect based on
the best possible estimate of the eventual coupon payment. Somewhat unintuitively,
the standard observation lag l between the overnight rate and its application appears to
have been selected in the European market to be five business days rather than two2.

1The daycount fraction is not simply 1/360 for most currencies and 1/365 for the Commonwealth
markets because there may be a weekend or public holiday between t and t + 1.
2This convention enables a longer-than-standard T+2 settlement while retaining defined
accrued interest.



--- [PAGE 5] ---

Floating-Rate Notes
173

17.3
DISCOUNT MARGIN

Floating-rate notes do not have predictable cashflows and therefore they do not
have yields. One approach to compare expected returns of FRNs is the so-called
fixed-equivalent yield where future cash flows are projected, either by simply assuming
constant coupons, or that future reference index levels can be predicted from some
form of forward curve. In the latter case, the actual coupon formula, e.g. Equation
(17.3), can be used directly. Once cashflow projections are obtained, a yield can be
calculated from this series of irregular cashflows in the same way as for any other bond.
The more common market convention, however, is to calculate a spread known as
the discount margin. Conceptually, the discount margin 𝜇′ is the quoted margin that
would make the price of a given FRN equal to par. That suggests that one should calcu-
late it based on a discount factor term structure as:

𝜇′ = 𝜇−
P −100
∑

iDCF(ti−1 −ti)Df(ti)
(17.9)

where the denominator of this fraction acts to distribute the difference between the mar-
ket price and par across each coupon period, bearing in mind that like the quoted mar-
gin, the discount margin is quoted in annualised terms and so needs to be de-annualised
for the daycount fraction of each coupon period. As presented here, the discount mar-
gin is more closely related to the notion of an asset swap spread (cf. Section 22.3.1 on
page 222).
Equation (17.9) is straightforward if one has a discount factor curve Df(t) to hand
but amounts to relying on external instruments to build that curve. The market conven-
tion is to calculate the discount margin from the bond alone. The approach resembles
that of the yield calculation, with the added assumption that the benchmark resets in
the future will be identical to the current rate. Specifically, the dirty price of the bond P
is expressed as:

n∑

P =
(R(tl) + 𝜇)DCF(tt, t1)
1 + DCF(t, t1)(R∗(t) + 𝜇′) +

i=2
Df(j)DCF(t, ti)(R(t) + 𝜇) + 100Df(n)
(17.10)

where the discount factors Df(k) are given by the recursive relationships:

Df(k) =
Df(k −1)
1 + DCF(tk−1, tk)(R(t) + 𝜇′)
(17.11)

and:
Df(1) =
1
1 + DCF(t, t1)(R∗(t) + 𝜇′)
(17.12)

Here R(tl) stands for the last fixing of the reference index while R∗(t) is the money mar-
ket rate between the settlement date and the next coupon date (the so-called stub rate).
The discount factors Df(k) amount to the compounded discounted value of a deposit
rolling at the frequency of the FRN with an interest rate equal to the current fixing of



--- [PAGE 6] ---

174
CASH INSTRUMENTS

the benchmark rate plus the fixed spread 𝜇′ which is what this nonlinear equation needs
to be solved for. The three terms in Equation (17.10) correspond to the discounted val-
ues of the next coupon, all subsequent coupons, and the principal, in that order. This
equation needs to be solved for 𝜇′ using a non-linear solver, similar to calculating a
compound yield.
In essence, the difference between Equations (17.9) and (17.10) is that the for-
mer would lead to a different result if the forward curve of the reference rate moved,
while the latter would not. When the yield curve steepens, the discount factors Df(ti)
in Equation (17.9) decline, so the asset swap spread for a given price increases. The
definition Equation (17.10) does not depend on the current yield curve at all (only on
the two rates R∗(t) and R(t)), so the discount margin is unaffected by curve changes.
That means, just as for yields, that it is methodologically incorrect to compare discount
margins across bonds of different maturities.
When the FRN is linked to overnight rates like €STR, Equation (17.10) is no longer
appropriate because the term rates R∗(t) and R(t) do not exist, and the next coupon
R(tl) + 𝜇is unknown. The sensible solution is to use the same 𝜌(t) from Equation (17.8)
instead of these term rates.

17.4
CMS AND CMT FLOATERS

Several entities, including the French, Italian and Japanese governments, have issued
variable-rate bonds where the coupons are set with reference to a long-term rate. In the
French and Japanese cases, that rate was a 10Y government yield, while Italy issued
eurobonds with coupons linked to various swap rates, usually the 10Y swap rate. Bonds
linked to benchmark yields in the government bond and swap markets are known as
constant-maturity treasury (CMT) and constant-maturity swap (CMS) floaters. Private
issuers also issue securities with more complex CMS structures, such as coupons linked
to the spread between 2Y and 10Y CMS rates3.
The first question about such bonds is how the relevant rates can be observed, given
that bond and swap markets are over-the-counter markets where prices are negotiated
in private. For CMT rates, the French market has a well-known benchmark known as
the TEC10 which is calculated from price quotations provided by the primary dealers in
French bonds. In Japan, the yields seen in the most recent government bond auction,
given the large volume transacted in such auctions, give a reliable pricing. For CMS
rates, standard fixings exist in the same way as Libor fixings4. Such fixing rates are now
subject to the same governance rules as other benchmark rates.
Because the fixing rate for the coupon does not coincide with the discount rate
applicable to the coupon period, Equation (17.6) does not have the effect of keeping
bond prices close to par. Instead, CMT and CMS structures have complex exposures

3This particular structure would be a 2–10 CMS steepener.
4At the time of writing, the Intercontinental Exchange (ICE) provides swap rate fixings for var-
ious currencies. These fixings were in the past administrated by the International Swap Dealers
Association and are therefore still sometimes colloquially called ISDAfix.



--- [PAGE 7] ---

Floating-Rate Notes
175

to long-term interest rates given that increasing long-term rates have both the effect of
higher forward rates (and thereby expected coupon resets) and lower discount factors.
The two effects partly counteract each other in their impact on bond prices so that the
convexity adjustment in their pricing is substantial.
CMS structures are generally easier to hedge than CMT structures because paying
or receiving swaps has a lower balance sheet cost than holding long or short positions
in bonds with the attendant repo operations. As a result, CMT portfolios are usually
hedged with CMS structures, exposing the hedge to basis risk. In this case, the risk is a
change in the CMS–CMT spread, which is in essence the swap spread of the government
bond curve.

