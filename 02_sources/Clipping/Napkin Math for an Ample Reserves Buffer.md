---
title: "Napkin Math for an Ample Reserves Buffer"
source: "https://rocarmenter.substack.com/p/napkin-math-for-an-ample-reserves"
author:
  - "[[Roc Armenter]]"
published: 2026-04-14
created: 2026-04-23
description: "After an avalanche of exactly two questions on the buffer needed to preserve reserves as ample, I am sharing my napkin trick to easily guess-estimate the amount. And somehow it works pretty well."
tags:
  - "clippings"
---
*The views expressed here are mine and do not necessarily reflect the views of the Federal Reserve Bank of Philadelphia or elsewhere in the Federal Reserve System.*

**Mini-news**: Annette posted her [TGA proposal slides](https://drive.google.com/file/d/1uY9iuLuRft9mBKhYFU6clBM1pslnugXD/view) on her website, so I will soon leverage my discussion to share her idea, my observations, and the options ahead here.

Meanwhile, one reader and one conference participant asked the same question: how did you compute the buffer for ample reserves of $150-250 bn? Some knowledge of how the Fed's balance sheet works would be very useful today. If you dare, I wrote another post, doing my best to get anyone up to speed with a chuckle or two, and not a iota more.

Proceed below for a quick read, the headline number, and the details.[^1]

## SitRep

- The Treasury General Account (TGA) is extremely volatile, and at high frequencies, any change in TGA is met with the opposite change in Reserves.
- A large, unexpected increase in the TGA could trigger loss of rate control and a subsequent intervention by the Desk at FRBNY—think September 2019, New York City.[^2]
- The Desk operates with a buffer to reduce “fault risk,” aware that the effective supply of reserves will vary outside its control between the Desk's regular interventions.

## What do we want? A number! Where do we want it? On a napkin!

![This image was so much easier to produce than half of this post.](https://substackcdn.com/image/fetch/$s_!dR66!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb74bdd08-6e7d-4e38-ba86-bbce2246f3ff_2048x2048.png)

This image was so much easier to produce than half of this post.

## Executive summary

The napkin formula for the buffer, in billions of dollars, is

$B = \sqrt{\Delta} \sigma z^{*} \left(\right. \frac{\epsilon \Delta}{2} \left.\right) ,$

where `\sigma>0` is the standard deviation of the change in the TGA, in billions of dollars; `\Delta>0` is the length of time between regular Desk operations; and `z*` is the critical value for a standard Normal CDF.[^3] Key parameter `\epsilon>0` governs the risk appetite: The buffer is set such that the probability of an undesirable event at any time during the interval is

$Pr \left(\right. \text{no bueno} \left.\right) = \epsilon \Delta .$

I am being facetious, as usual, but I am also advertising how little information is needed for the exercise: As long as the undesired event is triggered by a *low* level of reserves, the calculation of the buffer only requires the accepted fault probability—we need neither the always-elusive *level* of ample reserves nor the details of the undesired event.

Next, I plug in the parameter values I deem realistic—but I just shared the formula, so feel free to plug in yours.

- Let me start with `\Delta`. The idea is that the Desk will be conducting Reserve Management Purchases (RMPs) under the FOMC directives, sharing expected operations and tentative schedules.[^4] The interval `\Delta` captures a short period during which the Desk can only resort to outright intervention, like in September 2019, to restore reserves to the banking system.
	- I went for two weeks, the old reserve maintenance period. That is on the short end and pretty close to “active management,” if you ask me.
		- Do not use napkin math to explore periods longer than two months; it can substantially overstate the buffer.
		- **If you are not going to vary the period**, choose the unit of time such that `\Delta = 1`. Then remember that choice for the other parameters.
- Let’s continue with `\sigma`. For the period 2021-25, one standard deviation in the change of the TGA *over two weeks* is about $100 billion.
	- Month-to-month, the standard deviation in the change is a bit below $150 billion. Since we doubled `\Delta`, we can check whether `\sqrt{2}` $100 billion, or $142 billion, is close enough to the data. It is.
- Finally, the FOMC's risk tolerance is truly in the eye of the beholder, leaving us to talk ourselves into a value for `\epsilon`. Noting that the fault probability is halved since faults are one-sided, a critical value `z*` of 3 is roughly associated with 99.5% confidence or once every 200 months.
	- If you change `\Delta`, do not forget to adjust `z*`!

So lots of words to end up just tripling $100 bn. Since I felt the period is on the short side and the standard deviation is on the low side, I would rather bracket the number to the upside and end up with a guess-estimate of $300-400 bn.

What I like the most about the napkin math is… doing it again! For example, what if the TGA were to return to pre-pandemic management practices? I find that the standard deviation of TGA changes was a bit more than $50 bn. from 2016 to 2019. That is about half, and the napkin says that the buffer is linear in `\sigma. `Hence, a return to the pre-pandemic TGA volatility would allow a smaller buffer of between $100-150 billion.

That’s it, really. Below, I have included the math, though the derivation is quite standard. I briefly discuss why I think the napkin math holds up for periods of two months or shorter—but not longer. I also discuss a couple more caveats. Perhaps the most important one to note is that the Desk, perhaps in collaboration with the Treasury, can forecast high-frequency changes in reserves and money markets, and I would expect the standard deviation of the forecast errors to be smaller than that of the changes in TGA.

## The Math

Time is continuous. At regular intervals of length `\Delta`, the central bank supplies \`\`ex-ante’‘ reserves `M(t)`, which are fixed over the interval `[t, t+\Delta)`. The problem is identical across intervals, so we can focus on the first interval `[0,\Delta)` without loss of generality.

At all times, autonomous factors determine the effective supply according to

$\hat{M} \left(\right. t \left.\right) = M \left(\right. t \left.\right) + \sigma X \left(\right. t \left.\right) ,$

where `X(t)` is a standard Wiener process, with zero mean (without loss of generality) and unit variance.

There exists a fixed threshold `M*` such that if, at any time t, `\hat{M}(t) < M*`, an undesirable failure event arises. A key advantage of the formulation here is that we can obtain a guess-estimate of the buffer without needing to specify the value of `M*` or the nature of the failure event.

We assume the central bank will tolerate a small failure rate `\epsilon`, scaling linearly with the interval `\Delta`. That is, the central bank aims to minimize `M(0)` subject to

$Pr \left(\right. \underset{t \leq \Delta}{min} \hat{M} \left(\right. t \left.\right) \leq M^{*} \left.\right) \leq \epsilon \Delta .$

Note that failure is one-sided, unlike [Haubrich (2023](https://www.clevelandfed.org/publications/working-paper/2023/wp-2325-balance-sheet-policy-in-an-ample-reserves-framework)), which considers a similar \`\`inventory management’‘ problem but with two-sided costs.

Define the normalized buffer as

$b := \left(\right. M \left(\right. 0 \left.\right) - M^{*} \left.\right) / \sigma$

and the fault tolerance constraint becomes

$Pr \left(\right. \underset{t \leq \Delta}{min} X \left(\right. t \left.\right) \leq - b \left.\right) \leq \epsilon \Delta .$

Now we call upon the standard properties of a standard Wiener process starting at zero,

$Pr \left(\right. \underset{t \leq \Delta}{min} X \left(\right. t \left.\right) \leq - b \left.\right) = 2 \Phi \left(\right. \frac{- b}{\sqrt{\Delta}} \left.\right) ,$

where `\Phi` is the standard normal CDF. Rather trivially, the central bank will set initial reserves such that??? is binding. We can now solve:

$b = \sqrt{\Delta} \left(\right. - \Phi^{- 1} \left(\right. \epsilon \Delta / 2 \left.\right) \left.\right)$

and returning to billions of dollars,

$B = \sigma \sqrt{\Delta} \left(\right. - \Phi^{- 1} \left(\right. \epsilon \Delta / 2 \left.\right) \left.\right) ,$

which is the equation in the napkin.

## Caveats

Or not.

**There are no demand shocks or other supply shocks.** True, but… do you know one Hobokenite sang the line “if you make it here, you can make it anywhere?” Well, if reserves are ample given TGA shocks, they are ample enough for the other shocks.[^5]

**The Desk is blind.** That is a bit mean, but is perhaps the hole in the donut here. If you believe that the Desk can forecast TGA, other shocks to reserves and markets… then there is a predictable path ahead for effective supply of reserves. The exercise can easily be modified, but unfortunately, we then need the standard deviation of the Desk’s forecast *errors*.

**Layered vs. active management.** I do not know how to explain this in fewer than a thousand words.

**The TGA is not really a martingale**. True, but it is not a bad approximation for relatively short intervals, up to 2 months perhaps. The reason is likely that whatever mean-reversion forces act upon the TGA, they operate at a quarterly frequency stemming from the Treasury’s preference for announcements and predictability.

The key feature of a Wiener process is that the variance scales linearly with the length of the interval. The plot below shows what the data have to say about this:

![](https://substackcdn.com/image/fetch/$s_!a-hh!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19372a72-b2b0-4979-bc2b-c975e301df71_1050x750.png)

This looks pretty linear to me in both pre- and post-pandemic episodes for the first 6 weeks, and in the post-pandemic episode, perhaps up to 8 weeks.

[^1]: Substack's inability to allow for inline math has made this post approximately 39.23% harder. Grammarly also cannot believe I would include math in my text.

[^2]: Not [this](https://www.usopen.org/en_US/news/articles/2019-09-08/rafael_nadal_defeats_daniil_medvedev_in_fiveset_2019_us_open_final.html)

[^3]: Can you put math in a footnote? Yes, as long as the text is not below the math (?!). `Phi` is the standard normal CDF,

$z^{*} \left(\right. p \left.\right) := - \Phi^{- 1} \left(\right. p \left.\right) .$

[^4]: [Currently](https://www.newyorkfed.org/markets/reserve-management-reinvestment-purchases-faq), “ *the monthly amount of secondary market Treasury purchases on or around the ninth business day of that month alongside a tentative monthly schedule of operations expected to take place between the middle of the month and the middle of the following month that communicates the operation dates, times, security types, maturities, and maximum transaction amounts*.”

[^5]: Squared caveat! If shocks are correlated, we need to go back to the drawing board. As far as I can tell, none of the shocks to reserves are correlated at the frequencies we are looking at.