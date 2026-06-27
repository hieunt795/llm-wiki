---
title: "Choudhry_Analysing_Yield_Curve"
type: raw_source
source_pdf: "Choudhry_Analysing_Yield_Curve.pdf"
extractor: docling
---

<!-- image -->

## Analysing and Interpreting the Yield Curve

Founded in 1807, John Wiley &amp; Sons is the oldest independent publishing company in the United States. With offices in North America, Europe, Australia, and Asia, Wiley is globally committed to developing and marketing print and electronic products and services for our customers'   professional and personal knowledge and understanding.

The Wiley Finance series contains books written specifically for finance and investment professionals as well as sophisticated individual investors and  their  financial  advisors.  Book  topics  range  from  portfolio  management to e-commerce, risk management, financial engineering, valuation and financial instrument analysis, as well as much more.

For a list of available titles, visit our website at www.WileyFinance.com.

## Analysing and Interpreting the Yield Curve

Second Edition

## MOORAD CHOUDHRY

With contributions from Polina Bardaeva, Ken Kortanek, Kevin Liddy, Wolfgang Marty and Vladimir Medvedev First published 2004

<!-- image -->

Second Edition published 2019 © 2004, 2019 Moorad Choudhry

## John Wiley &amp; Sons Ltd

## Registered office

John Wiley &amp; Sons Ltd, The Atrium, Southern Gate, Chichester, West Sussex, PO19 8SQ, United Kingdom

For details of our global editorial offices, for customer services and for information about how to apply for permission to reuse the copyright material in this book, please see our website at www .wiley.com.

All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording or otherwise, except as permitted by the UK Copyright, Designs and Patents Act 1988, without the prior permission of the publisher.

Wiley publishes in a variety of print and electronic formats and by print-on-demand. Some material included with standard print versions of this book may not be included in e-books or in print-ondemand. If this book refers to media such as a CD or DVD that is not included in the version you purchased, you may download this material at http://booksupport.wiley.com. For more information about Wiley products, visit www.wiley.com.

Designations used by companies to distinguish their products are often claimed as trademarks. All brand names and product names used in this book are trade names, service marks, trademarks or registered trademarks of their respective owners. The publisher is not associated with any product or vendor mentioned in this book.

Limit of Liability/Disclaimer of Warranty: While the publisher and author have used their best efforts in preparing this book, they make no representations or warranties with respect to the accuracy or completeness of the contents of this book and specifically disclaim any implied warranties of merchantability or fitness for a particular purpose. It is sold on the understanding that the publisher is not engaged in rendering professional services and neither the publisher nor the author shall be liable for damages arising herefrom. If professional advice or other expert assistance is required, the services of a competent professional should be sought.

The views, thoughts and opinions expressed in this book are those of the author in his individual private capacity and should not in any way be attributed to any employing firm, or to Moorad Choudhry as a representative, officer, or employee of any employing institution or affiliated firm.

Whilst every effort has been made to ensure accuracy, no responsibility for loss occasioned to any person acting or refraining from action as a result of reading any material in this book can be accepted by the author, publisher or any named person or corporate entity. The author may or may not hold, or have held, any security identified in this book.

## Library of Congress Cataloging-in-Publication Data

| Names: Choudhry, Moorad.                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Title: Analysing and interpreting the yield curve / Moorad Choudhry.                                                                                                                                                                                  |
| Other titles: Analysing &interpreting the yield curve &#124; Analyzing and interpreting the yield curve                                                                                                                                               |
| Description: Second edition. &#124; Chichester, UK : Wiley, 2019. &#124; Series: Wiley finance &#124; Revised edition of the author's Analysing and interpreting the yield curve, c2004. &#124; Includes bibliographical references and index. &#124; |
| Identifiers: LCCN 2018056454 (print) &#124; LCCN 2018057854 (ebook) &#124; ISBN 9781119141068 (AdobePDF) &#124; ISBN 9781119141051 (ePub) &#124; ISBN 9781119141044 (hardback)                                                                        |
| Subjects: LCSH: Bonds-Valuation-Econometric models. &#124; BISAC: BUSINESS& ECONOMICS / Banks &Banking.                                                                                                                                               |
| Classification: LCC HG4651 (ebook) &#124; LCC HG4651 .C6793 2019 (print) &#124; DDC 332.63/23-dc23                                                                                                                                                    |
| LC record available at https://lccn.loc.gov/2018056454                                                                                                                                                                                                |
| Cover Design: Wiley                                                                                                                                                                                                                                   |
| Cover Images: top: © Gen Epic Solutions/Shutterstock, bottom: © hywards/shutterstock                                                                                                                                                                  |
| Set in 10/12pt and Sabon LT Std by SPi Global, Chennai                                                                                                                                                                                                |
| Printed in Great Britain by TJ International Ltd, Padstow, Cornwall, UK                                                                                                                                                                               |

For Lindsay Ultimate Yummy Mummy

<!-- image -->

## Contents

| Foreword                                                  | ix   |
|-----------------------------------------------------------|------|
| Preface                                                   | xi   |
| Preface to the First Edition                              | xiii |
| Acknowledgments                                           | xv   |
| About the Author                                          | xvii |
| PART 1                                                    |      |
| INTRODUCTION TO THE YIELD CURVE                           | 3    |
| CHAPTER 1                                                 |      |
| The Yield Curve                                           | 5    |
| CHAPTER 2                                                 |      |
| A Further Look at Spot and Forward Rates                  | 61   |
| PART 2                                                    |      |
| YIELD CURVE MODELLING AND POST-2008 YIELD CURVE ANALYTICS | 93   |
| CHAPTER 3                                                 |      |
| Interest Rate Modelling I: Primer on Basic Concepts       | 95   |
| CHAPTER 4                                                 |      |
| Interest Rate Modelling II: The Dynamic of Asset Prices   | 115  |

vii

| CHAPTER 5 Interest Rate Models I                                                                                        | 139   |
|-------------------------------------------------------------------------------------------------------------------------|-------|
| CHAPTER 6                                                                                                               |       |
| Interest Rate Models II                                                                                                 | 163   |
| CHAPTER 7                                                                                                               |       |
| The Index-Linked Bond Yield Curve                                                                                       | 181   |
| CHAPTER 8                                                                                                               |       |
| Yield Curve Analytics in the Post-2008 era                                                                              | 193   |
| CHAPTER 9                                                                                                               |       |
| negative Interest Rate Analytics                                                                                        | 219   |
| PART 3                                                                                                                  |       |
| FITTING THE YIELD CURVE                                                                                                 | 229   |
| CHAPTER 10                                                                                                              |       |
| estimating and Fitting the Yield Curve I                                                                                | 231   |
| CHAPTER 11                                                                                                              |       |
| estimating and Fitting the Yield Curve II                                                                               | 253   |
| PART 4                                                                                                                  |       |
| YIELD CURVES AND RELATIVE VALUE TRADING                                                                                 | 277   |
| CHAPTER 12                                                                                                              |       |
| Yield Curves and Relative Value                                                                                         | 279   |
| CHAPTER 13                                                                                                              |       |
| Identifying Relative Value in the US Treasury Market: Acquiring new Benchmark Definitions from an Ancillary Yield Curve | 291   |
| Appendix: Bond Yield Measurement                                                                                        | 321   |
| Index                                                                                                                   | 353   |

## Foreword

I t is an honour to be asked to contribute a few words at the beginning of this publication.

Moorad and I first met back in 2010. We were both attending the Group Balance Sheet Management Committee at The Royal Bank of Scotland, our employer at the time. Although I forget the specific theme of the discussion, I remember our desire, incidentally which was not necessarily shared by the other committee members, to investigate and better understand a trend in the balance sheet of our organisation and in the wider economy.

Respecting  each  other's  viewpoint,  we  quickly  became  good  friends. However, we are like 'chalk and cheese'. In Belbin's terminology,   Moorad possesses  many  of  the  qualities  of  the 'Plant'  and 'Resource  Investigator', being creative, imaginative and free-thinking as well as outgoing and enthusiastic, whereas I am most comfortable in the role of the 'Completer Finisher'.

Although our shared passion for the financial markets became evident at  our  first  meeting,  it  was  only  later  I  realised  Moorad  also  possesses  a burning  desire  to  pass  on  his  knowledge,  understanding  and  perceptive insights to others, by either delivering lectures and presentations or through the written word.

I first became aware of Moorad's teaching skills in 2014 when he invited me to speak to students studying for the Certificate of Bank Treasury Risk Management. This is  a  practitioner-oriented  professional  qualification  in bank asset-liability  management,  which  is  delivered  to  a  global  audience and was developed by Moorad and the team from WBS Training Ltd. There are also his numerous short course and conference performances I could highlight, all with financial risk management as the enduring theme.

When it comes to writing, Moorad is both versatile and prolific. By my counting, this updated edition of Analysing and Interpreting the Yield Curve is his third book of the year so far. However, there's still a way to go to catch Corin Tellado, a renowned Spanish author who published over 4,000 novels in her lifetime. The comparison is probably unfair as it is doubtless a more difficult challenge to combine risk management theory, practice and current market developments in a captivating read, whilst also pursuing a full-time career in banking!

Moorad is a past master at simplifying complex ideas and communicating them in an easy going and engaging manner. In these respects, this book is no different to all his other publications. Compared to the first edition, sections have been added for the latest developments in the financial markets, including: the multi-currency yield curve, the SONIA curve, the interpretation of negative yield curves, a post-crash discounting technique for the swap curve and how to use the theoretical and observed US Treasury curve as a means of identifying relative value in bond spread trades. These concepts will be of interest to anyone working in the bond markets, be they a trader, sales-person, fund manager, research analyst, investor or issuer, or, like me, simply a student of the financial markets.

I commend this book to you, hope you enjoy the read and leave you with the words of Benjamin Franklin:

An investment in knowledge pays the best interest.

Chris Westcott

Former Treasurer, Retail and Wealth Division The Royal Bank of Scotland 1 May 2018

## Preface

T he yield curve, and everything about it, was my first and most intense love in finance. It probably still is. I could talk about it for hours, at any time, day or night. I think it is the most significant topic in banking, the very foundation of finance. But it's interesting to me to observe how the perception, and  indeed  the  requirement,  for  technical  excellence  in  banking  changes subtly the more senior the level of practitioner. The higher one rises in the profession, the less it would appear that one needs to know about subjects such as the curve, how to interpret it, how best to interpolate it, and how to understand and make sense of what it's trying to tell us. What I thought was the most important and vital issue in finance, something that absolutely everyone had to know about, turns out to be just one more arcane specialism that is not discussed that often at the bank's asset-liability committee (ALCO), hardly at all at the executive management committee (EXCO), and fewer times still at the Board.

No matter, I still think that it's a very important topic and it's a pity that it isn't viewed in this way by everyone in banking. But that's their look out. The fact that you are reading this book shows that you agree that it's a worthwhile topic to get to grips with!

So, fully 15 years after the first edition, is there anything new to write about on the curve? As it happens, yes, a fair bit. The global financial markets are a very different beast today compared to what they were in 2003. Of course, the fundamentals of yield curve analysis, interpolation, and interpretation remain unchanged. But the behaviours of curves are different in various nuanced ways (and some not so nuanced, and in fact very much 'in your face' - for example, the negative interest rate curves that are a commonplace in some countries in the eurozone). That's why I think this book was worth updating, so that we might cover issues such as multi-currency curves, the overnight index swap (OIS) curve, and key factors in post-crash discounting of the swap curve. And speaking of interest-rate swaps, it is routine to see (for example, in US dollar markets) the swap curve trading through the sovereign bond curve. That would have been inexplicable when I was working as a government bond primary dealer in the 1990s . . . but then again, negative interest rates as routine would also have been inexplicable. Plenty for us to be getting on with then. And in an era of ever more intensive regulator and compliance burden, having to deal with a purely technical subject may even come across as a breath of fresh air to some practitioners!

I always try to emphasise the practical and the user-friendly in all my writing. There is such a disconnect between academia and practice in finance that there would be little value in me expounding purely on the theoretical. Unfortunately (or fortunately, depending on your point of view), the yield curve is one of those topics that it is difficult to leave the technical out of. That said, I hope the contents of the book are of relevance and practical value to the practitioner in banking and finance. This is not intended to be a textbook describing nothing that actually takes place in a bank, unlike some finance textbooks I have encountered over the years. Rather, it is meant for those who need to update the curve for use in internal funds transfer pricing, or to estimate the value to be derived from purchasing one bond in preference to another bond, or to price a new issue private placement structured product, or to have an idea of what the market thinks the state of the economy is. In other words, this book is for anyone that is using the yield curve for one or more of its myriad different practical applications in the financial markets.

Hence this second edition, which I hope you find of interest and of some use. As Ian MacDonald said in the preface to his final update of the majestic Revolution In The Head , no further editions will be forthcoming. Or as the last Oi! album proclaimed, 'That's yer lot!'.

Comments on the text are welcome and should be sent to me via John Wiley &amp; Sons Limited.

All the best.

Moorad Choudhry Surrey, England 19 December 2018 A Solid Bond In Your Heart

<!-- image -->

## Preface to the First Edition

A s Sir Arthur Conan Doyle would have put it, so elementary a form of literature  as  the  textbook  on  financial  economics  hardly  deserves  the dignity of a preface. It is possible though, to bring some instant clarity to the purpose of such a book if we open with a few words here.

In my book The Bond and Money Markets , I try to explain, from first principles, just how important the global debt market is, and describe the various participants that interact with each other in this market. Given the importance of the global bond market, one can never learn too much about it. But this is not a book about the bond market; rather it is about a very specific, and important part of the bond markets. In developed markets, as well as a fair number of developing ones, there is usually a large number of bonds trading at one time, at different yields and with varying terms to maturity. Investors and traders incessantly examine the relationship between the yields on bonds that are in the same class; plotting yields of bonds that differ only in their term to maturity produces what is known as the yield curve . The yield curve represents the bond market. It is sometimes referred to as the term structure of interest rates ,  but  as  we  shall  see  later  in  this book, this expression refers to only one specific type of yield curve. There are lots of different yield curves. We shall examine them all in detail later.

Much of the analysis and pricing activity that takes place in the bond markets revolves around the yield curve. The primary yield curve in any domestic capital market is the government bond yield curve, so for example, in the US market it is the US Treasury yield curve. So in this book we will talk mainly, but not exclusively, about the government yield curve. And because the author spent over five years as a United Kingdom government bond trader  (or  gilt-edged  market  maker),  most  of  the  examples  will  be from the gilt market. But the principles remain the same. It is the importance of the yield curve to just about every aspect of finance that has been the motivation behind writing this book. Our objective is to:

- ◾ describe what the yield curve is;
- ◾ explain what it tells us;
- ◾ try to explain why it assumes certain shapes;
- ◾ show how we can use it;
- ◾ introduce how it is modelled;
- ◾ show how it is fitted from market rates.

We begin with some basic description of bonds and bond mathematics, just to set the scene. We assume a basic knowledge and familiarity with bonds and market institutions, and concentrate on the yield curve. It is an arcane,  specialist  topic  but  well  worth  getting  familiar  with. We  explain term structure theory, describe the most popular mathematical approaches used to model the yield curve, and show how to fit the yield curve using econometric techniques. This knowledge is of great use to just about anyone involved in the bond markets: traders, bond salespersons, fund managers, research analysts, issuers of bonds . . . in fact issuers, investors, and all the middlemen in between. Investors in the equity markets can also benefit from an understanding of the yield curve, as it enables one to gain a better insight into market sentiment.

We must necessarily be quite focused and specialist in our discussion of  the  yield  curve.  Hopefully  the  more  technical  material  is  presented  in good order so that it remains accessible. There are any number of textbooks available for the complete beginner, which are recommended in end-chapter reading lists, along with further reading.

Moorad Choudhry Surrey, England 30 June 2003

## S

## Acknowledgments

pecial thanks to The Raynes Park Footy Boys and The Pink Tie Brigade . Thanks to everyone at Wiley, including Stephen Mullaly, Syd Ganaden, Jean-Karl Martin, Debbie Scott, Sandra Glue, Banurekha Venkatesan, Elisha Benjamin, Katy Smith and Aida Ferguson.

Big  thanks  to  my  co-authors,  Polina  Bardaeva,  Ken  Kortanek,  Kevin Liddy, Wolfgang Marty, and Vladimir Medvedev. It's a privilege to work with you.

Thanks  to  Marc  Dodd  and  everyone  at  King  &amp;  Shaxson  Ltd,  and Martin Ward at One Savings Bank for helping to make my latest return to the markets so enjoyable.

Thanks to everyone at Crown Law and NZIRD, fab people to work with, including Jane Norris, Meghan Nicholson, Lina Worthing, Paul Hale, and Mike Cook.

Thanks to everyone at Alderwick James, including Mr Alderwick and Ms  James  themselves  as  well  as  Liliana  Lolata,  Jolene  Rodrigues,  Sally Thurwood, and Sally Baldeh.

Thanks to everyone at The BTRM. What a genuinely great bunch of people I am privileged to work with.

Thanks  to  Philip  Curtis-Evans  at  Bloomberg  for  his  assistance  and instant responses whenever I requested screen print permissions.

For very kind and very much appreciated comments on Linked In, all the more touching as I have never actually met them, a very special thanks to Brian Twomey, Donald Van Deventer and David Harper. It meant a lot to me, thank you gentlemen.

And a very big, big thanks to Mike Kirsopp and everyone at Cambridge &amp; Counties Bank. And I mean everyone! The bank has at least one thing in common with the New Zealand All Blacks. . .

<!-- image -->

## About the Author

Moorad Choudhry is  Head  of  ALM  at  Cambridge  &amp;  Counties  Bank  in Leicester.

He  was  previously  a  gilt-edged  market-maker  and  money  markets trader at Hoare Govett Securities Limited (later ABN Amro Hoare Govett Limited) and a sterling bond proprietary trader at Hambros Bank Limited. He  subsequently  traded  money  markets,  asset-backed  commercial  paper, and structured finance repo at KBC Financial Products (a subsidiary of KBC Bank N.V.), and was latterly Treasurer, Corporate Banking Division at The Royal Bank of Scotland.

## Analysing and Interpreting the Yield Curve

But don't forget the songs That made you cry, And the songs that saved your life, Yes, you're older now And you're a clever swine,

But they were the only ones who ever stood by you. -- The Smiths, Rubber Ring (Rough Trade Records, 1985)

P A R T

I

## Introduction to the Yield Curve

I n Part I we describe the yield curve itself. The bulk of the discussion is in Chapter 1, which looks at the different types of yield curve and, more importantly, introduces the main theories of the yield curve. We also look at interpreting the curve. The language is non-specialist and should be accessible to anyone with an involvement in the financial markets. This is followed by a look at spot and forward rates, and the derivation of such rates from market yields. For this second edition we have relegated the introductory chapter on

bond yield measurement to the main Appendix.

After a couple of months, his patriotic zeal got on my nerves so much I began to question whether I agreed with him about communism being evil. I agreed it was a bad idea but no longer felt so sure it would ruin the planet. I began to consider the danger of blind faith in, or blind hatred of, a single idea, any idea.

-- Robert Wideman, Unexpected Prisoner: Memoir of a Vietnam POW, 2016

## CHAPTER  1 The Yield Curve

T he main measure of return associated with holding bonds is the yield to maturity (YTM) or gross redemption yield (GRY). In developed markets there is usually a large number of bonds trading at one time, at different yields and with varying terms to maturity. Investors and traders frequently examine the relationship between the yields on bonds that are in the same class. Plotting yields of bonds that differ only in their term to maturity produces the yield curve . The yield curve is an important indicator and knowledge source of the state of a debt capital market. 1  It is sometimes referred to as the term structure of interest rates , but strictly speaking this is not correct, as this expression should be reserved for the zero-coupon yield curve only. We shall examine this in detail later.

Much of the analysis and pricing activity that takes place in the bond markets revolves around the yield curve. The yield curve describes the relationship between a particular redemption yield and a bond's maturity. We should be aware that the GRY of a bond is only ever the actual yield one receives during the period one holds the bond if certain specific, and generally unrealistic, conditions are met. However, we will leave the discussion of this for later.

Plotting the yields of bonds along the maturity term structure will give us our yield curve. It is very important that only bonds from the same class of issuer or with the same degree of liquidity are used when plotting the yield curve. For example, a curve may be constructed for UK gilts or for AA-rated sterling Eurobonds, but not a mixture of both, because gilts and Eurobonds are bonds from different class issuers. The primary yield curve in any domestic capital market is the government bond yield curve, so for example, in the US market it is the US Treasury yield curve. With the advent of the euro currency in 11 (ultimately 19) countries of the European Union, in theory any euro-currency government bond can be used to plot a defaultfree  euro  yield  curve.  In  practice,  only  bonds  from  the  same  government are used, as for various reasons different bonds within euro-currency countries trade at different yields. Outside the government, bond markets yield curves are plotted for Eurobonds, money market instruments, off-balance sheet instruments, in fact virtually all debt market instruments. Therefore it is always important to remember to compare like-for-like when analysing yield curves across markets.

1   The author was tickled to read this description from someone obviously as excited about the yield curve as he is; Ryan (1997) writes:

'The future . . . of the global economy . . . may well rest on the success of how we finance the [yield] curve. God bless the Treasury Yield Curve!'

In this chapter, we look at the yield to maturity yield curve as well as other types of yield curves that may be constructed. We also consider how to derive spot and forward yields from a current redemption yield curve. The main emphasis though, is on interpreting the shape of the yield curve, and explaining why it assumes the shapes it does. Later in the book we examine more advanced techniques for fitting, analysing, and interpreting the yield curve.

First though, we introduce the yield curve for beginners, of course experienced practitioners and graduate students may skip this part.

## THE YIELD CURVE FOR BEGINNERS

This section is a summary of the importance and application of the yield curve. It was originally written with private investors in mind, so market practitioners may wish to skip this part.

## What is the Yield Curve?

The yield curve is a graph that plots the yield of various bonds against their term to maturity. In other words, it is a snapshot of the current level of yields in the market. It is not an historical graph, that is, it does not show the level of yields over time. That would be an historical price (or yield) chart.

Yield curves are like football . . .  it  is  very  easy  to  grasp  the  basics, but difficult to become expert at (to continue the football analogy, akin to being good enough to play on a Sunday-morning park football team and being good enough to play on a team that included David Beckham, Steven Gerrard, and Michael Owen). Let us imagine that we looked up gilt yields in the Financial Times on a day in August 2002 and saw the following:

TABLE 1.1 Gilt yields

| Gilt        |   Red Yield 2 |
|-------------|---------------|
| Tr 8% 03    |          3.79 |
| Tr 5% 04    |          4.00 |
| Tr 7.25% 07 |          4.62 |
| Tr 5% 12    |          4.70 |
| Tr 8.75% 17 |          4.74 |
| Tr 8% 21    |           468 |
| Tr 4.25% 32 |          4.52 |

Table 1.1 shows the yields for gilts of 1-, 2-, 5-, 10-, 15-, 20-, and 30-year maturity. (The 8% 2021 gilt is slightly under 20 years maturity but it will do for our purposes - there is no gilt that matures in 2022 at the time we are looking at this.)

We open up  Microsoft  Excel 3   and  write  down  two  columns,  one  for 'maturity' and one for  'yield'. The years to maturity column forms the x-axis of the graph, while the yield forms the y-axis. Then we use the Excel 'chart wizard' and it plots our graph for us! The result is as shown in Figure 1.1.

This curve looks about right. Intuitively, we expect that yields increase the greater the maturity. If we lend one person an amount of money for one year and another person the same amount of money for 10 years, we would not charge them both the same rate of interest (assuming both had the same credit risk) - we would most likely charge a higher rate to the 10-year borrower, for two reasons:

- i. inflation will erode the value of the loan over the longer term, and;
- ii. while the longer-dated borrower may be the same credit quality as the short-dated borrower, there are other risks. For example, the long-dated borrower may not be around in 10 years' time. Therefore, as a lender, we need a higher return to compensate for the greater risk the further out into the future we lend money.

2   'Red' means redemption yield.

3   The author has no hesitation in endorsing Microsoft Excel as a superior product. He remembers having to use Lotus 1-2-3 in DOS when he first started work in the City . . .

FIGURE 1.1 Creating a yield curve in Excel.

<!-- image -->

So this gives us the positively sloping yield curve we see in Figure 1.1. However,  if  that  is  the  case,  why  does  the  curve  not  continue  to  slope upwards, all the way to the 30-year mark? The rate of upward movement declines after the five-year mark, and then actually decreases to the 30-year point. This is a peculiarity of many markets - the 30-year bond, commonly called the long bond , is usually in such great demand among institutional investors, such as pension funds, that this demand outstrips supply. As a result, the price of this bond is forced upwards, and this moves the yield down to below what it should be.

Constructing  a  yield  curve  in  the  wholesale  markets  is  a  little  more involved than what we have described above, and a ever-so-slightly complicated branch of mathematics is employed to derive the models used to fit yield curves. We consider this in later chapters.

## Using the Yield Curve

The yield  curve  tells  us  where  the  bond  market  is  trading  now.  It  also implies  the  level  of  trading  for  the  future,  or  at  least  what  the  market thinks will be happening in the future. In other words, it is a good indicator  of  the  future  level  of  the  market.  It  is  also  a  much  more  reliable indicator than any other used by private investors, and we can prove this empirically.

Let us consider the main uses of the yield curve. All participants in the debt capital markets have an interest in the current shape and level of the yield curve, as well as what this information implies for the future. The main uses are introduced below:

- ◾ Setting  the  yield  for  all  debt  market  instruments. The  yield  curve essentially  fixes  the  cost  of  money  over  the  maturity  term  structure.

The yields of government bonds from the shortest-maturity instrument to the longest set the benchmark for yields for all other debt instruments in the market, around which all debt instruments are analysed. Issuers of debt (and their underwriting banks) therefore use the yield curve to price bonds and all other debt instruments. Generally the zero-coupon yield curve is used to price new issue securities, rather than the redemption yield curve.

- ◾ Acting as an indicator of future yield levels. As  we  discuss  later  in this  chapter,  the  yield  curve  assumes  certain  shapes  in  response  to market  expectations  of  the  future  interest  rates.  Bond  market  participants analyse the present shape of the yield curve in an effort to determine the implications regarding the future direction of market interest rates. This is perhaps one of the most important functions of the yield curve, and it is as much an art as a science. The yield curve is scrutinised for its information content, not just by bond traders and fund managers, but also by corporate financiers as part of project appraisal. Central banks and government treasury departments also analyse the yield curve for its information content, not just regarding  forward  interest  rates,  but  also  with  regard  to  expected  inflation levels.
- ◾ Measuring  and  comparing  returns  across  the  maturity  spectrum. Portfolio managers use the yield curve to assess the relative value of investments across the maturity spectrum. The yield curve indicates the returns that are available at different maturity points and is therefore very important to fixed income fund managers, who can use it to  assess  which  point  of  the  curve  offers  the  best  return  relative  to other points.
- ◾ Indicating  relative  value  between  different  bonds  of  similar  maturity. The yield curve can be analysed to indicate which bonds are cheap or dear to the curve. Placing bonds relative to the zero-coupon yield curve helps to highlight which bonds should be bought or sold either outright or as part of a bond spread trade.
- ◾ Pricing interest rate derivative securities. The price of derivative securities revolves around the yield curve. At the short end, products such as Forward Rate Agreements are priced off the futures curve, but futures rates  reflect  the  market's  view  on  forward  three-month  cash  deposit rates.  At  the  longer  end,  interest  rate  swaps  are  priced  off  the  yield curve, while hybrid instruments that incorporate an option feature such as convertibles and callable bonds also reflect current yield curve levels. The 'risk-free'  interest  rate,  which  is  one  of  the  parameters  used  in option pricing, is  the T-bill  rate  or  short-term  government  repo  rate, both constituents of the money market yield curve.

## YIELD TO MATURITY YIELD CURVE

The  most  commonly  occurring  yield  curve  is  the  yield  to  maturity  yield curve. The equation used to calculate the yield to maturity is given in the Appendix. The curve itself is constructed by plotting the yield to maturity against the term to maturity for a group of bonds of the same class. Three different examples are shown at Figure 1.2. Bonds used in constructing the curve will only rarely have an exact number of whole years to redemption, however, it is often common to see yields plotted against whole years on the x -axis. This is because once a bond is designated the benchmark for that term, its yield is taken to be the representative yield. For example, the then 10-year benchmark bond in the UK gilt market, the 5.75% Treasury 2009, maintained its benchmark status throughout 1999 and into 2000, even as its term to maturity fell below 10 years. The yield to maturity yield curve is the most commonly observed curve simply because yield to maturity is the most frequent measure of return used. The business sections of daily newspapers, where they quote bond yields at all, usually quote bond yields to maturity.

As we might expect, given the source data from which it is constructed, the  yield  to  maturity  yield  curve  contains  some  inaccuracies.  We  have already come across the main weakness of the yield to maturity measure, which is the assumption of a constant rate for coupon reinvestment during the bond's life at the redemption yield level. Since market rates fluctuate over time, it is not possible to achieve this (a feature known as reinvestment risk ). Only zero-coupon bondholders avoid reinvestment risk as no coupon is paid during the life of a zero-coupon bond.

FIGURE 1.2 Yield to maturity yield curves.

<!-- image -->

Users  of  the  Bloomberg  system  can  call  up  a  large  number  of  yield curves, for different sectors of the market and different instruments. The main screen is IYC, which presents a menu of government bond redemption yield curves. For example, Figure 1.3 shows screen IYC for the UK gilt curve, as at 18 June 2003. The curves are for benchmark bonds and for gilt zero-coupon bonds or strips. Figure 1.4 compares the gilt curve and the sterling swap curve. Figure 1.5 shows the corresponding curves for French and German government bonds, on the same screen, and Figure 1.6 shows the benchmark curve for US Treasuries.

Figure 1.7 shows the screen FMC, which presents a menu of different government and corporate bond yield curves. Users select the curve required from this menu. Selecting curves 664, 670, and 673 (see Figure 1.7) gives us composite yield curves for AAA-, A- and BBB-rated corporate bonds. These curves are shown at Figure 1.8.

Finally, Figure 1.9 shows screen SWCV, the interest rate swap curve. We show the screen as selected for sterling interest rate swaps.

The yield to maturity yield curve does not distinguish between different payment patterns that may result from bonds with different coupons, that is, the fact that low-coupon bonds pay a higher portion of their cash

FIGURE 1.3 UK gilt yield curves as at 18 June 2003. Source : © Bloomberg L.P. Reproduced with permission.

<!-- image -->

FIGURE 1.4 UK gilt yield curve and sterling interest rate swap curve as at 18 June 2003.

<!-- image -->

Source : © Bloomberg L.P. Reproduced with permission.

FIGURE 1.5 French and German government yield curves, 18 June 2003. Source : © Bloomberg L.P. Reproduced with permission.

<!-- image -->

FIGURE 1.6 Treasury yield curve as at 18 June 2003. Source : © Bloomberg L.P. Reproduced with permission.

<!-- image -->

FIGURE 1.7 Screen FMC, menu of corporate and government bond yield curves. Source : © Bloomberg L.P. Reproduced with permission.

<!-- image -->

FIGURE 1.8 Screen FMC, AAA-, A-, and BBB-rated corporate yield curves as at 18 June 2003.

<!-- image -->

Source : © Bloomberg L.P. Reproduced with permission.

FIGURE 1.9 Screen SWCV, selected for sterling swap curve as at 18 June 2003. Source : © Bloomberg L.P. Reproduced with permission.

<!-- image -->

flows  at  a  later  date  than  high-coupon  bonds  of  the  same  maturity. The curve also assumes an even cash flow pattern for all bonds. Therefore in this case, cash flows are not discounted at the appropriate rate for the bonds in the group being used to construct the curve. To compensate for this, bond analysts may sometimes construct a coupon yield curve , which plots yield to maturity against term to maturity for a group of bonds with the same coupon. This may be useful when a group of bonds contains some with very high coupons - high-coupon bonds often trade 'cheap to the curve', that is they have higher yields, than corresponding bonds of the same maturity but lower coupon. This is usually because of reinvestment risk and, in some markets (including the UK), for tax reasons.

Now is probably an appropriate time to remind readers that the YTM, and hence the YTM curve, is really just an 'assumed' yield. It isn't a true term structure of interest rates. This is because, for the investor to receive the YTM during the  period  the  bond  is  held,  the  bond  must  have  been (i)    purchased at par, and (ii) all the coupons received during the holding period must have been reinvested at the same YTM. Clearly, these two sets of conditions are rarely, if ever, met during the holding period. So whilst YTM is a useful measure for initial purchase and comparison purposes, one should remember that it is rarely, if ever, the return that is actually received.

## THE COUPON YIELD CURVE

The coupon yield curve is  a  plot  of  the  yield  to  maturity against term to maturity for a group of bonds with the same coupon. If we construct such a curve, we can see that in general high-coupon bonds trade at a discount (have higher yields) relative to low-coupon bonds, because of reinvestment risk  and  for  tax  reasons.  In  the  UK,  for  example,  on  gilts  the  coupon  is taxed as income tax, while any capital gain is exempt from capital gains tax. Even in jurisdictions where capital gain on bonds is taxable, this can often be deferred whereas income tax cannot. It is frequently the case that yields vary  considerably  with  coupon  for  the  same  term  to  maturity,  and  with term to maturity for different coupons. Put another way, usually we observe different coupon curves, not only at different levels, but also with different shapes. Distortions arise in the yield to maturity curve if no allowance is made for coupon differences. For this reason, bond analysts frequently draw a line of 'best fit' through a plot of redemption yields, because the coupon effect in a group of bonds will produce a curve with humps and troughs. Figure 1.10 shows a hypothetical set of coupon yield curves, however, since in any group of bonds it is unusual to observe bonds with the same coupon along the entire term structure, this type of curve is relatively rare.

FIGURE 1.10 Coupon yield curves.

<!-- image -->

## THE PAR YIELD CURVE

The par yield curve is not usually encountered in secondary market trading, however, it is often constructed for use by corporate financiers and others in  the  new  issues  or primary market. The  par  yield  curve  plots  yield  to maturity against term to maturity for current bonds trading at par. 4  The par yield is therefore equal to the coupon rate for bonds priced at par or near to par, as the yield to maturity for bonds priced exactly at par is equal to the coupon rate. Those involved in the primary market will use a par yield curve to determine the required coupon for a new bond that is to be issued at par. This is because investors prefer not to pay over par for a new-issue bond, so the bond requires a coupon that will result in a price at or slightly below par.

The par  yield  curve  can  be  derived  directly  from  bond  yields  when bonds are trading at or near par. If bonds in the market are trading substantially away from par, then the resulting curve will be distorted. It is then necessary to derive it by iteration from the spot yield curve. As we would observe at almost any time, it is rare to encounter bonds trading at par for any particular maturity. The market therefore uses actual non-par vanilla bond yield curves to derive zero-coupon yield curves and then constructs hypothetical par yields that would be observed were there any par bonds being traded.

4   Par price for a bond is almost invariably 100%. Certain bonds have par defined as 1,000 per 1,000 nominal of paper.

## THE ZERO-COUPON (OR SPOT) YIELD CURVE

The zero-coupon (or spot ) yield  curve plots  zero-coupon  yields  (or  spot yields) against term to maturity. A zero-coupon yield is the yield prevailing on a bond that has no coupons. In the first instance, if there is a liquid zerocoupon bond market we can plot the yields from these bonds if we wish to construct this curve. However, it is not necessary to have a set of zerocoupon bonds in order to construct the curve, as we can derive it from a coupon or par yield curve. In fact, in many markets where no zero-coupon bonds are traded, a spot yield curve is derived from the conventional yield to maturity yield curve. This is of course a theoretical zero-coupon (spot) yield curve, as opposed to the market or observed spot curve that can be constructed using the yields of actual zero-coupon bonds trading in the market. 5

## Interest Rates: Basic Concepts

Spot yields must comply with Equation (1.1). This equation assumes annual coupon payments and that the calculation is carried out on a coupon date so that accrued interest is zero:

<!-- formula-not-decoded -->

where

rs n is the spot or zero-coupon yield on a bond with n years to maturity df rs n n n 1 / 1 the corresponding discount factor .

In (1.1) rs 1 is the current one-year spot yield, rs 2 the current two-year spot yield, and so on. Theoretically, the spot yield for a particular term to maturity is the same as the yield on a zero-coupon bond of the same maturity, which is why spot yields are also known as zero-coupon yields. This last is an important result, as spot yields can be derived from redemption yields that have been observed in the market.

5   It is common to see the terms 'spot rate' and 'zero-coupon rate' used synonymously. However, the spot rate is a theoretical construct and cannot be observed in the market. The definition of the spot rate, which is the rate of return on a single cash flow that has been dealt today and is received at some point in the future, comes very close to that of the yield on a zero-coupon bond, which can be observed directly in the market. Zero-coupon rates can therefore be taken to be spot rates in practice, which is why the terms are frequently used interchangeably.

As with the yield to redemption yield curve, the spot yield curve is commonly used in the market. It is viewed as the true term structure of interest rates  because  there  is  no  reinvestment  risk  involved  -  the  stated  yield  is equal to the actual annual return. That is, the yield on a zero-coupon bond of n years maturity is regarded as the true n -year interest rate. Because the observed government bond redemption yield curve is not considered to be the true interest rate, analysts often construct a theoretical spot yield curve. Essentially this is done by breaking down each coupon bond being observed into its constituent cash flows, which become a series of individual zerocoupon bonds. For example, £100 nominal of a 5% two-year bond (paying annual coupons) is considered equivalent to £5 nominal of a one-year zerocoupon bond and £105 nominal of a two-year zero-coupon bond.

Let us assume that in the market there are 30 bonds all paying annual coupons. The first bond has a maturity of one year, the second bond of two years, and so on out to thirty years. We know the price of each of these bonds, and we wish to determine what the prices imply about the market's estimate of future interest rates. We expect interest rates to vary over time, but that all payments being made on the same date are valued using the same rate. For the one-year bond, we know its current price and the amount of the payment (comprised of one coupon payment and the redemption proceeds) we will receive at the end of the year, therefore we can calculate the interest rate for the first year - assume the one-year bond has a coupon of 5%. If the bond is priced at par and we invest £100 today, we will receive £105 in one year's time, hence the rate of interest is apparent and is 5%. For the two-year bond, we use this interest rate to calculate the future value of its current price in one year's time: this is how much we would receive if we had invested the same amount in the one-year bond . However, the two-year bond pays a coupon at the end of the first year and if we subtract this amount from the future value of the current price, the net amount is what we should be giving up in one year in return for the one remaining payment. From these numbers we can calculate the interest rate in year two.

Assume that the two-year bond pays a coupon of 6% and is priced at £99.00. If the £99.00 is invested at the rate we calculated for the one-year bond (5%), it will accumulate £103.95 in one year, made up of the £99.00 investment and interest of £4.95. On the payment date in one year's time, the one-year bond matures and the two-year bond pays a coupon of 6%. If everyone expected that at this time the two-year bond would be priced at more than 97.95 (which is 103.95 minus 6.00), then no investor would buy the one-year bond, since it would be more advantageous to buy the twoyear bond and sell it after one year for a greater return. Similarly, if the price is less than 97.95, no investor would buy the two-year bond, as it would be cheaper to buy the shorter bond and then buy the longer-dated bond with the proceeds received when the one-year bond matures. Therefore the two-year bond must be priced at exactly 97.95 in 12 months' time. For this £97.95 to grow to £106.00 (the maturity proceeds from the two-year bond, comprising the redemption payment and coupon interest), the interest rate in year two must be 8.22%. We can check this using the present value formula covered earlier. At these two interest rates, the two bonds are said to be in equilibrium.

This  is  an  important  result  and  shows  that  (in  theory)  there  can  be no arbitrage opportunity along the yield curve - using interest rates available today, the return from buying the two-year bond must equal the return from buying the one-year bond and rolling over the proceeds (or reinvesting) for  another year. This is known as the breakeven principle, a  law of no-arbitrage.

Using the price and coupon of the three-year bond, we can calculate the interest rate in year three in exactly the same way. Using each of the bonds in turn, we can link together the implied one-year rates for each year up to the maturity of the longest-dated bond. The process is known as boot-strapping. The 'average' of the rates over a given period is the spot yield for that term. In the example given above, the rate in year one is 5%, and in year two is 8.20%. An investment of £100 at these rates would grow to £113.61. This gives a total percentage increase of 13.61% over two years, or 6.588% per annum. (The average rate is not obtained by simply dividing 13.61 by 2, but - using our present value relationship again - by calculating the square root of '1 plus the interest rate' and then subtracting 1 from this number). Thus the one-year yield is 5% and the two-year yield is 8.20%.

In real-world markets it is not necessarily as straightforward as this, for  instance,  on  some  dates  there  may  be  several  bonds  maturing,  with different coupons, and on some dates there may be no bonds maturing. It is most unlikely that there will be a regular spacing of bond redemptions exactly one year apart. For this reason, it is common for analysts to use a software model to calculate the set of implied spot rates which best fits the market prices of the bonds that do exist in the market. For instance, if there are several one-year bonds, each of their prices may imply a slightly different rate of interest. We choose the rate that gives the smallest average price error. In practice, all bonds are used to find the rate in year one, all bonds with a term longer than one year are used to calculate the rate in year two, and so on. The zero-coupon curve can also be calculated directly from the coupon yield curve using a method similar to that described above. In this case, the bonds would be priced at par and their coupons set to the par yield values.

The zero-coupon yield curve is ideal to use when deriving implied forward rates, which we consider next, and defining the term structure of interest rates. It is also the best curve to use when determining the relative value , whether cheap or dear, of bonds trading in the market, and when pricing new issues, irrespective of their coupons. However, it is not an absolutely accurate  indicator  of  average  market  yields  because  most  bonds  are  not zero-coupon bonds.

## Zero-Coupon Discount Factors

Having introduced the concept of the zero-coupon curve in the previous paragraph, we can illustrate more formally the mathematics involved. When deriving spot yields from redemption yields, we view conventional bonds as being made up of an annuity, which is the stream of fixed coupon payments, and a zero-coupon bond, which is the redemption payment on maturity. To derive the rates we can use (1.1), setting P M d 100 and = 100 N C rm · as shown in (1.2) below. This has the coupon bonds trading at par, so that the coupon is equal to the yield:

<!-- formula-not-decoded -->

where rmN is the par yield for a term to maturity of N years, where the discount factor df N is the fair price of a zero-coupon bond with a par value of £1 and a term to maturity of N years, and where:

<!-- formula-not-decoded -->

is the fair price of an annuity of £1 per year for N years (with A 0 0 by convention). Substituting (1.3) into (1.2) and rearranging will give us the expression below for the N -year discount factor, shown at (1.4):

<!-- formula-not-decoded -->

If we assume one-year, two-year, and three-year redemption yields for bonds  priced  at  par  to  be  5%,  5.25%,  and  5.75%  respectively,  we  will obtain the following solutions for the discount factors:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We can confirm that these are the correct discount factors by substituting them back into equation (1.2). This gives us the following results for the one-year, two-year, and three-year par value bonds (with coupons of 5%, 5.25%, and 5.75% respectively):

<!-- formula-not-decoded -->

Now that we have found the correct discount factors  it  is  relatively straightforward to calculate the spot yields using equation (1.1), and this is shown below:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation (1.1) discounts the n -year cash flow (comprising the coupon payment  and/or  principal  repayment)  by  the  corresponding n -year  spot yield.  In  other  words, rs n is  the time-weighted rate of return on  a n -year bond. Thus, as we said in the previous section, the spot yield curve is the correct method for pricing or valuing any cash flow, including an irregular cash flow, because it uses the appropriate discount factors. That is, it matches each cash flow to the discount rate that applies to the time period in which the cash flow is paid. Compare this to the approach for the yield to maturity procedure discussed earlier, which discounts all cash flows by the same yield to maturity. This illustrates neatly why the N -period zero-coupon interest rate is the true interest rate for an N -year bond.

The  expressions  above  are  solved  algebraically  in  the  conventional manner, although those wishing to use a spreadsheet application such as Microsoft Excel ®  can input the constituents of each equation into individual cells and solve using the 'Tools' and 'Goal Seek' functions.

## EXAMPLE 1.1 ZERO-COUPON YIELDS

- ◾ Consider the following zero-coupon market rates:

| One-year (1y)   | 5.000%   |
|-----------------|----------|
| 2y              | 5.271%   |
| 3y              | 5.598%   |
| 4y              | 6.675%   |
| 5y              | 7.213%   |

Calculate the zero-coupon discount factors and the prices and yields of:

- a. a 6% two-year bond, and;

b. a 7% five-year bond.

Assume both are annual coupon bonds.

The zero-coupon discount factors are:

```
1y : 1 1 05 0 95238095 / . . 2y : 1 1 05271 0 90236554 2 / . . 3y : 1 1 05598 0 84924485 3 / . . 4y : 1 1 06675 0 77223484 4 / . . 5y :
```

1 1 07213 0 70593182 5 / . .

The price of the 6% two-year bond is then calculated in the normal fashion using present values of the cash flows:

<!-- formula-not-decoded -->

The  yield  to  maturity  is  5.263%,  obtained  using  the  iterative method, with a spreadsheet function such as Microsoft Excel ®  'Goal Seek' or a Hewlett Packard (HP) calculator.

The price of the 7% five-year bond is:

```
7 0 95238095 7 0 90236554 7 0 84924485 7 0 77223484 . . . . 107 0 70593182 99 8690 . .
```

The yield to maturity is 7.032%.

## FORMULA SUMMARY

Example 1.1 illustrates that if the zero-coupon discount factor for n years is df n and the par yield for N years is rp ,  then the expression at (1.5) is always true:

<!-- formula-not-decoded -->

## USING SPOT RATES IN BOND ANALYSIS

The convention in the markets is to quote the yield on a non-government bond as a certain spread over the yield on the equivalent maturity government bond, usually using the gross redemption yields. Traders and investment managers will assess the relative merits of holding the nongovernment bond based on the risk associated with the bond's issuer and the magnitude of its yield spread. For example, in the UK at the beginning of 2002, companies such as National Grid, Severn Trent Water, Abbey National plc, and Tesco plc  issued  sterling-denominated  bonds,  all  of  which  paid  a  certain spread over the equivalent gilt bond. 6  Figure 1.11 shows the average yield spreads of corporate bonds over gilts in the UK market through 2001-2002.

Traditionally, investors will compare the redemption yield of the bond they are analysing with the redemption yield of the equivalent government bond. Just as with the redemption yield measure, however, there is a flaw with this measure, in that the spread quoted is not really comparing like-forlike, as the yields do not reflect the true term structure given by the spot rate curve. There is an additional flaw if the cash flow streams of the two bonds do not match, which in practice they will do only rarely.

Therefore the correct method for assessing the yield spread of a corporate bond is to replicate its cash flows with those of a government bond, which can be done in theory by matching the cash flows of the corporate bond with a package of government zero-coupon bonds of the same nominal value. If no zero-coupon bond market exists, the cash flows can be matched synthetically by valuing a coupon bond's cash flows on a zero-coupon basis.

6   The spread is, of course, not fixed and fluctuates with market conditions and supply and demand.

FIGURE 1.11 Average yield spreads of UK corporate bonds versus gilts, 2001-2002. Source : Bank of England. Reproduced with permission.

<!-- image -->

The corporate bond's price is of course the sum of the present value of all its cash flows, which should be valued at the spot rates in place for each cash flow's maturity. It is the yield spread of each individual cash flow over the equivalent maturity government spot rate that is then taken to be the true yield spread.

This measure is known in US markets as the zero-volatility  spread or static spread, and it is a measure of the spread that is realised over the government spot rate yield curve if the corporate bond is held to maturity. It is therefore a different measure to the traditional spread, as it is not taken over one point on the (redemption yield) curve but over the whole term to maturity. The zero-volatility spread is that spread which equates the present value of the corporate bond's cash flows to its price, where the discount rates are each relevant government spot rate. The spread is found through an iterative process, and it is a more realistic yield spread measure than the traditional one.

## THE FORWARD YIELD CURVE

## Forward Yields

Most transaction in the market are for immediate delivery, which is known as the cash market, although some markets also use the expression spot market, which is more common in foreign exchange. Cash market transactions are settled straight away, with the purchaser of a bond being entitled to interest from the settlement date onwards. 7  There is a large market in forward transactions, which are trades carried out today for a forward settlement date. For financial transactions that are forward transactions, the parties to the trade agree today to exchange a security for cash at a future date, but at a price agreed today. So the forward rate applicable to a bond is the spot bond yield as at the forward date. That is, it is the yield of a zero-coupon bond that is purchased for settlement at the forward date. It is derived today, using data from a present day yield curve, so it is not correct to consider forward rates to be a prediction of the spot rates as at the forward date.

Forward rates can be derived from spot interest rates. Such rates are then known as implied forward rates, since they are implied by the current range of spot interest rates. The forward (or forward-forward ) yield curve is  a  plot  of  forward rates against term to maturity. Forward rates satisfy expression (1.6):

<!-- formula-not-decoded -->

where n n rf 1 is the implicit forward rate (or forward-forward rate) on a oneyear bond maturing in year n.

As a forward or forward-forward yield is implied from spot rates, the forward  rate  is  a  forward  zero-coupon  rate.  Comparing  (1.1)  and  (1.6), we see that the spot yield is the geometric mean of  the  forward rates, as shown below:

<!-- formula-not-decoded -->

This implies the following relationship between spot and forward rates:

<!-- formula-not-decoded -->

7   We refer to 'immediate' settlement, although of course there is a delay between trade date and settlement date, which can be anything from one day to seven days, or even longer in some markets. The most common settlement period is known as 'spot' and is two business days.

Using the spot yields we calculated previously, we can derive the implied forward rates from (1.8). For example, the two-year and three-year forward rates are given by:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Using our expression gives us 0 1 rf , equal to 5%, 1 2 rf equal to 5.539%, and 2 3 rf as  6.803%. This  means,  for  example,  that  given  current  spot yields, which we calculated from the one-year, two-year, and three-year bond redemption yields (which were priced at par), the market is expecting  the  yield  on  a  bond  with  one  year  to  mature  in  three  years'  time to  be  6.803%  (that  is,  the  three-year  one-period  forward-forward  rate is 6.803%).

The relationship between the par yields, spot yields, and forward rates is shown in Table 1.2.

Figure 1.12 highlights our results for all three yield curves graphically. This illustrates another important property of the relationship between the three curves, in that as the original coupon yield curve is positively sloping, so the spot and forward yield curves lie above it. The reasons behind this will be considered later in the chapter.

Let us now consider the following example. Suppose that a two-year bond with cash flows of £5.25 at the end of year 1 and £105.25 at the end of year 2 is trading at par, hence it has a redemption yield (indeed a par yield) of 5.25% (this is the bond in Table 1.2). As we showed in the section on zero-coupon yields and the idea of the break-even principle, in order to be regarded as equivalent to this, a pure zero-coupon bond or discount bond making a lump sum payment at the end of year 2 only (so with no cash flow at the end of year 1), requires a rate of return of 5.269%, which is the spot yield. That is, for the same investment of £100, the maturity value would have to be £110.82 (this figure is obtained by multiplying 100 by  1 0 05269 2 . ).

TABLE 1.2 Coupon, spot, and forward yields

|   Year |   Coupon yield (%) |   Zero-coupon yield (%) |   Forward rate (%) |
|--------|--------------------|-------------------------|--------------------|
|      1 |              5.000 |                   5.000 |              5.000 |
|      2 |              5.250 |                   5.269 |              5.539 |
|      3 |              5.750 |                   5.778 |              6.803 |

FIGURE 1.12 Redemption, spot, and forward yield curves: traditional analysis.

<!-- image -->

This illustrates why the zero-coupon curve is important to corporate financiers involved in new bond issues. If we know the spot yields, then we can calculate the coupon required on a new three-year bond that is going to be issued at par in this interest rate environment by making the following calculation:

<!-- formula-not-decoded -->

This is solved in  the  conventional  algebraic  manner  to  give C equal to 5.75%.

The  relationship  between  spot  yields  and  forward  rates  was  shown at (1.8). We can illustrate it as follows. If the spot yield is the average return , then the forward rate can be interpreted as the marginal return . If the marginal return between years 2 and 3 increases from 5.539% to 6.803%, then the average return increases from 5.269% up to the three-year spot yield of 5.778% as shown below:

<!-- formula-not-decoded -->

or 5.778%, as shown in Table 1.2.

## FORMULA SUMMARY

- ◾ The forward zero-coupon rate from interest period a to period b is given by (1.9):

<!-- formula-not-decoded -->

where rs a and rs b are the a and b period spot rates respectively.

- ◾ The forward rate from interest period a to period a 1  is given by (1.10):

<!-- formula-not-decoded -->

## Calculating Spot Rates From Forward Rates

The previous section showed the relationship between spot and forward rates. Just as we have derived forward rates from spot rates based on this mathematical relationship, it is possible to reverse this and calculate spot rates from forward rates. If we are presented with a forward yield curve, plotted from a set of one-period forward rates, we can use this to construct a spot yield curve. Equation (1.7) states the relationship between spot and forward rates, rearranged as (1.11) to solve for the spot rate:

<!-- formula-not-decoded -->

where 1 1 rf , 2 1 rf , 3 1 rf are the one-period versus two-period, two-period versus three-period forward rates up to the n 1  period versus n -period forward rates.

Remember to adjust (1.11) as necessary if dealing with forward rates relating to a deposit of a different interest period. If we are dealing with the current six-month spot rate and implied six-month forward rates, the relationship between these and the n -period spot rate is given by (1.11) in the same way as if we were dealing with the current one-year spot rate and implied one-year forward rates.

## EXAMPLE

## Example 1.2(i)

- ◾ The one-year cash market yield is 5.00%. Market expectations have priced one-year rates in one year's time at 5.95% and in two years' time at 7.25%. What is the current three-year spot rate that would produce these forward rate views?

To calculate  this  we  assume  an  investment  strategy  dealing  today at forward rates, and calculate the return generated from this strategy. The return after a three-year period is given by the future value relationship, which in this case is 1 05 1 0595 1 0725 1 1931 . . . . .

The three-year spot rate is then obtained by:

<!-- formula-not-decoded -->

## Example 1.2(ii)

- ◾ Consider the following six-month implied forward rates, when the six-month spot rate is 4.0000%:

| 0 1 rf   | 4.0000%   |
|----------|-----------|
| 2 3 rf   | 4.4516%   |
| 3 4 rf   | 5.1532%   |
| 4 5 rf   | 5.6586%   |
| 5 6 rf   | 6.0947%   |
| 6 7 rf   | 7.1129%   |

An investor is debating deciding between purchasing a three-year zero-coupon bond at a price of £72.79481 per £100 nominal or buying a six-month zero-coupon bond and then rolling over their investment every six months for the three-year term. If the investor is able to reinvest the proceeds every six months at the actual forward rates

( Continued )

in place today, what would the proceeds be at the end of the threeyear term?

An investment of £72.79481 at the spot rate of 4% and then reinvested at the forward rates in our table over the next three years would yield a terminal value of:

<!-- formula-not-decoded -->

This reflects our spot and forward rates relationship, in that if all the forward rates are realised, our investor's £72.79 will produce a terminal value that matches the investment in a three-year zero-coupon bond priced at the three-year spot rate. This illustrates the relationship between the three-year spot rate, the six-month spot rate, and the implied six-month forward rates. So what is the three-year zerocoupon bond trading at? Using (1.11), the solution to this is given by:

<!-- formula-not-decoded -->

which solves our three-year spot rate rs 6 as  5.4346%. Similarly, we could have solved for rs 6 using the conventional price/yield formula for zero-coupon bonds, however, the calculation above illustrates the relationship between spot and forward rates.

## ANALYSING AND INTERPRETING THE YIELD CURVE

From observing yield curves in different markets at any time, we notice that a yield curve can adopt one of four basic shapes, which are:

- ◾ normal or conventional : in which yields are at 'average' levels and the curve slopes gently upwards as maturity increases;
- ◾ upward-sloping or positive or rising : in which yields are at historically low levels, with long rates substantially greater than short rates;
- ◾ downward-sloping or inverted or negative : in which yield levels are very high by historical standards, but long-term yields are significantly lower than short rates;
- ◾ humped :  where yields are high with the curve rising to a peak in the mediumterm maturity area, and then sloping downwards at longer maturities.

Sometimes yield curves will incorporate a mixture of the above features. A great deal of effort is expended by bond analysts and economists analysing  and  interpreting  yield  curves.  There  is  often  a  considerable information content associated with any curve at any time. For example, Figure 1.13 shows the UK gilt redemption yield curve at three different times in the ten years from June 1989 to June 1999. What does the shape of each curve tell us about the UK debt market, and the UK economy at each particular time?

In this section, we consider the various explanations that have been put forward to explain the shape of the yield curve at any one time. None of the theories can adequately explain everything about yield curves and the shapes they assume at any time, so generally observers seek to explain specific curves using a combination of the accepted theories. This subject is a large one, indeed we could devote several books to it, therefore at this stage we will introduce the main ideas, reserving a more detailed investigation for later in the book.

The existence of a yield curve itself indicates that there is a cost associated with funds of different maturities, otherwise we would observe a flat yield curve. The fact that we very rarely observe anything approaching a flat yield curve suggests that investors require different rates of return depending on the maturity of the instrument they are holding. In this section, we review the main theories that have been put forward to explain the shape of the yield curve, which all have fairly long-dated antecedents.

FIGURE 1.13 UK gilt redemption yield curves. Source : Bloomberg L.P. Reproduced with permission.

<!-- image -->

An excellent account of the term structure is given in Theory of Financial Decision Making by Jonathan Ingersol (1987), Chapter 18. In fact it is worth purchasing this book just for Chapter 18 alone. Another quality account of the term structure is by Shiller (1990). In the following section we provide an introductory review of the research on this subject to date.

## The Expectations Hypothesis

The expectations hypothesis suggests that bondholders' expectations determine the course of future interest rates. There are two main competing versions of this hypothesis, the local expectations hypothesis and the unbiased expectations  hypothesis .  The return  to  maturity  expectations hypothesis and yield to maturity expectations hypothesis are also quoted (see Ingersoll  1987). The local expectations hypothesis states that all bonds of the same class, but differing in term to maturity, have the same expected holding period rate of return. This suggests that a six-month bond and a twenty-year bond will produce the same rate of return, on average, over the stated holding period. So if we intend to hold a bond for six months, we will receive the same return no matter what specific bond we buy. The author feels that this  theory is not always the case nor relevant, despite being mathematically neat, however, it is worth spending a few moments discussing it and related points. Generally, holding period returns from longer-dated bonds are  on  average  higher  than  those  from  short-dated  bonds.  Intuitively  we would expect this, with longer-dated bonds offering higher returns to compensate for their higher price volatility (risk). The local expectations hypothesis would not agree with the conventional belief that investors, being risk averse, require higher returns as a reward for taking on higher risk. In addition, it does not provide any insight about the shape of the yield curve. An article by Cox, Ingersoll and Ross (1981) showed that the local expectations hypothesis best reflected equilibrium between spot and forward yields. This was demonstrated using a feature known as Jensen's inequality, which is described in Appendix 1.2 of the first edition. Robert Jarrow (1996) states:

- '. . . in an economic equilibrium, the returns on . . . similar maturity zerocoupon bonds cannot be too different. If they were too different, no investor would hold the bond with the smaller return. This difference could not persist in an economic equilibrium'.

(Jarrow 1996, p. 50)

This reflects economic logic, but in practice other factors can impact on holding period returns between bonds that do not have similar maturities.

For instance, investors have restrictions as to which bonds they can hold, for example, banks and building societies are required to hold short-dated bonds for  liquidity  purposes.  In  an  environment  of  economic  disequilibrium, these investors still have to hold shorter-dated bonds, even if the holding period return is lower.

So although it is economically 'neat' to expect that the return on a long-dated bond is equivalent to rolling over a series of shorter-dated bonds, it  is  often  observed that longer-term (default-free) returns exceed annualised short-term default-free returns. Therefore an investor that continually rolled  over  a  series  of  short-dated  zero-coupon  bonds  would  most  likely receive a lower return than if they had invested in a long-dated zero-coupon bond. Rubinstein (1999) gives an excellent, accessible explanation of why this  is  so. The  reason  is  that  compared  to  the  theoretical  model,  in  reality future spot rates are not known with certainty. This means that shortdated zero-coupon bonds are more attractive to investors for two reasons; first,  they  are  more appropriate instruments to use for hedging purposes, and secondly they are more liquid instruments, in that they may be more readily converted back into cash than long-dated instruments. With regard to hedging, consider an exposure to rising interest rates. If the yield curve shifts upwards at some point in the future, the price of long-dated bonds will fall by a greater amount. This is a negative result for holders of such bonds, whereas the investor in short-dated bonds will benefit from rolling over their funds at the (new) higher rates. With regard to the second issue, Rubinstein (1999) states:

'.  .  .  it  can  be  shown  that  in  an  economy  with  risk-averse  individuals, uncertainty concerning the timing of aggregate consumption, the partial irreversibility  of  real  investments  (longer-term  physical  investments  cannot be converted into investments with earlier payouts without sacrifice), [and] . . . real assets with shorter-term payouts will tend to have a 'liquidity' advantage.'

(Rubinstein 1999, pp. 84-85)

Therefore the demand for short-term instruments is frequently higher, and hence short-term returns are often lower than long-term returns.

The pure or unbiased  expectations  hypothesis is  more  commonly encountered  and  states  that  current  implied  forward  rates  are  unbiased estimators of future spot interest rates. 8  It assumes that investors act in a way that eliminates any advantage of holding instruments of a particular maturity. Therefore if we have a positively sloping yield curve, the unbiased expectations hypothesis states that the market expects spot interest rates to rise. Equally, an inverted yield curve is an indication that spot rates are expected to fall. If short-term interest rates are expected to rise, then longer yields should be higher than shorter ones to reflect this. If this were not the case, investors would only buy the shorter-dated bonds and roll over the investment when they matured. Likewise, if rates are expected to fall, then longer yields should be lower than short yields. The unbiased expectations hypothesis states that the long-term interest rate is a geometric average of expected future short-term rates. This was in fact the theory that was used to derive the forward yield curve using (1.5) and (1.7) previously. This gives us:

8   For original discussion, see Lutz (1940) and Fisher (1986) (although he formulated

his ideas earlier).

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where rs N is the spot yield on a N -year bond and n n rf 1 is the implied oneyear rate n years ahead. For example, if the current one-year spot rate is rs 1 5 0 . % and the market is expecting the one-year rate in a year's time to be 1 2 5 539 rf . %, then the market is expecting a £100 investment in two one-year bonds to yield:

<!-- formula-not-decoded -->

after two years. To be equivalent to this, an investment in a two-year bond has to yield the same amount, implying that the current two-year rate is rs 2 5 7 . %, as shown below:

<!-- formula-not-decoded -->

which gives us rs 2 equal to 5.27%, and gives us the correct future value as shown below:

<!-- formula-not-decoded -->

This result must be so, to ensure no arbitrage opportunities exist in the market and in fact we showed as much earlier in the chapter when we considered forward rates. According to the unbiased expectations hypothesis, therefore, the forward rate 0 2 rf is an unbiased predictor of the spot rate 1 1 rs observed one period later. On average the forward rate should equal the subsequent spot rate. The hypothesis can be used to explain any shape in the yield curve.

or:

A rising yield curve is therefore explained by investors expecting shortterm interest rates to rise, that is 1 2 2 rf rs . A falling yield curve is explained by investors expecting short-term rates to be lower in the future. A humped yield curve is explained by investors expecting short-term interest rates to rise and long-term rates to fall. Expectations, or views on the future direction of the market, are a function mainly of the expected rate of inflation. If the market expects inflationary pressures in the future, the yield curve will be  positively  shaped,  while  if  inflation  expectations  are  inclined  towards disinflation, then the yield curve will be negative. However, several empirical studies including one by Fama (1976) have shown that forward rates are essentially biased predictors of future spot interest rates, and often overestimate future levels of spot rates. The unbiased hypothesis has also been criticised for suggesting that investors can forecast (or have a view on) very long-dated spot interest rates, which might be considered slightly unrealistic. As yield curves in most developed country markets exist to a maturity of up to 30 years or longer, such criticisms may have some substance. Are investors able to forecast interest rates 10, 20, or 30 years into the future? Perhaps not, nevertheless this is indeed the information content of say, a 30-year bond. Since the yield on the bond is set by the market, it is valid to suggest that the market has a view on inflation and future interest rates for up to 30 years forward.

The expectations hypothesis is stated in more than one way - we have already  encountered  the  local  expectations  hypothesis.  Other  versions include  the return  to  maturity expectations  hypothesis,  which  states  that the total return from holding a zero-coupon bond to maturity is equal to the total return that is generated by holding a short-term instrument and continuously rolling it over the same maturity period. A related version, the yield to maturity hypothesis, states that the periodic return from holding a zero-coupon bond is equal to the return from rolling over a series of coupon bonds, but refers to the annualised return earned each year rather than the total return earned over the life of the bond. This assumption enables a zero-coupon yield curve to be derived from the redemption yields of coupon bonds. The unbiased expectations hypothesis states that forward rates are equal to the spot rates expected by the market in the future. The CoxIngersoll-Ross article suggests that only the local expectations hypothesis describes a model that is purely arbitrage-free, as under the other scenarios it  is  possible  to  employ  certain  investment  strategies  that  would  produce returns in excess of what was implied by today's yields. Although it has been suggested 9  that the differences between the local and the unbiased hypotheses are not material, a model that describes such a scenario does not reflect investors' beliefs, which is why further research is ongoing in this area.

9   For example, see Campbell (1986) and Livingstone (1990).

The unbiased expectations hypothesis does not by itself explain all the shapes of the yield curve or the information content contained within it, so it is often tied in with other explanations, including the liquidity preference theory.

## Mathematical Description of Expectations Hypothesis

Simply put, the expectations hypothesis states  that  the  slope  of  the  yield curve reflects the market's expectations about future interest rates. There are in fact four main versions of the hypothesis, each distinct from the other and each not compatible with the others. The expectations hypothesis has a long history, first being described in 1896 by Fisher and later developed by Hicks (1946), among others. 10  As Shiller (1990) describes, the thinking behind it probably stems from the way market participants discuss their views on future  interest  rates  when  assessing  whether  to  purchase  long-dated  or short-dated bonds. For instance, if interest rates are expected to fall, investors will purchase long-dated bonds in order to 'lock in' the current high long-dated yield. If all investors act in the same way, the yield on long-dated bonds will decline as prices rise in response to demand, and this yield will remain low as long as short-dated rates are expected to fall, and will revert to a higher level only once the demand for long-term rates is reduced. Therefore, downward-sloping yield curves are an indication that interest rates are expected to fall, while an upward-sloping curve reflects market expectations of a rise in short-term interest rates.

Let us briefly consider the main elements of the discussion. The unbiased expectations hypothesis states that current forward rates are unbiased predictors of future spot rates. Let f T T t , 1  be the forward rate at time t for the period from T to T 1. If the one-period spot rate at time T is r T , then according to the unbiased expectations hypothesis:

<!-- formula-not-decoded -->

which states that the forward rate f T T t , 1  is the expected value of the future one-period spot rate given by r T at time T.

The return to maturity expectations hypothesis states  that  the  return generated from an investment of term t to T by  holding  a T t --period bond is equal to the expected return generated by a holding a series of oneperiod bonds and continually rolling them over on maturity. More formally, this can be expressed as (1.15):

10   See the footnote on page 644 of Shiller (1990) for a fascinating historical note on the origins of the expectations hypothesis. An excellent overview of the hypothesis itself is contained in Ingersoll (1987, pp. 389-392).

<!-- formula-not-decoded -->

The left-hand side of Equation (1.15) represents the return received by an investor holding a zero-coupon bond to maturity, which is equal to the expected return associated with rolling over £1 from time t to  time T by continually reinvesting one-period maturity bonds, each of which has a yield of the future spot rate r t . A good argument for this hypothesis is contained in Jarrow (1996, p. 52), which states that, essentially, in an environment of economic equilibrium , the returns on zero-coupon bonds of similar maturity  cannot  be  significantly  different,  otherwise  investors  would  not  hold the bonds with the lower return. A similar argument can be put forward in relation to coupon bonds of differing maturities. Any difference in yield would not therefore disappear as equilibrium was re-established. However, there are a number of reasons why investors will hold shorter-dated bonds, irrespective of the yield available on them, so it is possible for the return to maturity version of the hypothesis not to apply. In essence, this version represents an equilibrium condition in which expected holding period returns are equal, although it does not state that this return is the same from different bond-holding strategies.

From (1.14) and (1.15), we can determine that the unbiased expectations hypothesis and the return to maturity hypothesis are not compatible with each other, unless there is no correlation between future interest rates. As Ingersoll (1987) notes, although it would be both possible and interesting to model such an economic environment, it is not related to reality, as interest rates are highly correlated. Given positive correlation between rates over a period of time, bonds with maturity terms longer than two periods will have a higher price under the unbiased expectations hypothesis than under the return to maturity version. Bonds of exactly two-period maturity will have the same price.

The yield to maturity expectations hypothesis is described in terms of yields. It is given by:

<!-- formula-not-decoded -->

where the left-hand side of the equation specifies the yield to maturity of the zero-coupon bond at time t. In this version, the expected holding period yield on continually rolling over a series of one-period bonds is equal to the yield that is guaranteed by holding a long-dated bond until maturity.

The local expectations hypothesis states that all bonds will generate the same expected rate of return if held over a small term. It is given by:

<!-- formula-not-decoded -->

This version of the hypothesis is the only one that is consistent with noarbitrage, because the expected rates of return on all bonds are equal to the risk-free interest rate. For this reason, the local expectations hypothesis is sometimes referred to as the risk-neutral expectations hypothesis.

## Liquidity Preference Theory

Intuitively we might feel that longer maturity investments are more risky than shorter ones. An investor lending money for a five-year term will usually  demand a higher rate of interest than if they were to lend the same customer money for a five-week term. This is because the borrower may not be able to repay the loan over the longer time period as they may for instance, have gone bankrupt in that period. For this reason, longer-dated yields should be higher than short-dated yields, to compensate the lender for the higher risk exposure during the term of the loan. 11

We can consider this theory in terms of inflation expectations as well. Where inflation is expected to remain roughly stable over time, the market anticipates a positive yield curve. However, the expectations hypothesis cannot by itself explain this phenomenon, as under stable inflationary conditions one would expect a flat yield curve. The risk inherent in longer-dated investments, or the liquidity preference theory , seeks to explain a positively shaped curve. Generally, borrowers prefer to borrow over as long a term as possible, while lenders will wish to lend over as short a term as possible. Therefore, as we first stated, lenders have to be compensated for lending over the longer term. This compensation is considered a premium for a loss in liquidity for the lender. The premium is increased the further the investor lends across the term structure, so that the longest-dated investments will, all else being equal, have the highest yield. So the liquidity preference theory states that the yield curve should almost always be upward-sloping, reflecting bondholders' preference for the liquidity and lower risk of shorter-dated bonds.

11   For original discussion, see Hicks (1946).

An inverted yield curve could still be explained by the liquidity preference theory when it is combined with the unbiased expectations hypothesis. A humped yield curve might be viewed as a combination of an inverted yield curve together with a positively sloping liquidity preference curve.

The difference between a yield curve explained by unbiased expectations and an actual observed yield curve is sometimes referred to as the liquidity premium. This refers to the fact that in some cases short-dated bonds are easier to transact in the market than long-term bonds. It is difficult to quantify the effect of the liquidity premium, which in any cases is not static and fluctuates over time. The liquidity premium is so-called because, in order to encourage investors to hold longer-dated securities, the yields on such securities must be higher than those available on short-dated securities, which are more liquid and may be converted into cash more easily. The liquidity premium is the compensation required for holding less liquid instruments. If longer-dated securities then provide higher yields, as is suggested by the existence of the liquidity premium, they should generate on average, higher total returns over an investment period. This is not consistent with the local expectations hypothesis. More formally we can write:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where Ln is the premium for a bond with term to maturity of n years, which states  that  the  premium  increases  as  the  term  to  maturity  rises  and  that an otherwise flat yield curve will have a positively sloping curve, with the degree of slope steadily decreasing as we extend along the yield curve. This is consistent with the observation of yield curves under 'normal' conditions.

The expectations hypothesis assumes that forward rates are equal to the expected future spot rates, that is as shown in (1.18):

<!-- formula-not-decoded -->

where ( ) E is the expectations operator for the current period. This assumption implies that the forward rate is an unbiased predictor of the future spot rate, as we suggested in the previous paragraph. Liquidity preference theory on the other hand, recognises the possibility that the forward rate may contain an element of liquidity premium which declines over time as the period approaches, given by (1.19):

<!-- formula-not-decoded -->

and If there is uncertainty in the market about the future direction of spot rates and hence where the forward rate should lie, (1.19) is adjusted to give the reverse inequality.

An illustration of how liquidity preference will impact the 'clean' term structure suggested by the expectations hypothesis is given at Figure 1.14.

## Segmentation Hypothesis

The capital markets are made up of a wide variety of users, each with different  requirements.  Certain  classes  of  investors  will  prefer  dealing  at  the short end of the yield curve, while others concentrate on the longer end of the market. The segmented markets theory suggests that activity is concentrated  in  certain  specific  areas  of  the  market,  and  that  there  are  no  interrelationships between these parts of the market. The relative amounts of funds invested in each of the maturity spectrum causes differentials in supply and demand, which results in humps in the yield curve. That is, the shape of the yield curve is determined by supply and demand for certain specific maturity investments, each of which has no reference to any other part of the curve.

For example, banks and building societies concentrate a large part of their activity at the short end of the curve, as part of daily cash management (known  as asset  and  liability  management )  and  for  regulatory  purposes (known as liquidity requirements). Fund managers such as pension funds and insurance companies are active at the long end of the market. Few institutional investors, however, have any preference for medium-dated bonds. This behaviour on the part of investors leads to high prices (low yields) at both the short and long ends of the yield curve and lower prices (higher yields) in the middle of the term structure.

FIGURE 1.14 Yield curve explained by expectations hypothesis and liquidity preference theory.

<!-- image -->

According  to  the  segmented  markets  hypothesis,  a  separate  market exists for specific maturities along the term structure, and interest rates for these maturities are set by supply and demand. 12  Where there is no demand for a particular maturity, the yield lies above other segments. Market participants do not hold bonds in any other area of the curve outside their area of interest, 13  so that short-dated and long-dated bond yields exist independently of each other. The segmented markets theory is usually illustrated by reference to banks and life companies. Banks and building societies hold their funds in short-dated instruments, usually no longer than five years in maturity. This is because of the nature of retail banking operations, with a large volume of instant access funds being deposited at banks, and also for  regulatory  purposes.  Holding  short-term,  liquid  bonds  enables  banks to meet any sudden or unexpected demand for funds from customers. The classic theory suggests that as banks invest their funds in short-dated bonds, the yields on these bonds are driven down. When they then liquidate part of their holding, perhaps to meet higher demand for loans, the yields are driven up and prices of the bonds fall. This affects the short end of the yield curve, but not the long end.

The segmented markets theory can be used to explain any particular shape of the yield curve, although it fits best perhaps with positively sloping curves.  However, it  cannot  be  used  to  interpret  the  yield  curve  whatever shape it may be, and therefore offers no information content during analysis. By definition, the theory suggests that for investors, bonds with different maturities are not perfect substitutes for each other. This is because different bonds would have different holding period returns, making them imperfect substitutes of one another. 14  As a result of bonds being imperfect substitutes, markets are segmented according to maturity.

The  segmentations  hypothesis  is  a  reasonable  explanation  of  certain features  of  a  conventional  positively  sloping  yield  curve,  but  by  itself  is not sufficient. There is no doubt that banks and building societies have a requirement to hold securities at the short end of the yield curve, as much for regulatory purposes as for yield considerations, however, other investors are probably more flexible and will place funds where value is deemed to exist. Nonetheless the higher demand for benchmark securities does drive down yields along certain segments of the curve.

12   See Culbertson (1957).

13   For example, retail and commercial banks hold bonds in the short dates, while life assurance companies hold long-dated bonds.

14 Ibid.

A slightly modified version of the market segmentation hypothesis is known as the preferred habitat theory. This suggests that different market participants have an interest in specified areas of the yield curve, but can be encouraged to hold bonds from other parts of the maturity spectrum if there is sufficient incentive. Hence banks may at certain times hold longerdated bonds once the price of these bonds falls to a certain level, making the return on the bonds worth the risk involved in holding them. Similar considerations may persuade long-term investors to hold short-dated debt. So higher yields will be required to make bond holders shift out of their usual area of interest. This theory essentially recognises the flexibility that investors have, outside regulatory or legal requirements (such as the terms of an institutional fund's objectives), to invest in whatever part of the yield curve they identify value.

## Humped Yield Curves

When plotting a yield curve of all the bonds in a certain class, it is common to observe humped yield curves. These usually occur for a variety of reasons. In line with the unbiased expectations hypothesis, humped curves are observed when interest rates are expected to rise over the next several periods and then decline. On other occasions, humped curves can result from skewed expectations of future interest rates. This is when the market believes that fairly constant future interest rates are likely, but also believes that there is a small probability for lower rates in the medium term. The other common explanation for humped curves is the preferred habitat theory.

## The Combined Theory

The explanation for the shape of the yield curve at any time is more likely to be described by a combination of the pure expectations hypothesis and the liquidity preference theory, and possibly one or two other theories. Market analysts often combine the unbiased expectations hypothesis with the liquidity preference theory into an 'eclectic' theory. The result is consistent with any shape of yield curve, and is also a predictor of rising interest rates. In the combined theory, the forward interest rate is equal to the expected future spot rate, together with a quantified liquidity premium. This is shown at (1.20):

<!-- formula-not-decoded -->

where Li is  the liquidity premium for a term to maturity of i . The size of the liquidity premium is expected to increase with increasing maturity. 15  An illustration is given at Example 1.3.

15 So that L L i i 1 .

## EXAMPLE 1.3 POSITIVE YIELD CURVE WITH CONSTANT EXPECTED FUTURE INTEREST RATES

- ◾ Consider the interest rates structure in Table 1.3.

TABLE 1.3 Positive yield curve with constant expected future

interest rates

| Period n            | 0     | 1     | 2     | 3     | 4     | 5     |
|---------------------|-------|-------|-------|-------|-------|-------|
| E (rs)              |       | 4.50% | 4.50% | 4.50% | 4.50% | 4.50% |
| Forward rate 0 rf n |       | 5.00% | 5.50% | 6.00% | 6.50% | 7.50% |
| Spot rate rs n      | 5.00% | 5.30% | 5.80% | 6.20% | 6.80% | 7.00% |

The  current  term  structure  is  positively  sloping  since  the  spot  rates increase with increasing maturity. However, the market expects future spot rates to be constant at 4.5%. The forward and spot rates are also shown, however, the forward rate is a function of the expected spot rate and the liquidity premium. This premium is equal to 0.50% for the first year, 1.0% in the second, and so on.

The combined theory is consistent with an inverted yield curve. This applies  even  when  the  liquidity  premium  is  increasing  with  maturity,  for example,  where  the  expected  future  spot  interest  rate  is  declining.  Typically this would be where there was a current curve of falling yields along the term structure. The spot rates might be declining where the fall in the expected future spot rate exceeds the corresponding increase in the liquidity premium.

## The Flat Yield Curve

The conventional theories do not seek to explain a flat yield curve. Although it is rare to observe flat yield curves in a market, certainly for any length of time, at times they do emerge in response to peculiar economic circumstances.  In  the  conventional  thinking,  a  flat  curve  is  not  tenable  because investors should in theory have no incentive to hold long-dated bonds over shorter-dated bonds when there is no yield premium, so that as they sell off long-dated paper, the yield at the long end should increase, producing an upward-sloping curve. In previous circumstances of a flat curve, analysts have produced different explanations for their existence. In November 1988, the US Treasury yield curve was flat relative to the recent past. Researchers contended that this was the result of the market's view that long-dated yields would fall as bond prices rallied upwards. 16  One recommendation is to buy longer maturities when the yield curve is flat, in anticipation of lower long-term interest rates, which is the direct opposite to the view that a flat curve is a signal to sell long bonds. In the case of the US market in 1988, long bond yields did in fact fall by approximately 2% in the following 12 months. This indicates that our view of future long-term rates should be behind the decision to buy or sell long bonds, rather than the shape of the yield curve itself. A flat curve may well be more heavily influenced by supply and demand factors than anything else, with the majority opinion eventually winning out and forcing a change in the curve to a more conventional shape.

## Further Views on the Yield Curve

In this and the previous chapter, our discussion of present values, spot, and forward interest rates assumed an economist's world of the perfect market (also sometimes called the frictionless financial market). Such a perfect capital market is characterised by:

- ◾ perfect information;
- ◾ no taxes;
- ◾ bullet maturity bonds;
- ◾ no transaction costs.

Of  course  in  practice  markets  are  not  completely  perfect.  However, assuming perfect markets makes the discussion of spot and forward rates and the term structure easier to handle. When we analyse yield curves for their information content, we have to remember that the markets that they represent are not perfect, and that frequently we observe anomalies that are not explained by the conventional theories.

At any one time it is probably more realistic to suggest that a range of  factors  contributes  to  the  yield  curve  being  one  particular  shape.  For instance, short-term interest rates are greatly influenced by the availability of funds in the money market. The slope of the yield curve (usually defined as the ten-year yield minus the three-month interest rate) is also a measure of the degree of tightness of government monetary policy. A low, upwardsloping curve is often thought to be a sign that an environment of cheap money, due to a more loose monetary policy, is to be followed by a period of higher inflation and higher bond yields. Equally, a high downward-sloping curve is taken to mean that a situation of tight credit, due to more strict monetary policy, will result in falling inflation and lower bond yields. Inverted yield curves have often preceded recessions; for instance, The Economist in an article from April 1998 remarked that in the US every recession since 1955, except one, had been preceded by a negative yield curve. The analysis is  the same - if investors expect a recession, they also expect inflation to fall, so the yields on long-term bonds will fall relative to short-term bonds. So  therefore  the  conventional  explanation  for  an  inverted  yield  curve  is that the markets and the investment community expect either a slow-down of the economy, or an outright recession. 17  In this case, one would expect the monetary authorities to ease the money supply by reducing the base interest rate in the near future - hence an inverted curve. At the same time, a reduction of short-term interest rates will affect short-dated bonds and these are sold off by investors, further raising their yield.

16   See Levy (1999).

While  the  conventional  explanation  for  negative  yield  curves  is  an expectation of economic slow-down, on occasion other factors are involved. In  the  UK  in  the  period  July  1997-June  1999,  the  gilt  yield  curve  was inverted. 18  There was no general view that the economy was heading for recession, however. In fact the new Labour government led by Tony Blair inherited an economy believed to be in good health. Instead, the explanation behind the inverted shape of the gilt yield curve focused on two other factors: firstly, the handing of responsibility for setting interest rates to the Monetary Policy Committee (MPC) of the Bank of England, and secondly the expectation that the UK would, over the medium term, abandon sterling and join the euro currency. The yield curve at this time suggested that the market expected the MPC to be successful and keep inflation at a level around 2.5% over the long term (its target is actually a 1% range either side of 2.5%), and also that sterling interest rates would need to come down over the medium term as part of convergence with interest rates in euroland. These  are  both  medium-term  expectations,  however,  and  in  the  author's view not logical at the short end of the yield curve. In fact, the term structure moved to a positively sloped shape up to the six- to seven-year area, before inverting out to the long end of the curve, in June 1999. This is a more logical shape for the curve to assume, but it was short-lived and returned to being inverted after the two-year term.

There  is  therefore  significant  information  content  in  the  yield  curve, and economists and bond analysts will consider the shape of the curve as part of their policy-making and investment advice. The shape of parts of the curve, whether the short end or long end, as well that of the entire curve, can serve as useful predictors of future market conditions. As part of an analysis, it  is  also  worthwhile  considering  the  yield  curves  across  several  different markets and currencies. For instance, the interest rate swap curve, and its position relative to that of the government bond yield curve, is also regularly analysed for its information content. In developed country economies, the swap market is invariably as liquid as the government bond market, if not more liquid, and so it is common to see the swap curve analysed when making predictions about, say, the future level of short-term interest rates.

17   A recession is formally defined as two successive quarters of falling output in the domestic economy.

18   Although the curve briefly went positively sloped out to seven to eight years in July 1999, it very quickly reverted to being inverted throughout the term structure, and  remained  so  until  summer  2001.  It  subsequently  reverted  to  a  conventional

positively sloping curve.

Government policy influences the shape and level of the yield curve, including policy on public sector borrowing, debt management, and openmarket operations. The market's perception of the size of public sector debt influences bond yields. For example, an increase in the level of debt can lead to an increase in bond yields across the maturity range. Open-market operations, which refers to the daily operation by the Bank of England to control the level of the money supply (to which end the Bank purchases short-term bills and also engages in repo dealing), can have a number of effects. In the short-term,  it  can  tilt  the  yield  curve  both  upwards  and  downwards.  In the longer-term, changes in the level of the base rate will affect yield levels. An anticipated rise in base rates can lead to a decrease in prices for short-term bonds,  because  short-term  bond  yields  will  be  expected  to  rise  and  this can lead to a temporary inverted curve. Finally, debt management policy influences the yield curve. (In the UK this is the responsibility of the Debt Management Office.) Most government debt is rolled over as it matures, but the maturity of the replacement debt can have a significant influence on the yield curve in the form of humps in the market segment in which the debt is placed, if the debt is priced by the market at a relatively low price and hence high yield.

## AN INTRODUCTION TO FITTING THE YIELD CURVE

When graphing a yield curve, we plot a series of discrete points of yield against maturity. Similarly for the term structure of interest rates, we plot spot rates for a fixed time period against that time period. The yield curve itself, however, is a smooth curve drawn through these points. Therefore we require a method that allows us to fit the curve as accurately as possible, known as yield curve modelling or estimating the term structure . There are several ways to model a yield curve, which we introduce in this section. We will return to the subject in greater depth later in the book.

Ideally,  the  fitted  yield  curve  should  be  a  continuous  function, with no gaps in the curve, while passing through the observed yield vertices. The curve also needs to be 'smooth', as 'kinks' in the curve will produce sudden sharp jumps in derived forward rates. We have stated how it is possible to calculate a set of discrete discount factors or a continuous discount function. It has been shown that the discount function, par yield curve, spot rate yield curve, and forward rate curve are all related mathematically, such that if one knows any one of these, the other three can be derived. In practice, in many markets it is generally not possible to observe the curves directly, hence they need to be derived from coupon bond prices and yields. In attempting to model a yield curve from bond yields, we need to consider the two fundamental issues introduced above. Firstly, there is the problem of gaps in the maturity spectrum, as in reality there will not be a bond maturing at regular intervals along the complete term structure. For example, in the UK gilt market at the time of writing of the first edition, there was no bond at all maturing between 2017 and 2021, or between 2021 and 2028. Secondly, as we have seen, the term structure is formally defined in terms of spot or zero-coupon interest rates, but in many markets there is no actual zero-coupon bond market. In such cases spot rates cannot be inferred directly but must be implied from coupon bonds. Where zero-coupon bonds are traded, for example, in the US and UK government bond markets, we are able to observe zero-coupon yields directly in the market.

Further problems in fitting the curve arise from these two issues:

- ◾ How is the gap in maturities to be tackled? Analysts need to choose between  'smoothness'  and  'responsiveness'  of  the  curve  estimate. Most  models  opt  for  a  smooth  fitting,  however,  enough  flexibility should be retained to allow for true movements in the term structure where indicated by the data.
- ◾ Should the yield curve be estimated from the discount function or say, the par yield curve?

There are other practical factors to consider as well, such as the effect of withholding tax on coupons, and the size of bond coupons themselves. We will consider the issues connected with estimating the yield curve in a later chapter. At this point, however, we confine ourselves to introducing the main methods.

## Interpolation

The simplest method that is employed to fit a curve is linear interpolation , which involves drawing a straight line joining each pair of yield vertices. To calculate the yield for one vertex we use (1.21):

<!-- formula-not-decoded -->

where rmt is  the  yield  being  estimated  and n is  the  number  of  years  to maturity for yields that are observed. For example, consider the following redemption yields:

| 1 month:   | 4.00%   |
|------------|---------|
| 2 years:   | 5.00%   |
| 4 years:   | 6.50%   |
| 10 years:  | 6.75%   |

If we wish to estimate the six-year yield, we calculate it using (1.21), which is:

<!-- formula-not-decoded -->

The limitations of using linear interpolation are that first, the curve can have sharp angles at the vertices where two straight lines meet, resulting in unreasonable jumps in the derived forward rates. Second, and more fundamentally, being a straight-line method, it assumes the yield between two vertices should automatically be rising (in a positive yield curve environment) or falling. This assumption can lead to gross inaccuracies in the fitted curve.

Another approach is to use logarithmic interpolation ,  which involves applying linear interpolation to the natural logarithms of the corresponding discount factors. Therefore, given any two discount factors we can calculate an intermediate discount factor using (1.22):

<!-- formula-not-decoded -->

To calculate the six-year yield from the same yield structure above, we use the following procedure:

- ◾ calculate the discount factors for years 4 and 10 and then take the natural logarithms of these discount factors;
- ◾ perform a linear interpolation on these logarithms;
- ◾ take  the  anti-log  of  the  result,  to  get  the  implied  interpolated  discount factor;
- ◾ calculate the implied yield in this discount factor.

Using (1.22) we obtain a six-year yield of 6.6388%. The logarithmic interpolation method reduces the sharpness of angles on the curve and so makes it smoother, but it retains the other drawbacks of the linear interpolation method.

## Polynomial Models 19

The most straightforward method for estimating the yield curve involves fitting a single polynomial in time. For example, a model might use an F -order polynomial, illustrated with (1.23):

<!-- formula-not-decoded -->

rmi is the yield to maturity of the i -th bond;

Ni is the term to maturity of the i -th bond;

, 1 , are coefficients of the polynomial;

u i is the residual error on the i -th bond.

To determine the coefficients of the polynomial we minimise the sum of the squared residual errors, given by:

<!-- formula-not-decoded -->

where T is  the  number  of  bonds  used. This  is  represented  graphically  in Figure 1.15.

The type of curve that results is a function of the order of the polynomial F. If F is too large, the curve will not be smooth but will be in effect too 'responsive', such that the curve runs through every point, known as being 'over-fitted'. The extreme of this is given when F T 1. If F is too small, the curve will be an over-estimation.

The method described above has been supplanted by a more complex method, which fits different  polynomials  over  different,  but  overlapping, terms to maturity. The fitted curves are then spliced together to produce a single smooth curve over the entire term structure. This is known as a spline curve and is the one most commonly encountered in the markets. For an accessible introduction to spline techniques, see James and Webber (2000) and Choudhry et al. (2001).

The limitation of the polynomial method is that a 'blip' in the observed series of vertices, for instance, a vertex which is out of line with others in

19   These  are  standard  econometric  techniques.  For  an  excellent  account  see Campbell et al . (1997).

where the series, produces a 'wobbled' shape, causing wild oscillations in the corresponding  forward  yields. This  can  result  in  the  calculation  of  negative long-dated forward rates.

## Cubic Splines

The cubic spline method involves connecting each pair of yield vertices by fitting a unique cubic equation between them. This results in a yield curve where the whole curve is represented by a chain of cubic equations, instead of  a  single  polynomial. This  technique adds some 'stiffness' to the yield curve, while at the same time preserving its smoothness. 20

Using the same example as before, we wish to fit the yield curve from 0 to 10 years.

There are four observed vertices, so we require three cubic equations, rm i t , each one connecting two adjacent vertices n i and n i 1 as follows:

<!-- formula-not-decoded -->

where a b c , , , and d are  unknowns.  The  equations  each  contain  four unknowns (the coefficients a to d ),  and  there  are  three  equations  so  we require a total of twelve conditions to solve the system. The cubic spline method imposes certain conditions on the curves, which makes it possible to solve the system. The solution for this set is summarised in Appendix 1.3 of the first edition.

FIGURE 1.15 Polynomial curve-fitting.

<!-- image -->

20   In case you're wondering, a spline is a tool used by a carpenter in order to draw smooth curves.

Term to maturity The three cubic equations for the data in this example are:

<!-- formula-not-decoded -->

Using a cubic spline produces a smoother curve for both the spot rates and the forward rates, while the derived forward curve will have fewer  'kinks' in it.

To calculate the estimated yield for the six-year maturity, we apply the third cubic equation, which spans the four to ten year vertices, which is:

<!-- formula-not-decoded -->

From Appendix 1.3 of the first edition, it is clear that simply to fit a fourvertex spline requires the inversion of a fairly large matrix. In practice, more efficient mathematical techniques, known as basis splines or B-splines , are typically used when there is a larger number of observed yield vertices. This produces results that are very close to what we would obtain by simple matrix inversion.

## Regression Models

A variation on polynomial fitting is regression analysis. In this method, bond prices are used as the dependent variable, with the coupon and maturity cash flows of the bonds being the independent variables. This is given by (1.25):

<!-- formula-not-decoded -->

P d is the dirty price of the i -th bond;

Cni is the coupon of the i -th bond in period n;

n is the coefficient of the regression equation;

u i , is the residual error in the i -th bond.

In fact, the coefficient in (1.25) is an estimate of the discount factor, as shown by (1.26) and can be used to generate the spot interest rate curve.

<!-- formula-not-decoded -->

In the form shown, (1.25) cannot be estimated directly. This is because individual  coupon  payment  dates  differ  across  different  bonds,  and  in  a semi-annual coupon market there are more coupons than bonds available.

where

FIGURE 1.16 Grid point allocation in regression analysis.

<!-- image -->

In practice therefore, the term structure is divided into specific dates, known as grid points ,  along  the  entire  maturity  term;  and coupon payments are then allocated between two grid points. The allocation between two points is done in such a way so that the present value of the coupon is not altered. This is shown in Figure 1.16.

Note that there are more grid points at the short end of the term structure, with progressively fewer points as we reach the longer end. This is because the preponderance of the data is invariably at the shorter end of the curve, which makes yield curve fitting more difficult. At the long end, however , the shortage of data, due to the relative lack of issues, makes curve estimation more inaccurate.

The  actual  regression  equation  that  is  used  in  the  analysis  is  given at (1.27) where d ni * represents the grid points:

<!-- formula-not-decoded -->

The  two  methodologies  described  above  are  the  most  commonly encountered in the market. Models used to estimate the term structure generally  fall  into  two  distinct  categories,  these  being  the  ones  that  estimate the structure using the par yield curve, and those that fit it using a discount function. We shall examine these in greater detail in a later chapter.

## SPOT AND FORWARD RATES IN THE MARKET

## Using Spot Rates

The concepts discussed in this chapter are important and form a core part of debt markets analysis. It may appear that the content is largely theoretical, especially since many markets do not trade zero-coupon instruments and so spot rates are therefore not observable in practice, however, the concept of the spot rate is an essential part of bond (and other instruments') pricing. In the first instance, we are already aware that bond redemption yields do not reflect a true interest rate for that maturity, for which we use the spot rate. For relative value purposes, traders and portfolio managers frequently compare a bond's actual market price to its theoretical price, calculated using specific zero-coupon yields for each cash flow, and determine whether the bond is 'cheap' or 'dear'. Even where there is some misalignment between the theoretical price of a bond and the actual price, the decision to buy or sell may be based on judgemental factors, since there is often no zero-coupon instrument against which to effect an arbitrage trade. In a market where no zero-coupon instruments are traded, the spot rates used in the analysis are theoretical and are not represented by actual market prices. Traders therefore often analyse bonds in terms of relative value against each other, and the redemption yield curve, rather than against their theoretical zero-coupon based price.

What considerations apply where a zero-coupon bond market exists alongside a conventional coupon-bond market? In such a case, theoretically arbitrage trading is possible if a bond is priced above or below the price suggested by zero-coupon rates. For example, a bond priced above its theoretical price could be sold, and zero-coupon bonds that equated its cash flow stream could be purchased - the difference in price is the arbitrage profit. Similarly, a bond trading below its theoretical price could be purchased and its  coupons 'stripped'  and  sold  individually  as  zero-coupon  bonds. The proceeds from the sale of the zero-coupon bonds would then exceed the purchase price of the coupon bond. In practice, often the existence of both markets equalises prices between both markets so that arbitrage is no longer possible, although opportunities will still occasionally present themselves.

## Using Forward Rates

Newcomers to the markets frequently experience confusion when first confronted with forward rates. Do they represent the market's expectation of where interest rates will actually be when the forward date arrives? If forward rates are a predictor of future interest rates, exactly how good are they at making this prediction? Empirical evidence 21  suggests that in fact forward rates  are  not  accurate  predictors  of  future  interest  rates,  frequently  overstating them by a considerable margin. If this is the case, should we attach any value or importance to forward rates?

The value of forward rates does not lie, however, in its track record as a market predictor, but moreover in its use as a hedging tool. As we illustrate in Example 1.3, the forward rate is calculated on the basis that if we are to price say, a cash deposit with a forward starting date, but we wish to deal today, the return from the deposit will be exactly the same as if we invested for a start date today and rolled over the investment at the forward date. The forward rate allows us to lock in a dealing rate now. Once we have dealt today, it is irrelevant what the actual rate pertaining on the forward date is - we have already dealt. Therefore forward rates are often called hedge rates, as they allow us to lock in a dealing rate for a future period, thus removing uncertainty.

21   Including Fama (1976).

The existence of forward prices in the market also allows us to make an investment decision, based on our view compared to the market view. The forward rate implied by say, government bond prices is, in effect, the market's view of future interest rates. If we happen not to agree with this view, we will deal accordingly. We are effectively comparing our view on future interest rates with that of the market, and making our investment decision based on this comparison.

## ◾ Understanding forward rates

Spot and forward rates that are calculated from current market rates follow mathematical principles to establish what the market believe the arbitrage-free rates for dealing today at rates that are effective at some point in the future. As such forward rates are not a  type  of  market prediction of where interest rates will be (or should be!) in the future. As we have already noted, forward rates are not a prediction of future rates. It is important to be aware of this distinction. If we were to plot the forward rate curve for the term structure in three months' time, and then compare it in three months with the actual term structure prevailing at the time, the curves would almost certainly not match. When we calculate forward rates, we use the current term structure. The current term structure incorporates all known information, both economic and political, and reflects the market's views. This is exactly the same as when we say that a company's share price reflects all that is known about the company and all that is expected to happen with regard to the company in the near future, including expected future earnings. The term structure of interest rates reflects everything the market knows about relevant domestic and international factors. It is this information that goes into the forward rates calculation. In three months' time, however, there will be new developments that will alter the market's view and therefore alter the current term structure. These developments and events are (by definition, as we cannot know what lies in the future!) not known at the time we calculated and used the three-month forward rates. This is why rates actually turn out to be different from what the term structure predicted at an earlier date. However, for dealing today we use today's forward rates, which reflect everything we know about the market today. In essence then, forward rates and spot rates are two sides of the same coin: if we wish to deal today for a value date in the future, the forward rate is the rate given by the no-arbitrage concept. It is, in this respect, equivalent to the spot rate: it's just the spot rate for forward date value if we wish to execute the trade today.

## THE INTEREST-RATE SWAP CURVE AND THE SOVEREIGN BOND CURVE

We have noted at the outset the importance of interpreting the yield curve so one can understand as fully as possible what it is telling us about current and future expected market conditions. This is not necessarily a straightforward exercise even when all the accepted orthodoxies are in place; namely,

- ◾ positive interest rates;
- ◾ a positively sloping yield curve;
- ◾ domestic sovereign bond yields exhibiting the lowest rates in that currency.

All  of  the  above  conventions  are  commonly  not  evident  in  many  of today's  bond  markets. We  consider  negative  rates  in  a  subsequent  chapter. For now, consider Figure 1.17 which is the US Treasury and US dollar interest-rate swap curves as at 30 April 2018.

We note that the swap curve trades through the Treasury curve at the long end. Even this is not particularly extreme given the post-2008 environment, when in recent years one has observed the swap curve sitting below the Treasury curve at shorter tenors, including the five- and ten-year points. Given that the local market sovereign bond yield is generally regarded as the 'risk-free' rate in that economy (we accept that such a position is not 'risk free', this is just an expression for the lowest risk investment in that currency), how does one interpret a curve showing the swap rate lower than the sovereign bond yield?

FIGURE 1.17 US Treasury and US dollar interest rate swap curves, 30 April 2018. Rates source : YieldCurve.com, InterestRateSwapsToday.com.

<!-- image -->

Compared to the orthodoxy prevailing before 2008, we should note first that interest-rate swap markets, like all interbank derivatives markets now cleared through centralised clearing counterparties (CCPs), are collateralised. The counterparty risk is removed as a result of collateral passed to the CCP by the party that is negative mark-to-market on the swap. (Ignore margin period of risk in this instance.) This is on top of the initial margin (IM) that all CCP parties place with the clearing house or their agent bank. As such, one can view a swap transaction between banks as 'risk free' in the same way that one views a US Treasury holding as credit risk free. This would explain the swap curve being very close to the Treasury curve.

But in our example, which we noted is by no means the most extreme than the sovereign risk than the Treasury. What

manifestation of this phenomenon, the swap rate is lower rate. In other words, it is perceived as lower explanation can we offer for this behaviour?

In the first instance, there is supply and demand. Banks and non-bank financial institutions have a sizeable demand to hedge long-dated fixed-rate receivables risk, which means they need to pay fixed in the swap. The excess demand for swaps pushes the rate down at the market-making banks (who drive what the swap rate is). Then there is liquidity: the swap market is very liquid in a way that is not always available in the Treasury market, since the advent of more onerous capital rules for banks who run Trading Books (as opposed to the Banking Book).

Finally, there is the conventional feature of government bonds where the longest-dated yield, in a positively sloping environment, often drops below the prior tenor point (thereby becoming downward sloping). This isn't the case with the curve shown at Figure 1.17, and the explanation for that is the expectation that base interest rates will continue to rise in the short and medium term (as indeed, the Federal Reserve was indicating at that time). Thus this  feature  combined  with  the  other  two  factors  gives  us  the  two curves we are discussing.

## APPENDIX: CUBIC SPLINE INTERPOLATION

There are four observed vertices in the example quoted in the main text, which requires three cubic equations, m i t , , each one connecting two adjacent vertices n i and n i 1 , as follows:

<!-- formula-not-decoded -->

where a b c , , , and d are unknowns. The three equations require 12 conditions in all. The cubic spline method imposes the following set of conditions on the curves. Each cubic equation must pass through its own pair of vertices. Thus, for the first equation:

<!-- formula-not-decoded -->

For the second and third equations:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The resulting yield curve should be smooth at the point where one cubic equation joins with the next one. This is achieved by requiring the slope and the convexity of adjacent equations to be equal at the point where they meet,  ensuring  a  smooth  rollover  from  one  equation  to  the  next.  Mathematically, the first and second derivatives of all adjacent equations must be equal at the point where the equations meet.

Thus, at vertex n 1 :

<!-- formula-not-decoded -->

And at vertex n 2 :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Finally,  we  may  impose  the  condition  that  the  splines  tail  off  flat  at the end vertices, or more formally, we state mathematically that the second derivatives should be zero at the end points:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

These constraints together give us a system of 12 equations from which we can solve for the 12 unknown coefficients. The solution is usually using matrices, where the equations are expressed in matrix form. This is shown at Figure 1.18.

<!-- formula-not-decoded -->

```
1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 4 5 6.5 6.75 0 0 0 0 0 0 0 0 a 0 b 0 c 0 d 0 a 1 b 1 c 1 d 1 a 2 b 2 c 2 d 2 0 0 0 0 n 2 n 3 0 0 -1 0 0 0 n 0 n 1 0 0 0 0 1 0 0 0 0 0 n 0 2 n 1 2 0 0 0 0 2 n 1 2 0 0 2 0 n 0 3 n 1 3 0 0 0 0 3 n 1 2 6 n 1 0 0 6 n 0 0 0 0 n 1 3 n 2 3 0 0 -3 n 1 2 -6 n 1 3 n 2 2 6 n 2 0 0 0 0 n 1 2 n 2 2 0 0 -2 n 1 -2 2 n 2 2 0 0 0 0 n 1 n 2 0 0 -1 0 1 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 n 2 3 n 3 3 0 0 -3 n 2 2 -6 n 2 0 6 n 3 0 0 0 0 n 2 2 n 3 2 0 0 -2 n 1 -2 0 2 = ×
```

FIGURE 1.18 Cubic spline interpolation matrix.

In  matrix  notation  we  have n rm Coefficients therefore  the solution is  Coefficients n rm 1 . Inverting the matrix n and then premultiplying rm with the resulting inverse, we obtain the array of required coefficients:

<!-- formula-not-decoded -->

So the three cubic equations are specified as:

rm n n n n t 0 3 0 1 0 022 0 413 4 000 , for vertices . . . ,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## SELECTED BIBLIOGRAPHY AND REFERENCES

Anderson, N. and Sleath, J., Bank of England Quarterly Bulletin, November 1999.

Campbell, J., 'A Defence of Traditional Hypotheses about the Term Structure of Interest Rates', Journal of Finance, March 1986, pp. 183-193.

Campbell, J., Lo, A. and MacKinlay, A., The Econometrics of Financial Markets , Princeton UP, 1997, Chapters 10-11.

- Choudhry, M., 'The information content of the United Kingdom gilt yield curve', unpublished MBA assignment, Henley Management College, 1998.
- Choudhry, M., Joannas, D., Pereira, R. and Pienaar, R., Capital Markets Instruments, FT Prentice Hall, 2001.
- Cox, J., Ingersoll, J.E. and Ross, S.A., 'A re-examination of traditional hypothesis about the term structure of interest rates', Journal of Finance 36, September 1981, pp. 769-799.
- Culbertson, J.M., 'The term structure of interest rates', Quarterly Journal of Economics 71, November 1957, pp. 485-517.
- Fama, E.F., 'Forward rates as predictors of future spot interest rates', Journal of Financial Economics, Vol. 3, No. 4, October 1976, pp. 361-377.
- Fama, E.F., 'The information in the term structure', Journal of Financial Economics 13, December 1984, pp. 509-528.
- Fisher, I., 'Appreciation of Interest', Publication of the American Economic Association, August 1986, pp. 23-39.
- Heath, D., Jarrow, R. and Morton, A., 'Bond pricing and the term structure of interest rates', Journal of Financial and Quantitative Analysis 25, 1990, pp. 419-440.
- Hicks, J., Value and Capital , OUP, 1946.
- Ingersoll, J., Theory of Financial Decision Making , Rowman &amp; Littlefield, 1987, Chapter 18.
- James, J. and Webber, N., Interest Rate Modelling , John Wiley and Sons, 2000.
- Jarrow, R, 'Liquidity premiums and the expectations hypothesis', Journal of Banking and Finance 5(4), 1981, pp. 539-546.
- Jarrow, R., Modelling Fixed Income Securities and Interest Rate Options , McGraw-Hill, 1996
- Jarrow, R., and Turnbull, S., Derivative Securities , South-Western Publishing, 2000.
- Kessel, R.A., 'The cyclical behaviour of the term structure of interest rates', Essays in Applied Price Theory , University of Chicago, 1965.
- Kolb, R., Futures, Options and Swaps , Blackwell, 2000.
- Levy, H., Introduction to Investments , 2nd edition, South-Western College Publishing, 1999.
- Livingstone, M., Money and Capital Markets , Prentice-Hall, 1990, pp. 254-256.

Lutz, F., 'The Structure of Interest Rates',

November 1940, pp. 36-63.

- Mastronikola, K., 'Yield curves for gilt-edged stocks: a new model', Bank of England Discussion Paper (Technical Series), No. 49, 1991.
- McCulloch, J.H., 'An estimate of the liquidity premium', Journal of Political Economy 83, Jan-Feb 1975, pp. 95-109.
- Meiselman, D., The Term Structure of Interest Rates , Prentice Hall, 1962.
- Ryan, R. (ed.), Yield Curve Dynamics , Glenlake Publishing Company, 1997.
- Rubinstein, M., Rubinstein on Derivatives , RISK, 1999, pp. 84-85.
- Shiller, R. 'The Term Structure of Interest Rates', in Friedman, B., Hahn, F. (ed.), Handbook of Monetary Economics , North-Holland, 1990, Chapter 13.
- Windas, T., An Introduction to Option-Adjusted Spread Analysis , Bloomberg Publishing, 1993.

Quarterly Journal of Economics

,

He critically failed to delegate or appoint talented people lest they might undermine his overall authority. Instead he promoted those whose weaknesses he understood and could exploit. Competence was not an issue.

-- James Wyllie, Goering and Goering: Hitler's Henchman and his Anti-Nazi Brother , The History Press, 2006

## CHAPTER  2 A Further Look at Spot and Forward Rates

I n this chapter, we continue the analysis from Chapter 1, using more technical terminology. First we illustrate basic concepts, which is followed by a discussion of yield curve analysis and the term structure of interest rates.

We are familiar with two types of fixed income securities, zero-coupon bonds , also known as discount bonds or strips , and coupon bonds . A zerocoupon bond makes a single payment on its maturity date, while a coupon bond makes regular interest payments at regular dates up to and including its maturity date. A coupon bond may be regarded as a set of strips, with  each  coupon  payment  and  the  redemption  payment  on  maturity being equivalent to a zero-coupon bond maturing on that date. This is not a  purely  academic  concept,  which  is  illustrated  by  events  that  occurred before the advent of the formal market in US Treasury strips, when a number of investment banks traded the cash flows of Treasury securities as separate zero-coupon securities. 1 The literature we review in this section is set in a market of default-free bonds, whether they are zero-coupon bonds or coupon bonds. The market is assumed to be liquid so that bonds may be freely bought and sold. Prices of bonds are determined by the economy-wide supply and demand for the bonds at any time, so they are macroeconomic and not set by individual bond issuers or traders.

1   The term 'strips' comes from Separate Trading of Registered Interest and Principal of Securities, the name given when the official market was introduced in US Treasury  securities.  The  banks  would  purchase  Treasuries  which  would  then  be

## ZERO-COUPON BONDS

A zero-coupon bond is the simplest form of fixed income security. It is an issue of debt, the issuer promising to pay the face value of the debt to the bondholder on the date the bond matures. There are no coupon payments during the life of the bond, so it is a discount instrument, issued at a price that is below the face or principal amount. We denote as P t T , , the price of a discount bond at time t that matures at time T , with T t /greaterthanorequalangled . The term to maturity of the bond is denoted with n , where n T t . The price  increases  over  time  until  the  maturity  date  when  it  reaches  the maturity or par value. If the par value of the bond is £1, then the yield to maturity of the bond at time t is denoted by r t T , , where r is actually 'one plus the percentage yield' that is earned by holding the bond from t to T . We have:

<!-- formula-not-decoded -->

The yield may be obtained from the bond price and is given by:

<!-- formula-not-decoded -->

which is sometimes written as:

<!-- formula-not-decoded -->

Analysts  and  researchers  frequently  work  in  terms  of  logarithms  of yields  and  prices,  or  continuously  compounded  rates.  One  advantage  of

deposited in a safe custody account. Receipts were issued against each cash flow from each Treasury, and these receipts traded as individual zero-coupon securities. The market-making banks earned profit due to the arbitrage difference in the price of the original coupon bond and the price at which the individual strips were sold. The US Treasury formalised trading in strips after 1985, after legislation had been introduced that altered the tax treatment of such instruments. A market in UK gilt strips trading began in December 1997, however it never developed any depth or liquidity and was discontinued. Strips are also traded in France, Germany, and the Netherlands, among other countries.

this  is  that  it  converts  the  non-linear  relationship  in  (2.2)  into  a  linear relationship. 2

The bond price at time t 2 where t t T /lessthanorequalangled /lessthanorequalangled 2 is given by:

<!-- formula-not-decoded -->

which is consistent given that the bond price equation in continuous time is:

<!-- formula-not-decoded -->

so that the yield is given by:

<!-- formula-not-decoded -->

which is sometimes written as:

<!-- formula-not-decoded -->

The expression in (2.4) includes the exponential function, hence the use of the term continuously compounded.

The term structure of interest rates is the set of zero-coupon yields at time t for all bonds ranging in maturity from t t , 1  to t t m , where the bonds have maturities of  0 1 2 , , , , m . A good definition of the term structure of interest rates is given by Sundaresan, who states that it:

' . . . refers to the relationship between the yield to maturity of default-free zero coupon securities and their maturities.'

(Sundaresan 1997, p. 176)

2   A linear relationship in X would be a function Y f X in which the X values change via a power or index of 1 only and are not multiplied or divided by another variable or variables. So for example, terms such as X 2 , X and other similar functions are not linear in X , nor are terms such as XZ or X Z / where Z is another variable. In econometric analysis, if the value of Y is solely dependent on the value of X , then its rate of change with respect to X , or the derivative of Y with respect to X , denoted dY dX / , is independent of X . Therefore if Y X 5 then dY dX / 5, which is independent of the value of X . However, if Y X 5 2 , then dY dX X / 10 which is

The yield curve is a plot of the set of yields for r t t , 1  to r t t m , against n at time t . For example, Figures 2.1-2.3 show the log zero-coupon yield curve for US Treasury strips, UK gilt strips, and French OAT strips on 27 September 2000. Each of the curves exhibit peculiarities in their shape, although the most common type of curve is gently upward-sloping, as is the French curve. The UK curve is inverted . We explore further the shape of the yield curve later in this chapter.

<!-- image -->

FIGURE 2.1 US Treasury zero-coupon yield curve in September 2000. Source : Bloomberg L.P.

<!-- image -->

Term to maturity (years)

FIGURE 2.2 UK gilt zero-coupon yield curve, September 2000. Source : Bloomberg L.P.

not independent of the value of X . Hence this function is not linear in X . The classic regression function E Y X X i i | is a linear function with slope b and intercept a and the regression 'curve' is represented geometrically by a straight line.

French OAT zero-coupon yield curve.

<!-- image -->

FIGURE 2.3 Source : Bloomberg L.P.

## COUPON BONDS

The majority of bonds in the market make periodic interest or coupon payments during their life, and are known as coupon bonds. We have already noted  that  such  bonds  may  be  viewed  as  a  package  of  individual  zerocoupon bonds. The coupons have a nominal value that is a percentage of the nominal value of the bond itself, with steadily longer maturity dates, while the final redemption payment has the nominal value of the bond itself and is  redeemed on the maturity date. We denote a bond issued at time i and maturing at time T as having a w -element vector of payment dates: ( ) 1 2 -1 , , , , w t t t T … and  matching  date  payments 1 2 -1 , , , , w w C C C C … .  In  academic literature, these coupon payments are assumed to be made in continuous time, so that the stream of coupon payments is given by a positive function of time C t , i t T /lessthanorequalangled . An investor that purchases a bond at time t that matures at time T pays P t T , and will receive the coupon payments as long as they continue to hold the bond. 3

The  yield  to  maturity  at  time t of  a  bond  that  matures  at T is  the interest rate that relates the price of the bond to the future returns on the bond, that is, the rate that discounts the bond's cash flow stream 1, 2, w C … to its price P t T , .

3   Theoretically, this is the discounted clean price of the bond. For coupon bonds in practice, unless the bond is purchased for value on a coupon date, it will be traded with interest accrued. The interest that has accrued on a pro-rata basis from the last coupon date is added to the clean price of the bond, to give the market 'dirty' price that is actually paid by the purchaser.

This is given by:

<!-- formula-not-decoded -->

which says that the bond price is given by the present value of the cash flow stream of the bond, discounted at the rate r t T , . For a zero-coupon (2.7) reduces to (2.5). In academic literature, where coupon payments are assumed to be made in continuous time, the summation in (2.7) is replaced by the ∫ integral. We will look at this shortly.

In some texts, the plot of the yield to maturity at time t for the term of the bonds m is described as the term structure of interest rates but it is generally accepted that the term structure is the plot of zero-coupon rates only. Plotting yields to maturity is generally described as graphically depicting the yield curve, rather than the term structure. Of course, given the law of one price, there is a relationship between the yield to maturity yield curve and the zero-coupon term structure, and given the first one can derive the second.

The expression at (2.7) obtains the continuously compounded yield to maturity r t T , . It is the use of the exponential function that enables us to describe the yield as continuously compounded.

The market frequently uses the measure known as current yield ,  which is:

<!-- formula-not-decoded -->

where P d is the dirty price of the bond. The measure is also known as the running yield or flat yield . Current yield is not used to indicate the interest rate  or  discount  rate  and  therefore  should  not  be  mistaken  for  the  yield to maturity.

## BOND PRICE IN CONTINUOUS TIME 4

## Fundamental Concepts

In this section, we present an introduction to the bond price equation in continuous time. The necessary background on price processes is introduced in the next chapter. Readers will see the logic in this as we introduce term structure modelling there.

4   See also Avellaneda (2000), Baxter and Rennie (1996), Neftci (2000), Campbell et al . (1997), Ross (1999), and Shiller (1990), amongst others. These are all excellent texts of very high quality, and strongly recommended. For an accessible and

Let us consider a trading environment where bond prices evolve in a w -dimensional process:

<!-- formula-not-decoded -->

where the random variables are termed state variables that reflect the state of  the  economy at any point in time. The markets assume that the state variables evolve through a process described as geometric Brownian motion or a Weiner process. It is therefore possible to model the evolution of these variables, in the form of a stochastic differential equation.

The market assumes that the cash flow stream of assets such as bonds and equities is a function of the stated variables. A bond is characterised by its coupon process:

<!-- formula-not-decoded -->

The coupon process represents the cash flow that the investor receives during the time that they hold the bond. Over a small incremental increase in time of dt from the time t , the investor can purchase 1 C t dt units of the bond at the end of the period t dt . Assume that there is a very shortterm discount security such as a Treasury bill that matures at t dt ,  and during  this  period  the  investor  receives  a  return  of r t .  This  rate  is  the annualised short-term interest rate or short rate , which, in the mathematical analysis is defined as the rate of interest charged on a loan that is taken out at time t and which matures almost immediately. For this reason, the rate is also known as the instantaneous rate . The short rate is given by:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

highly readable introduction, Ross's book is worth buying for Chapter 4 alone, as is   Avellaneda's for his Chapter 12. For a general introduction to the main pricing concepts, see Campbell et al . (1997), Chapter 10. Chapter 3 in Jarrow (1996) is an accessible  introduction  for  discrete-time  bond  pricing. The  author  had  this  book with him on the sterling desk at Hambros Bank in 1997 and it's as valuable now as it was to him then. Sundaresan (1997) is an excellent overview text on the fixed income market as a whole, and is highly recommended.

and If we continuously reinvest the short-term security such as the T-bill at this short rate, we obtain a cumulative amount that is the original investment multiplied by (2.13a). 5

<!-- formula-not-decoded -->

where M is a money market account that offers a return of the short rate r t . If we say that the short rate is constant, making r t r , then the price of a risk-free bond that pays £1 on maturity at time T is given by:

<!-- formula-not-decoded -->

What (2.13b) states is that the bond price is simply a function of the continuously-compounded interest rate, with the right-hand side of (2.13b) being the discount factor at time t . At t T the discount factor will be 1, which is the redemption value of the bond and hence the price of the bond at this time.

Let us now consider the following scenario. A market participant may undertake the following:

- ◾ it can invest e r T t units cash in a money market account today, which will have grown to a sum of £1 at time T ;
- ◾ it can purchase the risk-free zero-coupon bond today, which has a maturity value of £1 at time T .

The market participant can invest in either instrument, both of which we know beforehand to be risk-free, and both of which have identical payouts at time T and have no cash flow between now and time T . As interest rates are constant, a bond that paid out £1 at T must have the same value as the initial investment in the money market account, which is e t r T t . Therefore equation (2.13b) must apply. This is a restriction placed on the zerocoupon bond price by the requirement for markets to be arbitrage-free.

If the bond was not priced at this level, arbitrage opportunities would present  themselves.  Consider  if  the  bond  was  priced  higher  than e t r T t . In this case, an investor could sell short the bond and invest the sale proceeds in the money market account. On maturity at time T , the short position will have a value of £1 (negative, because the investor is short the bond), while the money market will have accumulated £1, which the investor can use to pay the proceeds on the zero-coupon bond. However, the investor will have surplus funds because at time t :

5   This expression uses the integral operator. The integral is the tool used in mathematics to calculate sums of an infinite number of objects, that is where the objects are uncountable. This is different to the operator which is used for a countable number of objects. For a readable and accessible review of the integral and its use in quantitative finance, see Neftci (2000), pp. 59-66, a summary of which is shown at Appendix 3.2.

<!-- formula-not-decoded -->

and so will have profited from the transaction at no risk to himself.

The same applies if the bond is priced below e t r T t .  In  this  case,  the investor borrows e t r T t and buys the bond at its price P t T , . On maturity, the bond pays £1, which is used to repay the loan amount, however, the investor will gain because:

<!-- formula-not-decoded -->

Therefore the only price at which no arbitrage profit can be made is if:

<!-- formula-not-decoded -->

In academic literature, the price of a zero-coupon bond is given in terms of the evolution of the short-term interest rate, in what is termed the riskneutral measure . 6  The short rate r t is the interest rate earned on a money market account or short-dated risk-free security such as the T-bill suggested above, and it is assumed to be continuously compounded. This makes the mathematical  treatment  simpler. With  a  zero-coupon  bond  we  assume  a payment on maturity of 1 (say $1 or £1), a one-off cash flow payable on maturity at time T . The value of the zero-coupon bond at time t is therefore given by:

<!-- formula-not-decoded -->

which is the redemption value of 1 divided by the value of the money market account, given by (2.13a).

The bond price for a coupon bond is given in terms of its yield as:

<!-- formula-not-decoded -->

Expression (2.14) is very commonly encountered in academic literature. Its derivation is not so frequently occurring, however, and we present it in Appendix 2.3, which is a summary of the description given in Ross (1999). This reference is highly recommended reading. It is also worth referring to Neftci (2000), Chapter 18.

6 This is part of the arbitrage pricing theory . For detail on this see Cox et al . (1985), while Duffie (1992) is a fuller treatment.

The expression (2.14) represents the zero-coupon bond pricing formula when the spot rate is continuous or stochastic , rather than constant. The rate r s is the risk-free return earned during the very short or infinitesimal time interval t t dt , .  The rate is used in the expressions for the value of a money market account (2.13) and the price of a risk-free zero-coupon bond (2.15).

## Stochastic Rates in Continuous Time

In the academic literature, the bond price given by (2.15) evolves as a martingale process  under  the  risk-neutral  probability  measure P ˜ .  This  is  an advanced branch of fixed income mathematics, and is outside the scope of this book, however, it is discussed in an introductory fashion in Chapter 5. 7

For the purposes of this analysis, the bond price is given as:

<!-- formula-not-decoded -->

where the right-hand side of (2.16) is viewed as the randomly evolved discount factor used to obtain the present value of the £1 maturity amount. Expression (2.16) also states that bond prices are dependent on the entire spectrum of short-term interest rates r s in  the  future  during the period t s T . This also implies that the term structure at time t contains all the information available on short rates in the future. 8

From (2.16), we say that the function T P t T t T , ,  is  the  discount curve (or discount function ) at time t . Avellaneda (2000) notes that the markets usually replace the term T t -with a term meaning time to maturity , so the function becomes:

<!-- formula-not-decoded -->

Under a constant spot rate, the zero-coupon bond price is given by:

<!-- formula-not-decoded -->

7   Interested readers should consult Nefcti (2000), Chapters 2, 17-18, another accessible text is Baxter and Rennie (1996), while Duffie (1992) is a leading-edge reference for those with a strong background in mathematics.

8   This is related to the view of the short rate evolving as a martingale process. For a derivation of (2.16) see Neftci (2000), p. 417.

From (2.16) and (2.17) we can derive a relationship between the yield r t T , of the zero-coupon bond and the short rate r t , if we equate the two right-hand sides, namely:

<!-- formula-not-decoded -->

Taking the logarithm of both sides we obtain:

<!-- formula-not-decoded -->

This describes the yield on a bond as the average of the spot rates that apply during the life of the bond, and under a constant spot rate the yield is equal to the spot rate.

With a zero-coupon bond and assuming that interest rates are positive, P t T , is less than or equal to 1. The yield of the bond is, as we have noted, the continuously compounded interest rate that equates the bond price to the discounted present value of the bond at time t . This is given by:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In practice, this means that an investor will earn r t T , if they purchase the bond at t and hold it to maturity.

## Coupon Bonds

Using the same principles as in the previous section, we can derive an expression for the price of a coupon bond in the same terms of a risk-neutral probability measure of the evolution of interest rates. Under this analysis, the bond price is given by:

<!-- formula-not-decoded -->

so we obtain:

where:

P c is the price of a coupon bond

C is the bond coupon

t n is the coupon date, with n N /lessthanorequalangled , and t 0 at the time of valuation

w is the coupon frequency 9

and where 100 is used as the convention for principal or  bond  nominal value (that is, prices are quoted per cent, or per 100 nominal).

Expression (2.22) is written in some texts as:

<!-- formula-not-decoded -->

We can simplify (2.22) by substituting df to denote the discount factor part of the expression and assuming an annual coupon, which gives us:

<!-- formula-not-decoded -->

which states that the market value of a risk-free bond on any date is determined by the discount function on that date.

We know from Chapter 2 that the actual price paid in the market for a bond includes accrued interest from the last coupon date, so that price given by (2.24) is known as the clean price and the traded price, which includes accrued interest, is known as the dirty price .

## Forward Rates

An  investor  can  combine  positions  in  bonds  of  differing  maturities  to guarantee a rate of return that begins at a point in the future. That is, the trade ticket is written at time t but covers the period T to T 1 where t T (sometimes written as beginning at T 1 and ending at T 2 , with t T T 1 2 ). The interest rate earned during this period is known as the forward rate . 10 The mechanism by which this forward rate can be guaranteed is described in Example 2.1 below, following Jarrow (1996) and Campbell et al . (1997).

9   Conventional  or plain  vanilla  bonds pay  coupon  on  an  annual  or  semi-annual basis.  Other  bonds,  notably  certain  floating-rate  notes  and  mortgage-  and  other asset-backed securities also pay coupon on a monthly basis, depending on the structuring of the transaction.

10   See the footnote on page 639 of Shiller (1990) for a fascinating insight into the origin of the term 'forward rate', which Mr Shiller ascribes to John Hicks in his book Value and Capital , 2nd edition, Oxford University Press (1946).

## EXAMPLE 2.1 THE FORWARD RATE

An investor buys at time t 1 unit of a zero-coupon bond maturing at time T , priced at P t T , and simultaneously sells P t T P t T , / , 1 bonds that mature at T 1. From Table 2.1, we can see that the net result of these transactions is a zero cash flow. At time T there is a cash inflow of 1, and then at time T 1  there  is  a  cash  outflow  of P t T P t T , / , 1 . These cash flows are identical to a loan of funds made during the period T to T 1, contracted at time t . The interest rate on this loan is given by P t T P t T , / , 1 , which is therefore the forward rate. That is:

<!-- formula-not-decoded -->

Together with our earlier relationships on bond price and yield, from (2.25), we can define the forward rate in terms of yield, with the return earned during the period T T , 1 being:

<!-- formula-not-decoded -->

TABLE 2.1 Confirming the forward rate arbitrage

|                                                                        | Time                                               | Time                          |
|------------------------------------------------------------------------|----------------------------------------------------|-------------------------------|
| Transactions                                                           | t                                                  | T T 1                         |
| Buy 1 unit of T -period bond Sell P t T P t T T , / , 1 1 period bonds | P t T , [( P ( t , T )/ P ( t , T 1)] P ( t , T 1) | 1 ( P ( t , T )/ P ( t , T 1) |
| Net cash flows                                                         | 0                                                  | 1 ( P ( t , T )/ P ( t , T 1) |

From (2.25), we can obtain a bond price equation in terms of the forward rates that hold from t to T :

<!-- formula-not-decoded -->

( Continued )

A derivation of this expression can be found in Jarrow (1996), Chapter 3. Equation (2.27) states that the price of a zero-coupon bond is equal to the nominal value, here assumed to be 1, receivable at time T after it has been discounted at the set of forward rates that apply from t to T . 11

When calculating a forward rate, it is as if we are transacting at an interest rate today that is applicable at the forward start date, in other words we are trading a forward contract. The law of one price, or no-arbitrage, is used to calculate the rate. For a loan that begins at T and matures at T 1, similarly to the way we described in Example 2.1, consider a purchase of a T 1 period bond and a sale of p amount of the T -period bond. The net cash position at t must be zero, so p is given by:

<!-- formula-not-decoded -->

and to avoid arbitrage, the value of p must be the price of the T 1-period bond at time T . Therefore the forward yield is given by:

<!-- formula-not-decoded -->

If  the  period  between T and  the  maturity  of  the  later-dated  bond  is reduced, we now have bonds that mature at T and T 2 , and T T t 2 . The incremental change in time t ∆ becomes progressively smaller until we obtain an instantaneous forward rate, which is given by:

<!-- formula-not-decoded -->

This rate is defined as the forward rate and is the price today of forward borrowing at time T .  The forward rate for borrowing today where T t is equal to the instantaneous short rate r t . At time t , the spot and forward rates for the period t t , will be identical, while at other maturity terms they will differ .

11   The symbol ∏ means 'take the product of', and is defined as i n i n x x x x 1 1 2 · ····· , so that ( ) ( ) ( ) ( ) 1 , , · , 1 ····· , 1 T k t f t k f t t f t t f t T n -= = + -∏ , which is the result of multiplying the rates that are obtained when the index k runs from t to T 1.

For all points other than at t t , the forward rate yield curve will lie above the spot rate curve if the spot curve is positively-sloping. The opposite applies if the spot rate curve is downward-sloping. Campbell et al . (1997, pp. 400-401) observe that this property is a standard one for marginal and average cost curves. That is, when the cost of a marginal unit (say, of production) is above that of an average unit, then the average cost will increase with the addition of a marginal unit. This results in the average cost rising when the marginal cost is above the average cost. Equally, the average cost per unit will decrease when the marginal cost lies below the average cost.

## EXAMPLE 2.2 THE SPOT AND FORWARD YIELD CURVES

From the discussion in this section, we can see that it is possible to calculate bond prices, spot, and forward rates provided that we have a set of only one of these parameters. Therefore, given the following set of zero-coupon rates observed in the market, given in Table 2.2, we calculate the corresponding forward rates and zero-coupon bond prices as shown. The initial term structure is upward-sloping. The two curves are illustrated in Figure 2.4(a) and (b).

TABLE 2.2 Hypothetical zero-coupon yield and forward rates

|   Term to maturity 0,T | Spot rate r 0,T *   | One year forward rate f 0,T *   |   Bond price P 0,T |
|------------------------|---------------------|---------------------------------|--------------------|
|                      0 |                     |                                 |                  1 |
|                      1 | 1.054               | 1.054                           |            0.94877 |
|                      2 | 1.055               | 1.056                           |            0.89845 |
|                      3 | 1.0563              | 1.059                           |             0.8484 |
|                      4 | 1.0582              | 1.064                           |            0.79737 |
|                      5 | 1.0602              | 1.068                           |             0.7466 |
|                      6 | 1.0628              | 1.076                           |            0.69386 |
|                      7 | 1.06553             | 1.082                           |            0.64128 |
|                      8 | 1.06856             | 1.0901                          |            0.58833 |
|                      9 | 1.07168             | 1.0972                          |            0.53631 |
|                     10 | 1.07526             | 1.1001                          |            0.48403 |
|                     11 | 1.07929             | 1.1205                          |            0.43198 |

( Continued )

There are technical reasons why the theoretical forward rate has a severe kink at the later maturity.

Essentially,  the  relationship  between  the  spot  and  forward  rate curve is as stated by Campbell et al . (1997). The forward rate curve lies above the spot rate curve if the latter is increasing, and it lies below it if the spot rate curve is decreasing. This relationship can be shown mathematically. The forward rate or marginal rate of return is equal to the spot rate or average rate of return plus the rate of increase of the spot rate, multiplied by the sum of the increases between t and T . If the spot rate is constant (a flat curve), the forward rate curve will be equal to it.

However, an increasing spot rate curve does not always result in  an  increasing  forward  curve,  only  one  that  lies  above  it.  It  is possible for the forward curve to be increasing or decreasing while the spot rate is increasing. If the spot rate reaches a maximum level and then stays constant, or falls below this high point, the forward curve  will  begin  to  decrease  at  a  maturity  point earlier than  the spot curve high point. In the example in Figure 2.4(a), the rate of increase in the spot rate in the last period is magnified when converted to the equivalent forward rate. If the last spot rate is below the  previous-period rate,  the  forward  rate  curve  would  look  like that in Figure 2.4(b).

FIGURE 2.4(a) Hypothetical zero-coupon and forward yield curves.

<!-- image -->

<!-- image -->

## Calculating Spot Rates in Practice

Researchers have applied econometric techniques to the problem of extracting  a  zero-coupon  term  structure  from  coupon  bond  prices.  Some  wellknown  approaches  are  described  in  McCulloch  (1971,  1975),  Schaefer (1981), Nelson and Siegel (1987), Deacon and Derry (1994), Adams and Van Deventer (1994), and Waggoner (1997), to name but a few. The most accessible article is probably the one by Deacon and Derry. 12  In addition, a good overview of all the main approaches is contained in James and Webber (2000), and Chapters 15-18 of their book provide an excellent summary of this area.

We have noted that a coupon bond may be regarded as a portfolio of zero-coupon bonds. By treating a set of coupon bonds as a larger set of zerocoupon bonds, we can extract an implied zero-coupon interest rate structure from the yields on the coupon bonds.

If the actual term structure is observable, so that we know the prices of zero-coupon bonds of £1 nominal value 1 2 , , , N P P P … then the price P C of a coupon bond of nominal value £1 and coupon C is given by:

<!-- formula-not-decoded -->

12   This is in the author's opinion. Those with a good grounding in econometrics will find all these references both readable and accessible. Further recommended references are given in the bibliography and selected readings at the end of the chapter.

Conversely, if we observe the coupon bond yield curve so that we know the  prices 1 2 , , , C C CN P P P … ,  then  we  may  use  (2.30)  to  extract  the  implied zero-coupon term structure. We begin with the one-period coupon bond, for which the price is:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This process is repeated. Once we have the set of zero-coupon bond prices P P P N 1 2 1 , , , we obtain P N using:

<!-- formula-not-decoded -->

At this point we apply a regression technique known as ordinary least squares (OLS)  to  fit  the  term  structure. The  next  chapter  discusses  this area  in  greater  detail.  We  have  segregated  this  so  that  readers  who  do not require an extensive familiarity with this subject may skip the next chapter. Interested readers should also consult the references at the end of Chapter 4.

Expression 2.30 restricts the prices of coupon bonds to be precise functions of the other coupon bond prices. In fact, this is unlikely in practice because specific bonds will be treated differently according to liquidity, tax effects, and so on. For this reason, we add an error term to (2.30) and estimate the value using cross-sectional regression against all the other bonds in the market. If we say that these bonds are numbered i I 1 2 , , , then the regression is given by:

<!-- formula-not-decoded -->

for i I 1 2 , , , and where Ci is the coupon on the i th bond and Ni is the maturity of the i th bond. In (2.33), the regressor parameters are the coupon payments at each interest  period  date,  and  the  coefficients  are  the prices of the zero-coupon bonds P 1 to P N where j N 1 2 , , , . The values are  obtained  using  OLS  as  long  as  we  have  a  complete  term  structure and that I N /greaterthanorequalangled .

In practice, we will not have a complete term structure of coupon bonds and  so  we  are  not  able  to  identify  the  coefficients  in  (2.33).  McCulloch (1971,  1975)  described  a spline  estimation method,  which  assumes  that

so that:

zero-  coupon  bond  prices  vary  smoothly  with  term  to  maturity.  In  this approach we define P N ,  a  function of maturity P N ,  as  a discount function given by:

<!-- formula-not-decoded -->

The function f N j is a known function of maturity N , and the coefficients a j must be estimated. We arrive at a regression equation by substituting (2.34) into (2.33) to give us (2.35), which can be estimated using OLS:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The function f N j is usually specified by setting the discount function as a polynomial. In certain texts including McCulloch, this is carried out by  applying  what  is  known  as  a spline function.  Considerable  academic research has gone into the use of spline functions as a yield curve fitting technique, however, we are not able to go into the required level of detail here, which is left to the next chapter. Please refer to the selected reading for further information. For a specific discussion on using regression techniques for spline curve fitting methods, see Suits et al . (1978).

FIGURE 2.5 Hypothetical par, spot, and forward yield curves.

<!-- image -->

where:

## INTRODUCTION TO BOND ANALYSIS USING SPOT RATES AND FORWARD RATES IN CONTINUOUS TIME

This  section  analyses  further  the  relationship  between  spot  and  forward rates and the yield curve, illustrated diagrammatically in Figure 2.5.

## The Spot and Forward Rate Relationship

In the discussion to date, we have assumed discrete time intervals and interest rates in discrete time. Here we consider the relationship between spot and forward rates in continuous time. For this we assume the mathematical convenience of a continuously compounded interest rate.

We start by saying that at the interest rate r , compounded using e r , an initial investment of M earning r t T , over the period T t , (initial investment at time t and for maturity at T , where T t ), would have a value of Me r t T T t , on maturity. 13  If we denote the initial value Mt and the maturity value MT then we can state Me M t r t T T t T , and therefore the continuously compounded yield, defined as the continuously compounded interest rate r t T , , can be shown to be:

<!-- formula-not-decoded -->

We can then formulate a relationship between the continuously compounded interest rate and yield. It can be shown that:

<!-- formula-not-decoded -->

where r s is the instantaneous spot interest rate and is a function of time. It can further be shown that the continuously compounded yield is actually the equivalent of the average value of the continuously compounded interest rate. In addition it can be shown that:

<!-- formula-not-decoded -->

In a continuous time environment we do not assume discrete time intervals over which interest rates are applicable, rather a period of time in which a  borrowing of funds would be repaid instantaneously. So we define the forward rate f t s , as the interest rate applicable for borrowing funds where the deal is struck at time t ; the actual loan is made at s (with s t ) and repayable almost instantaneously. In mathematics the period s t is described as infinitesimally small. The spot interest rate is defined as the continuously compounded yield or interest rate r t T , . In an environment of no arbitrage, the return generated by investing at the forward rate f t s , over the period s t must be equal to that generated by investing initially at the spot rate r t T , . So we may set:

13 e is the mathematical constant 2.7182818 . . . and it can be shown that an investment of £1 at time t will have grown to e on maturity at time T (during the period T t ) if it is earning an interest rate of 1/ T t continuously compounded.

<!-- formula-not-decoded -->

which enables us to derive an expression for the spot rate itself, which is:

<!-- formula-not-decoded -->

The relationship described by (2.40) states that the spot rate is given by the arithmetic average of the forward rates f t s , where t s T . How does this differ from the relationship in a discrete time environment? From Chapter 2 we know that the spot rate in such a framework is the geometric average of the forward rates, 14  and this is the key difference in introducing the continuous time structure. Equation (2.40) can be rearranged to:

<!-- formula-not-decoded -->

and this is used to show (by differentiation) the relationship between spot and forward rates, given below:

<!-- formula-not-decoded -->

If we assume we are dealing today (at time 0) for maturity at time T , then the expression for the spot rate becomes:

<!-- formula-not-decoded -->

14   To be precise, if we assume annual compounding, the relationship is one plus the spot rate is equal to the geometric average of one plus the forward rates.

so we can write:

<!-- formula-not-decoded -->

This is illustrated in Figure 2.6 which is a diagrammatic representation showing that the spot rate r T 0, is the average of the forward rates from 0 to T , using the hypothetical value of 5% for r T 0, . Figure 2.6 also shows the area represented by (2.44).

What (2.42) implies is that if the spot rate increases, then by definition the forward rate (or marginal rate as has been suggested that it may be called 15 )  will  be  greater.  From (2.42) we deduce that the forward rate will be equal to the spot rate plus a value that is the product of the rate of increase of the spot rate and the time period T t . In fact the conclusions simply confirm what we already discovered in the discrete time analysis in Chapter 2: the forward rate for any period will lie above the spot rate if the spot rate term structure is increasing, and will lie below the spot rate if it is decreasing. In a constant spot rate environment, the forward rate will be equal to the spot rate.

FIGURE 2.6 Diagrammatic representation of the relationship between the spot and forward rates.

<!-- image -->

15   For example, see Section 10.1 of Campbell, et al . (1997), Chapter 10 which is an excellent and accessible study of the term structure, and provides proofs of some of the results discussed here. This book is written in very readable style and is worth purchasing for Chapter 10 alone.

However, it is not as simple as that. An increasing spot rate term structure only implies that the forward rate lies above the spot rate, but not that the forward rate structure is itself also increasing . In fact one can observe the forward rate term structure to be increasing or decreasing while spot rates are increasing. As the spot rate is the average of the forward rates, it can be shown that in order to accommodate this, forward rates must in fact be decreasing before the point at which the spot rate reaches its highest point. This confirms market observation. An illustration of this property is given in Appendix 2.1. As Campbell et al . (1997) state, this is a property of average and marginal cost curves in economics.

## Bond Prices as a Function of Spot and Forward Rates 16

In  this  section,  we  describe  the  relationship  between  the  price  of  a  zerocoupon bond and spot and forward rates. We assume a risk-free zero-  coupon bond of nominal value £1, priced at time t and maturing at time T . We also assume a money market bank account of initial value P t T , invested at time t . The money market account is denoted M . The price of the bond at time t is denoted P t T , and if today is time 0 (so that t 0), then the bond price today is unknown and a random factor (similar to a future interest rate). The bond price can be related to the spot rate or forward rate that is in force at time t .

Consider the scenario below, used to derive the risk-free zero-coupon bond price. 17

The  continuously  compounded constant spot  rate  is r as  before.  An investor has a choice of purchasing the zero-coupon bond at price P t T , , which will return the sum of £1 at time T or of investing this same amount of cash in the money market account, and this sum would have grown to £1 at time T . We know that the value of the money market account is given by Me r tT T t .  If M must have a value of £1 at time T ,  then the function e r t T T t , must give the present value of £1 at time t and therefore the value of the zero-coupon bond is given by:

<!-- formula-not-decoded -->

If  the  same amount of cash that could be used to buy the bond at t , invested in the money market account, does not return £1 then arbitrage opportunities  will  result.  If  the  price  of  the  bond  exceeded  the  discount function e r t T T t , then  the  investor  could  short  the  bond  and  invest the proceeds in the money market account. At time T the  bond  position would  result  in  a  cash  outflow  of  £1,  while  the  money  market  account would be worth £1. However, the investor would gain because in the first place ( ) ( )( ) , , -0 r t T T t P t T e --&gt; .  Equally,  if  the  price  of  the  bond  was  below e r t T T t , then  the  investor  would  borrow e r t T T t , in  cash  and  buy  the bond at price P t T , . On maturity the bond would return £1, which proceeds would be used to repay the loan. However, the investor would gain because e P t T r t T T t , -, 0. To avoid arbitrage opportunities we must therefore have:

16   For more detail on this see Neftci (2000), Chapter 18, Section 3. This is also an excellent, readable text.

17   This approach is also used in Campbell et al . (q.v.).

<!-- formula-not-decoded -->

Following the relationship between spot and forward rates, it is also possible to describe the bond price in terms of forward rates. 18  We show the result here only. First we know that:

<!-- formula-not-decoded -->

because the maturity value of the bond is £1, and we can rearrange (2.47) to give:

<!-- formula-not-decoded -->

Expression (2.48) states that the bond price is a function of the range of forward rates that apply for all f t s , that is, the forward rates for all time periods s from t to T (where t s T , and where s is infinitesimally small). The forward rate f t s , that results for each s arises as a result of a random or stochastic process that is assumed to start today at time 0. Therefore the bond price P t T , also results from a random process, in this case all the random processes for all the forward rates f t s , .

The zero-coupon bond price may also be given in terms of the spot rate r t T , , as shown at (2.46). From our earlier analysis we know that:

<!-- formula-not-decoded -->

which is rearranged to give the zero-coupon bond price equation:

<!-- formula-not-decoded -->

as before.

18 For instance, see ibid , Section 4.2.

Equation (2.50) describes the bond price as a function of the spot rate only, as opposed to the multiple processes that apply for all the forward rates from t to T . As the bond has a nominal value of £1, the value given by (2.50) is the discount factor for that term; the range of zero-coupon bond prices would give us the discount function.

What is the importance of this result for our understanding of the term structure of interest rates? First, we see (again, but this time in continuous time) that spot rates, forward rates, and the discount function are all closely related, and given one we can calculate the remaining two. More significantly, we may model the term structure either as a function of the spot rate only, described as a stochastic process, or as a function of all of the forward rates f t s , for  each  period s in  the  period T t ,  described by multiple random processes. The first yield curve models adopted the first approach, while a later development described the second approach.

## APPENDICES

## Appendix 2.1 Illustration of forward rate structure when spot rate structure is increasing

We assume the spot rate r T 0, is a function of time and is increasing to a high point at T . It is given by:

<!-- formula-not-decoded -->

At its high point the function is neither increasing nor decreasing, so we may write:

<!-- formula-not-decoded -->

and therefore the second derivative with respect to T will be:

<!-- formula-not-decoded -->

From (2.42) and (2.52) we may state:

<!-- formula-not-decoded -->

and from (2.53) and (2.54) the second derivative of the spot rate is:

<!-- formula-not-decoded -->

From (2.52) we know the spot rate function is zero at T so the derivative of the forward rate with respect to T would therefore be:

<!-- formula-not-decoded -->

So in this case the forward rate is decreasing at the point T when the spot rate is at its maximum value. This is illustrated hypothetically at Figure 2.6 and it is common to observe the forward rate curve decreasing as the spot rate is increasing.

## Appendix 2.2 The Integral

The approach used to define integrals begins with an approximation involving  a  countable  number  of  objects,  which  is  then  gradually  transformed into an uncountable number of objects. A common form of integral is the Riemann integral.

Given a calculable or deterministic function that has been graphed for a period of time, let us say we require the area represented by this graph. The function is f t and it is graphed over the period  0, T . The area of the graph is given by the integral:

<!-- formula-not-decoded -->

which is the area represented by the graph. This can be calculated using the Riemann integral, for which the area represented is shown at Figure 2.7.

To  make  the  calculation,  the  time  interval  is  separated  into n intervals, given by:

<!-- formula-not-decoded -->

The approximate area under the graph is given by the sum of the area of each of the rectangles, for which we assume each segment outside the graph is compensated by the area under the line that is not captured by any of the rectangles. Therefore we can say that an approximating measure is described by:

FIGURE 2.7 Diagrammatic representation of calculating area from applying integration.

<!-- image -->

<!-- formula-not-decoded -->

This states that the area under the graph can be approximated by taking the sum of the n rectangles, which are created from the base x -axis which begins from t 0 through to T and the y -axis as height, described as:

<!-- formula-not-decoded -->

This  approximation only works if a sufficiently  small  base  has  been used for each interval, and if the function f t is a smooth function, that is it does not experience sudden swings or kinks.

The definition of the Riemann integral is, given that:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

If  the  approximation is not sufficiently accurate, we can adjust it by making the intervals smaller still, which will make the approximation closer. This approach cannot be used if the function is not smooth. In mathematics, this requirement is stated by saying that the function must be integrable or Riemann integrable.

Other integral forms are also used, and a good introduction to these is given in Neftci (2000), Chapter 4.

defined by the limit:

## Appendix 2.3 The derivation of the bond price equation in continuous time

This section summarises the approach described in Ross (1999, pp. 54-56). This is an excellent reference, very readable, and accessible, and is highly recommended. We replace Ross's use of investment at time 0 for maturity at time t with the terms t and T respectively, which is consistent with the price equations given in the main text. We also use the symbol M for the maturity value of the money market account, again to maintain consistency with the expressions used in Chapters 1-3 of this book.

Assume a continuously compounded interest rate r s that is payable on a money market account at time s . This is the instantaneous interest rate at time s . Assume further that an investor places x in this account at time s ; after a very short time period of time h , the account would contain:

<!-- formula-not-decoded -->

Assume that M T is the amount that will be in the account at time T if an investor deposits £1 at time t . To calculate M T in terms of the spot rate r s , where t s T /lessthanorequalangled /lessthanorequalangled , for an incremental change in time of h , we have:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The approximation given by (2.62) turns into an equality as the time represented  by h becomes  progressively  smaller.  At  the  limit  given  as h approaches zero, we say:

<!-- formula-not-decoded -->

which can be re-arranged to give:

<!-- formula-not-decoded -->

which leads us to:

and:

From expression (2.65), we imply that in a continuous time process:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

However, we deposited £1 at time t , that is M t 1, so from (2.67), we obtain the value of the money market account at T to be:

<!-- formula-not-decoded -->

which was our basic equation shown as (2.13).

Let us now introduce a risk-free zero-coupon bond that has a maturity value of £1 when it is redeemed at time T . If the spot rate is constant, then the price at time t of this bond is given by:

<!-- formula-not-decoded -->

where r is  the  continuously compounded instantaneous interest rate. The right-hand side of (2.69) is the expression for the present value of £1, payable at time T , discounted at time t at the continuously compounded, constant interest rate r .

So we say that P t T , is the present value at time t of £1 to be received at time T . Since a deposit of  1/ M T at time t will have a value of 1 at time T , we are able to say that:

<!-- formula-not-decoded -->

If we say that the average of the spot interest rates from t to T is denoted by rf T ,  so  we  have rf T T r s ds t T 1 ,  then  the  function rf T is  the term structure of interest rates.

and that:

## SELECTED BIBLIOGRAPHY AND REFERENCES

- Adams, K. and Van Deventer, D., 'Fitting Yield Curves and Forward Rate Curves with Maximum Smoothness', Journal of Fixed Income 4, 1994, pp. 52-62.
- Avellaneda, M. and Laurence, P., Quantitative Modelling of Derivative Securities , Chapman &amp; Hall/CRC, 2000, Chapters 10-12.
- Baxter, M. and Rennie, A., Financial Calculus , Cambridge University Press, 1996, Chapter 5.
- Brennan, M. and Schwartz, E., 'A continuous time approach to the pricing of bonds', Journal of Banking and Finance 3, 1979, pp. 134 ff.
- Brennan, M. and Schwartz, E., 'Conditional predictions of bond prices and returns', Journal of Finance 35, 1980, pp. 405 ff.
- Campbell, J., Lo, A. and MacKinlay, A., The Econometrics of Financial Markets , Princeton University Press, 1997, Chapters 10-11.
- Choudhry, M., Bond Market Securities , FT Prentice Hall, 2001.
- Cox, J., Ingersoll, J. and Ross, S., 'An Inter-Temporal General Equilibrium Model of Asset Prices', Econometrica 53, 1985.
- Deacon, M. and Derry, A., 'Estimating the Term Structure of Interest Rates', Bank of England Working Paper Series No. 24, July 1994.
- Duffie, D., Dynamic Asset Pricing Theory , Princeton University Press, 1992.
- Fisher, L. and Leibowitz, M., 'Effects of alternative anticipations of yield curve behaviour on the composition of immunised portfolios and on their target returns', in Kaufmann, G, et al. (ed.), Innovations in Bond Portfolio Management , Jai Press, 1983.
- Guajarati, D., Basic Econometrics , 3rd edition, McGraw-Hill, 1999.
- Hicks, J., Value and Capital , 2nd edition, Oxford University Press, 1946.
- Ingersoll, J. Jr., Theory of Financial Decision Making , Rowman &amp; Littlefied, 1987, Chapter 18.
- James, J. and Webber, N., Interest Rate Modelling , Wiley, 2000.
- Jarrow, R., Modelling Fixed Income Securities and Interest Rate Options , McGraw-Hill, 1996, Chapter 3.
- Kitter, G., Investment Mathematics for Finance and Treasury Professionals , Wiley, 1999, Chapters 3, 5.
- McCulloch, J., 'Measuring the Term Structure of Interest Rates', Journal of Business 44, 1971, pp. 19-31.
- McCulloch, J., 'The Tax-Adjusted Yield Curve', Journal of Finance 30, 1975, pp. 811-830.
- Neftci, S., An Introduction to the Mathematics of Financial Derivatives , 2nd edition, Academic Press, 2000, Chapter 18.
- Nelson, C. and Siegel, A., 'Parsimonious Modelling of Yield Curves', Journal of Business 60(4), 1987, pp. 473-489.
- Ross, Sheldon M., An Introduction to Mathematical Finance , Cambridge University Press, 1999.
- Schaefer, S., 'Measuring a Tax-Specific Term Structure of Interest Rates in the Market for British Government Securities', Economic Journal 91, 1981, pp. 415-438.

- Shiller, R., 'The Term Structure of Interest Rates', in Friedman, B., Hanh, F., (ed.), Handbook of Monetary Economics , Volume 1, North Holland, 1990, Chapter 13.
- Suits, D., Mason, A. and Chan, L., 'Spline Functions Fitted by Standard Regression Methods', Review of Economics and Statistics 60, 1978, pp.132-139.
- Sundaresan, S., Fixed Income Markets and Their Derivatives , South-Western, 1997. The Economist, 'Out of Debt', The Economist , 12 February 2000.
- Van Deventer, D. and Imai, K., Financial Risk Analytics , Irwin 1997.
- Van Home, J., Financial Management and Policy, 10th edition, Prentice Hall, 1995. Waggoner, D., 'Spline Methods for Extracting Interest Rate Curves from Coupon Bond Prices', Working Paper, Federal Reserve Bank of Atlanta , 1997, pp. 97-10.
- In addition, interested readers may wish to consult the following recommended references on term structure analysis:
- Constantinides, G., 'A Theory of the Nominal Term Structure of Interest Rates', The Review of Financial Studies 5(4), 1992, pp. 531-552.
- Cox, J., Ingersoll, J. and Ross, S., 'A Re-examination of Traditional Hypotheses about the Term Structure of Interest Rates', Journal of Finance 36, 1981, pp. 769-799.
- Cox, J., Ingersoll, J. and Ross, S., 'A Theory of the Term Structure of Interest Rates', Econometrica 53, 1985, pp. 385-407.
- Culbertson, J., 'The Term Structure of Interest Rates', Quarterly Journal of Economics LXXI, 1957, pp. 489-504.
- McCulloch, J.H., 'A Reexamination of Traditional Hypotheses about the Term Structure: A Comment', Journal of Finance 63 (2), 1993, pp.779-789.
- Stambaugh, R., 'The Information in Forward Rates: Implications for Models of the Term Structure', Journal of Financial Economics 21, 1988, pp. 41-70.
- Shiller, R., Campbell, J. and Schoenholtz, K., 'Forward Rates and Future Policy: Interpreting the Term Structure of Interest Rates', Brookings Papers on Economic Activity 1, 1983, pp. 173-223.

He was possibly not a natural . . . but by absolute dedication to his craft, he made himself a master.

-- Max Hastings, writing about Leonard Cheshire VC (1917-1992), Bomber Command , Michael Joseph Limited, 1979

PA R T

II

## Yield Curve Modelling and Post-2008 Yield Curve Analytics

I n Part II we discuss yield curve modelling, illustrated with a number of yield  curve  models. The  emphasis  is  on  a  qualitative  discussion  for  all users, not just quantitative analysts, but as we are discussing a quantitative subject some mathematical notation is necessary. We introduce these in a sort of 'maths primer' in Chapters 3 and 4. Readers familiar with these concepts may move directly to Chapter 5 for the start of the discussion.

Next in Part II, we look at how the change in market conditions following the bank crash in 2008 has impacted yield curve analysis. There is a description of the factors associated with swap curve discounting, and the use of the overnight-index swap (OIS) curve in money markets, as well as a discussion of negative interest rates. We have retained the chapter on the index-linked or real yield curve that was presented in the first edition.

[Gene] Kranz is a leader. He is a man who gives others the feeling that they are about to go through the door together into the stadium where they are each going to play the best game of their life.

-- Norman Mailer, A Fire on the Moon , Boston: Little, Brown &amp; Company, 1970

## CHAPTER  3

## Interest Rate Modelling I: Primer on Basic Concepts

F ollowing the introduction in Part I we are now in a position to move to fundamental questions of the yield curve, the processes that determine the evolution of the interest rate term structure, and how these processes can be modelled. The chapters in Part II review a number of interest rate models and the assumptions underlying these models. We also look at the procedure involved in estimating and fitting the yield curve. This topic is one of the most heavily researched subjects in financial market economics, and indeed research is ongoing. There are a number of ways to estimate and fit the yield curve, and there is no one right or wrong method. It is all a matter of finding the approach of best fit (pun intended!).

It is important when discussing this subject to remember to place the relevant ideas in context, otherwise there is a danger of becoming too theoretical. The aim is to confine the discussion within the boundary of user application, as there is a great deal of published material that is, quite simply,  rather  too  academic. We  must  always  try  to  keep  in  touch  with  the markets themselves. These chapters are written from the point of view of the market practitioner. We emphasise that this is a book about the bond markets, rather than a mathematics textbook. There are very few derivations, and fewer (if any) proofs. (This material is covered abundantly in existing literature.)

In the following chapters, we summarise a number of interest rate models, in a practical way, that does exclude most of the mathematics. The aim is to discuss application of the models. In this way, readers should be able to assess the different methodologies for themselves and decide the efficacies of each for their own purposes. As always, selected recommended texts plus chapter references are listed at the end.

<!-- image -->

## THE DYNAMICS OF THE YIELD CURVE

In Chapter 2 we introduced the concept of the yield curve, and reviewed some preliminary issues concerning both the shape of the curve and to what extent the curve could be used to infer the shape and level of the yield curve in the future. We do not know what interest rates will be in the future, but given a set of zero-coupon (spot) rates today, we can estimate the future level of forward rates using a yield curve model. In many cases, however, we do not have a zero-coupon curve to begin with, so it then becomes necessary to derive the spot yield curve from the yields of coupon bonds, which one can observe readily in the market. If a market only trades short-dated debt instruments, it is possible to construct a short-dated spot curve.

It is important for a zero-coupon yield curve to be constructed as accurately as possible. This is because the curve is used in the valuation of a wide range  of  instruments,  not  only  conventional  cash  market  coupon  bonds, which we can value using the appropriate spot rate for each cash flow, but other interest rate products such as swaps.

If using a spot rate curve for valuation purposes, banks use what are known  as arbitrage-free yield  curve  models,  where  the  derived  curve  is matched to the current spot yield curve. The concept of arbitrage-free, also known as no-arbitrage pricing or 'the law of one price', is that if one is valuing the same product or cash flow in two different ways, the same result will be obtained from either method. Therefore, if we are valuing a two-year bond that is put-able by the holder at par in one year's time, it can be analysed as a one-year bond that entitles the holder to reinvest it for another year. The rule of no-arbitrage pricing states that an identical price will be obtained whichever way one chooses to analyse the bond. When matching derived yield curves, therefore, correctly matched curves generate the same price when valuing a bond, whether a derived spot curve is used or the current term structure of spot rates is used.

Many derivatives pricing models, starting with Black-Scholes, assume that asset price returns follow a lognormal distribution. The dynamics of interest rates and the term structure is the subject of some debate, and the main differences between the main interest rate models is in the way that they capture the change in rates over a time period. However, although volatility  of  the  yield  curve is the main area of difference, certain models are easier to implement than others, and this is a key factor that a bank should consider when deciding which model to use. The process of calibrating the model, that is, setting it up to estimate the spot and forward term structure using current interest rates that are input to the model, is almost as important as deriving the model itself. So the availability of data for a range of products, including cash money markets, cash bonds, futures, and swaps, is vital to the successful implementation of the model.

As we may expect, the yields on bonds are correlated, in most cases very closely positively correlated. This enables us to analyse interest rate risk in a portfolio, for example, but also to model the term structure in a systematic way. Much of the traditional approach to bond portfolio management assumes a parallel shift in the yield curve, so that if the five-year bond yield moves upwards by 10 basis points, then the 30-year bond yield also moves up by 10 basis points. This underpins traditional duration and modified duration analysis, and the concept of immunisation. To analyse bonds in this way, we assume, therefore, that bond yield volatilities are identical and correlations are perfectly positive. Although both types of analysis are still common, it is clear that bond yields do not move in this fashion, and so we must enhance our approach in order to perform more accurate analysis.

## TERM STRUCTURE MODELLING

Term structure modelling is based on theory describing the behaviour of interest  rates.  A  model  seeks  to  identify  the  elements  or factors that  are believed to explain the dynamics of interest rates. These factors are random or stochastic in nature, so that we cannot predict with certainty the future level of any particular factor. 1  An interest rate model must therefore specify a statistical process that describes the stochastic property of these factors, in order to arrive at a reasonably accurate representation of the behaviour of interest rates.

The first term structure models analysed in academic literature, describe the interest rate process as one where the short rate 2 follows a statistical process and where all other interest rates are a function of the short rate. So the dynamics of the short rate drive all other term interest rates. These models are known as one-factor models . A one-factor model assumes that all term rates follow on from when the short rate is specified, that is they are not randomly determined. Two-factor interest rate models are also in use. For instance, the model described by Brennan and Schwartz (1979) specified the factors as the short-term rate and a long-term rate, while a model described by Fong and Vasicek (1991) specified the factors as the short rate and short rate volatility.

1   The word stochastic is derived from a term in ancient Greek, the word stokhos which means 'a bull's eye'. The connection? Throwing darts at a board and aiming for the bull's eye is a stochastic process, as it will contain a number of misses.

2   We came across this expression in the previous chapter.

## BASIC CONCEPTS

The original class of interest rate models describes the dynamics of the short rate, and the later class of models known as 'HJM' models describes the dynamics of the forward rate, and we will introduce these later. The foundation of interest rate models is grounded in probability theory, so readers may wish to familiarise themselves with this subject. An excellent introduction to this is given in Ross (1999), while a more detailed treatment is given in the same author's better known book, Probability Models (2000).

In a one-factor model of interest rates, the short rate is assumed to be a random or stochastic variable, with the dynamics of its behaviour being uncertain and acting in an unpredictable manner. A random variable such as the short rate is defined as a variable which has a future outcome that can assume more than one possible value. Random variables are either discrete or continuous . A discrete variable moves in identifiable breaks or jumps. So for example, while time is continuous, the trading hours of an exchange-traded future are not continuous, as the exchange is shut outside business hours. Interest rates are treated in academic literature as being continuous, whereas in fact rates such as central bank base rates move in discrete  steps. A  continuous  variable  moves  in  a  manner  that has no breaks or jumps. Therefore, if an interest rate moves in a range from 5% to 10%, if it is continuous it can assume any value within this range, for instance, a value of 5.671291%. Although this does not reflect market reality, assuming that interest rates and the processes they follow are continuous, this allows us to use calculus to derive useful results in our analysis.

The short rate is said to follow a stochastic process, so although the rate itself cannot be predicted with certainty, as it can assume a range of possible values in the future, the process by which it changes from value to value can be assumed, and hence modelled. The dynamics of the short rate therefore are a stochastic process or probability distribution . A one-factor model of the interest rate actually specifies the stochastic process that describes the movement of the short rate.

The analysis of stochastic processes employs mathematical techniques originally used in physics. An instantaneous change in value of a random variable x is written as dx . The changes in the random variable are assumed to be normally distributed. The 'shock' to this random variable that generates it to change value, also referred to as noise , follows a randomly generated process known as a Wiener process or geometric Brownian motion. This is described in Appendix 3.1. A variable following a Wiener process is a random variable, termed x or z , where the value alters instantaneously, but where the patterns of change follow a normal distribution with mean 0 and standard deviation 1. If we assume that the yield r of a zero-coupon bond follows a continuous Wiener process with mean 0 and standard deviation 1, this would be written as:

<!-- formula-not-decoded -->

Changes or 'jumps' in the yield that follow a Wiener process are scaled by the volatility of the stochastic process that drives interest rates, which is given  by .  Therefore  the  stochastic  process  for  the  change  in  yields is given by:

<!-- formula-not-decoded -->

The value of this volatility parameter is user-specified, that is, it is set at a value that the user feels most accurately describes the current interest rate environment. Users often use the volatility implied by the market price of interest rate derivatives, such as caps and floors.

So far we've said that the zero-coupon bond yield is a stochastic process following a geometric Brownian motion that drifts with no discernible trend. However, under this scenario, over time the yield continuously rises to a level of infinity or falls to infinity, which is not an accurate representation of reality. We need to add to the model a term that describes the observed trend of interest rates moving up and down in a cycle. This expected direction of the change in the short rate is the second parameter in an interest rate model, which in some texts is referred to by a letter such as a or b and in other texts is referred to as µ .

The short rate process can therefore be described in the functional form given by (3.1):

<!-- formula-not-decoded -->

where:

dr is the change in the short rate;

a is the expected direction of change of the short rate or drift ;

dt is the incremental change in time;

is the standard deviation of changes in the short rate;

dz is the random process.

Equation  (3.1)  is  sometimes  seen  with dW or dx in  place  of dz .  It assumes that, on average, the instantaneous change in interest rates is given by the function adt , with random shocks specified by dz . It is similar to a number of models, such as those first described by Vasicek (1977), Ho and Lee (1986), Hull and White (1991), and others.

To reiterate, (3.1) states that the change in the short rate r over an infinitesimal period of time dt , termed dr , is a function of:

- ◾ the drift rate or expected direction of change in the short rate a ;
- ◾ a random process dz .

The two significant properties of the geometric Brownian motion are:

- ◾ the drift rate is equal to the expected value of the change in the short rate. Under a zero drift rate, the expected value of the change is also zero  and  the  expected  value  of  the  short  rate  is  given  by  its  current value;
- ◾ the variance of the change in the short rate over a period of time T is equal to T , while its standard deviation is given by T .

The  model  given  by  (3.1)  describes  a  stochastic  short  rate  process, modified with a drift rate to influence the direction of change. However, a more realistic specification would also build in a term that describes the long-term behaviour of interest rates to drift back to a long-term level. This process is known as mean reversion , and is perhaps best known by the HullWhite model. A general specification of mean reversion is a modification given by (3.2):

<!-- formula-not-decoded -->

where:

b is the long-term mean level of interest rates; and where a now describes the speed of mean reversion. Equation (3.2) is known as an Ornstein-Uhlenbeck process. When r is greater than b , it will be pulled back towards b ,  although random shocks generated by dz will delay this process. When r is below b , the short rate will be pulled up towards b .

A brief introduction to Brownian motion is given at Appendix 3.2.

## ITÔ'S LEMMA

Having specified a term structure model, it becomes necessary for market practitioners to determine how security prices related to interest rates fluctuate. The main occurrence of this is where we wish to determine how the price P of a bond moves over time as the short rate r varies. The formula used for this is known as Itô's lemma. For the background on the application  of  Itô's  lemma,  see  Hull  (1997),  or  Baxter  and  Rennie  (1996).  Itô's lemma transforms the dynamics of the bond price P in terms of a stochastic process in the following form:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The subscripts indicate partial derivatives. 3  The terms dr and dr 2 are dependent on the stochastic process that is selected for the short rate r . If this process is the Ornstein-Uhlenbeck process that was described in (3.2), then the dynamics of P can be specified as (3.4).

<!-- formula-not-decoded -->

What we have done is transform the dynamics of the bond price in terms of the drift and volatility of the short rate. Equation (3.4) states that the bond price depends on the drift of the short rate, and the volatility.

Itô's lemma is used as part of the process of building a term structure model. The generic process this follows involves the following:

- ◾ specifying the random or stochastic process followed by the short rate, for which we must make certain assumptions about the short rate itself;
- ◾ use Itô's  lemma to transform the dynamics of the zero-coupon bond price in terms of the short rate;
- ◾ impose the no-arbitrage  condition,  which  is  the  principle  of  hedging a position in one bond with one in another bond of a different maturity (for a one-factor model), in order to derive the partial differential equation of the zero-coupon bond price. We note this for a one-factor model and for a two-factor model we require two bonds as hedging instruments;
- ◾ solve the partial differential equation for the bond price, which is subject to the condition that the price of a zero-coupon bond on maturity is 1.

We consider now some of the models that are used in this process.

3   This is the great value of Itô's lemma, a mechanism by which we can transform a partial differential equation.

## APPROACHES TO MODELLING

The area of interest rate dynamics and yield curve modelling is one of the most heavily researched in financial economics. There are a number of models available in the market today, and generally it is possible to categorise them as following certain methodologies. By categorising them in this way, participants in the market can assess them for their suitability, as well as draw their own conclusions about how realistic they might be. Let us consider the main categories.

The process begins with the fair valuation of a set of cash flows. If we are  analysing  a  financial  instrument  comprised  of  a  cash  flow  stream  of nominal amount Ci , paid at times i N 1 2 , , , , then the value of this instrument is given by:

<!-- formula-not-decoded -->

where P t i 0, is the price today of a zero-coupon bond of nominal value 1 maturing at each point i , or the i -period discount factor. This expression can be written as:

<!-- formula-not-decoded -->

which indicates that in a no-arbitrage environment, the present value of the cash flow stream is obtained by discounting the set of cash flows and summing them. Therefore, in theory, it is straightforward to calculate the present value of any cash flow stream (and by implication virtually any financial instrument), using the yields observed on a set of risk-free and default-free zero-coupon bonds. In practice though, the set of such zero-coupon bonds is limited and is influenced by liquidity and other market considerations. We therefore require a technique that enables us to use conventional coupon bonds and extract a set of zero-coupon discount factors from these.

## ONE-FACTOR, TWO-FACTOR AND MULTI-FACTOR MODELS

The key assumption that is made by an interest rate model is whether it is one-factor, that is, the dynamics of the yield change process is based on one factor, or multi-factor. From observation, we know that in reality there are a number of factors that influence the price change process, and that if we are using a model to say, value an option product, the valuation of that product is dependent on more than one underlying factor. For example, the payoff on a bond option is related to the underlying bond's cash flows as well as to the reinvestment rate that is applied to each cash flow. Valuing an option, therefore, is a multi-factor issue. In many cases, however, there is a close degree of correlation between the different factors involved. If we are modelling the term structure, we can calculate the correlation between the different maturity spot rates by using a covariance matrix of changes in each of the spot rates, and thus obtain a common factor that impacts all spot rates in the same direction. This factor can then be used to model the entire term structure in a one-factor model, and although two-factor and multi-factor models are also in use, the one-factor model is still common. In principle, it is relatively straightforward to move from a one-factor to a multi-factor model, but implementing and calibrating a multi-factor model is a more involved process. This is because the model requires the estimation of more volatility and correlation parameters, which slows down the process.

Readers will encounter the term Gaussian in reference to certain interest rate models. Put simply, a Gaussian process describes one that follows a normal distribution under a probability density function. The distribution of rates in this way for Gaussian models implies that interest rates can attain negative values under positive probability, which makes the models undesirable for some market practitioners. Nevertheless, such models are popular because they are relatively straightforward to implement and because the probability of the model generating negative rates is low and occurs only under certain extreme circumstances.

## THE SHORT-TERM RATE AND THE YIELD CURVE

The application of risk-neutral valuation requires that we know the sequence of short-term rates for each scenario, which is provided in some interest rate models. For this reason, many yield curve models are essentially models of the stochastic evolution of the short-term rate. They assume that changes in the short-term interest rate is a Markov process. (It is outside the scope of this book to review the mathematics of such processes, but references are provided in subsequent chapters.) This describes an evolution of short-term rates in which the evolution of the rate is a function only of its current level, and not the path by which it arrived there. The practical significance of this is that the valuation of interest rate products can be reduced to the solution of a single partial differential equation.

Short-term  rate  models  are  composed  of  two  components.  The  first attempts to capture the average rate of change, also called the drift , of the short-term rate at each instant, while the second component measures the volatility as a function of the short-term rate. This is given by:

<!-- formula-not-decoded -->

where dr t is the instantaneous change in the short-term rate, and W t is the stochastic part of the process that describes the evolution of the interest rates, known as a Brownian or Wiener process.

The term r t dt , is  the  value  of  the  drift  multiplied  by  the  size  of the time period. The term r t dW t , is  the  volatility of the short-term rate multiplied by a random increment that is normally distributed. In most models,  the  drift  rate  term  is  determined  through  a  numerical  technique that matches the initial spot rate yield curve, while in some models, an analytical solution is available. Generally, models assume an arbitrage-free relationship  between  the  initial  forward  rate  curve,  the  volatility r t , ,  the market price of interest rate risk, and the drift term r t , In models such as those presented by Vasicek (1977) and Cox-Ingersoll-Ross (1985), the initial spot rate yield curve is given by an analytical formula in terms of the model parameters, and they are known as equilibrium models, because they describe yield curves as being derived from an assumption of economic equilibrium, based on a given market interest rate. So the Vasicek and CIR models are models of the short-term rate, and both incorporate the same form for the drift term, which is a tendency for the short-term rate to rise when it is below the long-term mean interest rate, and to fall when it is below the long-term mean. This is the mean reversion. Therefore we can describe the short-term rate drift in the form:

<!-- formula-not-decoded -->

where r is the short-term rate as before and and are the mean reversion and long-term rate constants. In the Vasicek model, the rate dependence of the volatility is constant, in the CIR model it is proportional to the squareroot of the short rate. In both models, because the dynamics of the short rate cover all possible moves, it is possible to derive negative interest rates, although under most conditions of initial spot rate and volatility levels, this is quite rare. Essentially, the Vasicek and CIR models express the complete forward rate curve as a function of the current short-term rate, which is why later models are sometimes preferred.

## APPENDICES

## Appendix 3.1 Mathematics Primer

The level of mathematics required for a full understanding of even intermediate concepts in finance is frighteningly high. To attempt to summarise even the basic concepts in just a few pages would be a futile task and risks trivialising the mathematics. Our intention is quite the opposite. As this is a financial markets book, and not a mathematics textbook, a certain level of knowledge has been assumed, and a formal or rigorous approach has not been adopted. Hence readers will find few derivations, and fewer proofs. What we provide here is a very brief introduction to some of the concepts the aim of this is simply to provide a starting point for individual research. We assist this start by listing recommended texts in the bibliography.

## Random variables and probability distributions

In financial mathematics, random variables are used to describe the movement  of  asset  prices,  and  assuming  certain  properties  about  the  process followed by asset prices allows us to state what the expected outcome of events  is.  A  random  variable  may  be  any  value  from  a  specified sample space . The specification of the probability distribution that applies to the sample space will  define  the  frequency  of  particular  values  taken  by  the random variable. The cumulative distribution function of a random variable X is defined using the distribution function f such that Pr X x f /lessthanorequalangled . A discrete random variable is one that can assume a finite or countable set of values, usually assumed to be the set of positive integers. We define a discrete random variable X with its own probability function p i such that p i Pr X i . In this case, the probability distribution is:

<!-- formula-not-decoded -->

with 0 1 /lessthanorequalangled /lessthanorequalangled p i for all i . The sum of the probabilities is 1.

Discrete probability distributions include the Binomial distribution and the Poisson distribution.

## Continuous random variables

The next step is to move to a continuous framework. A continuous random variable X may assume any real value and its probability density function f x is defined as:

<!-- formula-not-decoded -->

The probability distribution function is given as:

<!-- formula-not-decoded -->

Continuous distributions are commonly encountered in finance theory. The normal or  Gaussian distribution is perhaps the most important. It is described by its mean and  standard  deviation ,  sometimes  called  the location and spread respectively. The probability density function is:

<!-- formula-not-decoded -->

Where a random variable X is assumed to follow normal distribution, it is described in the form X N ˜ , 2 , where  ˜  means 'is distributed according to'. Examples of the graphical representation of the normal distribution are included in Chapter 4. The standard normal distribution is written as N 0 1 , with 0 and 1. The cumulative distribution function for the standard normal distribution is given by:

<!-- formula-not-decoded -->

The key assumption in the derivation of the Black-Scholes option pricing model is that the asset price follows a lognormal distribution, so that if we assume the asset price is P , we write:

<!-- formula-not-decoded -->

## Expected values

A probability distribution function describes the distribution of a random variable X . The expected value of X in a discrete environment is given by:

<!-- formula-not-decoded -->

and the equivalent for a continuous random variable is:

<!-- formula-not-decoded -->

The dispersion around the mean is given by the variance , which is:

<!-- formula-not-decoded -->

or:

<!-- formula-not-decoded -->

in  a  continuous  distribution.  A  squared  measure  has  little  application, so commonly the square root of the variance, that is the standard deviation, is used.

## Regression analysis

A linear relationship between two variables, one of which is dependent, can be estimated using the least squares method. The relationship is:

<!-- formula-not-decoded -->

where X is  the  independent  variable  and is  an  error  term  capturing those  explanatory  factors  not  covered  by  the  model. is  described  as i N ˜ 0, 2 . is the slope of the linear regression line that describes the relationship, while is the intercept of the y -axis. The sum of the squares of the form:

<!-- formula-not-decoded -->

is minimised in order to calculate the parameters.

Where we believe the relationship is non-linear, we can use a regression model of the form:

<!-- formula-not-decoded -->

This can be transformed into a form that is linear and then fitted using least squares. This is carried out by minimising squares and is described by:

<!-- formula-not-decoded -->

Yield curve fitting techniques that use splines are often fitted using multiple regression methods.

## Stochastic processes

This is perhaps the most difficult area of financial mathematics. Most references are also very technical and therefore difficult to access for the nonmathematician.

We begin with some definitions. A random process is usually referred to as a stochastic process. This is a collection of random variables X t and the process may be either discrete or continuous. We write X t t T , and a sample x t t t max ,0 /lessthanorequalangled /lessthanorequalangled of the random process X t t , /greaterthanorequalangled 0  is known as the realisation or path of the process.

A Markov process is one where the path is dependent on the present state of the process only, so that all historical data, including the path taken to arrive at the present state, is irrelevant. So in a Markov process, all data up to the present is contained in the present state. The dynamics of asset prices are frequently assumed to follow a Markov process, and in fact it represents a semi-strong form efficient market. It is written:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

A Wiener process or Brownian motion for X t t , /greaterthanorequalangled 0  has the following properties:

- ◾ X 0 0;
- ◾ X t t , /greaterthanorequalangled 0   has  independent  increments,  so  that X t b X t and X t b X t b 2 are independent and follow the same distribution;
- ◾ the variable X t has the property X t N t ˜ 0, for all t 0;
- ◾ X t X s N t s ˜ 0, for 0 s t .

Many interest rate models assume that the movement of interest rates over time follows a Wiener process.

## Stochastic calculus

The Wiener process is usually denoted with W , although Z and z are also used. For a Wiener process W t t , /greaterthanorequalangled 0  it can be shown that after an infini-

tesimal time interval ∆ t we have:

<!-- formula-not-decoded -->

If we also have U N ˜ , 0 1  then we may write:

<!-- formula-not-decoded -->

As the time interval decreases and approaches (but does not reach) 0, then the expression above may be written as:

<!-- formula-not-decoded -->

A Wiener process is not differentiable but a generalised Wiener process termed an Itô process is differentiable and is described in the form:

<!-- formula-not-decoded -->

where a is the drift and b the noise or volatility of the stochastic process.

## Appendix 3.2 Geometric Brownian Motion

Brownian motion was described in 1827 by the English scientist Robert Brown, and defined mathematically by the American mathematician Norbert Wiener in 1918. As applied to the price of a security, let us consider the change in price of a security as it alters over time. The time now is denoted as 0, with P t as the price of the security at time t from now. The collection of prices P t t ,0 /lessthanorequalangled is said to follow a Brownian motion with drift parameter µ and variance parameter 2 if for all non-negative values of t and T the random variable:

<!-- formula-not-decoded -->

is independent of all the prices P that have been recorded up to time t .  That is, the historic prices do not influence the value of the random variable. Also the random variable is normally distributed with a mean µ T and variance 2 T .

Standard Brownian motion has two drawbacks when applied to model security prices. The first and most significant is that, as the security price is  a  normally distributed. random variable, it can assume negative values with non-negative probability, a property of the normal distribution. This cannot happen with equity prices and only very rarely, under very special conditions, with interest rates. The second drawback of standard Brownian motion is that the difference between prices over an interval is assumed to follow a normal distribution irrespective of the price of the security at the start of the interval. This is not realistic, as the probabilities are affected by the initial price of the security.

For this reason, the geometric Brownian motion model is used in quantitative finance. Let us consider this now. Again, the time now is 0 and the security price at time t from now is given by P t .  The collection of prices P t t ,0 /lessthanorequalangled follows a geometric Brownian motion with drift and  standard  deviation or volatility 2 if  for  non-negative  values  of t and T the  random  variable P t T P t / is independent of all prices up to time t . In addition, the value:

<!-- formula-not-decoded -->

is a normally distributed random variable with mean µ T and variance 2 T .

<!-- image -->

Time

FIGURE 3.1 Evolution of Brownian or Wiener process.

What is the significance of this? It is this - once the parameters µ and have been ascertained, the present price of the security, and the present price only, determines the probabilities of future prices. The history of past prices has no impact. Also, the probabilities of the ratio of the price at future time T to the price now are not dependent on the present price. The practical impact of this is that the probability that the price of a security doubles in price at some specified point in the future is identical whether the price now is 5 or 50.

For our purposes, we need only be aware that at an initial price of P 0 , the expected price at time t is a function of the two parameters of geometric Brownian motion. The expected price, given an initial price P 0 , is given by:

<!-- formula-not-decoded -->

Equation  (3.5)  above  states  that  under  geometric  Brownian  motion, the  expected  price  of  a  security  is  the  present  price  increasing  at  the rate of 2 /2.

The evolution of a price process, including an interest rate, under varying parameters is shown at Figure 3.1, with an initial price level at 100.

## SELECTED BIBLIOGRAPHY AND REFERENCES

This field is an extensively researched one. Readers are first directed to the specific references cited in the text. If your interest is a general treatment of term structure models, we suggest James and Webber (2000), while Baxter and Rennie (1996) is an excellent treatment of the mathematics involved. For a general exposition of the theory of the yield curve, Chapter 18 of Ingersoll  (1987)  is  strongly  recommended. Rebonato (1996) looks at the practical issues involved in implementing interest rate models, and is a highly technical treatment. Finally, Van Deventer and Imai (1997) is an excellent accessible  account  of,  among  other  things,  term  structure  modelling  and yield curve smoothing techniques.

Baxter, A., and Rennie, D., Financial Calculus , Cambridge University Press, 1996. Gujarati, D., Basic Econometrics , AP, 1997.

- Hogg, R., and Craig, A., An Introduction to Mathematical Statistics , 5th edition, Prentice Hall, 1995.
- Kreyszig, E., Advanced Engineering Mathematics , Wiley, 1993.
- Ross, S., An Introduction to Probability Models , 5th edition, Academic Press, 1997.
- Ross, S., An Introduction to Mathematical Finance , Cambridge University Press, 1999.
- Baxter, M., and Rennie, A., Financial Calculus , Cambridge University Press, 1996, pp. 57-62
- Black, F., 'Interest Rates as Options', Journal of Finance , December 1995, pp. 1371-1376.
- Black, F., Derman, E., and Toy, W., 'A One-Factor Model of Interest Rates and its Application to Treasury Bond Options', Financial Analysts Journal , Spring 1990, pp. 33-39.
- Brennan, M., and Schwartz, E., 'A Continuous Time Approach to the Pricing of Bonds', Journal of Banking and Finance , July 1979, pp. 135-155.
- Campbell, J., 'A Defense of Traditional Hypotheses about the Term Structure of Interest Rates', Journal of Finance 41, 1986, pp. 183-193.
- Chen, R-R, and Scott, L., 'Pricing Interest Rate Options in a Two-Factor CoxIngersoll-Ross Model of the Term Structure', Review of Financial Studies , Winter 1992, pp. 613-636.
- Cox, J., Ingersoll, J., and Ross, S., 'A Theory of the Term Structure of Interest Rates', Econometrica 53, March 1985, pp. 385-407.
- Fong, H.G., and Vasicek, O., 'Fixed Income Volatility Management', Journal of Portfolio Management , Summer 1991, pp. 41-46.
- Gibbons, M., and Ramaswamy, K., 'The Term Structure of Interest Rates: Empirical Evidence', Review of Financial Studies , 1994.
- Haug, E., The Complete Guide to Option Pricing Formulas , McGraw-Hill, 1998, Chapter 4.
- Heath, D., Jarrow, R., and Morton, A., 'Bond Pricing and the Term Structure of Interest Rates: A New Methodology for Contingent Claims Valuation', Econometrica 60, January 1992, pp. 77-105.
- Ho, T., and Lee, S-B., 'Term Structure Movements and Pricing Interest Rate Contingent Claims', Journal of Finance, December 1986, pp. 1011-1029.
- Hull, J., Options , Futures and other Derivatives , 3rd edition, Prentice Hall, 1997, pp. 220-222.

- Hull, J., and White, A., 'Pricing Interest Rate Derivative Securities', Review of Financial Studies , 1990, pp. 573-592.
- Ingersoll, J., Jr., Theory of Financial Decision Making , Rowman &amp; Littlefield, 1987.
- James, J., and Webber, N., Interest Rate Modelling , Wiley, 2000, Chapters 5-15.
- Jarrow, R., Modelling Fixed Income Securities and Interest Rate Options , McGraw-Hill, 1996.
- Merton, R., Continuous Time Finance , Blackwell, 1993, Chapter 11.
- Rebonato, R., Interest Rate Option Models , Wiley, 1996.
- Rebonato, R., and Cooper, I., 'The Limitations of Simple Two-Factor Interest Rate Models', Journal of Financial Engineering , March 1996.
- Ross, S., Probability Models , 7th edition, Academic Press, 2000.
- Sundaresan, S., Fixed Income Markets and their Derivatives , South Western Publishing, 1997.
- Tuckman, B., Fixed Income Securities , Wiley, 1996.
- Van Deventer, D., and Imai, K., Financial Risk Analytics, Irwin, 1997, Chapter 5.
- Vasicek, O., 'An Equilibrium Characterization of the Term Structure', Financial Economics , 5, 1977, pp. 177-188.
- Journal of

My stomach knotted and I felt sick. I went to the toilet in case I vomited, but managed not to. Volunteering for operations was one thing, but actually going on one was quite another. Thoughts of being labelled LMF Lack of Moral Fibre - with its dreadful stigma, forced me back to the crew room.

-- Albert Smith, Mosquito Pathfinder : A Navigator's 90 WWII Bomber Operations , Crecy Publishing Limited, 2003

<!-- image -->

## Interest Rate Modelling II: The Dynamic of Asset Prices

T he  pricing  of  derivative  instruments  such  as  options  is  a  function  of  the movement in the price of the underlying asset over the lifetime of the option, and valuation models describe an environment where the price of an option is related to the behaviour process of the variables that drive asset prices. This process is described as a stochastic process, and pricing models describe the stochastic dynamics of asset price changes, whether this is a change in share prices, interest rates, foreign exchange rates or bond prices. To understand the mechanics of interest rate modelling therefore, we must familiarise ourselves with the behaviour of functions of stochastic   variables . The concept of a stochastic process is a vital concept in finance theory. It describes random phenomena that evolve over time, and these include asset prices. For this reason, an alternative title for this chapter could be An Introduction to Stochastic Processes .

In this chapter, we review the basic principles of the dynamics of asset prices, which are then put into context in the following chapters, which look at term structure models.

## THE BEHAVIOUR OF ASSET PRICES

The first property that asset prices, which can be taken to include interest rates, are assumed to follow is that they are part of a continuous process. This means that the value of any asset can and does change at any time and from one point in time to another, and can assume any fraction of a unit of measurement. It is also assumed to pass through every value as it changes, so for example, if the price of a bond moves from 92.00 to 94.00, it must also have passed through every point in between. This feature means that the asset price does not exhibit jumps , which is not the case in many markets, where price processes do exhibit jump behaviour. For now, however, we may assume that the price process is continuous.

## STOCHASTIC PROCESSES

Models that seek to value options or describe a yield curve also describe the dynamics of asset price changes. The same process is said to apply to changes in share prices, bond prices, interest rates, and exchange rates. The process by which prices and interest rates evolve over time is known as a stochastic process , and this is a fundamental concept in finance theory. 1  Essentially a stochastic process is a time series of random variables. Generally the random variables in a stochastic process are related in a non-random manner, and so therefore we can capture them in a probability density function .

Consider the function y f x . Given the value of x , we can obtain the value of y . If we denote the set W as the state of the world, where w W , the function f x w , has the property that given a value w W , it becomes a function of x only. If we say that x represents the passage of time, two functions f x W , 1 and f x w , 2 will be different because the second element w in  each case is different. With x representing time, these two functions describe two different processes that are dependent on different states of the world W . The element w represents an underlying random process, and so therefore the function f x w , is a random function . A random function is also called a stochastic process , one in which x represents time and x 0. The random characteristic of the process refers to the entire process, and not any particular value in that process at any particular point in time.

Examples  of  functions  include  the exponential function  denoted  by y e x and the logarithmic function log e y x .

The price processes of shares and bonds, as well as interest rate processes, are stochastic processes. That is, they exhibit a random change over time. For the purposes of modelling, the change in asset prices is divided into two components. These are the drift of the process, which is a deterministic element, 2  also called the mean, and the random component known as the noise , also called the volatility of the process.

We introduce the drift component briefly as follows. For an asset such as an ordinary share, which is expected to rise over time (at least in line with assumed growth in inflation), the drift can be modelled as a geometric growth progression. If the price process has no 'noise', the change in price of the stock over the time period dt can be given by:

<!-- formula-not-decoded -->

1   A formal definition of a stochastic process is given in Appendix 5.1.

2   There are two types of model: deterministic ,  which  involves  no  randomness so the variables are determined exactly, and stochastic , which incorporates the random nature of the variables into the model.

where the term µ describes the growth rate. Expression (4.1) can be rewritten in the form:

<!-- formula-not-decoded -->

which can also be written in integral form. For interest rates, the movement process can be described in similar fashion, although as we shall see, interest rate modelling often takes into account the tendency for rates to return to a mean level or range of levels, a process known as mean reversion . Without providing the derivation here, the equivalent expression for interest rates takes the form:

<!-- formula-not-decoded -->

where is the mean reversion rate that determines the pace at which the interest rate reverts to its mean level. If the initial interest rate is less than the drift rate, the rate r will increase, while if the level is above the drift rate, it will tend to decrease.

For  the  purposes  of  employing  option  pricing  models,  the  dynamic behaviour of asset prices is usually described as a function of what is known as a Wiener process , which is also known as Brownian motion . The noise or volatility component is described by an adapted Brownian or Wiener process, and involves introducing a random increment to the standard random process. This is described next.

## WIENER PROCESS OR BROWNIAN MOTION

The stochastic process we have briefly discussed above is known as Brownian motion or a Wiener process. In fact, a Wiener process is only a process that has a mean of 0 and a variance of 1, but it is common to see these terms used synonymously. Wiener processes are a very important part of continuoustime finance theory, and interested readers can obtain more detailed and technical data on the subject in Neftci (1996) and Duffie (1996) 3 , among others. It is a well-researched subject.

One of the properties of a Wiener process is that the sample pathway is continuous, that is, there are no discontinuous changes. An example of a discontinuous process is the Poisson process. Both are illustrated in Figures 4.1 and 4.2 below.

In  the  examples  illustrated,  both  processes  have  an  expected  change of 0 and a variance of 1 per unit of time. There are no discontinuities in the Wiener process, which is a plot of many tiny random changes. This is reflected in the 'fuzzy' nature of the sample path. However, the Poisson process has no fuzzy quality and appears to have a much smaller number of random changes. We can conclude that asset prices, and the dynamics of interest rates, are more akin to a Wiener process. This, therefore, is how asset prices are modelled. From observation we know that, in reality asset prices and interest rates do exhibit discontinuities or jumps , however, there are other advantages in assuming a Wiener process, and in practice because continuous-time stochastic processes can be captured as a combination of Brownian motion and a Poisson process, analysts and researchers use the former as the basis of financial valuation models.

3   Duffie's text requires a good grounding in continuous-time mathematics.

FIGURE 4.1 An example of a Wiener process.

<!-- image -->

FIGURE 4.2 An example of a Poisson process.

<!-- image -->

The first step in asset pricing theory builds on the assumption that prices follow a Brownian motion. The properties of Brownian motion W state that it is continuous, and the value of W t t 0  is normally distributed under a probability measure P as  a random variable  with  parameters N t 0, .  An incremental change in the asset value over time dt , which is a very small or infinitesimal change in the time given by W W s t s , is also normally distributed with the parameters N t 0, under P . Perhaps the most significant feature is that the change in value is independent of whatever the history of the price process has been up to in time s . If a process follows these conditions, it  is  Brownian motion. In fact, asset prices do not generally have a mean of 0, because over time we expect them to rise. Therefore modelling asset prices incorporates a drift measure that better reflects asset price movement, so that an asset movement described by:

<!-- formula-not-decoded -->

would be a Brownian motion with a drift given by the constant µ . A second parameter is then added, a noise factor, which scales the Brownian motion by another constant measure, the standard deviation . The process is then described by:

<!-- formula-not-decoded -->

which can be used to simulate the  price  path  taken  by  an  asset,  as  long as  we  specify  the  two  parameters.  Under  (4.5),  there  is  a  possibility  of achieving negative values, which is not realistic for asset prices. However, using the exponential of the process given by (4.5) is more accurate, and is given by (4.6):

<!-- formula-not-decoded -->

Brownian motion or the Wiener process is  employed  by  virtually  all option pricing models, and we introduce it here with respect to a change in the variable W over an interval of time t . If W represents a variable following a Wiener process and W ∆ is a change in value over a period of time t , the relationship between W ∆ and t ∆ is given by (4.7):

<!-- formula-not-decoded -->

where is a random sample from a normal distribution with a mean 0 and a standard deviation of 1. Over a short period of time the values of W ∆ are independent and therefore also follow a normal distribution with a mean 0 and a standard deviation of t ∆ Over a longer time period T made up of N periods of length t ∆ the change in W over the period from time 0 to time T is give by (4.8):

<!-- formula-not-decoded -->

The successive values assumed by W are serially independent, therefore from (4.8) we conclude that changes in the variable W from time 0 to time T follow a normal distribution with mean 0 and a standard deviation of T . This describes the Wiener process, with a mean of zero or a zero drift rate and a variance of T . This is an important result because a zero drift rate  implies  that  the  change  in  the  variable  (in  this  case,  the  asset  price)

in  the  future  is  equal  to  the  current  change. This  means  that  there  is  an equal chance of an asset return ending up 10% or down 10% over a long period of time.

The next step in the analysis involves using stochastic calculus. A stochastic process X incorporates a Newtonian term that is based on dt and a Brownian term based on the infinitesimal increment of W that is denoted by dWt . The Brownian term has a 'noise' factor of t . The infinitesimal change of X at Xt is given by the differential equation:

<!-- formula-not-decoded -->

where t is the volatility of the process X at time t and t µ is the drift of X at time t . For interest rates that are modelled on the basis of mean reversion, the process is given by:

<!-- formula-not-decoded -->

where the mean reverting element is as before. Without providing the supporting mathematics, which we have not covered here, the process described by (4.10) is called an Ornstein-Uhlenbeck process, and has been assumed by a number of interest rate models.

One other important point to introduce here is that a random process described by (4.10) operates in a continuous environment. In continuous-time mathematics, the integral is the tool that is used to denote the sum of an infinite number of objects, that is where the number of objects is uncountable . A formal definition of the integral is outside the scope of this book, but accessible accounts can be found in the texts referred to previously. A basic introduction is given at Appendix 4.4. However, the continuous stochastic process X described by (4.9) can be written as an integral equation in the form:

<!-- formula-not-decoded -->

where and µ are processes as before. The volatility and drift terms can be dependent on the time t but can also be dependent on X or W up to the point t . This is a complex technical subject and readers are encouraged to review the main elements in the referred texts.

## THE MARTINGALE PROPERTY

Continuous time asset pricing is an important part of finance theory and involves some more advanced mathematics. It is outside the scope of this book to derive, prove, and detail the main elements. However, we wish to summarise the essential property, and begin by saying that in continuous time,  asset  prices  can  take  on  an  unlimited  number  of  values.  Stochastic differential  equations are used to capture the dynamics of asset prices in a generalised form. So for example, as we saw in the previous section, an incremental change in the price of an asset S at time t could be given by:

<!-- formula-not-decoded -->

dS is an infinitesimal change in the price of asset S ;

Sd µ is  the  predicted  movement  during  the  infinitesimal  time  interval dt ;

SdW t is an unpredictable random shock.

Martingale theory is a branch of mathematics that classifies the trend in an observed time series set of data. A stochastic process is said to behave like a martingale if there are no observable trends in its pattern. The Martingale property  is  often  used  in  conjunction  with  a Wiener  process  to  describe asset price dynamics. The notion of the martingale property is that the best approximation of a set of integral random variables M at the end of a time period t is M 0 , which essentially states that the most accurate way to predict a future asset price is to use the price of the asset now. That is, using the price today is the same as using all available historical information, as only the newest information regarding the asset is relevant.

We do not describe or prove this property here but the Martingale property is used to derive (4.13), the price of an asset at time t:

<!-- formula-not-decoded -->

A martingale is an important type of stochastic process and the concept of a martingale is fundamental to asset pricing theory. A process that is a martingale is one in which the expected future value, based on what is known up to now, is the same as today's value. That is, a martingale is a process in which the conditional expected future value, given current information, is equal to the current value. The martingale representation theorem states that given a Wiener process, and the fact that the path of the Wiener process up to that point is known, then any martingale is equal to a constant plus a stochastic integral, with respect to the Wiener process. This can be written as:

<!-- formula-not-decoded -->

where:

Therefore, a stochastic process that is a martingale has no observable trend . The price process described by (4.9) is not a martingale unless the drift  component µ is  equal  to  zero,  otherwise  a  trend  will  be  observed. A  process  that  is  observed  to  trend  upwards  is  known  as  a submartingale ,  while  a  process  that  on  average  declines  over  time  is  known  as  a supermartingale .

What is the significance of this? Here we take it as given that because price processes can be described as equivalent martingale measures (which we do not go into here) they enable the practitioner to construct a risk-free hedge of a market instrument. By enabling a no-arbitrage portfolio to be described, a mathematical model can be set up and solved, including riskfree valuation models.

The  background  and  mathematics  to  martingales  can  be  found  in Harrison  and  Kreps  (1979),  and  Harrison  and  Pliska  (1981),  as  well  as Baxter and Rennie (1996). For a description of how, given that price processes are martingales, we are able to price derivative instruments, see James and Webber (2000, Chapter 4).

## GENERALISED WIENER PROCESS

The standard Wiener process is a close approximation of the behaviour of asset prices, but does not account for some specific aspects of market behaviour. In the first instance, the prices of financial assets do not start at zero, and their price increments have positive means. The variance of asset price moves is not always unity. Therefore, the standard Wiener process is replaced by the generalised Wiener process, which describes a variable that may start at something other than zero, and also has incremental changes that have a mean other than zero, as well as variances that are not unity. The mean and variance are still constant in a generalised process, which is the same as the standard process, and a different description must be used to describe processes that have variances that differ over time - these are known as stochastic integrals.

We now denote the variable as X and for this variable a generalised Wiener process is given by (4.15):

<!-- formula-not-decoded -->

where a and b are constants. This expression describes the dynamic process of the variable X as a function of time and dW . The first term adt is known as the deterministic term and states that the expected drift rate of X over time is a per unit of time. The second term bdW is the stochastic element and describes the variability of the move in X over time, and is quantified by b multiplied by the Wiener process. When the stochastic element is zero, dX adt , or put another way:

<!-- formula-not-decoded -->

From this, we state that at time t , X X a t 0 . This enables us to describe the price of an asset, given its initial price, over a period of time. That is, the value of X at any time is given by its initial value at time 0, which is X 0 , together with its drift multiplied by the length of the time period. We can restate (4.15) to apply over a long time period t ∆ shown as (4.16):

<!-- formula-not-decoded -->

As with the standard Wiener process, X ∆ has a normal distribution with mean a t ∆ and standard deviation b t ∆ .

The generalised Wiener process is more flexible than the standard one but is  still  not  completely  accurate  as  a  model  of  the  behaviour  of  asset prices. It has normally distributed values, which means that there is a probability of observing negative prices. For assets such as equities, this is clearly unrealistic.  In  addition,  the  increments  of  a Wiener  process  are  additive, whereas the increments of asset prices are more realistically multiplicative. In fact, as the increments of a Wiener process have constant expectation, this implies that the percentage incremental change in asset prices, or the percentage rate of return on the stock, is declining as the stock price rises. This is also not realistic. For this reason, a geometric process or geometric Brownian  motion  has  been  introduced, 4   which  is  developed  by  an  exponential transformation of the generalised process. From (4.16), a one-dimensional process is a geometric Brownian motion if it has the form e X , where X is a one-dimensional generalised Brownian motion with a deterministic initial value of X 0 . Both processes are illustrated at Figure 4.3.

FIGURE 4.3 Standard and generalised Wiener processes.

<!-- image -->

4   See for instance, Nielsen (1999).

Another type of stochastic process is an Itô process. This a generalised Wiener process where the parameters a and b are functions of the value of the variable X and time t . An Itô process for X can be written as (4.17):

<!-- formula-not-decoded -->

The  expected  drift  rate  and  variance  of  an  Itô  process  are  liable  to change over time - indeed the dependence of the expected drift rate and variance  on X and t is  the  main  difference  between  it  and  a  generalised Wiener process. The derivation of Itô's formula is given at Appendix 4.3.

## A MODEL OF THE DYNAMICS OF ASSET PRICES

The dynamics of the asset price X are represented by the Itô process shown at (4.18), where there is a drift rate of a and a variance rate of b X 2 2 :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The  uncertainty  element  is  described  by  the  Wiener  process  element, with:

<!-- formula-not-decoded -->

where is the error term, a random sample from the standardised normal distribution, so that N 0 1 , . From this, and for over a longer period of time t ∆ , we can write:

<!-- formula-not-decoded -->

Over this longer period of time, for application in a discrete-time environment, if we assume that volatility is zero, we have:

<!-- formula-not-decoded -->

so that:

and:

## EXAMPLE 4.1

A conventional bond has an expected return of 5.875% and a standard deviation of 12.50% per annum. The initial price of the bond is 100. From (4.20) the dynamics of the bond price are given by:

<!-- formula-not-decoded -->

and for the time period t ∆ by:

<!-- formula-not-decoded -->

If the short time interval t ∆ is four weeks or 0.07692 years, assuming 0 1 , , then the increase in price is given by:

<!-- formula-not-decoded -->

So the price increase is described as a random sample from a normal distribution with a mean of 0.452 and a volatility of 3.467. Over a time interval of four weeks, / P P ∆ is normal with:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Return is given by X X e at 0 .

The discrete time version of the asset price model states that the proportional return on the asset price X over a short time period is given by an expected return of a t ∆ and a stochastic return of b dt ε∆ . Therefore, the returns of asset price changes / X X ∆ is normally distributed with a mean of a t ∆ and a standard deviation of b t ∆ . This is the distribution of asset price returns and is given by (4.20):

<!-- formula-not-decoded -->

## STOCHASTIC CALCULUS MODELS: BROWNIAN MOTION AND ITÔ CALCULUS

We noted at the start of the chapter that the price of an option is a function of the price of the underlying stock and its behaviour over the life of the option. Therefore, this option price is determined by the variables that describe the process followed by the asset price over a continuous period of time. The behaviour that asset prices follow is a stochastic process, and so option pricing models - and term structure models - must capture the behaviour of stochastic variables behind the movement of asset prices. To accurately describe financial market processes, a financial model depends on more than one variable. Generally, a model is constructed where a function is itself a function of more than one variable. Itô's lemma, the principal instrument in continuous time finance theory, is used to differentiate such functions. This was developed by a mathematician, K. Itô, in 1951. Here we simply state the theorem, as a proof and derivation are outside the scope of the book. Interested readers may wish to consult Briys et al. (1998), and Hull  (1997)  for  background  on  Itô's  lemma. We  also  recommend  Neftci (1996). Basic background on Itô's lemma is given in Appendices 4.2 and 4.3.

## BROWNIAN MOTION

Brownian motion is very similar to a Wiener process, which is why it is common to see the terms used interchangeably. Note that the properties of a Wiener process require that it be a martingale, while no such constraint is required for a Brownian process. A mathematical property known as the Lévy theorem allows us to consider any Wiener process Wt with respect to an information set F t as  a  Brownian  motion Zt with  respect  to  the  same information set.

We can view Brownian motion as a continuous time random walk , visualised as a walk along a line, beginning at X 0 0 and moving at each incremental time interval t ∆ either up or down by an amount . t ∆ If we denote the position of the walk as Xn after the n th move, the position would be:

<!-- formula-not-decoded -->

where the and signs occur with an equal probability of 0.5. This is a simple random walk. We can transform this into a continuous path by applying linear interpolation between each move point, so that:

<!-- formula-not-decoded -->

It can be shown (but not here) that the path described at (4.22) has a number of properties, including that the incremental change in value each time it moves is independent of the behaviour leading up to the move, and that the mean value is 0 and variance is finite. The mean and variance of the set of moves are independent of t ∆ .

What is the importance of this? Essentially this - the probability distribution of the motion can be shown, as t ∆ approaches 0, to be normal or Gaussian .

## STOCHASTIC CALCULUS

Itô's theorem provides an analytical formula that simplifies the treatment of stochastic differential equations, which is why it is so valuable. It is an important rule  in  the  application  of  stochastic  calculus  to  the  pricing  of financial instruments. Here we briefly describe the power of the theorem.

The standard stochastic differential equation for the process of an asset price S t is given in the form:

<!-- formula-not-decoded -->

where a S t t , is  the  drift  coefficient  and b S t t , is  the  volatility  or diffusion coefficient. The Wiener process is denoted dWt and is the unpredictable events that occur at time intervals t ∆ . This is sometimes denoted dZ or dz .

Consider a function f S t t , dependent on two variables S and t , where S follows a random process and varies with t . If S t is a continuous-time process that follows a Wiener process Wt , then it directly influences the function f through the variable t in f S t t , . Over time, we observe new information about Wt as well the movement in S over each time increment, given by dS t . The sum of both these effects represents the stochastic differential and is given by the stochastic equivalent of the chain rule known as Itô ' s lemma . So for example, if the price of a stock is 30 and an incremental time period later is 30.5, the differential is 0.5.

If we apply a Taylor expansion in two variables to the function f S t t , , we obtain:

<!-- formula-not-decoded -->

Remember that t is the partial derivative while t ∆ is the derivative.

If  we  substitute  the  stochastic  differential  equation  (4.23)  for S t ,  we obtain Itô ' s lemma of the form:

<!-- formula-not-decoded -->

What we have done is taken the stochastic differential equation (SDE) for S t and  transformed  it  so  that  we  can  determine  the  SDE  for f t .  This is  a  valuable mechanism by which we can obtain an expression for pricing derivatives that are written on an underlying asset whose price can be determined using conventional analysis. In other words, using Itô's formula enables us to determine the SDE for the derivative, once we have set up the SDE for the underlying asset. This is the value of Itô's lemma.

The SDE for the underlying asset S t is written in most textbooks in the following form:

<!-- formula-not-decoded -->

which  has  denoted  the  drift  term a S t t , as t S µ and  the  diffusion  term b S t , t as S t . In the same way, Itô's lemma is usually seen in the form:

<!-- formula-not-decoded -->

although the noise term is sometimes denoted dZ . Further applications are illustrated in Example 4.2(i).

## EXAMPLE 4.2(i) LOGNORMAL DISTRIBUTION

A variable (such as an asset price) may be assumed to have a lognormal distribution if  the natural logarithm of the variable is normally distributed. Therefore, if an asset price S follows a stochastic process described by:

<!-- formula-not-decoded -->

we apply Itô's lemma.

then to determine the expression for In S If we say that F S ln , then the first derivative is:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We substitute these values into Itô's lemma given at (4.27) and this gives us:

<!-- formula-not-decoded -->

So we have moved from dF to dS using Itô's lemma, and (4.29) is a good representation of the dynamic of the asset price over time.

## EXAMPLE 4.2(ii) THE BOND PRICE EQUATION

The continuously compounded gross redemption yield at time t on a default-free zero-coupon bond that pays £1 at maturity date T is x .  We assume that the movement in x is described by:

<!-- formula-not-decoded -->

where a , , and s are positive constants. What is the expression for the process followed by the price P of the bond? Let us say that the price of the bond is given by:

<!-- formula-not-decoded -->

We have dx ,  and  we  require dP .  This  is  done  by  applying  Itô's lemma. We require:

<!-- formula-not-decoded -->

From Itô's lemma:

<!-- formula-not-decoded -->

which gives:

<!-- formula-not-decoded -->

which simplifies to:

<!-- formula-not-decoded -->

Therefore, using Itô's  lemma we have transformed the SDE for the bond yield into an expression for the bond price.

## UNCERTAINTY OF INTEREST RATES

All derivative valuation models describe a process followed by market interest rates. As the future level of the yield curve or spot rate curve is uncertain, the key assumption is that interest rates follow a normal distribution, and follow a Gaussian process. Thus the interest rate is described as being a Gaussian interest rate uncertainty. Only the short-term risk-free interest rate, for which we read the T-bill rate or (in certain situations) the government bond repo rate, is captured in most models. Following Merton (1973), Vasicek (1977), Cox, Ingersoll and Ross (1985), and Jamshidian (1991), the short-dated risk-free interest r applicable to the period t is  said  to  follow a Gaussian diffusion process under a constant volatility. The major drawback under this scenario is that under certain conditions it is possible to model a term structure that produces negative forward interest rates. However,  in  practice  this  occurs  only  under  certain  limited  conditions,  so  the validity of the models is not diminished. The future path followed by r t is described by the following stochastic differential equation:

<!-- formula-not-decoded -->

where a and b are constant deterministic functions and t is the instantaneous standard deviation of r t . Under (4.30), the process describing the returns generated by a risk-free zero-coupon bond P t T , that  expires at time T and has a maturity of T t under the risk-neutral probability Q ,  is  given by (4.31):

<!-- formula-not-decoded -->

where P is the standard deviation of the price returns of the T t bond and is a deterministic function defined by:

<!-- formula-not-decoded -->

In the Black-Scholes model, the value of a $1 (or £1) deposit invested at the risk-free zero-coupon interest rate r and continuously compounded over a period t will grow to the value given by the expression below, where Mt is the value of the deposit at time t .

<!-- formula-not-decoded -->

## APPENDICES

## Appendix 4.1 An introduction to stochastic processes

A stochastic process can be described with respect to the notion of a vector of variables. If we set the following parameters:

is the set of all possible states is a class of partition ; s of .

X is said to be a random variable when it is a measurable application from ( Ω , ) to . A vector of random variables X X Xn 1 , is  an  application  that  can  be  measured  from  ( Ω , )  into n .  Therefore, we have a vector of random variables that is similar to n ordinary variables defined under the same probability function.

A stochastic process is an extension of the notion of a vector of variables when the number of elements becomes infinite. It is described by:

<!-- formula-not-decoded -->

which is a set of random variables where the index varies in a finite or infinite group, and is denoted by X t .

## Appendix 4.2 Itô's lemma

If f is a continuous and differentiable function of a variable x , and x ∆ is a small change in x , then using a Taylor expansion, the resulting change in f is given by (4.33):

<!-- formula-not-decoded -->

If f is dependent on two variables x and y , then the Taylor expansion of f ∆ becomes (4.34):

<!-- formula-not-decoded -->

The limiting case where x ∆ and y ∆ are close to zero will transform (4.34) to (4.35):

<!-- formula-not-decoded -->

Let us now consider a derivative asset f x t , with a value dependent on time and on the asset price x .  We  assume  that x follows  the  general Itô process:

<!-- formula-not-decoded -->

where a and b are functions of x and t and dW is  a Wiener process. The asset price x is described by a drift rate of a and a standard deviation of b . Using Itô's lemma, it can be shown that a function f of x and t will follow the following process:

<!-- formula-not-decoded -->

and where dW is the Wiener process, therefore f follows an Itô process and its drift and standard deviation are described by the expressions below:

<!-- formula-not-decoded -->

This may also be stated as:

<!-- formula-not-decoded -->

where the term is normally distributed with a mean of 0, so that E 0, and  a  variance  of  1,  so  that E E 2 2 1.  In  the  limit  case  (4.34) becomes (4.38), which is Itô's lemma.

<!-- formula-not-decoded -->

The expression at (4.38) is Itô's lemma and if we substitute (4.36) for dx , it can be transformed to (4.39).

<!-- formula-not-decoded -->

The derivation of Itô's formula is given at Appendix 4.3.

## Appendix 4.3 Derivation of Itô's formula

Let Xt be a stochastic process described by:

<!-- formula-not-decoded -->

where Wt is a random variable and Brownian motion and dWt is an incremental change in the Brownian motion Wt ,  equal  to Z dt t , Z N t 0 1 , . Then suppose that we have a function Y f X t t t , and we require the differential dYt . Applying a Taylor expansion of Yt we obtain:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In (4.40), if we square dXt we obtain:

<!-- formula-not-decoded -->

The first two terms in (4.42) are of a higher order and of minimal impact when dt is sufficiently small, and may be ignored. It can be shown that the variance of the dWt 2 term will tend towards zero when the increment dt is sufficiently small. At this point it no longer has the property of a random variable and becomes more a constant with expected value:

<!-- formula-not-decoded -->

It can then be shown that for sufficiently small dt :

<!-- formula-not-decoded -->

The differential dYt has an element that tends towards 1 2 2 2 2 f x dt t t for sufficiently small dt , but cannot be dropped as were the higher-order terms of (4.42), as it is of order dt . So the first-order differential of Yt is:

<!-- formula-not-decoded -->

and now if we insert dXt from (4.40) into (4.44) we will obtain:

<!-- formula-not-decoded -->

If we follow this through, we will arrive at Itô's lemma. We can apply this immediately. Consider a process:

<!-- formula-not-decoded -->

for which the differential form is:

<!-- formula-not-decoded -->

If we set the function f X equal to Xt the results of applying the Itô lemma terms are:

<!-- formula-not-decoded -->

Therefore using Itô's lemma we obtain:

<!-- formula-not-decoded -->

which is what we expect. What we have here is a stochastic differential equation at (4.48) for which the solution is (4.46).

## Appendix 4.4 The integral

Stochastic integrals are continuous path martingales. The integral is used to calculate sums where we have an infinite or uncountable number of items, in contrast with the ∑ sum operator, which is used for a finite number of objects. In defining integrals, we begin with an approximation, where there is a countable number of items, and then set a limit and move to an uncountable number. Stochastic integration is an operation that is closely associated with Brownian paths - a path is partitioned into consecutive intervals or increments, and each increment is multiplied by a random variable. These values are then summed to create the stochastic integral. Therefore, the stochastic integral can be viewed as a random walk Brownian motion with increments that have varying values, a random walk with non-homogeneous movement.

Suppose we have a deterministic f x of time, with x 0, T that corresponds to a curve of f x over the period from 0 to T , and we wish to calculate the area given by the function from time t 0 to t T . This can be done by integrating the function over the time interval  0, T , given by:

<!-- formula-not-decoded -->

To calculate the integral, we split the area given by the function in the time period into a series of partitions or intervals, described by:

<!-- formula-not-decoded -->

The approximate value of the area required is:

<!-- formula-not-decoded -->

however, if we decrease the interval space such that it approaches 0, described by:

<!-- formula-not-decoded -->

the area under the space is given by the integral at (4.49), as the approximating sum approaches the area defined by the limit:

<!-- formula-not-decoded -->

## SELECTED BIBLIOGRAPHY AND REFERENCES

- Baxter, M. and Rennie, A., Financial Calculus , Cambridge University Press, 1996.
- Boyle, P., 'Option Valuation Using a Three Jump Process', International Options Journal 3, 1986, pp. 7-12.
- Cootner, p. (ed.), The Random Character of Stock Market Prices , MIT Press, 1964.
- Cox, D. and Miller, H., The Theory of Stochastic Processes , Chapman &amp; Hall, 1965.
- Duffle, D., Dynamic Asset Pricing Theory , Princeton University Press, 1996.
- Fama, E., 'The Behaviour of Stock Prices', Journal of Business 38, January 1965, pp. 34-105.
- Feller, W., Probability Theory and Its Applications , Vol. l and 2, John Wiley and Sons, 1950.
- Debreu, G., 'Representation of a Preference Ordering by a Numerical Function', in Thrall, R., Coombs, C., Davis, R. (ed.), Decision Processes , Wiley, 1954.
- Harrison, J. and Kreps, D., 'Martingales and Arbitrage in Multi-Period Securities Markets', Journal of Economic Theory 20, 1979, pp. 381-408.
- Harrison, J., Pliska, S., 'Martingales and Stochastic Integrals in the Theory of Continuous Trading', Stochastic Processes and Their Applications 11, 1981, pp. 216-260.
- Ingersoll, J., Jr, Theory of Financial Decision Making , Rowman &amp; Littlefield, 1987.
- Itô, K., 'On Stochastic Differential Equations', American Mathematical Society 4, 1951, pp. 1-51.
- James, J. and Webber, N., Interest Rate Modelling , John Wiley and Sons, 2000, Chapters 3-5, 7-9, 15-16.
- Jamshidian, F., 'Bond and Option Valuation in the Gaussian Interest Rate Model', Research in Finance 9, 1991, pp. 131-170.
- Merton, R., 'Theory of Rational Option Pricing', Bell Journal of Economics and Management Science 4, Spring 1973, pp. 141-183.
- Nielson, L.T., Pricing and Hedging of Derivative Securities , Oxford University Press, 1999.
- Neftci, S., An Introduction to the Mathematics of Financial Derivatives , Academic Press, 1996.
- Rendleman, R. and Bartter, B., 'Two State Option Pricing', Journal of Finance 34, 1979, pp. 1092-1110.
- Ross, S., Probability Models , 7th edition, Harcourt Academic Press, 2000.
- Vasicek, O., 'An Equilibrium Characterisation of the Term Structure', Journal of Financial Economics 5, 1977, pp. 177-188.
- Williams, D., Probability with Martingales , Cambridge University Press, 1991.

After the concert I was introduced to Ken Livingstone. It was the first time I'd met a politician, and I was astounded by the self-assurance of the man. It was a surprise to find that someone who was seemingly one of the good guys could also be in the fame game. I had naively assumed that if you claimed to be on the side of minority groups and represented equality for the less fortunate, you might show some signs of humility.

-- Johnny Marr, Set The Boy Free: The Autobiography , Century, 2016

<!-- image -->

## Interest Rate Models I

I n Chapter 4 we introduced the concept of stochastic processes. Most, but not all, interest rate models are essentially a description of the short-term rate in terms of a stochastic process. Recent literature has tended to categorise models into one of six different types, but for our purposes we can generalise them into two types. Thus, we introduce some of the main models, according to their categorisation as equilibrium or arbitrage-free models. This chapter looks at the earlier models, including the first ever term structure model presented by Vasicek in 1977. Chapter 6 considers what have been  termed 'whole  yield  curve'  models,  or  the  Heath-Jarrow-Morton family, while Part III reviews considerations in modelling the yield curve.

## INTEREST RATE MODELS

An interest rate model provides a description of the dynamic process by which rates change over time, in terms of a statistical construct, as well as a means by which interest rate derivatives such as options can be priced. It is often the practical implementation of the model that dictates which type is  used, rather than mathematical neatness or more realistic assumptions. An excellent categorization is given in James and Webber (2000) who list models as being one of the following types:

- ◾ the traditional one-, two- and multi-factor equilibrium models, known as affine term structure models (see James and Webber (2000) or Duffie (1996, p. 136)). These include Gaussian affine models such as Vasicek, Hull-White and Steeley, where the model describes a process with constant volatility, and models that have a square-root volatility such as Cox-Ingersoll-Ross (CIR);
- ◾ whole yield curve models such as Heath-Jarrow-Morton;
- ◾ so-called market models such as Jamshidian;
- ◾ so-called consol models such as Brennan and Schwartz.

There are also  other  types  of  models,  but  we  suggest  that  interested readers consult a specialist text - James and Webber is an excellent start, and also contains detailed sections on implementing models as well as a comparison of the different models themselves.

The  most  commonly  used  models  are  the  Vasicek  model  and  HullWhite type models, which are relatively straightforward to implement. The Hull-White and extended CIR models incorporate a mean reversion feature that means that they can be fitted to the term structure in place at the time. The CIR model has a square root factor in its volatility component, which prevents the short-term rate reaching negative values.

What criteria does a bank use in deciding which model to implement? Generally, a user will seek to implement a model that fits current market data, fits the process by which interest rates change over time, and is tractable. This means that it should be computationally efficient, and provide explicit solutions when used for pricing bonds and vanilla options.

## INTEREST RATE PROCESSES

Term structure models are essentially models of the interest rate process. The problem being posed is, what behaviour is exhibited by interest rates, and by the short-term interest rate in particular? The three most common processes that are used to describe the dynamics of the short-term rate are:

- ◾ the  Gaussian  or  normal  process: random  shifts  in  forward  rates  are normally  distributed  and  any  given  forward  rate  drifts  upward  at  a rate proportional to the initial time to the forward date. The interest rate volatility is independent of the current interest rate, and the volatility term has the form dW t ,  where W t is  a  generalised Weiner process or Brownian motion. An example of a Gaussian model is the Vasicek model;
- ◾ the square root or squared Gaussian process: the interest rate volatility is proportional to the square root of the current interest rate, so the volatility term is given by rdW t . An example of this is the CoxIngersoll-Ross model;
- ◾ the lognormal process: interest rate volatility is proportional to the current interest  rate,  with  the  volatility  term  described  by rdW t .  An example of this is the Black-Derman-Toy model.

To illustrate the differences, this means that if the current short-term rate  is  8%  and  is  assumed  to  have  an  annualised  volatility  of  100  basis points, and at some point in the future the short-term rate moves to 4%, under the Gaussian process the volatility at the new rate will remain at 100 basis points, the square root process will assume a volatility of 70.7 basis points, and the lognormal process will assume a volatility of 50 basis points.

The most straightforward models to implement are normal models, followed by square root models and then lognormal models. The process that is used will have an impact on the distribution of future interest rates predicted by the model. A generalised distribution is given at Figure 5.1.

Empirical studies have not pointed conclusively to one specific process as the most realistic. One study (BoE 1999), states that observation of interest rate behaviour in different markets suggests that when current interest rate  levels  are  low,  at  4%  or  below,  the  rate  process  has  tended  to  be  a Gaussian process, while when rates are relatively high, the process is more akin to a lognormal process. At levels between these two, it would seem that an 'intermediate' process is followed. However, these observations can be supported by economic argument. The nominal level of interest rates in an economy has two elements, a real interest rate and an inflation component.

Thus interest rate volatility arises as a result of real interest rate volatility and consumer prices volatility. When interest rates are low, the inflation  component is  negligible,  at  which  point  only  real  rate  volatility  has an  impact.  However,  as  real  rates  are  linked  to  the  rate  of  growth,  it  is reasonable to assume that they follow a normal distribution. An extreme case  has  occurred  in  some  markets  where  the  real  rates  on  index-linked bonds have occasionally been recorded as negative. When interest rates are

FIGURE 5.1 Distribution of future interest rates implied by different processes.

<!-- image -->

at relatively high levels, the inflation component is more significant, so that price   volatility is important. However, economic rationale suggests that the price of traded goods follows a lognormal distribution.

Where does this leave the thinking on interest rate models? As we demonstrate in the next section, one of the erstwhile potential drawbacks of Gaussian interest rate models is that they can result in negative forward rates. However, such a phenomenon is not completely unheard of, witness the long period of negative interest rates in the Eurozone after 2009, and so an environment of low interest rates is one that is best described by a Gaussian  process.  Pre-crash,  negative  interest  rates  were  observed  previously in the Japanese government bond repo market and certain other repo markets, and it is worth noting that rates in that country have been very low for some time now. Essentially then, a model that permits negative interest rates is not necessarily unrealistic. That said, outside of the specific security repo market, negative rates only persist when they are part of central bank monetary policy, so if a model is implying a negative forward rate in a jurisdiction where the central bank has stated that it is unlikely to pursue a negative base rate policy, then it is probably sensible to consider another model.

## ONE-FACTOR MODELS

A short rate model can be used to derive a complete term structure. We can illustrate this by showing how the model can be used to price discount bonds of any maturity. Let P t T , be the price of a risk-free zero-coupon bond at time t maturing at time T that has a maturity value of 1. This price is a random process, although we know that the price at time T will be 1. Assume that an investor holds this bond, which has been financed by borrowing funds of value Ct . Therefore, at any time t the value of the short cash position must be C P t T t , , otherwise there would be an arbitrage position. The value of the short cash position is growing at a rate dictated by the short-term risk-free rate r , and this rate is given by:

<!-- formula-not-decoded -->

By integrating this we obtain:

<!-- formula-not-decoded -->

which can be re-arranged to give:

<!-- formula-not-decoded -->

so that the random process on both sides is the same, hence their expected values are the same. This can be used to show that the price of the   zero-coupon bond at any point t is given by:

<!-- formula-not-decoded -->

Therefore, once we have a full description of the random behaviour of the short-rate r , we can calculate the price and yield of any zero-coupon bond at any time, by calculating this expected value. The implication is clear specifying the process r t determines the behaviour of the entire term structure, so if we wish to build a term structure model we need only (under these assumptions) specify the process for r t .

So now we have determined that a short-rate model is related to the dynamics of bond yields and therefore may be used to derive a complete term structure. We have also found that in the same way, the model can be used to value bonds of any maturity. Many models are one-factor models, which describe the process for the short-rate r in  terms  of  one  source  of uncertainty. This is used to capture the short-rate in the following form:

<!-- formula-not-decoded -->

where µ is the instantaneous drift rate and the standard deviation of the short rate r . Both these terms are assumed to be functions of the short-rate and independent over time. The key assumption made in a one-factor model is that all interest rates move in the same direction.

## THE VASICEK MODEL

In the Vasicek model (1977), the instantaneous short rate r is assumed to follow a stochastic process known as the Ornstein-Uhlenbeck process, a form of Gaussian process, described by (5.6):

<!-- formula-not-decoded -->

This  model  incorporates mean reversion ,  which  is  not  an  unrealistic feature. Mean reversion is the process that describes that when the shortrate r is high, it will tend to be pulled back towards the long-term average level. When the rate is low, it will have an upward drift towards the average level. In Vasicek's model, the short-rate is pulled to a mean level b at a rate of a . The mean reversion is governed by the stochastic term dW , which is normally distributed. Using (5.6), Vasicek shows that the price at time t of a zero-coupon bond of maturity T is given by:

<!-- formula-not-decoded -->

where r t is the value of r at time t ,

<!-- formula-not-decoded -->

and:

<!-- formula-not-decoded -->

It can be shown further that:

<!-- formula-not-decoded -->

which  describes  the  complete  term  structure  as  a  function  of r t with parameters  a,  b,  and  the  standard  deviation .  The  expression  at  (5.10) states  that r t T , is  a  linear  function  of r t ,  and  that  the  value  of r t determines the level of the term structure at time t .

Using the parameters described above, we can calculate the price function  for  a  risk-free  zero-coupon  bond.  Chan  et  al.  (1992)  used  the  following parameters: a long-run mean b of  0.07,  drift  rate a of  0.18,  and standard deviation of 0.02. Using these parameters, Figure 5.2 shows two zero-coupon bond price curves that result from two different initial short rates, r t 4% and r t 10%. The time to maturity T is measured on the x -axis, with the price of the zero-coupon bond with that time to maturity (a redemption value of 1) is measured along the y -axis.

FIGURE 5.2 Zero-coupon bond price curves at r t 0 04 . and r t 0 10 . .

<!-- image -->

For derived forward rates, the bond price function P t T , is continuously  differentiable  with  respect  to t .  Therefore,  the  model  produces  the following for the instantaneous forward rates:

<!-- formula-not-decoded -->

where f r T , is the function:

<!-- formula-not-decoded -->

The forward rate is a function of the short-rate and is normally distributed. Figure 5.3 shows the forward rate curves that correspond to the price curves in Figure 5.2, under the same parameters.

An increase in the initial short-rate r has the effect of raising forward rates, as does increasing the long-run mean value b . The effect of an increase in r is most pronounced at shorter maturities, whereas an increase in b has the  greatest  effect  the  longer  the  term  to  maturity.  An  equal  increase  or decrease in both r and b has the effect of moving all forward rates up or down by the same amount. With these changes, the forward curve moves up or down in a parallel fashion.

FIGURE 5.3 Forward rate curves with r t 0 04 . and r t 0 10 . .

<!-- image -->

The derived forward rate is a decreasing function of the instantaneous standard deviation , one of the model parameters. The partial derivative of the forward rate with respect to the standard deviation is given at (5.12):

<!-- formula-not-decoded -->

The expression at (5.12) states  that  the  forward  rate  is  a  decreasing function of T ,  that is it becomes more negative as T becomes larger. The effect of the standard deviation on the forward rate is shown in Figure 5.4, which shows the two forward rate curves from Figure 5.3, with two additional  forward  rate  curves  where  the  standard  deviation  has  been  raised from 0.02 to 0.06.

In describing the dynamics of the yield curve, the Vasicek model only captures changes in the short rate r , and not the long-run average rate b .

A point worth noting with this model is that as the short-rate follows a normal distribution, it has a positive probability of becoming negative at any point in time. This is common to all models that assume a Gaussian interest rate process, and although it may be considered a significant drawback, in fact it is only exhibited under extreme parameter values. For instance, in the example at Figure 5.3, the forward rates are not unusual, however, if we increase the standard deviation, the effect is to decrease forward rates, and this ultimately produces negative forward rates. For example, if we calculate the forward rates for a standard deviation 0 09 . , the result is to produce negative rates, as shown in Figure 5.5. A negative forward rate is equivalent to a zero-coupon bond price that decreases over time, which is clearly unrealistic under all but the most unusual and rare conditions (although, see Chapter 9). The reason that Gaussian interest rate models can produce

<!-- image -->

FIGURE 5.4 Forward rate curves standard deviations of 0.02 and 0.06.

<!-- image -->

-0.06

FIGURE 5.5 Forward rate curves under high standard deviation.

negative forward rates when the standard deviation is high is because the probability of achieving negative interest rates is high. Under certain parameter values, particularly under high values for the standard deviation, the probability of negative forward rates exists. However, we have seen that this is only under certain parameters, and in fact the presence of mean reversion makes this a low possibility.

It  may  be  considered  more  realistic  to  consider  that  there  are  no constant  parameters  for  the  drift  rate  and  the  standard  deviation  that would ensure that the price of a zero-coupon bond at any time is exactly the same as that suggested by observed market yields. For this reason, a modified version of the Vasicek model has been described by Hull and White (1990), known as the Hull-White or extended Vasicek, which we consider later.

## THE MERTON MODEL

In Merton's model (1971), the interest rate process is assumed to be a generalised Weiner process, described by (5.13) below:

<!-- formula-not-decoded -->

which, in differential form is given by (5.14):

<!-- formula-not-decoded -->

For ≤ ≤ 0 t T we obtain:

<!-- formula-not-decoded -->

The distribution of r T is normal with a mean of r t T t and standard deviation of T t .

For a fixed term to maturity T , the forward rate f r t T t , is an Itô process of the form:

<!-- formula-not-decoded -->

The continuously compounded yield at time t of a risk-free zero-coupon bond paying 1 on maturity at time T is given by:

<!-- formula-not-decoded -->

where R is the function:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The  average  future  interest  rate  over  the  time  period t T , ,  is  given by (5.19):

<!-- formula-not-decoded -->

In the Merton model, forward rates are always negative at long maturities, unlike the Vasicek model where there is a range of parameters under which  the  forward  rates  are  positive  at  all  maturities.  This  is  because although in both models the forward rate is negatively affected by the standard deviation of the future interest rate, which is an increasing function of the time to maturity, in the model it changes in a linear fashion to infinity, whereas in the Vasicek model it grows to a finite limit. Therefore, the standard deviation is more powerful in the Merton model, and it results in the forward rates being negative at long maturities.

## THE COX-INGERSOLL-ROSS MODEL

From the previous section, we see that under a model that assumes the short rate to follow a normal distribution there is the possibility of negative forward rates. The Cox-Ingersoll-Ross model (1985) is a one-factor model and as originally presented, removed the possibility of negative rates. Under the CIR model, the dynamics of the short rate are described by (5.20):

<!-- formula-not-decoded -->

which, like Vasicek, also captures a mean-reverting phenomenon. However, the stochastic term has a standard deviation that is proportional to r . This is a significant difference because it states that as the short rate increases, the standard deviation will increase. This means that forward rates will be positive. In the CIR model, the price of a risk-free zero-coupon bond is given by:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The long-term interest rate R t T , is a function of the short-term rate r t , so that the short-term rate only is all that is required to fit the entire term structure.

where:

and:

## ARBITRAGE-FREE MODELS

An equilibrium model of the term structure, of which we reviewed three in the previous section, is a model that is derived from (or consistent with) a general equilibrium model of the economy. They use generally constant parameters, including, most crucially, a constant volatility, and the actual parameters used are often calculated from historical time series data. Banks commonly also use parameters that are  calculated  from  actual  data  and implied volatilities, which are obtained from the price of exchange-traded option contracts.

An arbitrage-free model of the term structure on the other hand, can be made to fit precisely with the current, observed term structure, so that observed bond yields are in fact equal to the bond yields calculated by the model.  So  an  arbitrage-free  model  is  intended  to  be  consistent  with  the currently  observed  zero-coupon  yield  curve,  and  the  short  rate  drift  rate is dependent on time, because the future average path taken by the short rate is determined by the shape of the initial yield curve. This means that in a positively sloping yield curve environment, the short rate r increases, on average, while it decreases in an initial inverted yield curve environment. In a humped initial yield curve environment, the expected short rate path is also humped. In an equilibrium model, the drift term for the short rate (that is, the coefficient of the dt term given above) is not dependent on time.

In theory, the price predicted by any model, if it is observed in the market, renders that model to be arbitrage-free. However, arbitrage-free models are called this because they compare the model-predicted price to the actual market price. In an equilibrium model, the initial term structure is a product of the model, while in an arbitrage-free model the actual term structure is an input to the model in the first place. In practice, an equilibrium model may not be arbitrage-free under certain conditions, namely it may show small errors at particular points along the curve, or it may feature a large error across the whole term structure. The most fundamental issue in this regard is that the concept of the risk-free short-term interest rate is difficult to identify as an actual interest rate in the money market. In practice, there may be more than one interest rate that presents itself, for example, the T-bill rate or the same maturity government bond repo rate, however, this remains an issue.

For these reasons, practitioners prefer to use an arbitrage-free model if  one can be successfully implemented and calibrated. This is not always straightforward, and under certain conditions it is easier to implement an equilibrium multi-factor model (which we discuss in the next section), than it is to implement a multi-factor arbitrage-free model. Under one particular set of circumstances, however, it is always preferable to use an equilibrium model, and that is when reliable market data is not available. If modelling the term structure in a developing or 'emerging' bond market, it is more efficient to use an equilibrium model.

Note that some texts have suggested that equilibrium models can be converted into arbitrage-free models by making the short rate drift rate time dependent. However, this may change the whole nature of the model, presenting problems in calibration.

## THE HO AND LEE MODEL

The Ho-Lee model (1986) was one of the first arbitrage-free models and was presented using a binomial lattice approach, with two parameters - the standard deviation of the short rate, and the risk premium of the short rate. be the equilibrium is a discount function describing the entire term structure of interest rates,

We summarise it here. Following Ho and Lee, let P i n price of a zero-coupon bond maturing at time T under state i . That is P i n and will satisfy the following conditions:

<!-- formula-not-decoded -->

To  describe  the  binomial  lattice,  we  denote  the  price  at  the  initial time 0 as:

<!-- formula-not-decoded -->

At time 1, the discount function is specified by two possible functions P 1 1 0   and P 1 1 0 ,  which  correspond  respectively  to  the  upside  and  the downside outcomes. Therefore at time n the binomial process is given by the discount function P i n , which can move upward to a function P i n 1 1 and downwards to a function P i n 1 for i 0 to n .

As described by Ho and Lee, there are two functions denoted h T and h T * that describe the upstate and downstate as (5.22) and (5.23) respectively, below:

<!-- formula-not-decoded -->

with h H o * 0 1.

The two functions specify the deviations of the discount functions from the  implied  forward  functions.  To  satisfy  arbitrage-free  conditions,  they define  an  implied  binomial  probability π that  is  independent  of  time T , while the initial discount function P T is given by:

<!-- formula-not-decoded -->

and:

<!-- formula-not-decoded -->

Equation (5.25) shows that the bond price is equal to the expected value of the bond, discounted at the prevailing one-period rate. Therefore π is the implied risk-neutral probability.

The assumption that the discount function evolves from one state to another as a function only of the number of upward and downward movements is equivalent to the assumption that a downward movement followed by an upward movement is equivalent to an upward movement followed by a downward movement. This produces the values for h and h *  given by (5.26) and (5.27):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where is the interest rate spread.

It  has  been  shown  that  the  model  describes  a  continuous  time  process given by:

<!-- formula-not-decoded -->

where is the constant instantaneous standard deviation of the short rate and t is a time-dependent function that describes the short rate process and fits the model to the current observed term structure. This term defines the average direction that the short rate moves at time t , which is independent of the short rate. The variable t is given by:

<!-- formula-not-decoded -->

where f t 0, is the instantaneous forward rate for the period t at time 0. In fact, the t approximates to f t 0, which states that the average direction of the short rate in the future is given by the slope of the instantaneous forward curve.

The Ho and Lee model is straightforward to implement and is convenient because it uses the information available from the current term structure, so that it produces a model that precisely fits the current term structure. It also requires only two parameters. However, it assigns the same volatility to  all  spot  and  forward  rates,  so  the  volatility  structure  is  restrictive  for some market participants. In addition, the model does not incorporate mean reversion.

## THE HULL-WHITE MODEL

The Hull-White model (1990) is an extension of the Vasicek model designed to produce a precise fit with the current term structure of rates. It is also known as the extended Vasicek model ,  with  the  interest  rate  following  a process described by (5.30):

<!-- formula-not-decoded -->

It can also be written as:

<!-- formula-not-decoded -->

where a is the mean reversion rate and a and s are constants. It has been described as a Vasicek model with a time-dependent reversion level. The model  is  also  called  the  general  Hull-White  model,  while  a  special  case where a constant  is  known  as  the  simplified  Hull-White  model.  In  the Vasicek model, a constant and ab where b is constant.

The Hull-White model can be fitted to an initial term structure, and also a volatility term structure. A comprehensive analysis is given in Pelsser (1996) as well as James and Webber (2000).

It can be shown that:

<!-- formula-not-decoded -->

where the process K is given by:

<!-- formula-not-decoded -->

To calculate the price of a zero-coupon bond, the first step is to calculate the integral:

<!-- formula-not-decoded -->

which follows a normal distribution with mean m r t t T , ; and standard deviation v t T ; . The price of a bond is given by (5.33) below:

<!-- formula-not-decoded -->

where P r t t T , ; is the function:

<!-- formula-not-decoded -->

The price of a zero-coupon discount at time t is defined in terms of the short-rate r at time t and the current term structure. The price function is not static, and the price of a bond at time t that matures at time T is a function of the short rate, as we have noted, and separately of the time t .

The volatility  of  the  bond  price  is  given  by  the  function B t T t ; where B is defined as:

<!-- formula-not-decoded -->

The bond price volatility is a deterministic function of t . The 'pull to par'  of  the  zero-coupon  bond  is  captured  by  the  fact  that  the  volatility reduces to zero as t approaches T , as along as is continuous at t . As the mean m is normally distributed, it follows that the bond price is lognormally distributed, so therefore the function:

<!-- formula-not-decoded -->

where the function A t T , is defined by:

<!-- formula-not-decoded -->

The price function above can be continuously differentiated as a function of t . Therefore the forward rate is given by (5.36) below:

<!-- formula-not-decoded -->

where f r t T , ; is defined by the function below:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The forward rate function f at time t is not static and is a function of the short rate r at time t , the time t , and the time to maturity to time T . The Hull-White model can be calibrated in terms of the forward rate f . That is, at time t the information required to implement this is the short rate r t , the standard deviation s of the short rate, the forward rate f and the standard deviations B t T t T , , of the forward rates at time t . If the forward rates are known in a form that allows their first differential to be calculated with respect to t , using the other information it is possible to calculate the function BT , the derivative of this function, and then the value for a t using the relationship at (5.38) below:

<!-- formula-not-decoded -->

which describes the volatility of the bond price as a function of the maturity date T.

The continuously compounded yield of a zero-coupon bond at time t that matures at time T is given by (5.39):

<!-- formula-not-decoded -->

where R is given by the function shown at (5.40):

<!-- formula-not-decoded -->

Like the bond price function, the yield on a zero-coupon bond is a function of the short rate r and follows a normal distribution and the yield curve is a function of the short rate r , the time t and the time to maturity T . The long-term average future interest over the time to maturity t T , is normally distributed and given by:

<!-- formula-not-decoded -->

## THE BLACK-DERMAN-TOY MODEL

In the models we have reviewed in this chapter, there has only been one function of time, the parameter . In certain models, either or both of the parameters a and are also made to be functions of time. In their 1990 paper, Black, Derman and Toy (BDT) proposed a binomial lattice model that is described by (5.42) below:

<!-- formula-not-decoded -->

where t is the partial derivative of with respect to time t . The BDT model is a lognormal model, which means that the short-term rate volatility is proportional to the instantaneous short rate, so that the ratio of the volatility to the rate level is constant. The drift term is more complex than that described in the earlier models, and so the BDT model requires numerical fitting to the observed current interest rate and volatility term structures. That is, the drift term is not calculated analytically. The short rate volatility is also linked to the mean reversion such that where long-term rates are les volatile than short-term rates, the short rate volatility decreases in the longterm. A later model developed by Black and Karasinski (1992) removed the relationship between mean reversion and the volatility level. This is given at (5.43) below:

<!-- formula-not-decoded -->

As with the previous models, the key factor is the short rate. Using the binomial tree approach, a one-step tree is used to derive the current short rate to the short rates one period in the future. These derived rates are then used to derive rates two periods away, and so on.

## FITTING THE MODEL

Implementing an interest rate model requires the input of the term structure yields and volatility parameters, which is the process of calibrating the model. The process of fitting the model is called calibration. This can be done in at least three ways, which are:

- ◾ calibration to the current spot rate yield curve, using a pre-specified volatility level and not the volatility values given by the prices of exchangetraded options. This may result in mispriced bonds and options if the selected volatilities are not accurate;
- ◾ calibration  to  the  current  spot  rate  curve  and  using  the  volatilities implied by the prices of exchange-traded options; therefore the model is  implemented  using  volatility  parameters  that  are  exactly  the  same as those implied by the traded option prices. In practice, this may be a lengthy process;
- ◾ calibrating  the  model  to  the  current  spot  rate  curve,  using  volatility parameters  that  are  approximately  close  enough  to  result  in  prices that are near to those of observed exchange-traded options. This is the method that is usually followed.

Generally,  volatility  values  for  the  different  period  interest  rates  are taken from the volatilities of exchange-traded options. However, where great accuracy is not required, for example, for regulatory capital purposes, practitioners may use the first method, while for the purposes of fixed income research, the third method is suitable. In both the second and third methods there is the danger that calibrating the model to option prices will result in error simply because the options are mispriced. This is quite possible if using long-dated and/or OTC options, which frequently differ in price according to which bank is pricing them.

In any case, a model usually therefore uses volatility inputs from option prices for a range of options that range in maturity from the shortest period to the longest in the term structure. To test the accuracy of the model, one can use the expression at (5.44):

<!-- formula-not-decoded -->

where p n is the observed price of the n 'th option and P n is the price of the option as calculated by the model, and N options have been used to calibrate the model. A model that has the lowest value given by (5.44) can be considered to be the most accurate. In deciding which option products should be used to calibrate the model, care should be taken to use instruments that are most similar to the instrument that is being priced by the model.

The different models lend themselves to a particular calibration method. In the Ho-Lee model, only parallel yield curve shifts are captured and the current yield curve is a direct input, therefore a constant volatility parameter is used. This implies that all the forward rate implied volatilities are identical.  In  practice,  this  is  not  necessarily  realistic,  as  long-dated bond prices often experience lower volatility than short-dated bond prices. The model also assumes that volatility is a decreasing function of the time to maturity, which may also be unrealistic. Models that incorporate mean reversion can be implemented with more realistic volatility parameters, as it is the mean reversion effect that results in long-dated bonds having lower volatilities. Therefore  a  mean-reverting  model  can  be  implemented  more  accurately using the second or third methods described above.

Let  us  consider  the  issues  involved  in  fitting  the  extended  Vasicek model or Hull-White model. This describes the short rate process as following the form:

<!-- formula-not-decoded -->

In implementing this model, there are three possible approaches. The model can be calibrated by keeping and a constant and calibrating the standard deviation parameter. This means that the model is fitted to the current yield curve and the volatility value is adjusted to that required to produce the observed curve. However, this may result in high volatility values, which rise by a squared function, and therefore is not realistic. The second method is to calibrate , keeping the other two parameters constant. This is adjusting the mean reversion rate in order to fit the derived curve with the observed curve. The resulting derived yield curve will be a function of the current short rate and the mean reversion rate. This method is sometimes applied in practice, although it can result in inaccurate volatility levels for long-dated bonds, because large adjustments in the mean reversion rate are needed to fit the derived curve to the long-dated part of the observed curve. The third approach is to calibrate ar ,  keeping  the  other  parameters  constant. This produces a stable yield curve and is most commonly followed by practitioners in the market.

## SUMMARY

In  this  chapter,  we  have  considered  both  equilibrium  and  arbitrage-free  interest rate models. These are one-factor Gaussian models of the term structure of interest rates. We have seen that in order to specify a term structure model, the dynamics of the price process are described, and this is then used to price a zero-coupon bond. The short rate that is modelled is assumed to be a risk-free interest rate, and once this is modelled, we can derive the forward rate and the yield of a zero-coupon bond, as well as its price. So it is possible to model the entire forward rate curve as a function of the current short rate only, in the Vasicek and Cox-Ingersoll-Ross models, among others. Both the Vasicek and Merton models assume constant parameters, and because of equal probabilities of forward rates and the assumption of a normal distribution, they can, under certain conditions relating to the level of the standard deviation, produce negative forward rates.

The models are based on the fact that the price of a bond, which exhibits a pull-to-par effect, and the forward rate, are both Itô processes. For the bond price, the relative drift is the interest rate, and is deterministic, as is the forward rate. The bond price, yield, and forward rate are functions of the current short rate, and follow a normal distribution. An increase in the short rate results in a rise in the forward rates, and this is more pronounced for the shortest maturity rates. The instantaneous volatility of the forward rates decreases with decreasing time to maturity, and approaches the volatility of the current short-rate at time t .

The Vasicek, Cox-Ingersoll-Ross, Hull-White, and other models incorporate mean reversion. As the time to maturity increases and as it approaches infinity, the forward rates converge to a point at the long-term mean reversion level of the current short rate. This is the limiting level of the forward rate and is a function of the volatility  of  the  current  short  rate. As  the  time  to  maturity  approaches  zero,  the short-term forward rate converges to the same level as the instantaneous short rate. In the Merton and Vasicek models, the mean of the short rate over the maturity period T , is assumed to be constant. The same constant for the mean, or the drift of the interest rate, is described in the Ho-Lee model, but not the extended Vasicek or Hull-White model.

We have also noted that the efficacy of a model is not necessarily solely related to how realistic its assumptions might be, but how straightforward it is to implement in practice, that is, the ease with which it may be calibrated.

## SELECTED BIBLIOGRAPHY AND REFERENCES

Baxter, M. and Rennie, A., Financial Calculus, Cambridge University Press, 1996. Black, F., Derman, E. and Toy, W., 'A one-factor model of interest rates and its application to Treasury bond options', Financial Analysts Journal, Jan-Feb 1990, pp. 33-39.

Black, R. and Karasinski, P., 'Bond and option prices when short rates are lognormal', Financial Analysts Journal , Ju1-Aug 1991, pp. 52-59.

- Chan, K., et al., 'An empirical comparison of alternative models of the short-term interest rate', Journal of Finance 47, 1992, pp. 1209-1227.
- Cox, J., Ingersoll, J. and Ross, S., 'A theory of the term structure of interest rates', Econometrica 53, 1985, pp. 385-407.
- Duffie, D., Dynamic Asset Pricing Theory, 2nd edition, Princeton University Press, 1996.
- Ho, T. and Lee, S., 'Term structure movements and pricing interest rate contingent claims', Journal of Finance 41, 1986, pp. 1011-1029.
- Hull, J. and White, A., 'Pricing interest-rate derivative securities', Review of Financial Studies 3, 1990, pp. 573-592.
- James, J. and Webber, N., Interest Rate Modelling, Wiley, 2000.
- Jamshidian, F., 'Bond, futures and option valuation in the quadratic interest rate model', Applied Mathematical Finance 3, 1996, pp. 93-115.
- Jarrow, R., Modelling Fixed Income Securities and Interest Rate Options, McGraw-Hill, 1996.
- Merton, R., 'Optimum consumption and portfolio rules in a continuous time model', Journal of Economic Theory 3, 1971, pp. 373-413.
- Merton, R., 'Theory of option pricing', Bell Journal of Economics and Management Science 4, 1973, pp. 141-183.
- Pelsser, A., 'Efficient methods for valuing and managing interest rate and other derivative securities', PhD thesis, Erasmus University, Rotterdam, 1996.
- Pliska, S., 'A stochastic calculus model of continuous trading: optimal portfolios', Mathematics of Operations Research II, 1986, pp. 371-382.
- Rogers, L., 'Which model for the term-structure of interest rates should one use?' in Davis, M., et al. (ed.), Mathematical Finance, Springer-Verlag, 1995, pp. 93-115.
- Rebonato, R., Interest Rate Option Models, 2nd edition, Wiley, 1998.
- Steeley, J., 'Estimating the gilt-edged term structure: basis splines and confidence intervals', Journal of Business Finance and Accounting 18, 1991, pp. 513-530.
- Vasicek, O., 'An equilibrium characterization of the term structure', Journal of Financial Economics 5, 1977, pp. 177-188.

I had the good fortune to have grown up under several outstanding leaders who had given me a lot of hands-on experience with people and technically complex missions. I didn't have . . . innate talent, so I surrounded myself with smart people and relied on them to work with me as a team to get the job done. My credo: always hire people who are smarter and better than you are, and learn with them.

-- Gene Kranz, Failure Is Not An Option: Mission Control from Mercury to Apollo 13 and Beyond , New York, NY: Berkley Books, 2000

## CHAPTER  6

## Interest Rate Models II

I n this chapter, we consider multi-factor and whole yield curve models. As  we  noted  in  the  previous  chapter,  short  rate  models  have  certain drawbacks, which though not necessarily limiting their usefulness, do not accommodate later developments. The potential shortcoming is that, as the single short rate is used to derive the complete term structure, in practice this can be unsuitable for the calculation of longer-dated bond yields. In this situation, it becomes difficult to visualise the actual dynamics of the yield curve, and the model no longer fits observed changes in the curve. This means that the accuracy of the model cannot be observed. Another drawback is that in certain equilibrium model cases, the model cannot be fitted precisely to the observed yield curve, as it has constant parameters. In these cases,   calibration of the model is on a 'goodness of fit' or 'best fit' approach.

In response to these issues, interest rate models have been developed that  model  the  entire  yield  curve.  In  a  whole  yield  curve,  the  dynamics of  the  entire  term  structure  are  modelled.  In  this  case,  the  volatility  of the term structure is given by a specified function, which may be a function of time, term to maturity or zero-coupon rates. A simple approach is described in the Ho-Lee model, in which the volatility of the term structure is a parallel shift in the yield curve, the extent of which is independent of the current time and the level of current interest rates. The Ho-Lee model is not widely used, however it is the basis for the Heath-Jarrow-Morton (HJM) model, which is widely used. The HJM model describes a process whereby the whole yield curve evolves simultaneously, in accordance with a set of volatility term structures. The model is usually identified as being the one that describes the evolution of the forward rate, however, it can also be expressed in terms of the spot rate or of bond prices (see for example, James and Webber 2000, Chapter 8). For a more detailed description of the HJM framework, refer to Baxter and Rennie (1996), Hull (1997), Rebonato (1998), Bjork (1998), and James and Webber (2000). Baxter and Rennie is very accessible, while Neftci (1996) is an excellent introduction to the mathematical background.

## MULTI-FACTOR TERM STRUCTURE MODELS

In  seeking  to  develop  a  model  for  the  entire  term  structure,  the  requirement is to model the behaviour of the entire forward yield curve, that is the behaviour of the forward short rate f t T , for all forward dates T . Therefore, we require the random process f T for  all  forward dates T .  Given this, it can be shown that the yield R on a T -maturity zero-coupon bond at time t is the average of the forward rates at that time on all the forward dates s between t and T , given by (6.1) below:

<!-- formula-not-decoded -->

To model the complete curve it is necessary to specify a drift rate and volatility level for f t T , for each T .

The single-factor HJM model specifies the forward rate process for each maturity T , given an initial forward rate curve f T 0, as:

<!-- formula-not-decoded -->

in differential form, or as a stochastic integral in the form:

<!-- formula-not-decoded -->

where the volatility and drift parameters t T , and t T , can be dependent on the rates as well as the history of the Brownian motion Wt .

A general multi-factor complete yield curve model is described by Heath, Jarrow, and Morton (1992). In theory, the HJM approach is ideal because it models not only the short rate but longer-term rates as well, and the model inputs are the current term structure, and volatility term structure for each independent change in the yield curve. However, the model must analyse a  considerable  amount  of  information,  which  slows  down  the  modelling process and hinders model effectiveness. We shall consider these issues later. The simplest version of the HJM approach is that presented by Cheyette (1992) and Ritchken and Sankarasubramanian (1995), also referred to as a two-state Markov model. In this model, the volatility of the short rate is dependent on the time t and the level of the rate r , and the forward rate f t T , is a function of the term to maturity T . Hence the volatility of the forward rate is described by (6.4):

<!-- formula-not-decoded -->

where r t r t t , , , is the volatility of the short rate and k t is the mean reversion or the rate of decrease of the volatility of the forward rate, which decreases with increasing term to maturity. Thus in this model the derivation of forward rates is a function of the current short rate (and the slope of the forward curve at the current time), and the level of volatility of the forward rate at the time of T ,  at  which point it is now the short rate. The model describes the dynamics of these two variables in the form given by (6.5):

<!-- formula-not-decoded -->

where r t r t f t 0, is  the  deviation  of  the  short  rate  from  the  forward rate curve at the current time. The variable V t has an initial value of zero and does not follow a stochastic process and integrating it results in (6.6) below:

<!-- formula-not-decoded -->

where there are s forward dates between t and T . Therefore the forward rate curve is given by:

<!-- formula-not-decoded -->

where:

<!-- formula-not-decoded -->

and is a deterministic function.

Therefore in this model in order to derive the complete forward rate curve, only the two variables detailed above are required.

## THE MULTI-FACTOR HEATH-JARROW-MORTON MODEL

A multi-factor model of the whole yield curve has been presented by Heath, Jarrow and Morton (1992). 1  The approach models the forward curve as a process arising from the entire initial yield curve, rather than the short rate only. The spot rate is a stochastic process and the derived yield curve is a function of a number of stochastic factors. The HJM model uses the current yield curve and forward rate curve, and then specifies a continuous time stochastic process to describe the evolution of the yield curve over a specified time period.

The model is summarised here only - readers interested in the derivation of the model are directed to the original paper or a discussion of it in Baxter and Rennie (1996), Hull (1997), or James and Webber (2000). To describe the model, we use the following notation:

- t T , is the trading interval for a fixed period from t to T , where t 0;
- W t is  the  independent  Brownian  motion  or Weiner  process  that describes the interest rate process;
- , , F Q is the probability space where F is the -algebra representing measurable events and Q is the measure of probability;
- P t T , is  the  price  at  time t of  a  zero-coupon  bond  that  matures at time T .

The bond has a redemption value of 1 at time T . The instantaneous forward rate f t T , at time t is given by (6.9):

<!-- formula-not-decoded -->

and describes the interest rate that is applicable on a default-free loan at time t for the period from T to a point one instant later. In their paper, Heath, Jarrow, and Morton state that the solution to the differential equation of (6.8), results in the expression for the price of the bond, shown at (6.10):

<!-- formula-not-decoded -->

1   Heath, D., Jarrow, R., and Morton, A., 'Bond pricing and the term structure of interest rates: a new methodology', Econometrica 60(1), 1992, pp. 77-105.

while the spot interest rate at time t is the instantaneous forward rate at time t for maturity date t , shown by:

<!-- formula-not-decoded -->

We  now  describe  the  model's  exposition  of  movements  in  the  term structure.

The HJM model describes the evolution of forward rates given an initial forward rate curve, which is taken as given. For the period T t 0, the forward rate f t T , satisfies the equation at (6.11):

<!-- formula-not-decoded -->

The expression describes a stochastic process composed of n independent Weiner processes, from which the whole forward rate curve, from the initial curve at time 0, is derived. Each individual forward rate maturity is a function of a specific volatility coefficient. The volatility values i t T , , are not specified in the model and are dependent on historical Weiner processes. From (6.11) following the HJM model, the spot rate stochastic process is given by (6.12) below:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

for the period t T 0, .

The model then goes to show that the process of changes in the bond price is given by:

<!-- formula-not-decoded -->

where:

and:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The expression at (6.13) describes the dynamics of the bond price as a continuous stochastic process with a drift of r t b t T , , , , and a volatility value of a t T i , , .

The no-arbitrage condition is set by defining the price of a zero-coupon bond that matures at time T in  terms  of  an 'accumulation factor' B t , which is the value of a money market account that is invested at time 0 and reinvested at time t at an interest rate of r t . This accumulation factor is defined as (6.14):

<!-- formula-not-decoded -->

and  the  value  of  the  zero-coupon  bond  in  terms  of  this  accumulation factor is:

<!-- formula-not-decoded -->

for the period T t 0, and t T 0, .

Following HJM, by applying Itô's lemma the model obtains the following result for Z t T , , shown at (6.15):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In the HJM model, the processes for the bond price and the spot rate are not independent of each other. As an arbitrage-free pricing model it differs in crucial respects from the equilibrium models presented in the previous chapter. The core of the HJM model is that given a current forward rate curve, and a function capturing the dynamics of the forward rate process, it

models an entire term structure.

A drawback of the model is that it requires the input of instantaneous forward rates,  which  cannot  necessarily  be  observed  directly  in  the  market. Models have been developed that are in the HJM approach that take this factor into account, including those presented by Brace, Gatarek, and Musiela (1997), and Jamshidian (1997). This family of models is known as the LIBOR market model or the BGM model. In the BGM model, there is initially one factor, the forward rate f t , which is the rate applicable from time t k to time t k 1 at time t . The forward rate is described by (6.16):

<!-- formula-not-decoded -->

where the market is assumed to be forward risk-neutral.

The relationship between forward rates and the price of a zero-coupon bond at time t is given by (6.17):

<!-- formula-not-decoded -->

where i is the compounding period between t and t i 1 .

To determine the volatility of the zero-coupon bond price v t at time t , it can be shown that by applying Itô's lemma to (6.17), we obtain:

<!-- formula-not-decoded -->

It is possible to extend the BGM model to incorporate more independent factors.

## JUMP MODELS

There is a category of models that attempts to describe the jump feature of asset prices and interest rates. Observation of the markets confirms that many asset price patterns and interest rate changes do not move continuously  from  one  price  (interest  rate)  to  another,  but  sometimes  follow  a series of jumps. A good example of a jump movement is when a central bank changes the base interest rate;  when  this  happens,  the  entire  yield curve shifts to incorporate the effect of the new base rate. There is a considerable body of literature on the subject, and we only refer to a small number of texts here.

One type of jump model is the jump-augmented HJM model, described in  Jarrow and Madan (1991), Bjork (1996), and Das (1997). This is not described here because we have not covered the necessary technical background. Another is the jump-augmented Vasicek model described by Das and Foresi (1996), and Baz and Das (1996). In this, the short rate process is captured by:

<!-- formula-not-decoded -->

where Nt is a Poisson process with a constant intensity and J is a random jump size.

Other  jump  models  have  been  described  by  Attari  (1999),  Das  and Foresi (1996), and Honore (1998).

## ASSESSING ONE-FACTOR AND MULTI-FACTOR MODELS

In assessing the value of the different models that have been developed and the efficacy of each, what is important is how they can be applied in the market, rather than any notion that multi-factor models are necessarily 'better' than one-factor models because they are somehow more 'realworld'. What is required is a mechanism that efficiently prices bonds and interest rate options. A term structure model attempts to accomplish this by describing the dynamics of the interest rate process and generating random interest rate paths. The generated paths are then used to discount the cash flows from the fixed income instrument, having initially been used to generate the cash flows in the first place. In practice, a one-factor model that has been accurately calibrated values fixed income instruments efficiently. This is because of the determinants of bond pricing. To illustrate, consider a fixed income instrument with a fixed maturity date. To value such a bond at a particular time, we need only know the bond yield at that time, and this is essentially a one-factor process. Similarly for a callable bond - when generating its cash flow, we will know whether it will be called by knowing its price at a future date. Generating this cash flow from the interest rate model is again a one-factor process. Therefore if we are pricing a bond, the dynamics of the price process can be adequately described using (6.20):

<!-- formula-not-decoded -->

which is  the  process  followed  by,  for  example,  the  Black-Scholes  option model when used to price an interest rate option. This model does not discount the forward price of the option, which is the second part of the B-S approach, assuming a single continuously compounded short-term risk-free interest rate.

While this approach works in practice, it only applies to a single security portfolio - it would be unwieldy and inaccurate for valuing a number of securities. As banks and market-makers must value many hundreds of cash and derivative instruments, another approach is required. This other approach was considered earlier in this chapter and involves describing the dynamics of the bond price process in the form of a term structure model. Under this situation, a multi-factor model may be more suitable,   particularly when used to value options.

To consider one-factor models then, we know that the yield of a bond at a future date is essentially a one-factor process, so a one-factor model may well be accurate. A one-factor model describes only parallel shift yield changes, and it assumes that bond yields and discount rates are perfectly correlated, so that it will not generate all the possible paths of the future discount rate. In practice, however, much yield curve movement is close to a parallel shift, so this may not be as much of a problem for the majority of situations. If a term structure model accurately reflects the random evolution of the price of a bond, and the actual current rate and forward rate volatilities of the bond are as generated by the model, then the model can be considered effective, and it will generate reasonable cash flow scenarios and with accurate probabilities. It is possible to achieve this with onefactor models. Essentially then, a bank can use a one-factor model when conditions are appropriate, and need only use a multi-factor model where the one-factor model cannot be expected to be accurate. That said, why not simply use a multi-factor model at all times? The main reason is because generating  forward  rates  and  valuations  from  a  multi-factor  model  is  a time-consuming process, requiring more computing power, and as rapidity of analysis and response may be of the essence in the markets, it is logical to use a slower model only when it is significantly more accurate than the one-factor model.

It is generally accepted that one-factor models can be used for most bond applications.  Multi-factor  models  are  more  appropriate  in  the    following situations:

- ◾ where the instrument being valued is linked to two different interest rates, for example, an interest rate quanto option, or an option with a payoff profile that is a function of the spread between two different reference rates;
- ◾ for the valuation of long-dated options or deeply in-the-money or outof-the-money options, which are affected by the volatility 'smile'. As a  stochastic  volatility  factor  impacts  the  price,  a  model  that  assumes constant volatilities is inaccurate;
- ◾ for  the  valuation  of  securities  that  are  to  some  extent  reflected  in the  slope  of  the  yield  curve,  such  as  certain  mortgage-backed  bonds whose level of prepayment is sometimes a function of the slope of the yield curve;
- ◾ for the valuation of very long-dated options, where all possible paths of the future discount rate may be required.

The optimum approach appears to be a combination of a one-factor model and a multi-factor model to suit individual requirements. However, this may not be practical - it might not be ideal to have different parts of a bank using different models (although of course this happens frequently, the larger investment banks use a large number of models) and valuing instruments using different models. The key factors to focus on are accessibility, accuracy, appropriateness, and speed of computation.

## CHOOSING A TERM STRUCTURE MODEL

The  selection  of  an  appropriate  term  structure  model  is  as  much  art  as science. The different types of model available, and the different applications and user requirements, mean that it is not necessarily clear-cut which approach should be selected. For example, a practitioner's requirements will determine whether a single-factor model or a two- or multi-factor model is more appropriate. The Ho-Lee and BDT models, for example, are arbitrage models, which means that they are designed to match the current term structure. With arbitrage (or arbitrage-free) models, assuming that the specification of the evolution of the short rate is correct, the law of no-arbitrage can be used to determine the price of interest rate derivatives. There is also a class of interest rate models known as equilibrium models, which make an assumption of the dynamics of the short rate in the same way as arbitrage models do, but are not designed to match the current term structure. With equilibrium models, therefore, the price of zero-coupon bonds given by the model-derived term structure is not required to (and does not) match prices seen in the market. This means that the prices of bonds and interest rate derivatives are not given purely by the short rate process. Overall then, arbitrage models take the current yield curve as described by the market prices of default-free bonds as given, whereas equilibrium models do not.

What considerations must be taken into account when deciding which term structure model to use? Some of the key factors include:

- ◾ Ease of application. The key input to arbitrage models is the current spot rate term structure, which is straightforward to determine using the market price of bonds currently trading in the market. This is an advantage over equilibrium models, where the inputs are more difficult to obtain.
- ◾ Capturing market imperfections. The  term  structure  generated  by  an arbitrage model reflects the current market term structure, which may include pricing irregularities due to liquidity and other considerations. If this is not desired, it is a weakness of the arbitrage approach. Equilibrium models do not reflect pricing imperfections.
- ◾ Pricing  bonds  and  interest  rate  derivatives. Traditional  'seat-of-thepants' market-making used to employ a combination of the trader's expertise, the range of prices observed in the market (often from interdealer broker screens) and 'gut feeling' to price bonds. 2  For a more

2   Typified par excellence by the lads at Hoare Govett Securities Ltd during the author's time there. He observed rather less of this approach subsequently at JPMorgan Chase Bank, KBC Financial Products and The Royal Bank of Scotland though . . .!

scientific approach or for relative-value trading, 3  a yield curve model may well be desirable. In this case, an equilibrium model is the preferred model, as the trader will want to compare the theoretical price given by the model to the actual price observed in the market. An arbitrage model is not appropriate because it takes the observed yield curve, and hence the market bond price, as given, and therefore assumes that the  market  bond  prices  are  correct.  Put  another  way,  using  an  arbitrage model for relative-value trading suggests to the trader that there is no gain to be made from entering into say, a yield curve spread trade. Pricing derivative instruments such as interest rate options or swaptions requires a different emphasis. This is because the primary consideration of the derivative market-maker is the technique and price of hedging the derivative. That is, upon writing a derivative contract, the marketmaker simultaneously hedges the exposure using either the underlying asset or a combination of this and other derivatives such as exchangetraded futures. The derivative market-maker generates profit through extracting premium and from the difference in price over time between the price of the derivative and the underlying hedge position. For this reason, only an arbitrage model is appropriate, as it prices the derivative relative to the market, which is important for a market-maker; an equilibrium model prices the derivative relative to the theoretical market, which is not appropriate since it is a market instrument that is being used as the hedge.

- ◾ Use of models over time. Initially,  the  parameters  used  in  an  interest rate model, most notably the drift, volatility, and (if applicable) mean reversion rate, reflect the state of the economy up to that point. This state is not constant, and so consequently over time any model must be continually re-calibrated to reflect the current market state. That is, the drift rate used today when calculating the term structure may well be a different value tomorrow. This puts arbitrage models at a disadvantage, as their parameters are changed continuously in this way. Put another way, use of arbitrage models is not consistent over time. Equilibrium model parameters are calculated from historic data or from intuitive logic, and so may not be changed as frequently. However, their accuracy over time may suffer. It is up to users to decide whether they prefer the continual tweaking of the arbitrage model over the more consistent use of the equilibrium model.

3   For example, yield curve trading where bonds of different maturities are spread against each other, with the trader betting on the change in spread as opposed to the direction of interest rates, are a form of relative-value trade.

This is just the beginning, and there are a range of issues which must be considered by users when selecting an interest rate model. For example, in practice it has been observed that models incorporating mean reversion work more accurately than those that do not feature this. Another factor is the computer processing power available to the user, and it is often the case that single-factor models are preferred precisely because processing is more straightforward.

## IMPORTANCE OF PRACTICALITY

It is important to remain focused on the practical requirements of interest rate modelling. Market participants are more concerned with the ease with which a model can be implemented, and its accuracy with regard to pricing. In practice, different models are more suited to different applications, so  the  range  of  products  traded  by  a  market  practitioner  also  influences which model is chosen. For instance, the extended Vasicek model can be fitted very accurately to the initial term structure, and its implementation is relatively straightforward, being based on a lattice structure. It is also able to accurately price most products, however, like all one-factor models, it is not a valid model to use when pricing instruments that are sensitive to two or more risk factors, for example, quanto options. The extended CIR model is also quite tractable, although it has a more restricted set of term structures compared to the extended Vasicek model, as a result of the limitations imposed by the r t term on the volatility parameter. Both types of models are unable to capture the dynamics of the whole yield curve, for which HJM models must be used.

A drawback of these models is that although they fit the initial term structure, due to their structure they may not continue to calculate prices as the term structure evolves. In practice, the models must be re-calibrated frequently to ensure that they continue to describe term structure volatilities that reflect the market.

In selecting the model, a practitioner selects the market variables that are incorporated in the model. These can be directly observed such as zerocoupon rates or forward rates, or swap rates, or they can be indeterminate such as the mean of the short rate. The practitioner then decides the dynamics of these market or state variables ,  so  for  example, the short rate may be assumed to be mean-reverting. Finally, the model must be calibrated to market prices, so the model parameter values must be input that produce market prices as accurately as possible. There are a number of ways that parameters can be estimated, the most common techniques of calibrating to time series data such as interest rate data are general method of moments and the maximum likelihood method. For information on these estimation methods, refer to the bibliography.

Models exhibit different levels of sensitivity to changes in market prices and rates. The extent of a model's sensitivity also influences the frequency with  which  the  model  must  be  re-calibrated.  For  example,  the  BlackDerman-Toy model is very sensitive to changes in market prices, because it is a logr model, and changes in the process of the underlying variable are larger than those in the process for r t itself. Some practitioners believe that as they take bond prices and the term structure as given, arbitrage models  suffer  from  an  inherent  weakness.  Liquidity  and  other  considerations frequently  result  in  discrepancies  between  market  yields  and    theoretical value, and such discrepancies feed through into an arbitrage model. This drawback of arbitrage models means that users must take care about term structure inputs, and the curve-fitting techniques and smoothing techniques that are used become critical to model effectiveness. This is discussed in the next chapter.

Other considerations are detailed below:

Model inputs. Arbitrage models use the term structure of spot rate as an input, and this data is straightforward to obtain. Equilibrium models  require  a  measure  of  the  investor's  market  risk  premium, which  is  rather  more  problematic.  Practitioners  analyse  historical data on interest rate movements, which is considered less desirable.

Using models as part of a bond trading strategy. A key element of market-makers'  and  proprietary  traders'  strategy  is  relative  value trading,  which  includes  simultaneous  buying  and  selling  of  certain bonds against others, or classes of bonds against other classes. A yield curve spread trade is a typical relative value trade. How does one  determine  relative  value? 4 Using  an  interest  rate  model  is  the answer. For such purposes though, only equilibrium models can be used. By definition, since arbitrage models take bond prices and the current term structure as given, they cannot be used to assess relative value. This is because the current price structure is assumed to be correct. If we were to use such a model for a yield curve trade, it would imply a zero profit potential. Therefore only equilibrium models can be used for such purposes.

4   Some traders used to determine relative-value by conducting the analysis inside their head! Nowadays one needs to back up one's gut feeling with formal analysis. A term

structure model will assist.

Model  consistency. As  we  have  noted  elsewhere,  using  models requires their constant calibration and re-calibration over time. For instance, an arbitrage model makes a number of assumptions about the interest rate drift rate and volatility, and in some cases the mean reversion of the dynamics of the rate process. Of course, these values fluctuate constantly over time, so that the estimate of these model parameters used one day will not remain the same over time. So the model will be inconsistent over time and must be re-calibrated to the market. Equilibrium models use parameters that are estimated from historical data, and so there is no unused daily change. Model parameters remain stable. Over time, therefore, these models remain consistent,  at  least  with  themselves.  However,  given  the  points  we have noted above, market participants usually prefer to use arbitrage models and re-calibrate them frequently.

We have only touched on the range of considerations that must be followed when evaluating and implementing an interest rate model. This is a complex subject with a number of factors to consider, and ongoing research in the area serves to reinforce the fact that it is an important and very current topic.

## SELECTED BIBLIOGRAPHY AND REFERENCES

- Attari, M., 'Discontinuous Interest Rate Processes: An Equilibrium Model for Bond Option Prices', Working Paper , University of Iowa, [1999], pp. 1-32, 1996.
- Baz, J. and Das, S., 'Analytical approximations of the term structure for jump diffusion processes: a numerical analysis', Journal of Fixed Income , June 1996, pp. 78-86.
- Bjork, T., 'Interest rate theory', CIME Lectures, Working Paper , Stockholm School of Economics, 1996, pp. 1-90.
- Black, F. and Karasinski, P., 'Bond an option pricing when short rates are lognormal', Financial Analysts Journal , Jul-Aug 1991, pp. 52-59.
- Brennan, M. and Schwartz, E., 'An equilibrium model of bond pricing and a test of market efficiency', Journal of Financial and Quantitative Analysis 17(3), September 1982, pp. 301-329.
- Brace, A., Gatarek, D. and Musiela, M., 'The market model of interest-rate dynamics', Mathematical Finance 7(2), 1997, pp. 127-155.
- Cheyette, O., 'Term structure dynamics and mortgage valuation', Journal of Fixed Income , March 1992, pp. 28-41.
- Das, S., 'A Direct Discrete-Time Approach to Poisson-Gaussian Bond Option Pricing in the Heath-Jarrow-Morton model', Working Paper , Harvard Business School, 1997, pp. 1-44.

- Das, S., Foresi, S., 'Exact Solutions from Bond and Option Prices with Systematic Jump Risk', Review of Derivatives Research 1, 1996, pp. 1-24.
- Duffie, D. and Kan, R., 'A yield-factor model of interest rates', Mathematical Finance 6(4), 1996, p. 379-406.
- Heath, D., Jarrow, R. and Morton, A., 'Bond pricing and the term structure of interest rates: a discrete time approximation', Journal of Financial and Quantitative Analysis 25(4), December 1990, pp. 419-440.
- Heath, D., Jarrow, R. and Morton, A., 'Bond pricing and the term structure of interest rates: a new methodology', Econometrica 60(1), 1992, pp. 77-105.
- Ho, T.S.Y. and Lee, S-B., 'Term structure movements and pricing interest rate contingent claims', Journal of Finance 41, 1986, pp. 1011-1029.
- Honore, P., 'Five Essays on Financial Econometrics in Continuous-Time Models', PhD Thesis, Aarhus School of Business, 1998.
- Hughston, L., (ed.), 'Vasicek and Beyond: Approaches to Building and Applying Interest Rate Models', Risk Publications, 1996.
- Hull, J. and White, A., 'Bond option pricing based on a model for the evolution of bond prices', Advances in Futures and Options Research 6, 1993, pp. 1-13.
- Hull, J. and White, A., 'Numerical procedures for implementing term structure models II: two-factor models', Journal of Derivatives 2(2), Winter 1994, pp. 37-48.
- Jamshidian, F., 'LIBOR and swap market models and measures', Finance and Stochastics 1, 1997, pp. 293-330.
- Jarrow, R. and Madan, D., 'Option Pricing Using the Term Structure of Interest Rates to Hedge Systematic Discontinuities in Asset Returns', Working Paper , Cornell University, 1991, pp. 1-47.
- Rebonato, R., Interest Rate Option Models , 2 nd  edition, John Wiley &amp; Sons, 1998.
- Rebonato, R. and Cooper, I., 'The limitations of simple two-factor interest-rate models', Journal of Financial Engineering , March 1996.
- Ritchken, R and Sankarasubramanian, L., 'Volatility structures of forward rates and the dynamics of the term structure', Mathematical Finance 5, 1995, pp. 55-72.
- Uhrig, M. and Walter, U., 'A new numerical approach for fitting the initial yield curve', Journal of Fixed Income , March 1996, pp. 82-90.

## REFERENCES ON ESTIMATION METHOD

- Andersen, T. and Lund, J., 'Estimating continuous-time stochastic volatility models of the short-term interest rate', Journal of Econometrics 77, 1997, pp. 343-377.
- Brown, R. and Schaefer, S., 'The term structure of real interest rates and the Cox, Ingersoll and Ross model', Journal of Financial Economics 35, 1994, pp. 2-42.
- Campbell, J., Lo, A. and MacKinlay, C., The Econometrics of Financial Markets , Princeton University Press, 1997.
- Davidson, R. and MacKinnon, J., Estimation and Inference in Econometrics , Oxford University Press, 1993.

- Duffie, D. and Singleton, K., 'Simulated moments estimation of Markov models of asset prices', Econometrica 61, 1993, pp. 929-952.
- Hansen, L., 'Large sample properties of generalized method of moments estimators', Econometrica 50, 1982, pp. 1029-1055.
- Lo, A., 'Statistical tests of contingent claims asset pricing models', Journal of Financial Economics 17, 1986, pp. 143-173.
- Longstaff, F. and Schwartz, E., 'Interest rate volatility and the term   structure: a two-factor general equilibrium model', Journal of Finance 47, 1992, pp. 1259-1282.

'Houston, Tranquility Base here. The Eagle has landed.' It was Armstrong's voice, the quiet voice of the best boy in town, the one who pulls you drowning from the sea and walks off before you can offer a reward.

-- Norman Mailer, A Fire on the Moon , Boston, MA: Little, Brown &amp; Company, 1970

## CHAPTER  7

## The Index-Linked Bond Yield Curve

B onds that have part or all of their cash flows linked to an inflation index form an important segment of several government bond markets. In the UK, the first sovereign index-linked bonds were issued in 1981 and at the end of 2018 they accounted for approximately 20% of outstanding nominal value in the gilt market. Index-linked bonds have also been issued in the US Treasury market and in Australia, Canada, the Netherlands, New Zealand and Sweden. There is no uniformity in market structure and as such there are significant differences between the index-linked markets in these countries. There is also a wide variation in the depth and liquidity of these markets.

Index-linked bonds or inflation-indexed bonds present additional issues in their analysis, due to the nature of their cash flows. Measuring the return on index-linked bonds is less straightforward than with conventional bonds, and in certain cases there are peculiar market structures that must be taken into account as well. For example, in the US index-linked Treasuries market (known as 'TIPS' from Treasury inflation-indexed securities), there is no significant lag between the inflation link and the cash flow payment date. In the UK, there is an eight-month lag between the inflation adjustment of the cash flow and the cash flow payment date itself (changed to a three-month lag for bonds issued from 2005), while in New Zealand there is a three-month lag. The existence of a lag means that inflation protection is not available in the lag period, and that the return in this period is exposed to inflation risk - this also must be taken into account when analysing the bond.

From market observation, we know that index-linked bonds can experience considerable volatility in prices, similar to conventional bonds, and therefore there is an element of volatility in the real yield return of these bonds. Traditional economic theory states that the level of real interest rates is constant, however, in practice they do vary over time. In addition, there

are liquidity and supply and demand factors that affect the market prices of index-linked bonds. In this chapter, we present analytical techniques that can be applied to index-linked bonds, the duration and volatility of indexlinked bonds, and the concept of the real interest rate term structure.

## INDEX-LINKED BONDS AND REAL YIELDS

The real return generated by an index-linked bond, or its real yield, is usually  defined as yield on risk-free index-linked bonds; in other words, the long-term interest rate on risk-free funds minus the effect of inflation. There may also be other factors involved, such as the impact of taxation. Therefore the return on an index-linked bond, should in theory, move in line with the real cost of capital. This is influenced by the long-term growth in the level of real gross domestic product in the economy. This is because in an economy experiencing rapid growth, real interest rates are pushed upwards as the demand for capital increases, and investors therefore expect higher real yields. Returns are also influenced by the demand for the bonds themselves.

The effect of general economic conditions and the change in these over time results in real yields on index-linked bonds fluctuating over time, in the same way nominal yields fluctuate for conventional bonds. This means that the price behaviour of indexed bonds can also be quite volatile.

The yields on indexed bonds can be used to imply market expectations about the level of inflation. For analysts and policy makers to use indexed bond yields in this way, it is important that a liquid secondary market exists in the bonds themselves. For example, the market in Australian index-linked bonds is relatively illiquid, so attempting to extract information content from their yields may not be valid. Generally though, the real yields on indexed bonds reflect investors' demand for an inflation premium, or rather a premium for the uncertainty regarding future inflation levels. This is because holders of indexed bonds are not exposed to inflation-eroded returns, therefore if future inflation is expected to be zero, or known with certainty (whatever  its  level),  there  is  no  requirement  for  an  inflation  premium,  because there is no uncertainty. In the same way, the (nominal) yields on conventional bonds reflect market expectations on inflation levels. Therefore higher volatility of the expected inflation rate leads to a higher inflation risk premium on conventional bonds, and a lower real yield on indexed bonds relative to nominal yields. It is the uncertainty regarding future inflation levels that creates a demand for an inflation risk yield premium, rather than past experience of inflation levels. However, investor sentiment may well demand a higher inflation premium in a country with a poor record in combating inflation.

Traditionally, information on inflation expectations has been obtained by survey methods or theoretical methods. These have not proved reliable, however,  and  were  followed  only  because  of  the  absence  of  an  inflation indexed  futures  market. 1   Certain  methods  for  assessing  market  inflation expectations are not analytically valid, for example, the suggestion that the spread between short-term and long-term bond yields cannot be taken to be a measure of inflation expectation, because there are other factors that drive this yield spread, and not just the inflation risk premium. Equally, the spread between the very short-term (overnight or one week) interest rate and the two-year bond yield cannot be viewed as purely driven by inflation expectations. Using such approaches to glean information on inflation expectations is logically unsound. One approach that is valid, as far as it goes, is to analyse the spread between historical real and nominal yields, although this is not a forward-looking method. It does, however, indicate the market's inflation premium over a period of time. The best approach, then, is to use the indexed bond market. Given a liquid market in conventional and indexlinked bonds, it is possible to derive estimates of inflation expectations from the yields of both sets of bonds. This is reviewed later in the chapter.

## THE REAL TERM STRUCTURE OF INTEREST RATES

Some approaches used to measure inflation expectations include:

- ◾ the 'simple'  approach,  where  the  average  expected  inflation  rate  is calculated  using  the  Fisher  identity,  so  that  the  inflation  estimate  is regarded as the straight difference between the real yield on an indexlinked bond, at an assumed average rate of inflation, and the yield on a conventional bond of similar maturity;
- ◾ the 'break-even' inflation expectation, where average inflation expectations are estimated by comparing the return on a conventional bond against that on an indexed bond of similar maturity, but including an application of the compound form of the Fisher identity. This has the effect of decomposing the nominal rate of return on the bond into components of real yield and inflation;
- ◾ a variation of the break-even approach, but matching stocks by duration rather than by maturity.

1   The New York Coffee, Sugar and Cocoa Exchange introduced a futures contract on the US consumer prices index (CPI) in the 1980s.

Each of these approaches has drawbacks. A more valid approach is to construct a term structure of the real interest rates, which indicate, in exactly the same way that the conventional forward rate curve does for nominal rates, the market's expectations on future inflation rates. In countries where there are liquid markets in both conventional and inflation-indexed bonds, we can observe a nominal yield curve and a real yield curve. It then becomes possible  to  estimate  both  a  conventional  term  structure  and  a  real  term structure. Using these allows us to create pairs of hypothetical conventional and indexed bonds that have identical maturity dates, for any point on the term structure. 2  We could then apply the break-even approach to any pair of bonds to obtain a continuous curve for both the average and the forward inflation expectations. To maximise use of the available information, we can use all the conventional and indexed bonds that have reasonable liquidity in the secondary market.

In this section, we review one method that can be used to estimate and fit a real term structure.

## THE TERM STRUCTURE OF IMPLIED FORWARD INFLATION RATES

In previous chapters, we reviewed the different approaches to yield curve modelling used to derive a nominal term structure of interest rates. We have seen that the choice of yield curve model can have a significant effect on the resulting term structure. In the same way, the choice of model impacts the resulting real rate term structure as well. One approach has been described by McCulloch (1975), while in the UK market, the Bank of England uses a modified version of the approach first posited by Waggoner (1997), which we reference in Chapter 11. McCulloch's approach involves estimating a discount function by imposing a constraint on the price of bonds in the sample to equal the sum of the discounted values of the bonds' cash flows. The Waggoner approach uses a cubic spline-based method, like McCulloch, with a roughness penalty that imposes a trade-off between the smoothness of the curve and its level of forward rate oscillation. The difference between the two approaches is that with McCulloch it is the discount function that is specified by the spline function, whereas in the Waggoner model it is the zero-coupon curve. Both approaches are valid. In fact due to the relationship  between  the  discount  function,  zero-coupon  rate  and  forward  rate, both methods derive similar curves under most conditions.

2 We  are  restricted,  however,  to  the  longest-dated  maturity  of  either  of  the  two types of bonds.

Using the prices of index-linked bonds, it is possible to estimate a term structure of real interest rates. The estimation of such a curve provides a real interest counterpart to the nominal term structure that was discussed in the previous chapters. More importantly, it enables us to derive a real forward rate curve. This enables the real yield curve to be used as a source of information on the market's view of expected future inflation. In the UK market there are two factors that present problems for the estimation of the real term structure: the first is the eight-month (or three-month) lag between the indexation uplift and the cash flow date, and the second is that fact that there are fewer index-linked bonds in issue, compared to the number of conventional bonds. The indexation lag means that in the absence of a measure of expected inflation, real bond yields are dependent to some extent on the assumed rate of future inflation. The second factor presents practical problems in curve estimation. For example, in December 1999 there were only 11 index-linked gilts in existence in the UK gilt market, and this is not sufficient for most models. Neither of these factors presents an insurmountable problem, however, and it is still possible to estimate a real term structure.

## ESTIMATING THE REAL TERM STRUCTURE

There are a number of techniques that can be applied in estimating the real term structure. One method was described by Schaefer (1981). The method we describe here is a modified version of the cubic spline technique described by Schaefer. This is a relatively straightforward approach. The adjustment involves simplifying the model, ignoring tax effects, and fitting the yield to maturity structure. A reduced number of nodes defining the cubic spline is specified than is the case with the conventional term structure, because of the fewer number of index-linked bonds available, and usually only three node points are used. Our approach, therefore, estimates three parameters, defining a spline consisting of two cubic functions, using 11 data points. The approach is defined below.

In the first instance, we require the real redemption yield for each of the indexed bonds. This is the yield that is calculated by assuming a constant average rate of inflation, applying this to the cash flows for each bond, and computing the redemption yield in the normal manner. The yield is therefore the market-observed yield, using the price quoted for each bond. These yields are used to define an initial estimate of the real yield curve, as they form the initial values of the parameters that represent the real yield at each node point. The second step is to use a non-linear technique to estimate the values of the parameters that will minimise the sum of the squared residuals between the observed and fitted real yields. The fitted yield curve is viewed as the real par yield curve. From this curve we calculate the term structure of real interest rates and the implied forward rate curve, using the technique described in Chapter 10. In estimating the real term structure in this way, we need to be aware of any tax effects. In the UK market, there is a potentially favourable tax effect, which may not apply in say, the US Tips market. Generally for UK indexed gilts, high marginal taxpayers are the biggest holders of index-linked bonds because of the ratio of capital gain to income, and their preference is to hold shorter-dated indexed bonds. On the other hand, pension funds, which are exempt from income tax, prefer to hold longerdated indexed gilts. The approach we have summarised here ignores any tax effects, but to be completely accurate any tax impact must be accounted for in the real term structure.

## FITTING THE DISCOUNT FUNCTION

The term structure method described by McCulloch (1971) involved fitting a discount function, rather than a spot curve, using the market prices of a sample of bonds. This approach can be used with only minor modifications to produce a real term structure.

Given the bond price equation at (7.1):

<!-- formula-not-decoded -->

where P C T M i i i i , , , are the price, coupon, maturity, and principal payment of the i th bond, we set the set of discrete discount factors as the discount function df , defined as a linear combination of a set of k linearly independent underlying basis functions, given by (7.2):

<!-- formula-not-decoded -->

where f T j is the j th basis function and a j is the corresponding coefficient, with j k 1 2 , ,… . It  can  be  shown  (see  Deacon  and  Derry  1994)  that  for index-linked bonds, equation (7.2) can be adapted by a scaling factor i ∆ that is known for each bond, once an assumption has been made about the future average inflation rate, to fit a discount function for indexed bonds. We estimate the coefficients a j from:

<!-- image -->

where:

<!-- formula-not-decoded -->

where P C T M i i i i , , , , are as before, but this time representing the index-linked bond. The scaling i ∆ is that for the i th bond, and depends on the ratio of the retail price index (RPI) at the time compared to the RPI level in place at the time the bond was issued, known as the base RPI. 3 If, in fact, the RPI that is used to index any particular cash flow is not known, it must be estimated using  the  latest  available  RPI  figure,  in  conjunction  with  an  assumption about the path of future inflation, using e π .

## DERIVING THE TERM STRUCTURE OF INFLATION EXPECTATIONS

Using the discount function approach summarised above, we can construct curves for both the nominal and the real implied forward rates. These two curves  can  then  be  used  to  infer  market  expectations  of  future  inflation rates. The term structure of forward inflation rates is obtained from both these curves by applying the Fisher identity:

<!-- formula-not-decoded -->

where f is the implied nominal forward rate, r is the implied real forward rate,  and i is  the  implied  forward  inflation  rate. As  with  the  term  structure  of  real  spot  rates,  the  real  implied  forward  rate  curve  is  dependent on an assumed rate of inflation. To make this assumption consistent with the inflation term structure that is calculated, we can use an iterative procedure for the assumed inflation rate. Essentially this means that the real yield curve is re-estimated until the assumed inflation term structure and the estimated inflation term structure are consistent. Real yields are usually calculated using either a 3% or a 5% flat inflation rate. This enables us to estimate the real yield curve, from which the real forward rate curve is derived. Using (7.3) we can then obtain an initial estimate of the inflation term structure. This forward inflation curve is then converted into an average inflation curve, using (7.4):

3   Due to the lag in the UK gilt market, for index-linked gilts the base RPI is actually the level recorded for the month eight months (or three months, for bonds issued since 2005) before the issue date.

<!-- formula-not-decoded -->

if is the forward inflation rate at maturity i ;

i i i is the average inflation rate at maturity i .

From this average inflation curve, we can select specific inflation rates for each index-linked bond in our sample. The real yields on each indexed bond are then re-calculated using these new inflation assumptions. From these yields the real forward curve is calculated, enabling us to produce a new estimate of the inflation term structure. This process is repeated until there is consistency between the inflation term structure used to estimate the real yields and that produced by (7.3).

Using the modified Waggoner method, which is described in Chapter 11, the nominal spot yield curve for the gilt market in July 1999 is shown at Figure 7.1. The real term structure is also shown, which enables us to draw the implied forward inflation expectation curve, which is simply the difference between the first two curves.

FIGURE 7.1 UK market nominal and real term structure of interest rates, July 1999.

<!-- image -->

Yield source : Bank of England.

where:

## APPLICATION

Real yield curves are of some use to investors, for a number of reasons. These include applications that arise in insurance investment management and corporate finance, such as the following:

- ◾ they  can  be  used  to  value  inflation-linked  liabilities,  such  as  indexlinked annuity contracts;
- ◾ they can be used to value inflation-linked revenue streams, such as taxes that are raised in line with inflation, or for returns generated in corporate finance projects - this makes it possible to assess the real returns of project finance or government revenue;
- ◾ they can be used to estimate the present value of a company's future staff costs, which are broadly linked to inflation.

Traditionally,  valuation  methods  for  such  purposes  use  nominal  discount rates and an inflation forecast, which are constant. Although the real term structure also includes an assumption element, using estimated market real yields is equivalent to using a nominal rate together with an implied market inflation forecast, which need not be constant. This is a more valid approach - a  project  financier  in  the  UK  in  July  1999  can  obtain  more meaningful estimates on the effects of inflation using the rates implied in Figure 7.1, rather than an arbitrary, constant inflation rate. The inflation term structure can be used in other ways as well, for example, an investor in mortgage-backed bonds, who uses a prepayment model to assess the prepayment risk associated with the bonds, will make certain assumptions about the level of prepayment of the mortgage pool backing the bond. This prepayment rate is a function of a number of factors, including the level of interest rates, house prices, and the general health of the economy. Rather than use an arbitrary assumed prepayment rate, the rate can be derived from market inflation forecasts.

In essence, the real yield curve can and should be used for all the purposes for which the nominal yield curve is used. Provided that there are enough liquid index-linked bonds in the market, the real term structure can be estimated using standard models, and the result is more valid as a measure  of  market  inflation  expectations  than  any  of  the  other  methods  that have been used in the past.

## SELECTED BIBLIOGRAPHY AND REFERENCES

Arak, M. and Kreicher, L., 'The real rate of interest: inferences from the new UK indexed gilts', International Economic Review 26(2), June 1985, pp. 399-408. Bootie, R., Index-Linked Gilts , 2nd edition, Woodhead-Faulkner, 1991.

- Brown, R. and Schaefer, S., 'Ten years of the real term structure: 1984-1994', Journal of Fixed Income , March 1996, pp. 129-141.
- Brynjolfsson, J. and Fabozzi, F. (ed.), Handbook of Inflation-Indexed Bonds , FSF Associates, 1999.
- Deacon, M. and Derry, A., 'Deriving Estimates of Inflation Expectations from the Prices of UK Government Bonds', Bank of England Working Paper No. 23, 1994.
- Deacon, M. and Derry, A., Inflation-Indexed Securities , Prentice Hall, 1998.
- McCulloch, J., 'Measuring the term structure of interest rates', Journal of Business Vol. XLIV, January 1971, pp. 19-31.
- McCulloch, J., 'The tax-adjusted yield curve', Journal of Finance 30(3), June 1975, pp. 811-830.
- Roll, R., US Treasury inflation-indexed bonds: the design of a new security', Journal of Fixed Income , December 1996, pp. 321-335.
- Schaefer, S., 'Measuring a tax-specific term structure of interest rates in the market for British government securities', The Economic Journal 91, June 1981, pp. 415-438.

'Raisuli, what shall we do? We have lost everything!' 'Sherif, was there never anything in your life for which it was worth losing everything for?'

-- From The Wind and The Lion (MGM Films, Columbia Pictures) 1975

## Yield Curve Analytics in the

## CHAPTER  8 Post-2008 Era

T he bank crash of 2008 has been covered extensively in the business and financial literature, so there is no need for us to dwell on it here. What is worth considering is how yield curve analytics have adjusted to the changes in market conditions, some desired, some by regulatory legislative fiat, and some  unintended,  that  have  taken  place  since  then.  Whereas  previously in essence, one was concerned with the sovereign bond yield curve, often referred to as the 'benchmark' curve, and which itself was generally positively sloping and starting with a positive interest rate at the shortest tenor, today and for the foreseeable future there are other considerations to bear in mind. We look at these in detail in this chapter.

## OVERNIGHT INDEX SWAP (OIA) YIELD CURVE 1

An important reference yield curve today is the overnight index swap (OIS) curve. (In the United Kingdom sterling markets, this is known as the sterling overnight index or SONIA curve.)  This is similar to the conventional swap curve, except it references the overnight rate on the floating leg of the swap, compared to the three-month or six-month rate on the floating leg of a conventional swap. Prior to the 2008 crash, derivative pricing and valuations were based on the simple principle of the time value of money. A breakeven price was calculated such that when all the future implied cash flows were discounted back to today, the Net Present Value of all the cash flows was zero. The breakeven price was used for valuations or spread by a bid-offer price to create a trading price. Bid-offer prices would generally incorporate a counterparty-dependent markup to cover various costs and a return on capital in a fairly ill-defined way.

1   This section was co-authored with Kevin Liddy.

A breakeven price required the construction of a projection curve for the index being referenced, which could be a tenor of Libor, such as threemonth, for three-month Libor swaps, or an overnight rate in the case of Overnight Index Swaps. The projection curve would use market observable inputs and various interpolation methodologies to derive market implied future rates used to project the future floating rate fixings. In other words:

- ◾ A conventional swap curve is a projection curve based on the threemonth (or six-month) Libor fix; whereas
- ◾ An OIS curve is a projection curve based on the overnight rate.

Once the market implied future fixings were known, a discount curve would then be used to discount cash flow mismatches in such a way that the breakeven fixed rate gives a result where all the cash flow mismatches have a net present value of zero. Historically, market practice was to discount cash flows using a Libor discount curve, the assumption being that all cash flow mismatches could be borrowed or reinvested at Libor. It was implicitly assumed that Libor was the risk-free rate at which these cash flow mismatches could be funded.

Figure 8.1 shows the GBP OIS (SONIA) and GBP swap curves as at 13 October 2016. The OIS curve lies below the conventional swap curve because of the term liquidity premium (TLP) difference between the two tenors (the TLP is higher the longer the tenor).

In  the  case  of  a  collateralised  trade  transacted  under  the  terms  of  a Credit Support Annexe (CSA) agreement, 2  the posting of collateral ensures that  the  net  present  value  (NPV)  of  a  trade  is  always  zero  net  of  collateral held or posted. All future funding mismatches are therefore explicitly funded directly by the exchange of collateral and as a result do not require any  external  funding. The  collateral  remuneration  rate  is  defined  by  the CSA and is normally the relevant OIS rate. As it is the relevant OIS rate that becomes the applicable rate for funding cash flow mismatches, market practice has evolved to discount future cash flows using OIS rates when pricing or valuing a collateralised trade, rather than Libor, so-called OIS discounting. It is impossible to determine precisely when market practice changed but it is generally accepted that when the London Clearing House (which clears derivative transactions) changed to OIS discounting in 2010, it was doing so to reflect market best practice.

Where multiple forms of collateral were permissible under a CSA, market practice evolved to take into account the embedded option for the collateral poster. Pricing assumed that a counterparty would always act rationally and Source : © Bloomberg LP. Reproduced with permission.

2   It is an 'annexe' to the standard ISDA derivatives contract.

FIGURE 8.1

<!-- image -->

GBP SONIA and GBP Swap curves, 13 October 2016.

post the cheapest to deliver collateral with the discount curve reflecting the relevant collateral OIS rate, so-called cheapest-to-deliver (CTD) or CSA discounting. A further enhancement is often used where the collateral is non-cash such as a government bond. In these instances the discount curve reflects the price at which the bonds can be traded in the repo market. For complex CSAs where collateral was multi-currency, the discount curve is often a multi-currency hybrid curve which reflects that the CTD may change at a future date.

For  uncollateralised  trades,  not  only  was  the  use  of  a  Libor  rate  to discount cash flow mismatches clearly inappropriate given the increase in funding spreads during the 2008 crisis but also, in the absence of collateral, the NPV of an uncollateralised trade represented a potential funding requirement. Pricing for uncollateralised trades now generally contains an upfront adjustment to the price to take into account the expected funding costs of non-collateralisation referred to as the Funding Valuation Adjustment or FVA. FVA along with a Credit Valuation Adjustment (CVA) now represent a more rigorously defined part of the bid-offer adjustment.

Collateral posted at the London Clearing House (LCH), for example, has no optionality allowed - it must be in cash and in the currency of the transaction. Hence the swap screen price now reflects the price for a cleared swap at LCH. Because the collateral is unambiguous (cash in the currency of the trade) remunerated at the relevant OIS, so the discount/funding rate is always known and is not counterparty dependent. Anything other than a LCH cleared trade means the price will be different to take into account the impact of the type of collateral. This is an important point: observable swap rates are for LCH cleared trades only.

The yield curve is the best snapshot of the state of the financial markets. It  is  not  the  sole  driver  of  customer  prices  in  banking,  but  it  is  the  most influential.  Being  aware  of  the  relationship  between  spot  rates,  forward rates, and yield to maturity is therefore important, as is the relationship and interplay between different types of curve.

In the next section, we look at OIS curve construction.

## POST-CRASH DISCOUNTING PRINCIPLES FOR YIELD-CURVE CONSTRUCTION 3

In this section, we consider how the market in yield-curve construction and valuation principles has been adjusted since 2008, and we describe the process used to construct the OIS curve based on collateralised swap rates. We discuss further the peculiarities and difficulties in application of this curve for valuation.

## Why the OIS Curve Gained Importance

Before the crisis of 2007-2008, the most widely used group of indicators for yield curve construction was Libor (including Euribor, CHF Libor, etc.), and conventional plain vanilla interest rate swaps (IRS) based on Libor and its analogues for other currencies. Libor and other Libor-like rates for tenors before six months to one year and IRS after one year were used for   determining discount factors and implied forwards for IRS curve   construction. 4

3   This section was co-authored with Polina Bardaeva.

4   Note that LIBOR is being replaced from 2021. The form of the replacement differs by currency, with USD, GBP and EUR each having their own references. In GBP markets the reference will be an official SONIA fixing from the Bank of England, while for USD the replacement is known as the Secured Overnight Financing Rate (SOFR), based on the US Treasury repo rate.

After  the  crash,  market  participants  became  more  concerned  about the credit risk of counterparties in the interbank markets. An indication of the significance of credit and liquidity risk was the widening of the spread between OIS and three-month Libor, as shown at Figure 8.2.

To  mitigate  risk  with  respect  to  the  credit  quality  of  counterparties,  swap  transactions  in  the  market  are  collateralised  with  the  negative mark-to-market (MTM) party posting collateral to the value of the MTM. Generally dealer banks will also insist on an initial margin (IM) collateral posting from all customer banks. The most common collateral for swaps is cash, which is placed with the counterparty and earns the daily overnight interest rate (here, the OIS). Collateral doesn't only guarantee the fulfillment of obligations of the deal but impacts the swap price (the rate for the fixed leg) as a result of equality of the contracts' cash flows present value.

As the market for referencing the OIS rate became universal, with collateralised dealing becoming the norm, the vanilla Libor/IRS group curves were used less as reference rates. Instead, practitioners and market commentators began to refer to the 'risk-free OIS yield curve'. Hence the OIS curve was viewed as the market 'benchmark' curve.

FIGURE 8.2 Three-month Euribor and EONIA spread, 2002-2017. Rates source : Bloomberg, Reprinted with permission.

<!-- image -->

## EXAMPLE 8.1 TERMINOLOGY AND ACTUALITY

It is important to understand what is going on here. As we noted in the previous section, a swap curve is essentially a projection curve based on the three-month rate and the OIS curve is a projection curve based on the overnight rate. One is no more a 'risk-free' or 'collateralised' rate than the other. However, because the OIS rate is most commonly associated with the interest rate payable on collateral postings, and collateral postings are what make an interest-rate swap a credit-riskfree transaction (ignore margin period of risk), it is not uncommon to hear the OIS curve referred to as the 'risk-free curve'.

OIS is a derivative on total return on the reference rate with daily interest compounding, for which in different jurisdictions (for different currencies) the most common overnight money market rate is used: for US dollar it is the Fed Funds rate, for the euro it is EONIA, and for the British Pound it is SONIA. For other countries and currencies, a weighted average of brokered deals by banks for overnight tenor is taken. Compared to the Libor reference rate, the major difference of these overnight rates is that they are based on actual deals (less of outliers) that were conducted by market participants during the day (the previous day), while the Libor group of rates is based on quotations for deals but not actual transactions undertaken at the prices quoted.

## Construction of the OIS Curve

In general, in order to construct a swap curve one should first understand that a swap curve is a set of rates for the fixed leg of the swap. These rates can be retrieved by equaling present values of cash flows for the fixed and floating legs. Present values of cash flows are calculated by discounting. For the floating leg, the future cash flows should be defined via forward rates. Thus, for every swap curve construction there should be discount factors and implied forward curves.

The second step will be to define what market yield curves exist. Based on these available curves one should construct a zero-coupon curve (that is, infer zero-coupon rates from the observed market rates - see Chapter 2). The rates on the zero-coupon curve are then used to define the discount factors. These discount factors can then be used to obtain the implied forward rates.

While constructing a simple IRS curve, following from the description above, the discounting curve and the forward curve are based on the same zero-coupon curve (derived from Libor group indicators).

This step is changed for an OIS curve: discount rates and implied forwards are based on different sets of market curves. So the forward rates should be defined based on available market curves for Eonia/Fed rate and the OISs. Meanwhile the discounting should be done based on Euribor/Libor and IRS curves (forward curves can be applied in the middle of the curve).

An example of the calculations is presented in the table below.

The steps involved are:

1. The zero-coupon curve (curve of spot rates) is derived from Libor-based curves by solving the following equations. The required parameter is marked with shading.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

. . .

<!-- formula-not-decoded -->

2. Discount factors from Libor-based zero-coupon bonds are then calculated:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

3. The same equations are used to construct zero-coupon curve and discount factors for OIS based curves.
4. Using  calculated  discount  factors,  the  implied  forward  rates  can be derived:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

5. For  the  next  step,  the  present  value  of  cash  flows  for  the  fixed  and floating legs is calculated and by equalling them the swap rate for every tenor can be determined.

The result is shown at Table 8.1 and illustrated at Figure 8.3.

FIGURE 8.3 Illustration of example curve construction calculations. Source : Author's notes.

<!-- image -->

## Application of OIS Curve

The OIS curve is used to price collateralised swap contracts. The major difference from the pre-crisis valuation is that calculated discount factors are based on OIS quotes and not on Libor and IRS rates. At the same time the forward rates are still being derived from current Libor group indicators. Thus, post-crash yield curve construction one should use both Libor and OIS curves, to take into account the credit risk spread.

In general, the impact of using OIS based discount factors instead of Libor and IRS based discount factors will be larger when the tenor increases or  when  the  level  of  rates  is  high.  (Of  course  there  are  a  wide  range  of factors that influence the pricing mechanism and the results.)

For example, the calculation becomes more complicated when collateral is posted in a currency different from the currency of the swap (of the reference rate). It adds to our formula the FX forward component (since the collateral is converted and invested at each date of the curve in the currency of the curve), which will double the amount of curves to be used in the calculations and add to the complexity of the system of equations. This situation  can  be  observed  often  as  large  dealer  bank  market  participants use collateral in one currency for all their contracts (in different currencies) depending on the optionality stated in their CSA agreements. Where a CSA allows a counterparty to place collateral in any currency, there is a need to check whether no arbitrage can be realised and include this in the swap price (to eliminate arbitrage opportunities).

This process requires a bank to calculate a multi-currency yield curve and  also  gives  rise  to  the  cheapest-to-deliver  (CTD)  collateral  currency. Multi-currency  curve  construction  is  discussed  in  the  author's  book The Principles of Banking (Wiley 2012).

Other issues that should be taken into account while valuing contracts based on collateralised swap rates are:

- ◾ Operational risk which arises in the process of daily re-calculation of margin calls for collaterals;
- ◾ Not-perfect coverage by collateral of the deals (and hence a small portion of credit risk left uncovered);
- ◾ Type  and  liquidity  of  collaterals  (they  can  differ  from  cash  and instruments may possess not-perfect liquidity);
- ◾ Netting of collaterals in a portfolio of deals (and complexity to calculate the effect of having collateral for each particular contract);
- ◾ Rehypothecation of collateral (in other words usage of instruments already accepted as collateral from another counterparty);
- ◾ Seasonal  spikes  of  rates  (including  spikes  at  the  end  of  reporting periods);
- ◾ Different day-count conventions applied for different contracts and even swap legs also require more precise calculations.

Inclusion of any of the above mentioned issues into valuation requires application of assumptions and, thus, raises subjectivity of calculations and difficulty  (or  inability)  to  verify  them.  It  often  results  in  the  employment of third-party independent evaluators which specialise in specific financial markets and provide their yield curves for pricing products on that market.

## FOUR CURVES: SOVEREIGN, LIBOR, OIS, AND INTERNAL FUNDING CURVE

There is understandable interplay between the sovereign bond, Libor-swap, and OIS curves, and also a fourth curve, which is the internal curve used by a bank as part of its funds transfer pricing (FTP) framework. 5  This is especially important for banks that are derivative market-makers or otherwise run a large trading book in derivatives. Before we discuss this we need to cover some background on the CSA and funding for derivatives.

5   For full details on FTP, please see Chapter 15 of the author's book The Principles of Banking (Wiley 2012), and Chapter 12 of the book Moorad Choudhry Anthology (Wiley 2018).

## CSA and Derivatives Collateral Funding

The discount curve applied in valuation of a derivatives transaction should reflect the transacting firm's funding level on that trade, which is exactly the same as would be observed with a cash transaction.

Post-crash, the pre-crash Libor-flat convention used for swap discounting was consigned to the history books, and best-practice principle suggests the bank's actual cost of term funding (at appropriate tenor points) should be used for swap valuation. (That said, when liquidity is abundant, the valuation discrepancy as a result of different discount curve choice is relatively small except at very long tenors. However, for large size transactions even one basis point can have significant impact on the P&amp;L!).

Up  until  the  credit  crunch,  the  convention  had  been  to  discount  on Libor-flat  or  its  equivalent.  This  was  not  an  issue  when  the  difference between overnight and three-month borrowing rate is only a few basis points and stable. However, in 2008 the Libor-OIS basis blew out to 364 bps in US dollar (shortly after the Lehman bankruptcy). At the same time, banks' unsecured funding spreads rose by similar amounts.

This issue impacts curve choice when it comes to valuation. At the same time, the optionality in place in a CSA also impacts curve usage. 6

In  practice,  the  precise  details  within  each  ISDA  CSA  with  different counterparties means there is significant impact on funding levels. CSA terms also often have wide variation and optionality embedded in them. Interbank derivatives are all fully collateralised and hence have moved onto OIS based pricing, as clearly LIBOR discounting is now inappropriate for collateralised trading. But the appropriate discount curve will then be influenced by the CSA terms. Some aspects of optionality in CSA parameters include:

- ◾ eligible currencies and securities;
- ◾ MTM thresholds;
- ◾ call frequency;
- ◾ interest paid on collateral.

All these parameters can have a significant impact on discount rate. A common CSA usually used between major dealers, has a $0.00 threshold and daily margin calls. It allows for the choice of posting cash in USD, GBP, or EUR where OIS, SONIA and EONIA are paid, respectively. At each point in time, the discount rate on a trade is the interest rate applied to  the  collateral  posted/received  at  that  time.  However,  because  of  the complexity that can (and often times does) exist within a CSA, the forward levels of this rate cannot always be implied or replicated from market traded instruments. For example, when a CSA allows more than one eligible currency or security, it gives rise to an option that cannot be easily priced, and which calls for a multi-currency curve - and a long-dated one at that.

6   Derivatives  now  settle  through  a  centralised  clearing  counterparty  (CCP),  but within  the  clearing  house  rule  there  is  also  an  essence  of  optionality  with  type, although not currency, of collateral. Non-vanilla (that is, exotic) derivatives remain outside of the CCP framework.

A side conclusion we draw from this effectively kills off the 'law of one price' debate with respect to derivatives valuation, and argues for a funding valuation adjustment (FVA). When a CSA does not exist at all (for example, with corporate customers using derivatives to hedge funding or FX risk) there is no collateral posting and so the discount rate applied to a derivatives trade must therefore reflect the bank's outright borrowing (funding) cost at medium-dated tenor.

Collateralised discount curves depend on the CSA terms with each particular counterparty with whom a trade is executed. One of the most important forms of CSA, employed by the London Clearing House, specifies the following terms:

- ◾ Bilateral, daily collateral call;
- ◾ Zero MTM threshold;
- ◾ Cash collateral only;
- ◾ Collateral posting currency in accord with trade currency;
- ◾ Corresponding overnight rate paid on cash collateral held.

In this case, the overnight curve in the trade currency would be used to discount the derivative (EONIA for EUR, OIS for USD, SONIA for GBP, and so on).

The most common interbank CSA is similar to that of LCH, with the exception that it allows for the choice of posting EUR, USD, and GBP cash. Under this type of CSA, a rational collateral manager would post whichever currency that yields the highest return to it - hence the 'CTD' concept we introduced earlier. Paradoxically, a bank may wish to post the currency that has the lowest funding cost. This ties in with what would be needed under prudent derivatives funding policy - the collateral funding requirement is funded in the long-term, with long-term funds.

This  argues  for  a  second  approach:  constructing  a  forward  curve embedding  this  optionality  requires  market  observable  inputs  from options on a cross-currency basis. Where there are insufficient data points for this approach, one would take the intrinsic value of the option and construct  a  hybrid  curve  by  comparing  the  forward  OIS,  EONIA  and SONIA curves and taking the maximum value at each point in time, or conversely  the  minimum  value.  Collateral  agreements  implying  other optionalities are similarly constructed and where the collateral currency is  different  from  trade    currency,  a  cross-currency  basis  adjustment  will need to be made.

A multi-currency 'hybrid' curve is not a smooth curve as such, because as one moves from one currency to another this creates a kink (analogous to the problem one has in constructing conventional curves when moving from money market to futures input rates, or from money market to bond or swap rates). The example shown at Figure 8.4 plots the cross currency basis adjusted discount curves for USD swaps under four CSA scenarios: USD cash only, EUR cash only, GBP cash only, and choice among USD/EUR/ GBP cash. As shown, at each point in time, the orange hybrid curve overlaps with exactly one of the three single currency curves and only three curves can be seen at any given time.

In summary, we would conclude that derivatives valuation is now in the cash valuation environment, namely:

- ◾ If collateralised, use OIS discounting;
- ◾ If uncollateralised, use the bank's internal FTP cost-of-funds (COF) discounting curve.

FIGURE 8.4 Example of a multi-currency curve.

<!-- image -->

CSA terms exhibit wide variation and this influences the choice and build of the discounting curve. A bank free to post collateral in any currency will construct a multi-currency curve, to assist in posting:

- ◾ the currency of highest return; or
- ◾ the currency of lowest funding cost.

Bear in mind that a derivatives portfolio is essentially a long-dated funding requirement (to the expected or contractual maturity date of the longest-dated derivative on the book) - this calls for sensible term funding policy, articulated in the bank's Derivatives Funding Policy. The terms of such a policy are discussed in Chapter 11 of the author's book Moorad Choudhry Anthology .

## Derivatives Funding Curves

For  a  derivatives  trading  book,  funding  curves  need  to  be  dynamic  but above all reflect the bank's actual cost of funds (COF). This means generally re-setting the derivative funding spreads quarterly or more often if there is a volatile market. Generally, the Treasury department derivatives funding curve is a function of the overall COF curve. That way Treasury is pricing  off  a  single,  consistent,  mid-market  funding  curve. The  curve  should incorporate  orthodox  term  structure  principles,  because  the  derivatives book cash flows will be long-dated. (See Figure 8.5 for an example of the modelled   derivatives contractual and collateral cash flows tenor profile.)

<!-- image -->

-2000

FIGURE 8.5 Derivatives book modelled funding profile.

As we note, the derivatives funding curve has a term structure by definition. This ensures that trading activity takes funding requirements into consideration when pricing externally for customers. This ensures that the business line considers its expected funding requirements and cost of funding as part of its trading strategy. However, a funding spread term structure is difficult to implement under an orthodox discount curve differential approach. For example, a common valuation methodology for pricing at inception  is  to  compare  the  PV  of  a  trade  when  discounted  off  the  spot curve to the PV when discounted by a shifted curve. When a flat funding spread curve is used, this is approximated by a parallel shift of the curve. However, due to the nature of interest rate curve construction, interpolation, and tenor point set-up, this produces inconsistent highly oscillating forward rates (see Figure 8.6).

Using a discount curve differential approach requires smooth forwards. In essence we require continuous forwards which are straightforward for the business line to apply. Under the discount curve differential approach, we would have to have different discount curves for each desired funding tenor  -  which  is  not  practical. Therefore  we  cease  using  discount  curves and instead apply the funding curve term structure directly to the designated derivative exposure amount. In other words, for transaction pricing we should calculate the funding costs of the expected transaction exposure (EE) directly off the funding spread curve - which is built from the bank's COF curve. Also, the curve interpolation methodology should be one that

minimises forward rate oscillation.

The bank's internal funding curve is the one used as the baseline for its FTP regime. Liquidity risk management principles dictate that customer pricing reflects the bank's COF: this is the liquidity premium input to customer loan pricing, for example. In other words, the business line internal pricing reflects the bank's COF, which is the key ingredient of the FTP mechanism. Of course, there is more than one COF curve, reflecting the different types of funding that make up the liabilities side of the bank's balance sheet (see the example at Figure  8.7). The actual FTP curve used (and there may not necessarily be one curve for all the bank's business lines) may be an average of the various different COFs - what the author calls the weighted average cost of funds curve (WACF) - or it may be a single one based on the highest COF. The bank's current and intended balance sheet shape and structure will influence the approach taken to setting the internal FTP curve.

A real-world  example  of  the  kind  of  issues  that  would  be  discussed when it comes to implementing a funding curves procedure in a bank is given at the   Appendix to this chapter.

FIGURE 8.6 Example of forward curve oscillation arising from using flat term structure and parallel shift.

<!-- image -->

FIGURE 8.7 Bank COF curves.

<!-- image -->

## APPENDIX

## ALCO submission

Author:

Moorad Choudhry GBM Treasury

Global Banking &amp; Markets

135 Bishopsgate London EC2M 3UR

Date:

22 July 2011

Subject:

Proposal to formalise the procedure for producing the GBM cross-currency yield curve and recovery-rate adjusted yield curve in G11 currencies

As part of BAU certain business lines in FICC and ESR undertake issuance in or linked to currencies outside the 'core' GBM currencies of GBP, EUR and USD. This creates a funding pricing requirement in the transacted currency  and  a  cross-currency  hedge  exposure  that  is  addressed  with  crosscurrency basis swaps. Currently there is no formal procedure in GBM that is addressed to all business lines. Business best-practice calls for an explicit procedure to be centralised across the firm, to avoid the operational risk and opacity associated with individual desks applying their own risk management practices. This requires a cross-currency (XCCY) TLP curve to be published by the internal funding desk.

A related issue concerns the curve to be used for CLN issuance and secondary market marking of RBS bonds. This would be calculated with the appropriate  recovery-rate  (RR)  adjustment  from  the  baseline  risky  TLP  curve published by FFP on a daily basis. The procedure for the baseline curve has already been ratified by GBM ALCO. [1]

This proposal outlines procedures for publishing the XCCY and RR-adjusted curves in GBM in G11 currencies. It has been reviewed and agreed within FICC, as well as by Market Risk, FFP and QARC. If adopted, this procedure would not apply to currencies outside this grouping, which would remain within the existing procedure.

<!-- image -->

## Background

Issuing liabilities in or linked to non-core currencies that are not required to  fund  GBM  assets  creates  the  need  for  a  cross-currency  hedge  when exchanging the proceeds into usable currencies. This raises correlation and RBS funding quanto risk management risk exposures that must be managed dynamically (see Appendix 1). This issue is not new, but has become pertinent since the banking crisis because the impact of the correlation relationships on pricing and hedging is now material (due to higher and more volatile  bank  funding  spreads,  and  due  to  greater  focus  on  funding  risk management). [2] Theoretically the issue is one of determining the relationship between the funding risk premia for two different currencies and their volatility, and how the no-arbitrage assumption is affected. [3]

Practically, this raises a need for risk management on a dynamic basis. Thus, every business line that undertakes transactions in this space must allow for, and incorporate, quanto corrections into its hedging process. However, this would result in a large number of correlation adjustments to the baseline funding curve, reflecting the individual business lines, as well as separate hedging  arrangements.  This  is  not  business  best-practice,  which  recommends a centralised procedure for the curve adjustment and the hedge.

In the secondary market, RBS bonds trade at material premium or discount to  par.  Current  business  best-practice  is  for  the  mark  on  these  bonds  to include an element of non-100% RR. This requires a RR-adjustment to the baseline curve.

Under the accepted logic of a unified bank risky credit curve, GBM would operate in this space as follows:

- ◾ GBM FFP desk publishes the baseline funding curve in EUR for all the GBM business  lines  (this  procedure  was  ratified  at  April  2011  GBM ALCO and is now live);
- ◾ FFP publishes (i) a funding curve in every currency that GBM conducts business in and (ii) a RR-adjusted funding curve, both calculated from the baseline curve.

The curves would ideally reflect the correlation values relevant to the business line, however this is secondary to the need to make the procedure tractable and unified for all business lines.

## Recommended procedure: XCCY curve

To address these issues and to move to business best-practice arrangements, we recommend the following procedure:

## 1- FFP desk publishes XCCY TLP curves, as follows:

quanto adjustment.

ForeignTLP EURTLP xccy basis swap This is updated daily automatically .

The business line will then be able to deposit proceeds with the FFP desk, which will swap these into a core currency using a XCCY basis swap in the conventional manner. The quanto adjustment for 'core' currencies may not be material, and for USD and GBP could for practical intents and purposes be ignored. However to maintain consistency across all business lines the procedure will be uniform for all non-EUR currency curves. For non-core currencies the adjustment is expected to be material.

2- The parameter inputs used to convert the baseline curve (volatility surface and correlations) will be the responsibility of GBM Treasury. Advice will be obtained from the business lines, for instance by the Emerging Markets desk, when deciding on inputs. Correlation and volatility values will be input to MDX, and used by FFP to obtain the XCCY TLP. Parameter values will be reviewed by Market Risk and GBM Treasury. The quanto adjustment calculation based on the inputs supplied in MDX will be integrated in CAF, so that those using the same inputs obtain the same result.

The FFP desk will be set quanto risk limits, which will act to control overall GBM risk exposure in this space. Senior trading management in GBM will appreciate that there is noise in this business, hedge costs etc, and this will get attributed back to GBM pro rata at each year-end. This reflects the logic that the cost of managing this risk is a cost of doing business, therefore this cost will be borne by the business.

The FFP desk will not be a profit centre for this business. As the target is a zero PnL, the bid-offer spread will set as narrow as possible to facilitate this.

The above procedure results in a single, transparent process for the entire GBM business. It will also enable Market Risk to monitor exposures with greater clarity.

Note that the process of accepting currencies into one centralised desk, and assuming the portfolio's flow is non-totally self hedging, FFP will accumulate  market  risk  and  basis  exposures. This  will  need  to  be  managed  in  a separate hedge book. The procedure and infrastructure for this is currently under discussion will be addressed in a separate, parallel procedure to the XCCY curve procedure.

The swap hedge book will have a zero PnL target. It will operate in a markto-market environment. This is because future contingent claims need to be  turned into expected present values.  That is, anticipated dynamic hedging gains/losses are  turned into a certainty equivalent in the risk-neutral measure.

The benefit of this procedure is a unified approach for non-core G11 currency transactions.

## Recommended procedure: RR-adjusted curve

An RR-adjusted curve is required to mark products such as: secondary market RBS-issued bonds that are trading below par, RBS-issued CLNs from Day 1, and long-dated zero-coupon RBS issued bonds. This is because the business  lines  need  to  account  for  the  RBS  RR  when  valuing  the  bonds, because a non-zero assumed RR impacts the expected cash flow.

The baseline TLP curve is constructed using a methodology that does not account for the RR at any value [1]. To address the above issues and to move to business best-practice arrangements, we recommend the following procedure:

- 1-  FFP apply a RR adjustment to the baseline curve assuming an RR of between 30% and 40%, the level to be set by GBM Treasury. This reflects historical observation and market practice.
- 2- FFP publish the curve daily, using parameter inputs supplied by the business lines.

The parameter inputs will be reviewed on a regular basis by Market Risk and GBM Treasury. The two procedures will be linked. FFP will be publishing XCCY TLP curves with an implied RR. The RR will be the same across all currencies.

## REFERENCES

- [1]  RBS GBM, Formalising the procedure for constructing the GBM internal yield curve , ALCO Submission paper, April 2011 (Agenda Item 5: Internal Curve Methodology Paper)
- [2]  Bianchetti, M., 'Two curves, one price', Life and Pension RISK , October 2010, pp. 38-44
- [3]  Geman, H., and R. Souveton, 'No-Arbitrage Between Economies and Correlation Risk Management', Computational Economics , Vol 10, No 2, 1997, pp. 119-138

## Discussion Note

Author:

Moorad Choudhry

Global Banking &amp; Markets 135 Bishopsgate London EC2M 3UR

Date:

7 March 2011

Subject:

Issues in risk management: cross-currency basis and correlation risk

GBM is currently exposed to risk arising from transactions in non-core and emerging market (EM) currencies. This paper discusses the nature of this risk; a separate paper presents a proposal for optimum hedging of this risk and the associated infrastructure required.

This risk exposure is a live issue because this business is currently being undertaken; going forward it is imperative that RBS seeks to manage the risks on an efficient and business best-practice basis. Currently the issuing desk manages the resulting risks; while this is common practice in banks, the purpose of this note is to raise for discussion whether another arrangement may be preferred.

## Background

The Hybrids and EM desks, in particular, issue structured notes (SMTNs) and credit-linked notes (CLNs) in currencies other than core ones. Often this  is  because  of  an  opportunity  to  generate  arbitrage  funding,  and/or to derive benefit from the embedded derivative. Issuing such notes raises funds in non-core currencies, for which RBS London has no requirement. These funds therefore have to be exchanged into a core currency such as EUR or USD.

This  business  creates  a  requirement  for  GBM  to  be  able  to  risk  manage swapped FX balances in a range of exotic currencies. A further complication is that these may be freely convertible, for example Israeli shekel (ILS)  or not at all convertible, for example Brazilian real (BRL).

Currently, the internal funding desk (FFP) is not set up take deposits in such currencies. This means that the issuing desk must use cross-currency basis swaps in order to remit the Day 1 hard currency (usually US dollar, USD) equivalent. This is placed with the FFP desk, which pays the standard term rate for the core currency deposit.

<!-- image -->

The process of turning the exotic currency issue into a term EUR or USD deposit creates cross-currency, quanto and correlation risks that the issuing desk has to manage. Borrowing and lending in exotic currencies that are always basis-swapped back to 3-month EUR or USD creates a dynamic hedging requirement. The risk exposures reflect continuous fluctuations in FX rates,  swap  rates  and  the  RBS  credit  spread,  as  well  the  correlations between these factors.

The  process  of  managing  ongoing  dynamic,  credit/correlation-dependent risk exposures requires consistent, advanced treatment.

## Risks arising when funding is cross-currency basis swapped

Assume an issuer who reports in say USD that issues a term liability in an emerging market currency, such as ILS. In addition to placing the bonds with an investor, his arranger will also give him a collateralised swap to  immunise him to the  structured coupons due to the bondholder and instead leave the issuer paying  USD funding according to his funding target.

In this  'cross currency' case, that swap will feature front-end  /  back-end principal exchanges to transform issue proceeds into hard currency on Day 1, and then back into local currency at maturity. In this manner, the issuers have always  believed they have  generated hard currency liquidity for the life of the deal, with no further complications.

In fact this is not accurate, and recent experience has shown that the additional risks that arise can be material. One is due to linkages between FX markets and the issuer's credit. The other is due to the cost/benefit of collateral postings due under the embedded derivative.

## Correlation risks

The quantum of hard currency liquidity the investor perceives as  generated is in fact based on the local currency nominal amount, combined with the initial FX rate. His valuation of this is ideally represented as a  deposit on accreting nominal.

Assume that the FX rate moves: the issuer would have to adjust both nominal of the hard currency deposit used to represent and value the use of proceeds, and also the basis swaps  /  FX forward trades which  transformed this liquidity from ILS to USD. To keep the portfolio risk neutral,  the FX move implies  a  number of dynamic rebalancing  trades, in both forward FX and also in 'deposits' of the issuer.

In a frictionless market, and in the absence of any systematic correlation between the FX rate and the Issuer's cost of funds, this adjustment will be little  more  than 'noise'.  Over  time,  the  expectation  would  be  that  such rebalancing would not make or lose any money for the issuer. As long as it keeps re-hedging frequently, it would count itself lucky  (unlucky) should a  major  market move happen just before the adjusted hedge for the latest mismatch.

Market data, and GBM's experience, suggests systematic linkage between FX rates and the credit spread of risky issuers. For example, Lat-Am countries and currencies coming under pressure, will mean that RBS will have to claw money back from its term buffer and reduce its valuation of liquidity raised by issuing in those currencies. Therefore one can perceive that this scenario produces a rise in RBS's cost of funds.

Quantifying the ex ante expected losses under this scenario produces the so-called 'quanto adjustment' arising from this effect. In our context, one would consider the Libor + X spread we use to communicate our cost of funds in USD, reduce the spread by the quanto adjustment, and express the equivalent ILS funding curve using the reduced 'spread.'

## Collateral Risks

Valuation  aside,  the  typical  booking  setup  will  result  in  requirement  for collateral postings. This is because the hedging swap is secured via a credit support annexe (CSA) but the bond and funding representation trades are unsecured. This topic is well documented elsewhere (see my note on SMTN issuance operating model issues) and we omit further details for brevity. For our purposes we note that:

(a) the size of this exposure is both variable and links dynamically to various deal parameters

(b) the presence of large principal exchanges in these swap deals means these exposures can accumulate much faster for the issuer than they would if he only ever issued in his reporting currency (and as a result these large flows were not present in his hedging swaps).

I think that people should be recognized for their achievements and the value that adds to society's progress. But it can be easily overdone. I think highly of many people and their accomplishments, but I don't believe that that should be paramount over the actual achievements themselves. Celebrity shouldn't supersede the things they've accomplished.

-- Neil Armstrong, quoted in James Hansen, First Man: The Life of Neil Armstrong , Simon &amp; Schuster, 2005

<!-- image -->

## Negative Interest Rate Analytics 1

I n this chapter, we consider the issues arising in a comparison of negative with positive interest rates, principally with respect to discount factors, the yield to maturity, and different compounding schemes. This is an area of practical concern for banks in the post-2008 era, given that negative interest rates have become almost a 'norm' in the eurozone and also in, for example, the German and Swiss government bond markets. With respect to the orthodox discipline of bank asset-liability management (ALM) therefore, it is necessary for cash managers to be aware of the specific issues surrounding a negative interest yield curve.

## THE DISCOUNT FACTOR

Discount  factors  translate  money  through  time  and  for  positive  interest rates the value of money is worth more today than in the future. Orthodox financial analysis assumes interest rates always to be positive. In the current market environment, however, interest rates in a number of jurisdictions are close to zero and are even negative. In this section, we discuss the domain of definition of discount factors and start with the definition.

Definition: The discount factor function (DK) , or for short the discount factor d r t t ,t,t k k with  a  discount  rate  function  r t t k -1  at  an arbitrary time point t k R 1 measured in the base period defined for arbitrary t R 1 , by:

<!-- formula-not-decoded -->

and for equidistant knots t j j with r r t j j and t k 0 the evaluation in t j is then:

1   This chapter was written by Wolfgang Marty, AgaNola AG.

and

<!-- formula-not-decoded -->

We illustrate the DKs in Figure 9.1.  We consider three discount factors for t 1 1, t 2 2 and t 3 3 and for all t we assume r t r t r t r t r 1 2 3 . We discuss the DFs as a function of r.

First of all, there is a singularity in 1, that is, the DK is not defined 1, and we discuss three pieces of the domain of definition of the DKs. For r 1, the values of the DKs are meaningless and are deemed by the business to be not relevant values .  For r 1 the business relevant values of  the  DK are covered. For  1 0 r , the DK are unbounded for r towards 1. Thus for negative value of r the money is growing in the future. For r 0, we have the traditional situation where the value of the money is declining in the future. For r 0, the value of the money stays the same and is unchanged in the future.

For r 1, the sign of the derivative is alternating and as we have by (1):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

we see the DKs are monotonically decreasing and the curvature is   positive. The appreciation of the DK is bigger for negative interest than the deprecation of the DK for positive interest rate for the same absolute of the interest rate. This is expressed by the convexity of the DK.

FIGURE 9.1 Discount factors.

<!-- image -->

## EXAMPLE 9.1 WE CONSIDER A DISCOUNT FACTOR OVER A UNIT PERIOD

FIGURE 9.2 Compounding effect.

<!-- image -->

If the unit time in (2) is a year, then (2) is the base for annual compounding. Over the unit interval it is not specified how the return over [0, 1] is distributed. For instance, the return can be distributed twice a year without being reinvested or daily when considering the coupon of a bond (Accrued Interest). In (2) there is no reinvestment. The money is either spent or kept until the end of the year. Compounding is only essential for time spam over a period. So, (2) is the same as:

<!-- formula-not-decoded -->

We can say that (1) mirrors continuously compounding, i.e. money grows less at the beginning than at the end of the interval.

In Figure 9.3 we show the difference of the DKs in the time 1 to 2 minus the DK in the time 0 to 1 rebased at time 1. It shows again the convexity of the DKs. For interest, with the same absolute value, the deprecation of the DK for negative interest rate is more pronounced compared to the appreciation of the DKs for positive interest rates. In Figure 9.2 the variable is the interest rate and in Figure 9.3 the variable is the time.

<!-- image -->

Definition : Compounding is  the  reinvestment  of  the  income  to  earn more income in the subsequent periods. If the income and the gains are retained within the investment vehicle or reinvested, they will accumulate and contribute to the starting balance for each subsequent period's income calculation.

Referring to the definition above, we distinguish between calculating the  end  value  of  investment  and  determining  the  internal  rate  of  return assuming an underlying reinvestment assumption. We illustrate the difference with the following examples.

## EXAMPLE ILLUSTRATIONS

In the first example, we consider the discount factor:

<!-- formula-not-decoded -->

Table 9.1 shows that the difference to 1 is different for different signs of the interest rate. In addition, we see that the sequences are not unbounded and are converging faster for interest closer to 0. For example for positive interest rates, the DKs are smaller than 1, which means the value today is less than in the future and for a fixed amount today, the future value is increasing with increasing n. For r 0 05 5 . %  annualised rate, with an initial value of $100 we obtain the following end values EV n n , , 1 2, , namely:

TABLE 9.1 First example results

| r   |   -0.05 |   -0.01 |    0.00 |    0.01 |    0.05 |
|-----|---------|---------|---------|---------|---------|
| 1   | 1.05263 | 1.01010 | 1.00000 | 0.99010 | 0.95238 |
| 2   | 1.05194 | 1.01008 | 1.00000 | 0.99007 | 0.95181 |
| 3   | 1.05171 | 1.01007 | 1.00000 | 0.99007 | 0.95162 |
| 4   | 1.05160 | 1.01006 | 1.00000 | 0.99006 | 0.95152 |
| 5   | 1.05154 | 1.01006 | 1.00000 | 0.99006 | 0.95147 |
| 6   | 1.05149 | 1.01006 | 1.00000 | 0.99006 | 0.95143 |
| 7   | 1.05146 | 1.01006 | 1.00000 | 0.99006 | 0.95140 |
| 8   | 1.05144 | 1.01006 | 1.00000 | 0.99006 | 0.95138 |
| 9   | 1.05142 | 1.01006 | 1.00000 | 0.99006 | 0.95136 |
| 10  | 1.05140 | 1.01006 | 1.00000 | 0.99005 | 0.95135 |
| 100 | 1.05128 | 1.01005 | 1.00000 | 0.99005 | 0.95124 |
| exp | 1.05127 | 1.01005 | 1.00000 | 0.99005 | 0.95123 |

EV1  = $105.000000 (Annual);

EV2  = $105.062500 (Semi-annual);

EV4  = $105.094534 (Quarterly);

EV ∞ = $105.127110 (Continuous).

In Figure 9.4 exp represents the continuously compounding curve, assuming  that  proceeds  are  reinvested  instantaneously.  The  series  grows  not unbounded, but it is a series that is increasing as it is bounded.

In the next example, we consider:

<!-- formula-not-decoded -->

for r fixed and given. We solve for:

<!-- formula-not-decoded -->

and for n towards infinity we have:

<!-- formula-not-decoded -->

In Figure 9.4 ln 1 r  represents the continuously compounding or differently expressed n towards infinity in Table 9.2.

<!-- image -->

Interest rate

FIGURE 9.4 Continuously compounding.

TABLE 9.2 Second example results

| r       |    -0.05 |    -0.01 |    0.00 |    0.01 |    0.05 |
|---------|----------|----------|---------|---------|---------|
| 1       | -0.05000 | -0.01000 | 0.00000 | 0.01000 | 0.05000 |
| 2       | -0.05064 | -0.01003 | 0.00000 | 0.00998 | 0.04939 |
| 3       | -0.05086 | -0.01003 | 0.00000 | 0.00997 | 0.04919 |
| 4       | -0.05097 | -0.01004 | 0.00000 | 0.00996 | 0.04909 |
| 5       | -0.05103 | -0.01004 | 0.00000 | 0.00996 | 0.04903 |
| 6       | -0.05107 | -0.01004 | 0.00000 | 0.00996 | 0.04899 |
| 7       | -0.05111 | -0.01004 | 0.00000 | 0.00996 | 0.04896 |
| 8       | -0.05113 | -0.01004 | 0.00000 | 0.00996 | 0.04894 |
| 9       | -0.05115 | -0.01004 | 0.00000 | 0.00996 | 0.04892 |
| 10      | -0.05116 | -0.01005 | 0.00000 | 0.00996 | 0.04891 |
| 100     | -0.05128 | -0.01005 | 0.00000 | 0.00995 | 0.04880 |
| ln(1+r) | -0.05129 | -0.01005 | 0.00000 | 0.00995 | 0.04879 |

## THE YIELD TO MATURITY

The yield to maturity (YTM) of a bond is probably the most popular yield measurement of a bond, although it is has its well-known deficiencies and weaknesses. The yield of maturities is based on a non-arbitrage condition. The market price of a bond is equal to the future cash flows of the bond and the yield of maturity is a solution of this equation. The solution can in general not be calculated by simple algebraic manipulation, but a numerical procedure has to be used instead. Although this equation has in general many solutions (see Shostapoloff and Wolfgang, 2011) it is usually assumed that there is a locally unique solution near zero. If the solution is zero, it means the market price is equal to the sum of the future cash flows. Traditionally, the solutions are positive, but in recent market movement the yield to maturity has been slightly lower than zero. If the solution is negative, the sum of the cash flow is lower than the market price.

## EXAMPLE 9.2 YTM OF SWISS GOVERNMENT BONDS

The bonds issued by the Swiss Government are called Eidgenossen. In Figure 9.5 we see a scatter plot of YTM, i.e. a graphical representation of the time versus YTM. The yield curve is normal and the yields of  the  short  end  are  negative.  For  the  analytics  of  yield  curves  see Wolfgand (2017).

Source : Based on data from SIX Exchange. FIGURE 9.5 YTM of Eidgenossen.

<!-- image -->

<!-- image -->

## SELECTED BIBLIOGRAPHY AND REFERENCES

Shestopaloff, Y., and Wolfgang, M., 'Properties of the IRR equation with regards to the ambiguity of calculating the rate of return and a maximum number of solutions', Journal of Performance Measurement 15(3), 2011, pp. 302-310.

Wolfgang, M., Fixed Income Analytics , Springer, Cham International Publisher, 2017.

Do I stick with life as I know it, be happy and content with the considerable challenges of appreciating and improving that, or shoot for the Moon and risk being dissatisfied, finding that it wasn't what I expected, or that nothing else can match it afterwards?

-- Andrew Smith, Moondust: In Search of the Men Who Fell to Earth , London: Bloomsbury Press, 2005, page 197

P

A

R

T

<!-- image -->

## Fitting the Yield Curve

I n Part III we discuss issues around fitting the yield curve. This looks at the main methods used to fit the term structure into as smooth a curve as possible, using market rates such as bond yields. We describe the techniques, which include cubic splines and parametric interpolation techniques, and provide background information on regression splines in the Appendix.

One night, I dreamed I was back on the USS Hancock , briefing for a 2:00am flight . . . I woke up in a cold sweat, looked up at my mosquito net, and thought, 'Thank God, I'm only in a communist prison camp!' I didn't fully realize until that moment that I had talked myself into believing that I liked flying off an aircraft carrier at night to drop bombs. In reality, I had been scared ****less every time I flew over Vietnam.

-- Robert Wideman, Unexpected Prisoner: Memoir of a Vietnam POW , 2016

## Estimating and Fitting

## CHAPTER  10 the Yield Curve I

I n this chapter, we introduce some of the techniques used to fit the term structure. The yield curve models described in the previous chapter defined the interest rate process under various assumptions about the nature of the stochastic process that drives these rates. However, the zero-coupon curve derived by models such as those described by Vasicek (1977), Brennan and Schwartz (1979), and Cox, Ingersoll and Ross (1985) do not fit the observed market rates or spot rates implied by market yields, and generally market yield curves are found to contain more variable shapes than those derived using term structure models. Hence the interest rate models described in Chapters 5 and 6 are required to be calibrated to the market, and in practice they are calibrated to the market yield curve. This is carried out in two ways - the model is either calibrated to market instruments such as money market products and interest rate swaps, which are used to construct the yield curve, or the yield curve is constructed from market instrument rates and the model is calibrated to this constructed curve. If the latter approach is  preferred,  there  are  a  number  of non-parametric methods that may be used. We will consider these later.

The academic literature contains a good deal of research into the empirical estimation of the term structure, the object of which is to fit a zerocoupon curve 1   that  is  a  reasonably  accurate  fit  to  the  market  prices and is  a  smooth function. There is an element of trade-off between these two objectives. The  second  objective  is  as  important  as  the  first,  however,  in order to derive a curve that makes economic sense. In other words, it is possible to fit the curve perfectly at the expense of smoothness, but this renders the exercise almost meaningless. Market practitioners require smooth curves to make the process of pricing and valuation more straightforward.

1 The  zero-coupon  or  spot  curve,  or  equivalently  the  forward  rate  curve  or  the discount function - all are describing essentially the same thing.

In this chapter, we present an overview of some of the methods used to fit the yield curve. By the way, an excellent overview of the approaches described  here  is  given  in Anderson et  al .  (1996),  but  unfortunately  this book has been out of print for many years.

## YIELD CURVE SMOOTHING

An early approach used to estimate the term structure was described by Carleton and Cooper (1976). It assumes that default-free bond cash flows are payable on specified discrete dates, with a set of unrelated discount factors that apply to each cash flow. These discount factors are then estimated as regression coefficients, with each bond cash flow acting as the independent variables, and the bond price for that date acting as the dependent variable. 2  Using simple linear regression in this way produces a discrete discount function, not a continuous one, and forward rates that are estimated from this  function  are  very  jagged. An approach more readily accepted by the market was described earlier by McCulloch (1971), who fitted the discount function  using  polynomial  splines.  This  method  produces  a  continuous function, and one that is linear, so that the ordinary least squares regression technique can be employed. In a later study, Langetieg and Smoot (1981) 3 used an extended McCulloch method, fitting cubic splines to zero-coupon rates  instead  of  the  discount  function,  and  using  non-linear  methods  of estimation.

So much for the historical summary of early efforts. But let us get back to  the  beginning.  We  know  that  the  term  structure  can  be  described  as the complete set of discount factors, the discount function, which can be extracted from the price of default-free bonds trading in the market. The standard bootstrapping technique may be used to extract the relevant discount factors. However, there are a number of reasons why this approach is problematic in practice. First, it is unlikely that the complete set of bonds in  the  market  will  pay  cash  flows  at  precise  six-month  intervals  every six months from today to 30 years or longer. An adjustment is made for cash flows received at irregular intervals, and for the lack of cash flows available at longer maturities. Another issue is the fact that the technique presented earlier allows practitioners to calculate the discount factor for six-month maturities, whereas it may be necessary to determine the discount factor for non-standard periods, such as four-month or 14.2-year maturities. This is often the case when pricing derivative instruments.

2   The basics of regression are summarised briefly in Appendix 10.1.

3   Reference in Vasicek and Fong (1982).

A third issue concerns the market price of bonds. These often reflect specific investor considerations, which include:

- ◾ the  liquidity,  or  lack  thereof,  of  certain  bonds,  caused  by  issue  sizes, market-maker support, investor demand, non-standard maturity and a host of other factors;
- ◾ the fact that bonds do not trade continuously, so that some bond prices are 'newer' than others;
- ◾ the tax treatment of bond cash flows, and the effect that this has on bond prices;
- ◾ the effect of the bid-offer spread on the market prices used.

The statistical term used for bond prices subject to these considerations is error . It is also common to come across the statement that these effects introduce noise into market prices.

To construct a fit to the yield curve that better handles the above considerations, smoothing techniques  are  used  to  derive  the  complete  set  of discount  factors  from  market  bond  prices,  known  as  the  discount  function. Using the simple technique presented in Chapter 2, we graph the discount function for the UK gilt prices as at 12 June 2000. This is shown at Figure 10.2. The yield curve plotted from gilt redemption yields is shown at Figure 10.1. Figure 10.3 shows the zero-coupon yield curve and forward rate curve that correspond to the discount function from the date.

From  Figure  10.2,  we  can  see  that  the  discount  function  is  quite smooth,  while  the  zero-coupon  curve  is  also  relatively  smooth,  although not as smooth as the discount function. The forward rate curve is distinctly

FIGURE 10.1 Gilt gross redemption yields, 12 June 2000. Source : © Bloomberg LP. Reproduced with permission.

<!-- image -->

FIGURE 10.2 Discount factors from gilt prices, 12 June 2000.

<!-- image -->

FIGURE 10.3 Zero-coupon (spot) and forward rates obtained from gilt yields, 12 June 2000.

<!-- image -->

'unsmooth', (if the reader will permit such as an expression), and there is obviously something wrong. In fact the jagged nature of implied forward rates is one of the main concerns of the fixed income analyst, and indicates in the first instance that the discount function and zero-coupon curve are not as smooth as they appear. Using the estimation method here, the main reason why the forward rates oscillate wildly 4  is that minor errors at the discount factor stage are magnified many times over when translated into the forward rate. That is, any errors in the discount factors (and these errors may stem from any of the reasons given above) are compounded when spot rates are calculated from them, and these are compounded into larger errors when calculating forward rates.

4   When writing the first edition, I'd been looking for an excuse to use this expression, for an obscure reason that was revealed with reference to Goddard (2002), p. 140. . . ☺

## SMOOTHING TECHNIQUES

A common technique that may be used, but which is not accurate and so not recommended, is linear interpolation . In this approach the set of bond prices are used to graph a redemption yield curve (as in the previous section), and where bonds are not available for the required maturity term, the yield is interpolated from actual yields. Using gilt yields for 26 June 1997, we plot this as shown at Figure 10.4. The interpolated yields are those that are not marked by a cross. Figure 10.4 looks reasonable for any practitioner's purpose. However, spot and forward yields that are obtained from this curve are likely to behave in an unrealistic fashion, as shown in Figure 10.5. The forward curve is very bumpy, and each bump corresponds to a bond used in the original set. The spot rate has a kink at 21.5 years, and so the forward curve jumps significantly at this point. This curve appears to be particularly unrealistic.

For this reason, market analysts do not bother with linear interpolation and instead use multiple regression or spline-based methods. One approach is to assume a functional form for the discount function and estimate parameters of this form from the prices of bonds in the market. We consider these approaches next.

FIGURE 10.4 Linear interpolation of bond yields, 26 June 1997.

<!-- image -->

FIGURE 10.5 Spot and forward rates implied from Figure 10.4.

<!-- image -->

## USING A CUBIC POLYNOMIAL

A simple functional form for the discount function is a cubic polynomial . This approach consists of approximating the set of discount factors using a  cubic  function  of  time.  If  we  say  that d t is  the  discount  factor  for maturity t , we approximate the set of discount factors using the following cubic function:

<!-- formula-not-decoded -->

In some texts the coefficients are written as a , b , and c rather than a 1 , and so on.

The discount factor for t 0, that is at time now, is 1. Therefore a 0 1, and (10.1) can then be re-written as:

<!-- formula-not-decoded -->

The market price of a traded coupon bond can be expressed in terms of discount factors. So at (10.3) we show the expression for the price of an N -maturity bond paying identical coupons C at  regular  intervals  and redeemed at maturity at M .

<!-- formula-not-decoded -->

Using the cubic polynomial equation (10.2), expression (10.3) is transformed into:

<!-- formula-not-decoded -->

We require the coefficients of the cubic function in order to start describing the yield curve, so we re-arrange (10.4) in order to express it in terms of these coefficients. This is shown at (10.5):

<!-- formula-not-decoded -->

In the same way, we can express the pricing equation for each bond in our data set in terms of the unknown parameters of the cubic function. From (10.5) we may write:

<!-- formula-not-decoded -->

where Xi is the appropriate expression in square brackets in (10.5). This is the form in which the expression is encountered commonly in textbooks.

## EXAMPLE 10.1 CUBIC SPLINE FITTING EXAMPLE

A benchmark semi-annual coupon four-year bond with a coupon of 8% is trading at a price of 101.25. Assume the first coupon is precisely six months from now, so that t 1 0 5 . and so t N 4. Set up the cubic function expression.

We have C 4 and M 100 so therefore:

<!-- formula-not-decoded -->

( Continued )

This means that we now have an expression for the three coefficients, which is:

<!-- formula-not-decoded -->

The  prices  for  all  other  bonds  are  expressed  in  terms  of  the unknown parameters. To calculate the coefficient values, we use a statistical  technique  such  as  linear  regression,  such  as least  squares to find the best fit values of the cubic equation. An introduction to this technique is given at Appendix 10.1.

In practice, the cubic polynomial approach is too limited a technique, requiring one equation per bond, and does not have the required flexibility to fit market data satisfactorily. The resulting curve is not really a curve, but rather a set of independent discount factors that have been fit with a line of best fit. In addition, the impact of small changes in the data can be significant at the non-local level, so for example, a change in a single data point at the early maturities can result in 'badly behaved' longer maturities. Alternatively, a piecewise cubic polynomial approach is used, whereby d t is assumed to be a different cubic polynomial over each maturity range. This means that the parameters a 1 , a 2 and a 3 are different over each maturity range. We will look at a special case of this use, the cubic spline, a little later.

## NON-PARAMETRIC METHODS

Outside of the cubic polynomial approach described in the previous section there are two main approaches to fitting the term structure. These are usually grouped into parametric and non-parametric curves. Parametric curves are based on term structure models such as the Vasicek model or Longstaff and Schwartz model. Non-parametric curves are not derived from an interest rate model and are general approaches, described using a set of parameters. They include spline-based methods.

## SPLINE-BASED METHODS

A  spline  is  a  statistical  technique  and  a  form  of  a  linear  interpolation method. There is more than one way of applying it, and the most straightforward method to understand the process is the spline function fitted using regression  techniques.  For  the  purposes  of  yield  curve  construction,  this method can cause curves to jump wildly and be over-sensitive to changes in parameters. 5  However, we believe that it is the most accessible method to understand and an introduction to the basic technique, as described in Suits et al. (1978), is given at Appendix 10.2. 6

An n -th  order  spline  is  a  piecewise  polynomial  approximation  with n -degree  polynomials  that  are  differentiable n 1  times.  Piecewise  means that the different polynomials are connected at arbitrarily selected points known as knot points (see Appendix 10.2). A cubic spline is a three-order spline, and is a piecewise cubic polynomial that is differentiable twice along all its points.

The x -axis in the regression is divided into segments at arbitrary points known as knot points. At each knot point the slopes of adjoining curves are required to match, as must the curvature. Figure 10.6 is a cubic spline. The knot points are selected at 0, 2, 5, 10 and 25 years. At each of these points the curve is a cubic polynomial, and with this function we can accommodate a high and low in each space bounded by the knot points.

Cubic spline interpolation assumes that there is a cubic polynomial that can estimate the yield curve at each maturity gap. We can think of a spline as a number of separate polynomials of y f X where X is the complete range, divided into user-specified segments, which are joined smoothly at the knot points. If we have a set of bond yields 0 1 2 , , , n r r r r … at maturity points 0 1 2 , , , n t t t t … , we can estimate the cubic spline function in the following way:

FIGURE 10.6 Cubic spline with knot points at 0, 2, 5, 10 and 25 year tenors.

<!-- image -->

5   For instance, see James and Webber (2000), Section 15.3.

6 The original article by Suits et al . (1978) is excellent and highly recommended.

- ◾ the yield on bond i at time t is expressed as a cubic polynomial of the form r t a bt c t d t i i i i i 2 3 for the interval over t i and t i 1 ;
- ◾ the coefficients of the cubic polynomial are calculated for all n intervals between the n 1 data points, which results in 4 n unknown coefficients that must be computed;
- ◾ these equations can be solved because they are made to fit the observed data. They are twice differentiable at the knot points, and these derivatives are equal at these points;
- ◾ the constraints specified are that the curve is instantaneously straight at  the  start  of  the  curve  (the  shortest  maturity),  and  instantaneously straight at the end of the curve, the longest maturity, that is r 0 0.

An accessible and readable account of this technique can be found in Van Deventer and Imai (1997).

The general formula for a cubic spline is:

<!-- formula-not-decoded -->

where is  the  time  of  receipt  of  cash  flows,  and  where Xp refers  to  the points  where  adjacent  polynomials  are  joined,  and  which  are  known as knot points, with X X X X p n n p p 0 1 0 1 , , , , , , . In addition, X X p p max ,0 . The cubic spline is twice differentiable at the knot points. In practice, the spline is written down as a set of basis functions with the general spline being made up of a combination of these. One way to do this is by using what are known as B-splines . For a specified number of knot points  X 0 , , Xn this is given by (10.8):

<!-- formula-not-decoded -->

where Bp are cubic splines which are approximated on X Xn 0 , , with the following function:

<!-- formula-not-decoded -->

with max , , 3 1 n the  required  coefficients.  The  maturity  periods 1 , , n specify  the  B-splines  so  that ( ) { } 3, , -1, 1, , p j p n j m B B τ =- … = … = and

1 , , m . This allows us to set:

<!-- formula-not-decoded -->

and therefore the regression equation:

<!-- formula-not-decoded -->

with D CB .

are the minimum errors. The regression at (10.11) is computed using ordinary least squares regression.

An illustration of the use of B-splines is given in Steeley (1991), and with a complete methodology, by Didier Joannas in Choudhry et al . (2001).

## NELSON AND SIEGEL CURVES

The curve-fitting technique first described by Nelson and Siegel (1985) has since been applied and modified by other authors, which is why they are sometimes described as a 'family' of curves. These curves provide a satisfactory rough fit of the complete term structure, with some loss of accuracy at the very short and very long end. In the original curve, the authors specify four  parameters.  The  approach  is  not  a  bootstrapping  technique,  rather a  method  for  estimating  the  zero-coupon  rate  function  from  the  yields observed on T-bills, under an assumed function for forward rates.

The Nelson and Spiegel curve states that the implied forward rate yield curve may be modelled along the entire term structure using the following function:

<!-- formula-not-decoded -->

where;

0 1 2 1 , , , , t is the vector of parameters describing the yield curve, and m is  the  maturity  at  which  the  forward  rate  is  calculated. There  are three components, the constant term, a decay term, and a term reflecting the 'humped' nature of the curve. The shape of the curve gradually leads into an asymptote at the long end, the value of which is given by 0 , with a value of 0 1 at the short end.

A version of the Nelson and Siegel curve is the Svensson model (1994) with an adjustment to allow for the humped characteristic of the yield curve. This is fitted by adding an extension, as shown by (10.13).

<!-- formula-not-decoded -->

The Svensson curve is modelled using six parameters, with additional input of 3 and t 2 .

Nelson and Siegel curves are popular in the market because they are straightforward to calculate. Jordan and Mansi (2000) state that one of the advantages of these curves is that they force the long-term forward curve into a horizontal asymptote, while another is that the user is not required to specify knot points, the choice of which determines the effectiveness or otherwise of cubic spline curves. The disadvantage they note is that these curves are less flexible than spline-based curves and there is therefore a chance that they do not fit the observed data as accurately as spline models. 7  James and Webber (2000, pp.  444-445)  also  suggest  that  Nelson  and  Siegel  curves are  slightly  inflexible  due  to  the  limited  number  of  parameters,  and  are accurate for yield curves that have only one hump, but are unsatisfactory for curves that possess both a hump and trough. As they are only reasonable for approximations, Nelson and Siegel curves are not appropriate for no-arbitrage applications.

## COMPARING CURVES

Whichever curve is chosen depends on the user's requirements and the purpose for which the model is required. The choice of modelling methodology is usually a trade-off between simplicity and ease of computation and accuracy. Essentially the curve chosen must fulfil the qualities of:

- ◾ accuracy : is the curve a reasonable fit of the market curve? Is it flexible enough to accommodate a variety of yield curve shapes?;
- ◾ model consistency : is the curve-fitting method consistent with a theoretical yield curve model such as Vasicek or Cox-Ingersoll-Ross?;
- ◾ simplicity : is the curve reasonably straightforward to compute, that is,
- is it tractable?

7   This is an excellent article, strongly recommended: a good overview introduction to curve-fitting is given in the introduction, and the main body of the article gives a good insight into the type of research that is currently being undertaken in yield curve analysis.

The different methodologies all fit these requirements to greater or lesser extent. In practice it is worthwhile to implement more than one method, and then  observe  which  one  gives  the  most  efficient  results  over  time  before deciding on one technique.

## APPENDICES

## Appendix 10.1 Linear regression: ordinary least squares

The main purpose of regression analysis is to estimate or predict the average  value  of  a dependent variable  given  the  known  values  of  an  independent or explanatory variable. In one way it measures the relationship between two sets of data. This data may be the relationship between family income and expenditure and in this case the income is the independent  variable  and  expenditure the dependent variable. More relevant for our purposes, it can also be the relationship between the change in price of a corporate bond, priced off the benchmark yield curve, and changes in  the  price  of  a  short-dated  benchmark  bond  and  the  price  of  a  longterm bond. In this case, the price of the corporate bond is the dependent variable, while the prices of the short- and long-term government bonds are  independent  variables.  If  there  is  a  linear  relationship  between  the dependent and independent variables, we may use a regression function to determine the relationship between them. In this Appendix, we provide a basic overview and introduction to regression and ordinary least squares. Regression analysis is a key part of financial econometrics, and advanced econometric analysis is extensively used in fixed income work. For a background in basic econometrics, we recommend the book of the same name by Damodar Gujarati, published by McGraw-Hill (third edition, 1995), which is  excellent.  Gujarati's  book  is  very  accessible  and  readable,  and provides a good grounding in the topic. For more advanced applications we recommend The Econometrics of Financial Markets by Campbell, Lo, and MacKinlay (Princeton, 1997).

If our data set consists of the entire population, rather than a statistical sample of the population, we estimate the relationship between two data sets using the population regression function. Given an independent variable X and dependent variable Y it can be shown that the conditional mean E Y Xi | is a function of Xi . This would be written as:

<!-- formula-not-decoded -->

where f Xi is a function of the independent variable Xi . Equation (10.14) is  termed the two-variable population regression function and states that the average value of Y given Xi is a linear function of Xi . It can further be shown that:

<!-- formula-not-decoded -->

where and are the regression coefficients - they are unknown, but fixed parameters. The term is the intercept coefficient and is the slope coefficient. These are shown at Figure 10.7. The objective of regression analysis is to estimate the values of the regression coefficients using observations of the values of X and Y .

Equation  (10.15)  is  a  two-variable  regression  and  it  is  sometimes written as:

<!-- formula-not-decoded -->

Where  there  are  more  than  two  variables  we  use  a  multi-variable regression.

It can further be shown that given a value for Xi , the independent variable value will be clustered around the average value for Y at that Xi , in other words around the conditional expectation. The deviation of an individual Yi around its expected value is defined as:

<!-- formula-not-decoded -->

This is re-arranged to give:

<!-- formula-not-decoded -->

FIGURE 10.7 Regression line passing through value of X and Y .

<!-- image -->

where the term u i is  an  unknown  random  variable  and  is  known  as  the stochastic disturbance or stochastic error term or simply error term .  It  is written as in some textbooks.

The value of the dependent variable is the sum of two elements - the systematic or deterministic element, which is given by the regression function  above,  and  a  random  or  non-systematic  element,  which  is  the  error term. Essentially, the error term captures all those elements that have been missed out or left out of the regression model.

In practice, it is most unlikely that we have data sets available for the entire population, so we use statistical sample data instead. When regression is carried out on sample data, we use the sample regression function (SRF), which is (10.19) below:

<!-- formula-not-decoded -->

ˆ  is the estimator of ;

ˆ  is the estimator of .

The SRF is determined using a statistical technique known as ordinary least squares or OLS. This approach is covered in any number of statistics and econometrics textbooks, and we suggest Chapter 3 in Gujarati (1995). A very brief description is given here.

Let  us  expand  our  regression  model.  Assume  we  have N observations and m independent variables. Say that Yi is the i th observation on the dependent variable and Xit is  the i th  observation on the t th  independent variable. The regression function of the relationship between the dependent and independent variables is given by:

<!-- formula-not-decoded -->

and where we must estimate the 1 2 , , , m regression coefficients. This is done using OLS. From (10.20), i is the error in the model, the random element that is left out in predicting the i th value of the dependent variable. From our earlier description we know that:

<!-- formula-not-decoded -->

We require the sum of squared errors , which is given by 1 2 2 2 2 /midhorizellipsis i , and OLS determines the coefficients that minimise this sum of squared errors.

Earlier in the chapter, we  illustrated a bond  pricing equation, which was: 472 1796 7528 30 75 1 2 3 a a a . .

where:

What this expression tells us is that  30 75 . is the value of the dependent variable and there are three independent variables with values of 472, 1796, and 7528. As there are three unknowns, we require only four such bond price equations and we can solve for a 1 , a 2 , and a 3 . This may appear slightly daunting if it is to be carried out by hand, and in fact software applications are used to speed the process. Using such a package, we can calculate the values that minimise the sum of squared errors on the model.

If we say that the values are  ˆ a 1 ,  ˆ a 2 , and  ˆ a 3 , then the OLS estimate of the discount function, given the market bond prices used to derive the coefficient equations, is given by:

<!-- formula-not-decoded -->

## Appendix 10.2 Regression splines

. (1978), an excellent account of how a spline function may be fitted using regression methods. The article is

This follows the approach used in Suits et al very accessible and strongly recommended.

A standard econometric approach is that of piecewise linear regression . However, this method is not suitable for fitting a relationship that is not purely linear (such as a term structure), as illustrated by Figure 10.8.

To get around this problem, one approach is to join a series of linear

regressions, at arbitrary points specified by the user. This is described by:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In (10.23), Di is what is known as a dummy variable, with a value of 1 for all observations whenever X X X i i 1 , and a value of 0 at other times. As it stands, (10.23) is discontinuous at X 1 and X 2 , but this can be removed by imposing the following constraints:

<!-- formula-not-decoded -->

If (10.24) is substituted into (10.23) the following is obtained:

<!-- formula-not-decoded -->

FIGURE 10.8 Piecewise linear regression

<!-- image -->

The expression at (10.25) has converted a piecewise linear regression into a multiple regression. Y is the dependent variable and is regressed on three composite variables , the values for which are obtained from:

- ◾ the X data sets;
- ◾ the values for Xi at the points at which the curve is required to 'bend';
- ◾ the widths of the selected intervals;
- ◾ the three dummy variables.

As Suits et al. state, it is possible to calculate the coefficients by hand (!) but there are a number of standard software packages that the user can employ to solve the regression.

The disadvantages of piecewise linear regression if used for a number of applications, including yield curve-fitting, are two-fold; first, the derivatives of the function are not continuous, and this discontinuity can seriously distort the curve at the derivative points, which make the curve meaningless at these points. Secondly, and more crucial for yield curve applications, it may not be obvious where the linear segments should be placed - the scatter diagram of observations may indicate several possibilities. This situation may make it desirable to specify Xi at user-specified (arbitrary) points, and this makes linear regression unsuitable.

To get around these problems, we use a spline function .  For this, the linear function described by (10.25) is replaced with a set of piecewise polynomial functions. It is possible to use polynomials of any degree, but the most common approach is to use cubic polynomials. The x -axis is divided into three intervals, at the points X X X 0 1 2 , , and X 3 . These points are known as knot points and are illustrated at Figure 10.9.

FIGURE 10.9 Illustrating knot points

<!-- image -->

In Figure 10.9, the segments chosen following Suits et al., are at equal intervals. This is not essential to the procedure, however, and for applications including yield curve modelling, is not undertaken - instead the knots are placed at points where the user thinks the relationship changes most. For example, for the term structure the knots may be placed at 0-, 2-, 5- and 10-year maturities. If more than four knots are required, for instance, to go beyond to 20- and 30-year maturities, than the analyst will require a greater number of composite variables, as discussed later. The downside associated with a greater number of intervals is that, as more composite variables are required to fit the curve, there is a loss of additional degrees of freedom.

The regression relationship now becomes:

<!-- formula-not-decoded -->

where Di is a dummy variable specified by the interval i .

This time both the function described by (10.26) and its derivatives, are discontinuous at the knot points, but this feature can be removed by applying constraints to the coefficients. The constraints ensure the following:

- ◾ for a i the values of the very short end and the very long end are equal at the start and end knot points;
- ◾ for b i the first derivatives, the slope of the left- and right-hand sides of each knot point, are equal;
- ◾ for c i the second derivatives are equal.

The constraints are given by (10.27):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Using the expression above, a spline function becomes a multiple regression of the dependent variable Y on five composite variables and Suits et al. show this to be:

<!-- formula-not-decoded -->

where D 1 * and D 2 * are dummy variables where Di * 1 if X Xi , at other times the dummy variable is equal to 0. To compute the coefficients, the regression we can use is the least-squares procedure, available on standard software packages.

Finally,  if  we  wish  to  select  more  than  three  intervals,  that  is  more than  four  knot  points,  which  is  common  in  yield  curve  applications,  we can  use  (10.29)  below,  derived  in  Suits et  al. (1978).  This  is  a  multiple regression, a fitted spline function with n 1 intervals, with knot points at X X X Xn 0 1 2 1 , , , , and corresponding dummy variables * * * 1 2 , , , n D D D …

<!-- formula-not-decoded -->

With each extra interval, an extra composite variable is required and this results in the loss of one more degree of freedom.

## SELECTED BIBLIOGRAPHY AND REFERENCES

Anderson, N., Breedon, F., Deacon, M., Derry, A. and Murphy, M., Estimating and Interpreting the Yield Curve , Wiley, 1996.

Carleton, W. and Cooper, I., 'Estimation and uses of the term structure of interest rates', Journal of Finance , September 1976, pp. 1067-1083.

- Choudhry, M., Joannas, D., Pereira, R. and Pienaar, R., Capital Market Instruments: Valuation and Analysis , FT Prentice Hall, 2001.
- Deacon, M. and Derry, A., 'Estimating the Term Structure of Interest Rates', Bank of England Working Paper No 24, July 1994.
- Goddard, S., The Smiths : Songs That Saved Your Life , Reynolds &amp; Hearn, 2002.
- Gujarati, D., Basic Econometrics , 3rd edition, McGraw-Hill, 1995.
- James, J. and Webber, N., Interest Rate Modelling , Wiley, 2000.
- Jordan, J. and Mansi, S., 'How well do constant-maturity treasuries approximate the on-the-run term structure?', Journal of Fixed Income 10:2, September 2000, pp. 35-45.
- McCulloch, J.H., 'Measuring the term structure of interest rates', Journal of Business , January 1971, pp. 19-31.
- Questa, G., Fixed Income Analysis for the Global Financial Market , Wiley, 1999.
- Steeley, J.M., 'Estimating the gilt-edged term structure: basis splines and confidence intervals', Journal of Business Finance and Accounting 18, 1991, pp. 513-530.
- Suits, D., Mason, A. and Chan, L., 'Spline functions fitted by standard regression methods', Review of Economics and Statistics 60, 1978, pp. 132-139.
- Tuckman, B., Fixed Income Securities , Wiley, 1996.
- Van Deventer, D. and Imai, K., Financial Risk Analytics , Irwin, 1997.
- Vasicek, O. and Fong, H.G., 'Term structure modelling using exponential splines', Journal of Finance 37(2), May 1982, pp. 339-348.

Disappointments and setbacks have to be faced in life. There must be no recriminations. I had learnt this lesson when I was dropped from the Marlborough XI on the morning of our match against Rugby at Lord's. There is always something else ahead.

-- Lt. Gen. Sir Hugh Stockwell, quoted in Turner, B., Suez 1956 , London: Hodder and Stoughton, 2006

## CHAPTER  11 Estimating and Fitting the Yield Curve II

T here are a number of techniques that can be used to fit the yield curve. These include the regression methods and spline techniques introduced in  Chapter 10. More recent methods such as kernel approximations and linear  programming are  also  used  by  practitioners.  In  this  chapter,  we provide an introduction to some of these. We discuss fitting the spot and forward yield curve, and review the methods used to estimate spot and   forward yield curves.

For a number of reasons, practitioners, investors, central  banks,  and government authorities are interested in fitting the zero-coupon yield curve, or the true term structure of interest rates, from market observed yields. Practitioners  used  the  curve  for  valuation  and  investment  decision  making, whilst central banks use it for this as well as monetary policy formulation. The use of yield curves is standard in monetary policy analysis, and central banks use forward interest rates for this purpose as well. Forward rates  must  be  estimated  from  the  yield  curve  that  has  been  constructed from current market yields, generally T-bill and government bond yields. Particularly useful information that can be derived from government bond prices includes the yield curve for implied forward rates, as these reflect the market's expectations of the future path of interest rates. 1  They are also used by the market to price bonds and determine the extent of the credit spread applicable to corporate bonds. The requirements of the monetary authorities, however, are slightly different to those of market practitioners. Central bankers and the government are not so concerned with the accuracy of the spot curve with regard to pricing securities, but rather, they are interested in the information content of the fitted curve, particularly concerning implied forward rates and the market expectations of future interest rates and levels of inflation.

1   From our discussions in Chapter 1 and later, we recall that the forward rate is derived from the current spot rate term structure, and therefore although it is an expectation based on all currently known information, it is not a prediction of the term structure in the future. Nevertheless, the forward rate is important because it enables market-makers to price and hedge financial instruments for transaction today.

<!-- image -->

We know that there is a relationship between a set of discount factors, and the discount function, the par yield curve, the zero-coupon yield curve,  and  the  forward  yield  curve.  If  we  know  one  of  these  functions, we may readily compute the other three. In practice, although the zerocoupon yield curve is directly observable from the yields of zero-coupon government bonds, liquidity and investor preferences usually mean that a theoretical set of all these curves is derived from the yields of coupon government bonds in the market. There are a number of ways that the zero-coupon curve can be fitted, using either a discount function or the par yield curve.

As we noted, central banks such as the US Federal Reserve and the Bank of England use forward interest rates as an indicator for monetary policy purposes. We know that a forward rate is an interest rate applicable to a debt instrument whose term begins at a future date, and ends at a date beyond that. Although there is a market in forward rates, the prices at which forward instruments are quoted are derived from spot interest rates. That  is, implied forward  rates  are  calculated  from  the  spot  yield  curve, which is in turn modelled from the prices of instruments in the market, usually government bills and bonds. This suggests that the shape and position of the spot curve reflects market belief on future interest rates, which is why it is used to calculate forward rates. The information content and predictive power of a spot term structure is based on this belief. Forward rates may be estimated using any one of a number of models. They can be interpreted as reflecting the market's expectations of future short-term interest rates, which in turn are indicators of expected inflation levels. The same information is contained in the spot yield curve, however, monetary authorities often prefer to use forward rates, as they are more suited to policy analysis. Whereas the spot yield curve is the expected average of forward rates, the forward rate curve reflects the expected future time period of one short-term forward rate. This means that the forward curve can be split  into  short-term  and  long-term  segments  in  a  more  straightforward fashion than the spot curve.

Invariably, researchers use the government debt market as the basis for modelling the term structure. This is because that is the most liquid debt market in any country, and also because government securities are viewed as carrying the lowest default risk in any particular jurisdiction, so that government borrowing rates are considered the lowest risk. Whatever method is used to fit the term structure, it should aim to meet the following criteria when the main use is for government policy, rather than the pricing of financial instruments:

- ◾ the  method  should  attempt  to  fit  implied  forward  rates,  because the    primary  objective  is  to  derive  the  forward  curve  and  not  market spot yields;
- ◾ the resulting derived forward curve should be as smooth as possible, again because the aim is to provide information on the future level and direction of interest rates, and expectations on central bank monetary policy, rather than an accurate valuation of financial instruments along the maturity term structure;
- ◾ it should have as few market assumptions as possible.

To meet these objectives there are a number of curve-fitting methods that we can consider.

## RECAP: BOND MARKET INFORMATION

Central banks and market practitioners use interest rates prevailing in the government bond market to extract certain information, the most important of which is implied forward rates. These are an estimate of the market's  expectations  about  the  future  direction  of  short-term  interest  rates. They are important because they signify the market's expectations about the future path of interest rates, however, they are also used in derivative pricing and to create synthetic bond prices from the extent of credit spreads of corporate bonds.

Forward rates may be calculated using the discount function or spot interest rates. If spot interest rates are known, then the bond price equation can be set as:

<!-- formula-not-decoded -->

C is the coupon;

M is the redemption payment on maturity (par);

rs t is  the spot  interest  rate applicable  to  the  cash  flow  in  period t t n 1, .

where:

The bond price equation is usually given in terms of discount factors , with the present value of each coupon payment and the maturity payment being the product of multiplying them by their relevant discount factors. This allows us to set the price equation as shown by (11.2):

<!-- formula-not-decoded -->

where df t is the t -period discount factor t m 1, given by (11.3):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

A discount factor is a value for a discrete point in time, whereas markets  often  prefer  to  think  of  a  continuous  value  of  discount  factors  that applies a specific discount factor to any time t . This is known as the discount function ,  which  is  the  continuous  set  of  discrete  discount  factors  and  is indicated by df t t t .

The discount function relates the current cash bond yield curve to the spot  yield  curve  and  the  implied  forward  rate  yield  curve.  From  (11.3) we can set:

<!-- formula-not-decoded -->

As the spot rate rs is the average of the implied short-term forward rates 1 2 , , t rf rf rf … we state:

<!-- formula-not-decoded -->

From (11.4)  we  are  able  to  see  that 1 rs t is  the  geometric  mean  of 1 1 1 1 2 rf rf rf t , , , .

Implied  forward  rates  indicate  the  expected  short-term  (one-period) future interest rate for a specific point along the term structure. They reflect the spread on the marginal rate of return that the market requires if it is investing in debt instruments of longer and longer maturities.

In order to calculate the range of implied forward rates, we require the term structure of spot rates for all periods along the continuous discount function. This is not possible in practice because a bond market only contains a finite number of coupon-bearing bonds maturing on discrete dates. While the coupon yield curve can be observed, we are then required to 'fit'

the  observed  curve  to  a  continuous  term  structure.  Note  that  in  the  UK gilt market, for example, there is a zero-coupon bond market, so that it is possible to observe spot rates directly, but for reasons of liquidity, analysts prefer to use a fitted yield curve (the theoretical curve) and compare this to the observed curve.

## ESTIMATING YIELD CURVE FUNCTIONS

The traditional approach to yield curve-fitting involves the calculation of a set of discount factors from market interest rates. From this a spot yield curve can be estimated. The market data can be money market interest rates, futures and swap rates, and bond yields. In general though, this approach tends to produce 'jagged' spot rates and a forward rate curve with pronounced jagged knot points, due to the scarcity of data along the maturity structure. 2  A refinement of this technique is to use polynomial approxima-

tion to the yield curve.

The McCulloch method (1971, 1975) describes the discount function as a linear combination of a specified number of approximating functions, so for example, if there are k such functions on which j coefficients are estimated, the discount function that is generated by the set of approximations is a k th degree polynomial. The drawback of this approach is that unless the market observations are spaced at equal intervals through the maturity range, such a polynomial will fit the long end of the curve fairly inaccurately. To account for this, McCulloch proposed using piecewise polynomial functions or splines to approximate the discount function. A polynomial spline can be thought of as a number of separate polynomial functions, joined smoothly at a number of join, break, or knot points. In mathematics, the term 'smooth' has a precise meaning, but in the context of a piecewise r -degree spline it is generally taken to mean that the r -1 th derivative of the functions either side of each knot point are continuous. McCulloch originally used a quadratic spline to estimate the discount function. This results, however, in extreme bumps or 'knuckles' in the corresponding forward rate curve, which makes the curve unsuitable for policy analysis. To avoid this effect, it is necessary to increase the number of estimating functions and to use a cubic spline . This was presented by McCulloch in his second paper, and his specification is summarised in Appendix 11.1.

One of the main criticisms of cubic and polynomial functions is that they produce forward rate curves that exhibit unrealistic properties at the long end, usually a steep fall or rise in the curve. A method proposed by Vasicek and Fong (1982) avoids this feature, and produces smoother forward curves. Their approach characterises the discount function as exponential in shape, which is why splines, being polynomials, do not provide a good fit to the discount function, as they have a different curvature to exponential functions. Vasicek and Fong instead propose a transform to the argument T of the discount function v T . This transform is given by:

2   For a good account of why this approach is not satisfactory, see James and Webber (2000, Chapter 15).

<!-- formula-not-decoded -->

and has the effect of transforming the discount function from an approximately exponential function of T to an approximately linear function of x . Polynomial splines can then be employed to estimate this transformed discount function. Using this transform, it is straightforward to impose additional constraints on the discount function. The parameter constitutes the limiting value of the forward rates, and can be fitted to the date as part of the estimation. Vasicek and Fong use a cubic spline to estimate the transformed discount function. In terms of the original variable T , this is equivalent to estimating the discount function by a third-order exponential spline, that is between each pair of knot points v T takes the form:

<!-- formula-not-decoded -->

However,  Shea  (1985)  has  indicated  that,  in  practice,  exponential splines do not produce more stable estimates of the term structure than polynomial splines. He also recommended using basis splines or B-splines , functions that are identically zero over most of the approximation space, to prevent loss of accuracy due to the lack of observations at the long end of the curve.

## CURVE-FITTING TECHNIQUES: PARAMETRIC

In Chapter 10 we discussed the basic approach to spline-fitting techniques. We look at these techniques in greater detail now.

The Bank of England uses a variation of the Svensson yield curve model, a one-dimensional parametric yield curve model. This is similar to the   Nelson and Siegel model and defines the forward rate curve f m as a function of a set of unknown parameters, which are related to the short-term interest rate and the slope of the yield curve. The model was summarised in Chapter 10. Anderson and Sleath (1999) assess parametric models, including the Svensson model, against spline-based methods such as those described by Waggoner (1997), and we summarise their results later in this chapter.

## PARAMETRIC TECHNIQUES

Curve-fitting techniques generally fit into two classes, parametric methods and spline-based methods. Parametric techniques are so-called because they model the forward rate using a parametric function. An early parametric technique was that described by Nelson and Siegel (1987), which models the forward rate curve. Given the relationship between spot and forward rates, such an approach is identical to modelling a spot rate curve by taking a geometric average of the forward rates curve. A fairly flexible function for the forward rate is described in the Nelson-Siegel approach, known as a Laguerre function (plus a constant) and is given by:

<!-- formula-not-decoded -->

where T is the variable being calculated and 0 , 1 , 2 , and 1 are the parameters required to be estimated. Remembering that the spot rate is an average of the forward rates, that is:

<!-- formula-not-decoded -->

then (11.7) implies that the spot rate is given by:

<!-- formula-not-decoded -->

To illustrate implementation, we set parameter values of:

<!-- formula-not-decoded -->

and denote the remaining parameter as a , which reduces (11.9) to:

<!-- formula-not-decoded -->

Setting 0 as 5.0 means that the spot rate has been set to a common value of 5.0%. As an exercise, we evaluate the possible results setting parameters of the initial spot rate and values for the term to maturity of 10, 20, 30 and 1,000 years and the value for a to -5, -3, -1, 0, 1, 3 and 5. The results are given in Table 11.1. As the value for T increases to very high values, the convergence of spot rates to the initial value proceeds only slowly. However, our results illustrate the process.

TABLE 11.1 Spot rate values using Nelson-Siegel model and user-specified parameters

| Maturity ( T ) years   |     -5 |     -3 |     -1 |   a values 0 |      1 |      3 |      5 |
|------------------------|--------|--------|--------|--------------|--------|--------|--------|
| 10                     | 4.4003 | 4.6002 | 4.8001 |       4.9000 | 5.0000 | 5.1999 | 5.3998 |
| 20                     | 4.7000 | 4.8000 | 4.9000 |       4.9500 | 5.0000 | 5.1000 | 5.2000 |
| 30                     | 4.8000 | 4.8667 | 4.9333 |       4.9667 | 5.0000 | 5.0667 | 5.1333 |
| 1,000                  | 4.9940 | 4.9960 | 4.9980 |       4.9990 | 5.0000 | 5.0200 | 5.0040 |

An evaluation fitting the Nelson-Siegel curve to actual gilt yields from June 1997 is described in the next section.

Another parametric method is described by Svensson (1994, 1995). This adds an extra coefficient to the Nelson-Siegel model and has been described as an extended Nelson-Siegel model. The extra parameter introduces greater flexibility, so that the resulting curve can model forward curves that have more than one 'hump'. It is given by (11.11):

<!-- formula-not-decoded -->

In the Svensson model, there are six coefficients 0 , 1 , 2 , 3 , 1 and 2 , that  must  be  estimated.  The  model  was  adopted  by  central  monetary authorities such as the Swedish Riksbank and the Bank of England (who subsequently adopted a modified version of this model, which we describe shortly,  following  the  publication  of  the Waggoner  paper  by  the  Federal Reserve Bank of England). In their 1999 paper, Anderson and Sleath evaluate the two parametric techniques we have described, in an effort to improve their flexibility, based on the spline methods presented by Fisher, Nychka, and Zervos (1995) and Waggoner (1997).

## PARAMETERISED YIELD CURVES

The technique for curve-fitting presented by Nelson and Siegel and variants on it described by Svensson (1994), Wiseman (1994), and Bjork and Christensen (1997), have a small number of parameters, and generally one obtains a relatively close  approximation to the yield curve. As we discussed previously, the Nelson and Siegel curve contains four parameters, while the Svensson curve has six parameters. The curve presented by  Wiseman  contains  2 1 n parameters,  given  by j j j n k , , , 0 .  The curve is f 2 :

<!-- formula-not-decoded -->

The original Nelson and Siegel curve does not produce close approximations for all types of yield curves, because the small number of parameters limits flexibility. It can be used to model the spot rate or the forward rate curve, but does not produce accurate results if used to model the discount curve. An example of a fitted Nelson and Siegel curve is shown at Figure 11.1 for UK gilt yields from June 1997. The actual gilt yields used are shown at Table 11.2.

FIGURE 11.1 A Nelson and Siegel fitted yield curve and gilt redemption yield curve.

<!-- image -->

TABLE 11.2 Gilt redemption yields used to fit curve in Figure 11.1

|   Term to maturity |   Gilt Redemption Yield% | Term to maturity   | Gilt Redemption Yield%   |
|--------------------|--------------------------|--------------------|--------------------------|
|                0.5 |                     5.90 | 7                  | 6.52                     |
|                  1 |                     6.29 | 8                  | 6.54                     |
|                  2 |                     6.37 | 9                  | 6.55                     |
|                  3 |                     6.40 | 12                 | 6.60                     |
|                  4 |                     6.47 | 15                 | 6.58                     |
|                  5 |                     6.45 | 21                 | 6.54                     |
|                  6 |                     6.50 |                    |                          |

Source

: Butler Gilts.

The fitted curve is a close approximation to the redemption yield curve, and is also very smooth. However, the fit is inaccurate at the very short end, indicating an underpriced six-month bond, and also does not approximate the long end of the curve. For this reason, B-spline methods are more commonly used.

## THE CUBIC SPLINE METHOD FOR ESTIMATING AND FITTING THE YIELD CURVE

In mathematical applications, a spline is a piecewise polynomial , this being a function that is composed of a number of individual polynomial segments that are joined at user-specified points known as knot points. The function is twice-differentiable at each knot point, which produces a smooth curve at  each  connecting  knot  point. The  most  common  approach uses regression methods to fit the spline function. The approach was demonstrated in Chapter 10. In this section we summarise the spline approach described by Waggoner in his ground-breaking article published by the   Federal Reserve Bank of Atlanta in 1997.

Spline  methods  are  commonly  used  to  derive  spot  and  forward  rate curves and the discount function from the observed yields of bonds in the market. A popular method was that proposed by McCulloch (1975), who used  regression  cubic  splines  to  derive  the  discount  function.  Waggoner (1996)  has  written  that  this  method  however,  while  accurate  and  stable, produces forward rate curves that oscillate. In fact, this property is exhibited by virtually all curve-fitting techniques, but the objective for the analyst is to produce curves with the smallest amount of oscillation. A technique posited by Fisher, Nychka and Zervos (1995) used a cubic spline that incorporates a 'roughness penalty' when extracting the forward rate curve. This approach produces a decreased level of oscillation but also reduces the fit of the curve to the actual observed yields. A later technique modified this method by using a 'variable roughness penalty' (Waggoner 1997) and this approach is described here.

## USING A CUBIC SPLINE: THE WAGGONER MODEL

A cubic spline approach can be used as the functional form for the discount function or the forward rate curve. We define a function g on the interval t t N 1 , as a cubic spline with node points t t t n 1 2 /midhorizellipsis if it is a cubic polynomial on each of the subintervals t t j j 1 , for 1 j n and  if  it  can  be continuously differentiated over the interval t t j N 1 , . The node points are 1 2 /midhorizellipsis n ,  which are the cash flow and maturity dates of the set of bonds (assuming the bonds are semi-annual coupon instruments). Following Waggoner (1997), we set 0 0 so that the curve is derived from the point zero to the point of the longest-dated bond in the sample. It is possible to use all the node points in the interval to produce the yield curve, however, the more points there are in a cubic spline, the greater the tendency for  the  derived  forward  curve  to  oscillate,  more  so  at  longer  maturities. We wish to minimise the level of oscillation, because for monetary policy purposes the curve is used to provide information on expected future interest rates. A fluctuating yield curve implies oscillations in expected future prices, and this can produce illogical results, particularly at the long end of the curve. For example, a curve may imply that while the current yield of a six-month T-bill is £97.50, the price of a six-month bill in one year's time will be £98, while the price of such a bill in two years' time will be £95. This is not an unreasonable expectation. However, the same implications for six-month bill prices in 25, 26 and 27 years' time is less reasonable. Therefore the fitted curve should smooth out the forward rates at longer maturities, which calls for a reduced level of oscillation. The McCulloch technique uses regression splines to reduce forward rate fluctuation, while the Fisher et al. and the Waggoner approach use a smoothed spline and a modified smoothed spline.

In a regression spline, a smaller number of node points are used in order to  reduce  the  level  of  oscillation.  This  affects  the  flexibility  of  the  cubic spline over the interval that is being considered - there is a trade-off between accuracy and the level of oscillation. By reducing node points at the longer end, but keeping more at the short end, oscillation is reduced but the curve retains accuracy at the short end. In practice, it is common for node points to be set in one of the ways shown at Figure 11.2, but obviously there are any number of ways that node points may be set.

Once we have chosen the node points, we set the yield curve as the cubic spline that minimises the function at (11.13):

<!-- formula-not-decoded -->

FIGURE 11.2 Suggested node points.

<!-- image -->

The technique proposed by McCulloch (1975) uses a regression cubic spline to approximate the discount function, and he suggested that the number of node points that are used be roughly equal to the square root of the number of bonds in the sample, with equal spacing so that an equal number of bonds mature between adjacent nodes. A number of writers have suggested that this approach produces accurate results in practice. 3  The discount function is constrained to set v 0 1.  Given  these  parameters,  the discount function chosen is the one that minimises the function at (11.14). As this is a discount function and not a yield curve, (11.14) can be solved using the least squares method.

<!-- formula-not-decoded -->

For a smoothed spline, the level of oscillation is controlled by setting a 'roughness  penalty'  in  the  function,  and  not  by  reducing  the  number of  node  points. The  yield  curve is  chosen  that  minimises  the  objective function at (11.15):

<!-- formula-not-decoded -->

for all the cubic splines over the node points 0 1 2 /midhorizellipsis N . In minimising this function, there is a trade-off between the goodness of fit, which is given by the first term, and the degree of smoothness, which is measured by the second term. This trade-off is known as the 'roughness penalty' and is given by which is a positive constant. If is set to zero, the function reverts to a regression spline, and as it increases, g approaches a linear function. The flexibility of the spline is a function of both the spacing between the node points and the magnitude of , although as increases, the impact of the node spacing decreases. For large values of the  flexibility  of  the spline  is  essentially  similar  across  all  terms.  This  is  not  necessarily  ideal because as we saw from Figure 11.1 we require the spline to be more flexible at the short end, and less so at the long end. Therefore Waggoner (1997) has proposed a modified smoothed spline. For a modified smoothed spline, the objective function at (11.16) is minimised over the whole term covering the node points points 0 1 2 /midhorizellipsis N .

<!-- formula-not-decoded -->

3   For example, see Bliss (1997).

The approach used by Fisher (1995) is a smoothed cubic spline that approximates  the  forward  curve. The  number  of  nodes  to  use  is  recommended as approximately one-third of the number of bonds used in the sample, spaced apart so that there is an equal number of bonds maturing between adjacent nodes. This is different to the theoretical approach, which is  to  have node points at every interval where there is a bond cash flow. However, in practice, using the smaller number of nodes proposed by Fisher, produces essentially an identical forward rate curve, but with fewer calculations required. The resulting forward rate curve is the cubic spline that minimises the function at (11.17):

<!-- formula-not-decoded -->

The value of is  obtained by a method known as generalised crossvalidation (GCV). It is the value that minimises the expression at (11.18):

<!-- formula-not-decoded -->

N is the number of bonds in the sample;

rss is  the  residual  sum  of  squares,  given  by: rss P P f i N i i f 1 2 /circumflexnosp where f is the forward rate curve that minimises the expression; ep is the effective number of parameters; is the cost or tuning parameter.

The higher the value , the more rigid is the resulting spline. Fisher et al. and Waggoner both set equal to 2. Expression (11.17), for a fixed term , can be solved using a non-linear least squares method. The GCV method can be implemented by using a method known as a line search .

Following Fisher et al ., Waggoner (1997) proposes using a cubic spline to approximate the forward rate function, with the number of nodes again being approximately one-third of the number of bonds in the sample, and spaced so that there is an equal number of bonds maturing between adjacent nodes. The Waggoner approach is termed the 'variable roughness penalty method' (VRP). The cubic spline forward rate curve is selected that will minimise the function at (11.19):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where:

The roughness penalty is set as follows:

<!-- formula-not-decoded -->

where t is  measured  in  years. The VRP method is non-linear and can be solved using the non-linear least squares method.

## THE ANDERSON-SLEATH MODEL

In this section, we describe the Anderson and Sleath model first described in the Bank of England Quarterly Bulletin in  November 1999. The main objective of this work was to evaluate the relative efficacy of parametric versus spline-based methods. In fact, different applications call for different methods - the main advantage of spline methods is that individual functions in between knot points may move in a fairly independent fashion, which makes the resulting curve more flexible than that possible using parametric  techniques.  In  the  following  section,  we  reproduce  their  results  (with permission), which shows that a shock introduced at one end of the curve produces unsatisfactory results in the parametric curve.

The Anderson-Sleath model, which is the method adopted by the Bank of  England, is a modification of the Waggoner approach in a number of significant ways. The t function of Waggoner was adapted thus:

<!-- formula-not-decoded -->

where the parameters to be estimated are L , S , µ . In addition, the difference in bond market and theoretical prices is weighted with the inverse of the modified duration of the bond. This accounts for observed pricing errors for bonds that are more volatile than others.

The model therefore minimises the expression at (11.21):

<!-- formula-not-decoded -->

where P and MD are  the  price and modified duration of bond i , c is  the parameter vector of the polynomial spline being estimated and M is the time to maturity of the longest-dated bond.

The outstanding feature of the Anderson-Sleath approach is their adaptation of both spline and parametric techniques.

## APPLICATIONS

Each of the methods described in this section can be used to fit the zerocoupon  curve.  In  practice,  results  produced  by  each  method  imply  that certain techniques are more suitable than others under specific conditions. Generally,  the  incorporation  of  a 'roughness'  penalty  that  varies  across maturities produces more accurate pricing of short-dated bonds, and this is the case in the Fisher and Waggoner methods. The McCulloch technique is reasonably accurate and, as it is a linear method, is more straightforward to implement than the other techniques. It produces a similar curve to the VRP method in terms of goodness of fit and smoothness. Therefore in most cases it is reasonable to use this method. The advantage of the VRP method is that it allows the user to select the degree of smoothing.

In  deciding  which  method  to  use,  practitioners  need  to  consider  the effectiveness of each approach with regard to flexibility, simplicity, and consistency. The  requirements of central monetary authorities differ in some respects to investment and commercial banks, as we noted at the start of the chapter. Generally, however, curves should fit as wide a range of term structures  as  possible,  and  be  tractable,  or  straightforward  to  compute. They should also be consistent with a yield curve model. For example, the approach presented by Bjork and Christensen (1997) is compatible with the Hull-White or extended Vasicek yield curve model. In the same paper, it is stated that the Nelson and Siegel technique is not consistent with any common term structure model. James and Webber (2000) state that the simplicity  of  the  Nelson  and  Siegel  approach,  which  is  an  advantage  of  the technique, is also its main drawback. In the same review, it is concluded that B-spline methods are the most flexible and consistent, along with that described by Bjork and Christensen.

## THE ANDERSON-SLEATH EVALUATION

## Fitting the Spot Curve

In  this  section,  we  summarise  results  obtained  by  Anderson  and  Sleath (1999), comparing the different methods. The accuracy of any of the techniques is usually tested by using a goodness of fit measure, for example, if  we fit the curve using n bonds we wish to minimise the measure given by (11.22):

<!-- formula-not-decoded -->

where:

- P i is the market price of the i th bond;
- MDi is the modified duration of the i th bond;
- i is the fitted price of the i th bond.

A popular technique is the spline-based method of curve-fitting, which we introduced in Chapter 10. Unlike other methods (such as the parametric Svensson method), which specify a single short rate to describe the instantaneous forward rate curve, spline-based methods fit a curve to observed data that is composed of a number of sections, but with constraints to ensure that the curve is smooth and continuous. As this is one of the aims we stated at the beginning, this is an advantage of the spline-based method, as it allows individual sections of the curve to move independently of each other. This is demonstrated with Figures 11.3 and 11.4, which show a hypothetical yield curve that has been fitted, from an assumed set of bond prices, using the cubic spline method and a parametric method such as Svensson. The change of the long bond yield has a significant effect on the Svensson curve, notably at the short end of the curve. The spline curve, however, undergoes only a slight change in response to the change in yield, and only at the long end.

The effect of a change in a yield on the Svensson curve is amplified because the technique specifies a constraint that results in yields converging to a constant level. This assumption is based on the belief that forward rates

FIGURE 11.3 Yield curves fitted using cubic spline method and Svensson parametric method, hypothetical bond yields.

<!-- image -->

Source : Reproduced with permission from the Bank of England Quarterly Bulletin , November 1999.

FIGURE 11.4 Effect on fitted yield curves of change in long-dated bond yield. Source : Reproduced with permission from the Bank of England Quarterly Bulletin , November 1999.

<!-- image -->

reflect market expectations of the future level of short rates, and following this, the 30-year forward rate is expected not to be significantly different from the 25-year or 20-year forward rate. This causes the forward rate to converge to a constant level after about 10 years.

We can compare fitted yield curves to an actual spot rate curve wherever there is an active government (risk-free) zero-coupon market in operation. In the UK, a zero-coupon bond market was introduced in December 1997. (Although it never developed any market depth and has since been discontinued.) In theory, any derived spot rate curve can be compared to the actual spot rate curve, this comparison serving to provide an instant check of the accuracy of the yield curve model. In practice, however, discrepancies between the observed and fitted curves may not have that much significance, because of the way that strip yields behave in practice. In the UK market there was a high level of illiquidity associated with strip yields at certain points of the term structure and the UK market also exhibited a common trait of strip markets everywhere that the longest-dated issue traded dear to the yield curve. Another factor is that coupon strips trade cheaper to principal strips - which yield should be used in the comparison? 4  In Figure 11.5, we compare the theoretical spot curve fitted using the Svensson method to the observed coupon strip curve in July 1998, at a time when the UK gilt yield curve was inverted.

4   This is the observation that, due to demand and liquidity reasons, zero-coupon bonds sourced from the principal cash flow of a coupon bond trade at a lower yield than equivalent-maturity zero-coupon bonds sourced from the coupon cash flow of a conventional bond.

FIGURE 11.5 Comparison of fitted spot yield curve to observed spot yield curve. Source : Reproduced with permission from the Bank of England Quarterly Bulletin , November 1999.

<!-- image -->

The fitted curve exhibits the constant long yield that we observed in the hypothetical yield curve in Figure 11.1, while the strip curve traded expensive at the long end, which as we noted is a common observation. Nevertheless, for the purposes of accurate fitting, the parametric method exhibits a significant difference to the observed curve. A cubic spline-based fitted curve such as that proposed by Waggoner (1997) produces a more realistic curve, as shown by Figure 11.6.

This reflects the properties of the spline curve, including the fact that forward rates are described by a series of segments that are in effect connected.  This  has  the  effect  of  localising  the  influence  of  individual  yield movements to only the relevant part of the yield curve and it also allows the curve to match more closely the observed yield curve. The effectiveness of the spline-based method is measured using (11.23):

<!-- formula-not-decoded -->

where f m is the second derivative of the fitted forward curve and M is the maturity of the longest-dated bond. The term t m is the 'roughness penalty'. Figure 11.6 shows that the spline-based method generates a  more  realistic  curve  that  better  mirrors  the  strip  yield  curve  seen  in Figure 11.5.

FIGURE 11.6 Fitted yield curves and observed strip yield curve, July 1998. Source : Reproduced with permission from the Bank of England Quarterly Bulletin , November 1999.

<!-- image -->

## REPO AND ESTIMATING THE SHORT END OF THE YIELD CURVE

For the purposes of conducting monetary policy and for central government requirements, little use is made of the short end of the yield curve. This is for two reasons. One is that monetary and government policy is primarily concerned with medium-term views, for which a short-term curve has no practical input. The second is that there is often a shortage of data that can be used to fit the short-term curve accurately. In the same way that the longterm term structure must be fitted using risk-free instruments, the shortterm  curve  can  only  be  estimated  using Treasury  bills. The T-bill  can  be restricted to only a small number of participants in some markets, moreover the yield available on T-bills reflects its near cash, risk-free status, and so it may not be the ideal instrument to use when seeking to extract market views on forward rates. Therefore for liquidity purposes, the existence of an alternative instrument to T-bills is useful. In most respects, the government repurchase  market  or  repo  market  is  a  satisfactory  substitute  for T-bills. Although there is an element of counterparty risk associated with repo that does not apply to T-bills, they can be considered to be essentially risk-free instruments, more so if margin has been taken by the party lending cash. We can therefore consider general collateral repo to be essentially a liquid, short-term and risk-free instrument. 5

5 See The Global Repo Markets (Wiley  2004) for more information on the repo markets and the UK gilt repo market.

FIGURE 11.7 Fitting short-term yield curves using government repo rates. Source : Reproduced with permission from the Bank of England Quarterly Bulletin , November 1999.

<!-- image -->

The  fitted  spot  curve  can  differ  considerably  if  yields  on  short-term repo are included. The effect is shown in Figure 11.7, which is reproduced from Anderson and Sleath (1999). Note that this is a short-term spot curve only,  the  maturity  extends  out  to  only  two  years. Two  curves  have  been estimated - the cubic spline-based yield curve using the repo rate and without the repo rate. The curve that uses repo data generates a curve that is much closer to the money market yield curve than the one that does not. The only impact is at the very short end. After about one year, both approaches generate very similar curves.

For an account of the impact of 'special' repo rates on term structure modelling, see Duffie (1996).

## APPENDIX 11.1 THE MCCULLOCH CUBIC SPLINE MODEL

This was first described by McCulloch (1975) and is referred to in Deacon and  Derry  (1994). We  assume  the  maturity  term  structure  is  partitioned into q knot points with 1 , , q q q … where q 1 0 and q q is the maturity of the longest-dated bond. The remaining knot points are spaced such that there is, as far as possible, an equal number of bonds between each pair of knot points. With j q , we employ the following functions:

- ◾ for m qj

<!-- formula-not-decoded -->

for q m q j j 1

◾ q m q j j 1

where:

- ◾ for q m j 1

<!-- formula-not-decoded -->

◾ for j q

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

the f m m q for all values of m .

## SELECTED BIBLIOGRAPHY AND REFERENCES

- Anderson, N., Breedon, F., Deacon, M., Derry, A. and Murphy, M., Estimating and Interpreting the Yield Curve , Wiley, 1996.
- Anderson, N. and Sleath, J., 'New estimates of the UK real and nominal yield curves', Bank of England Quarterly Bulletin , November 1999, pp. 384-392. Bank of England, Quarterly Bulletin , August 1999.
- Barone, E. and Risa, S., 'Valuation of Floaters and Options on Floaters under Special Repo Rates', Instituto Mobiliare Italiano, 1994.
- Bjork, T. and Christensen, B., 'Interest Rate Dynamics and Consistent Forward Rate Curves', University of Aarhus Working Paper, 1997.
- Bliss, R., 'Testing term structure estimation methods', Advances in Futures and Options Research 9, 1997, pp. 197-231.
- Brenner, R. and Jarrow, R., 'A Simple Formula for Options on Discount Bonds', Advances in Futures and Options Research 6, 1993, pp. 45-51.
- Choudhry, M., The Global Repo Markets : Analysis and Strategies , John Wiley, 2004.

- Cox, J., Ingersoll, J. and Ross, S., 'A theory of the term structure of interest rates', Econometrica 53, 1985, pp. 385-407.
- Dahlquist, M. and Svensson, L., 'Estimating the term structure of interest rates for monetary policy analysis', Scandinavian Journal of Economics 98, 1996, pp. 163-183.
- Dothan, u., 'On the term structure of interest rates', Journal of Financial Economics 6, 1978, pp. 59-69.
- Deacon, M. and Derry, A., 'Estimating the term structure of interest rates', Bank of England Working Paper No. 24, July 1994.
- Duffie, D., Special Repo Rates , Graduate School of Business, Stanford University, 1993.
- Edmister, R.O. and Madan, D.P., 'Informational Content in Interest Rate Term Structures', The Review of Economics and Statistics 75 (4), November 1993, pp. 695-699.
- Fisher, M., Nychka, D. and Zervos, D., 'Fitting the term structure of interest rates with smoothing splines', Finance and Economic Discussion Series 95-1, Federal Reserve Board, 1995.
- Harrison, J. and Pliska, S., 'Martingales and Stochastic Integrals in the Theory of Continuous Trading', Stochastic Processes and their Applications 11, 1981, pp. 215-260.
- Heath, D., Jarrow, R. and Morton, A., 'A new methodology for contingent claims valuation', Econometrica 60, 1992, pp. 76-106.
- James, J., Webber, N., Interest Rate Modelling , Wiley, 2000.
- Kim, J., 'A Discrete-Time Approximation of a One-Factor Markov Model of the Term Structure of Interest Rates', Graduate School of Industrial Administration, Carnegie-Mellon University, 1993.
- Lancaster, P. and Salkauskas, K., Curve and Surface Fitting: An Introduction , Academic Press, 1986.
- Mastronikola, K., 'Yield curves for gilt-edged stocks: a new model', Bank of England Discussion Paper ( Technical Series ) No. 49, 1991.
- McCulloch, J., 'Measuring the term structure of interest rates', Journal of Business 44, January 1971, pp. 19-31.
- McCulloch, J., 'The tax adjusted yield curve', Journal of Finance 30, June 1975, pp. 811-829.
- Nelson, C. and Siegel, A., 'Parsimonious modelling of yield curves', Journal of Business Vol. 60, 1987, p. 473.
- Schaefer, S., 'Measuring a tax-specific term structure of interest rates in the market for British government securities', The Economic Journal Vol. 91, June 1981, pp. 415-438.
- Shea, G., 'Interest-rate term structure estimation with exponential splines: a note', Journal of Finance 40(1), March 1985, pp. 319-325.
- Svensson, L., 'Estimating and Interpreting Forward Interest Rates: Sweden 1992-94', International Monetary Fund Working Paper 114, 1994.
- Svensson, L., 'Estimating forward interest rates with the extended Nelson &amp;  Siegel method', Sveriges Riksbank Quarterly Review , 1995:3, p. 13.

- Waggoner, D., 'The robustness of yield and forward rate extraction methods', unpublished working paper, Federal Reserve Bank of Atlanta, September 1996.
- Waggoner, D., 'Spline methods for extracting interest rate curves from coupon bond prices', Working Paper No. 97-10, Federal Reserve Bank of Atlanta, 1997.
- Vasicek, 0., 'An equilibrium characterization of the term structure', Journal of Financial Economics 5, 1977, pp. 177-188.
- Vasicek, 0., Fong, H.G., 'Term structure modelling using exponential splines', Journal of Finance 37(2), May 1982, pp. 339-356.
- Wiseman, J., 'The Exponential Yield Curve Model', European Fixed Income Research, Technical Specification, JP Morgan, 1994.

Neil Kinnock swept in with a huge fuss and fanfare. It was the third time I'd been in the presence of a politician . . . I was to witness the showbiz nature of politics once again. It was then that I realised that most politicians are ultimately fame hounds. They may have the rhetoric and may even stand for the right things, but they're more than a little ambitious and they're definitely more than okay with being famous. They just weren't cool enough to be musicians and not good enough to be footballers.

-- Johnny Marr, Set The Boy Free: The Autobiography , Century, 2016

<!-- image -->

## Yield Curves and Relative Value Trading

I n this final part of the book, we look at how market participants such as primary dealers and fund managers analyse the yield curve as part of relative value and spread trading. In the first edition of this book, we covered the basic principles in Chapter 12, using the UK gilt market for illustration. These principles remain unchanged, so we have retained this chapter as is.

However, compared to the 1990s, when much of what inspired the writing of Chapter 12 was observed, while the principles remain unchanged, there  are  fewer  and  fewer  opportunities  to  apply  them.  Hence  we  have dropped the first  edition's  other  chapter  on  specific  relative  value  trades such as butterfly and barbell trades. For this second edition, Kenneth Kortanek and Vladimir Medvedev apply a fine and accurate approach to relative value analysis in the US Treasury market, taking into account the paucity of genuine arbitrage relative value occurrences in what is a large and liquid market. There is also a reference to the authors' website where readers can apply  the  techniques  demonstrated  in  Chapter  13. This  hopefully  brings Part IV bang up to date!

Many things can only happen when we try less hard, when we relax, when we switch off the conscious mind . . . When a sportsman (or, for that matter, a musician) is at peak performance, the conscious mind is often very still. Rather, it is the subconscious competence, built up over many years of practice, that is given full rein.

-- Matthew Syed , The Times , 26 February 2014

## CHAPTER  12 Yield Curves and Relative Value

B ond  market  participants  take  a  keen  interest  in  both  cash  and  zerocoupon  (spot)  yield  curves.  In  markets  where  an  active  zero-coupon bond market exists, much analysis is undertaken into the relative spreads between derived and actual zero-coupon yields. In this chapter, we review how yield curve analysis are used in the market, with respect to bonds that are default-free, such as US and UK government bonds. We then look at a specific case study example in the next (and final) chapter.

## THE DETERMINANTS OF GOVERNMENT BOND YIELDS

Market-makers in government bond markets analyse various factors in the market in deciding how to run their book. Customer business apart, decisions to purchase or sell securities is a function of their views on:

- ◾ market direction itself,  that  is  the  direction  in  which  short-term  and long-term interest rates are headed;
- ◾ which maturity point along the entire term structure offers the best value;
- ◾ which  specific  issue  within  a  particular  maturity  point  offers  the best value;
- ◾ how best to hedge the market and credit risk exposures that arise as a result of undertaking the customer business mentioned above.

All  these  areas  are  related  but  react  differently  to  certain  pieces  of information. A report on the projected size of the government's budget deficit,  for  example,  will  not  have  too  much  effect  on  two-year  bond  yields, whereas if the expectations come as a surprise to the market it may have an adverse effect on long-bond yields. The starting point for analysis is the yield curve, both the traditional coupon curve plotted against duration and the  zero-  coupon  curve.  Figure  12.1  illustrates  the  yield  curve  for  gilts  in October 1999.

<!-- image -->

FIGURE 12.1 Yield and duration of gilts, 21 October 1999. Source : Bloomberg.

<!-- image -->

For a first-level analysis, many market practitioners go no further than Figure 12.1. An investor who has no particular view on the future shape of the yield curve or the level of interest rates may well adopt a neutral outlook and hold bonds that have a duration that matches their investment horizon. If they believe interest rates are likely to remain stable for a time, they might hold bonds with a longer duration in a positively sloping yield curve environment, and pick up additional yield but with higher interest rate risk. Once the decision has been made on which part of the yield curve to invest in or switch in to, the investor must decide on the specific securities to hold, which then brings us on to relative  value  analysis.  For  this,  the  investor analyses specific sectors of the curve, looking at individual stocks. This is sometimes called looking at the 'local' part of the curve.

An assessment of a local part of the yield curve includes looking at other features of individual stocks in addition to their duration. This recognises that the yield of a specific bond is not only a function of its duration, and that two bonds with near-identical duration can have different yields. The other determinants of yield are liquidity of the bond and its coupon. To illustrate the effect of coupon on yield, let us consider Table 12.1. This shows that, where the duration of a bond is held roughly constant, a change in coupon of a bond can have a significant effect on the bond's yield.

In  the  case  of  the  long  bond,  an  investor  could,  under  this  scenario, both shorten duration and pick up yield, which is not the first thing that an investor might expect. However, an anomaly of the markets is that, liquidity issues aside, the market does not generally like high coupon bonds, so they usually trade cheap to the curve.

TABLE 12.1 Duration and yield comparisons for bonds in a hypothetical inverted curve environment

| Coupon   | Maturity   |   Duration | Yield   |
|----------|------------|------------|---------|
| 8%       | 20-Feb-02  |      1.927 | 5.75%   |
| 12%      | 5-Feb-02   |      1.911 | 5.80%   |
| 10%      | 20-Jun-10  |      7.134 | 4.95%   |
| 6%       | l-Jul-10   |      7.867 | 4.77%   |

The other factors affecting yield are supply and demand, and liquidity. A shortage of supply of stock at a particular point in the curve has the effect of  depressing  yields  at  that  point. A  reducing  public  sector  deficit  is  the main reason why such a supply shortage might exist. In addition, as interest rates decline, for example, ahead of or during a recession, the stock of high coupon bonds increases, as the newer bonds are issued at lower levels, and these 'outdated' issues can end up trading at a higher yield. Demand factors are driven primarily by the investor's views of the country's economic prospects, but also by government legislation, for example, the Minimum Funding Requirement in the UK compelled pension funds to hold a set minimum amount of their  funds  in  long-dated  gilts,  which  had  the  effect  of permanently keeping demand high. 1

Liquidity often results in one bond having a higher yield than another, despite both having similar durations. Institutional investors prefer to hold the  benchmark  bond,  which  is  the  current  two-year,  five-year,  ten-year or thirty-year bond and this depresses the yield on the benchmark bond. A bond that is liquid also has a higher demand, thus a lower yield, because it  is  easier  to  convert  into  cash  if  required. This  can  be  demonstrated by valuing the cash flows on a six-month bond with the rates obtainable in the Treasury bill market. We could value the six-month cash flows at the six-month bill rate. The lowest obtainable yield in virtually every market 2 is the T-bill yield, therefore valuing a six-month bond at the T-bill rate will

1   The requirements of the MFR were removed in 2002.

2 The  author  is  not  aware  of  any  market  where  there  is  a  yield  lower  than  its shortest-maturity T-bill yield, but that does not mean such a market doesn't exist!

produce a discrepancy between the observed price of the bond and its theoretical price implied by the T-bill rate, because the observed price will be lower. The reason for this is simple, because the T-bill is more readily realisable into cash at any time, it trades at a lower yield than the bond, even though the cash flows fall on the same day.

We have therefore determined that a bond's coupon and liquidity level, as well as its duration, will affect the yield at which it trades. These factors can be used in conjunction with other areas of analysis, which we look at next, when deciding which bonds carry relative value over others.

## CHARACTERISING THE COMPLETE TERM STRUCTURE

As  many readers  would  have  concluded,  the  yield  versus  duration  curve illustrated in Figure 12.1 is an ineffective technique with which to analyse the market.

This is because it does not highlight any characteristics of the yield curve other than its general shape and this does not assist in the making of trading decisions. To facilitate a more complete picture, we may wish to employ the technique described here. Figure 12.2 shows the bond par yield curve 3  and T-bill yield curve for the same set of gilts in October 1999. Figure 12.3 shows the difference between the yield on a bond with a coupon that is 100 basis points below the par yield level, and the yield on a par bond. The other curve in Figure 12.3 shows the level for a bond with a coupon that is 100 basis

FIGURE 12.2 T-bill and par yield curve, October 1999.

<!-- image -->

3   See Chapter 1 for a discussion of the par yield curve.

<!-- image -->

-5

FIGURE 12.3 Structure of bond yields, October 1999.

points above the par yield. These two curves show the 'low coupon' and 'high coupon' yield spreads. Using the two figures together, an investor can see the impact of coupons, the shape of the curve, and the effect of yield on different maturity points of the curve.

## IDENTIFYING RELATIVE VALUE IN GOVERNMENT BONDS

Constructing  a  zero-coupon  yield  curve  provides  the  framework  within which a market participant can analyse individual securities. In a government  bond  market,  there  is  no  credit  risk  consideration  (unless  it  is  an emerging market government market), and therefore no credit spreads to consider. There are a number of factors that can be assessed in an attempt to identify relative value.

The objective of much of the analysis that occurs in bond markets is to  identify  value,  and  identify  which  individual  securities  should  be  purchased and which should be sold. At the overview level, this identification is a function of whether one thinks interest rates are going to rise or fall. At the local level though, the analysis is more concerned with a specific sector of the yield curve, whether this will flatten or steepen, whether bonds of similar duration are trading at enough of a spread to warrant switching from one into another. The difference in these approaches is one of identifying  which  stocks  have  absolute  value,  and  which  have  relative  value. A trade decision based on the expected direction of interest rates is based on assessing absolute value, whether interest rates themselves are too low or too high. Yield curve analysis is more a matter of assessing relative value. On (very!) rare occasions, this process is fairly straightforward; for example,  if  the  three-year  bond  is  trading  at  5.75%  when  two-year yields are 5.70% and four-year yields are at 6.15%, the three-year bond appears to be  overpriced.  However,  this  is  not  really  a  real-life  situation.  Instead,  a trader might assess the relative value of the three-year bond compared to much shorter- or longer-dated instruments. That said, there is considerable difference between comparing a short-dated bond to other short-term securities  and comparing say, the two-year bond to the thirty-year bond. Although it looks like it on paper, the space along the x -axis should not be taken to imply that the smooth link between one-year and five-year bonds is repeated from the five-year out to the thirty-year bonds. It is also common for the very short-dated sector of the yield curve to behave independently of the long end.

One method used to identify relative value is to quantify the coupon effect on the yields of bonds. The relationship between yield and coupon is given by (12.1):

<!-- formula-not-decoded -->

where:

rm is the yield on the bond being analysed;

rmp is the yield on a par bond of specified duration;

CPD is  the  coupon on an arbitrary bond of similar duration to the part bond;

and c and d are coefficients. The coefficient c reflects the effect of a high coupon on the yield of a bond. If we consider a case where the coupon rate exceeds the yield on the similar-duration par bond ( C rm PD p ), (12.1) reduces to (12.2):

<!-- formula-not-decoded -->

Equation (12.2) specifies the spread between the yield on a high coupon bond and the yield on a par bond as a linear function of the spread between the first bond's coupon and the yield and coupon of the par bond. In reality this relationship may not be purely linear, for instance, the yield spread may widen at a decreasing rate for higher coupon differences. Therefore  (12.2)  is  an  approximation  of  the  effect  of  a  high  coupon  on  yield where the approximation is more appropriate for bonds trading close to par.

TABLE 12.2 Yields and excess yield spreads for selected gilts, 22 October 1999

| Coupon   | Maturity   |   Duration |   Yield% |   Excess yield spread (bp) |
|----------|------------|------------|----------|----------------------------|
| 8%       | 07/12/2000 |      1.072 |    5.972 |                      -1.55 |
| 10%      | 26/02/2001 |     1.2601 |    6.051 |                        4.5 |
| 7%       | 07/06/2002 |      2.388 |    6.367 |                       -1.8 |
| 5%       | 07/06/2004 |      4.104 |    6.327 |                       -3.8 |
| 6.75%    | 26/11/2004 |      4.233 |    6.351 |                        2.7 |
| 5.75%    | 07/12/2009 |      7.437 |     5.77 |                       -4.7 |
| 6.25%    | 25/11/2010 |      7.957 |     5.72 |                       1.08 |
| 6%       | 07/12/2028 |     15.031 |     4.77 |                       -8.7 |

The same analysis can be applied to bonds with coupons lower than the same-duration par bond.

The value of a bond may be measured against comparable securities or against the par or zero-coupon yield curve. In certain instances the first measure may be more appropriate when, for instance, a low coupon bond is priced expensive to the curve itself but fair compared to other low coupon bonds. In that case, the overpricing indicated by the par yield curve may not represent unusual value, rather a valuation phenomenon that is shared by all low coupon bonds. Having examined the local structure of a yield curve, the analysis can be extended to the comparative valuation of a group of similar bonds. This is an important part of the analysis, because it is particularly informative to know the cheapness or dearness of a single stock compared to the whole yield curve, which might be somewhat abstract. Instead we may seek to identify two or more bonds, one of which is cheap and the other dear, so that we might carry out an outright switch between the two, or put on a spread trade between them. Using the technique we can identify excess positive or negative yield spread for all the bonds in the term structure. This has been carried out for our five gilts, together with other less liquid issues as at October 1999, and the results are summarised in Table 12.2.

From Table 12.2 as we might expect, the benchmark securities are all expensive to the par curve, and the less liquid bonds are cheap. Note that the 6.25% 2010 appears cheap to the curve, but the 5.75% 2009 offers a yield pick-up for what is a shorter-duration stock - this is a curious anomaly and one that disappeared a few days later. 4

4   In other words, we've missed the opportunity! This analysis used mid-prices, which are not available in practice.

## YIELD SPREAD TRADES

Spread trading is not market-directional trading, but rather the expression of a viewpoint on the shape of a yield curve, or more specifically the spread between two particular points on the yield curve. Generally, there is no analytical relationship between changes in a specific yield spread and changes in the general level of interest rates. That is to say, the yield curve may flatten when rates are both falling or rising, and equally may steepen under either scenario as well. The key element of any spread trade is that it is structured so that a profit (or any loss) is made only as a result of a change in the spread, and not due to any change in overall yield levels. That is, spread trading eliminates market-directional or first-order market risk.

## BOND SPREAD WEIGHTING

Table 12.3 shows data for our selection of gilts but with additional information on the basis point value (BPV) for each point. This is also known as the 'dollar value of a basis point' or DV01.

If a trader believed that the yield curve was going to flatten, but had no particular strong feeling about whether this flattening would occur in an environment of falling or rising interest rates, and thought that the flattening would be most pronounced in the two-year versus ten-year spread, they could put on a spread consisting of a short position in the two-year and a long position in the ten-year. This spread must be duration-weighted to eliminate first-order risk. At this stage we must point out, and it is important to be aware of, the fact that basis point values, which are used to weight the trade, are based on modified duration measures. From an elementary understanding of bond maths we know that this measure is an approximation, and will be inaccurate for large changes in yield. Therefore the trader must monitor the spread to ensure that the weights are not going out of line, especially in a volatile market environment.

TABLE 12.3 Bond basis point value, 22 October 1999

| Coupon   | Maturity   |   Duration |   Yield% |   Price |     BPV |
|----------|------------|------------|----------|---------|---------|
| 8%       | 07/12/2000 |      1.072 |    5.972 |  102.17 | 0.01095 |
| 10%      | 26/02/2001 |     1.2601 |    6.051 |  105.01 | 0.01880 |
| 7%       | 07/06/2002 |      2.388 |    6.367 |   101.5 | 0.02410 |
| 5%       | 07/06/2004 |      4.104 |    6.327 |   94.74 | 0.03835 |
| 6.75%    | 26/11/2004 |      4.233 |    6.351 |  101.71 | 0.03980 |
| 5.75%    | 07/12/2009 |      7.437 |     5.77 |   99.84 | 0.07584 |
| 6.25%    | 25/11/2010 |      7.957 |     5.72 |   104.3 | 0.07526 |
| 6%       | 07/12/2028 |     15.031 |     4.77 |  119.25 | 0.17834 |

To  weight  the  spread,  the  trader  should  use  the  ratios  of  the  BPVs of  each  bond  to  decide  on  how  much  to  trade.  Assume  that  the  trader wants to purchase £10 million of the ten-year.  In  this  case,  he  must  sell ((0.07584/0.02410) × 10,000,000) or £31,468,880 of the two-year bond. It is also possible to weight a trade using the bonds' duration values, but this is rare. It is common practice to use the BPV.

The payoff from the trade depends on what happens to the two-year versus ten-year spread. If the yields on both bonds move by the same amount, there will be no profit generated, although there will be a funding consideration. If the spread does indeed narrow, the trade will generate profit. Note that disciplined trading calls for both an expected target spread as well as a fixed time horizon. So for example, if the current spread is 59.7 basis points, the trader may decide to take the profit if the spread narrows to 50 basis points, with a three-week horizon. If, at the end of three weeks, the spread has not reached the target, the trader should unwind the position anyway, because that was their original target. On the other hand, what if the spread has narrowed to 48 basis points after one week and looks like narrowing further  -  what  should  the  trader  do? Again,  disciplined  trading  suggests the  profit  should  be  taken.  If  contrary  to  expectations,  the  spread  starts to widen, if it reaches 64.5 basis points the trade should be unwound, this 'stop-loss' being at the half-way point of the original profit target.

The financing of the trade in the repo markets is an important aspect of the trade, and will set the trade's break-even level. If the bond being shorted (in  our  example, the two-year bond) is special ,  this  will  have  an  adverse impact on the financing of the trade. The repo considerations are reviewed in the author's book The Global Repo Markets (Wiley 2004).

## TYPES OF BOND SPREADS

A bond spread has two fundamental characteristics; in theory there should be no profit or loss effect due to a general change in interest rates, and any profit or loss should only occur as a result of a change in the specific spread being traded. Most bond spread trades are yield curve trades where a view is taken on whether a particular spread will widen or narrow. Therefore it is important to be able to identify which sectors of the curve to sell. Assuming that a trader is able to transact business along any part of the yield curve, there are a number of factors to consider. In the first instance, the historic spread between the two sectors of the curve. To illustrate in simplistic fashion, if the 2-10-year spread has been between 40 and 50 basis points over the  last  6  months,  but  very  recently  has  narrowed  to  less  than  35  basis points, this may indicate imminent spread widening. Other factors to consider are demand and liquidity for individual stocks relative to others, and any market intelligence that the trader gleans. If there has been considerable customer interest in certain stocks relative to others, because investors themselves  are  switching  out  of  certain  stocks  and  into  others,  this  may indicate a possible yield curve play. It is a matter of individual judgement.

An historical analysis requires that the trader identifies some part of the yield curve within which he expects to observe a flattening or steepening. It is, of course, entirely possible that one segment of the curve will flatten while another segment is steepening, in fact this scenario is quite common. This  reflects  the  fact  that  different  segments  respond  to  news  and  other occurrences in different ways. An example of this is shown at Figure 12.4.

A more exotic type of yield curve spread is a curvature trade. Let us consider,  for  example,  a  trader  who  believes  that  three-year  bonds  will outperform on a relative basis, both two-year and five-year bonds. That is, he  believes  that  the  two-year  or  three-year  spread  will  narrow  relative to  the  three-year  or  five-year  spread,  in  other  words  that  the  curvature of the yield curve will decrease. This is also known as a butterfly / barbell trade.  In  our  example,  the  trader  will  buy  the  three-year  bond,  against short sales of both the two-year and the five-year bonds. All positions are duration-weighted.

FIGURE 12.4 2-year and 10-year spread, UK gilt market March 1999. Source : Bloomberg.

<!-- image -->

In the final chapter of the book, we look at identifying anomalies in the yield curve that may point to potential spread trade opportunities.

Neil Armstrong seemed more the observer than the participant, but when you looked at his eyes you knew that he was the commander and had all the pieces assembled in his mind. I don't think he ever raised his voice. He just saved his energy for when it was needed.

-- Gene Kranz, Failure Is Not An Option: Mission Control from Mercury to Apollo 13 and Beyond , New York, NY: Berkley Books, 2000

## CHAPTER  13

## Identifying Relative Value in the US Treasury Market: Acquiring New Benchmark Definitions from an Ancillary Yield Curve 1

I n the US, there have been numerous attempts to derive a benchmark yield curve from subsets of available sovereign bonds such as the US Treasury Quotes published daily.  Typically obvious non-liquid instruments are avoided in an attempt to converge to an extraction on the remaining relatively large list of securities, which is termed a 'benchmark' curve. In a real sense this is a problem which has no clear solution that nevertheless must be 'solved' so that business can be conducted! Previously we have developed an optimisation method with which we have obtained a benchmark yield curve from its application to all US Treasury bills, notes, and bonds published in the Wall Street Journal , roughly 339 in total. But for practitioner application we have sought smaller collections than this entire list. Looking for a curve that would coalesce with the benchmark curve, we have performed an extraction on all T-bills and a subset of notes and bonds for a yield curve termed 'ancillary' which coalesces with the aforementioned benchmark curve and which is more accurate with respect to recovering internal rate of returns closer to the published Ask Yields, which are the published Bond Equivalent Yields for the US Treasury bills. In contrast to what has been termed 'benchmark securities',  for  example,  2YR,  5YR,  10YR,  25YR,  and  so  on,  these  new ancillary securities are connected individually to the yield curve and thereby provide an expansion of the classical benchmarks.

1   This chapter was written by Kenneth Kortanek, John F. Murray Emeritus Professor at The University of Iowa, and Dr Vladimir Medvedev, HED Inc., Hartford WI.

## THE NATURE OF THE UNDERLYING OPTIMISATION: CONVERTING THE PRESENT VALUE APPARATUS INTO A MULTINOMIAL POLYNOMIAL OPTIMISATION

We must state at the outset the importance of Chapters 6, 8 and 9 in Part II of this book as background material for the theory we are about to review. 2

The purpose of this section is to show how using the exponentiation involved in the continuously compounding present value apparatus of the discount  function  leads  to  multivariables  in  the  form  of  as  multinomial polynomials as products of strictly positive variables having arbitrary exponents. This is shown in Kortanek et al. (2010) in full detail.

In  Chapter  2  the  discount  function  is  given  in  the  continuously compounded  realm,  using  the  Napierian  logarithm e 2 71828 . 3 See (3.36-3.38), e.g.

<!-- formula-not-decoded -->

where f ( t,s ) represents the forward rate function for all time periods, inclusively in the interval, [ t T ]. As described in Chapters 1 and 2, ibid. , the discount functions are used to compute the price (Present Value) of a coupon paying bond over a period of time. We take t 0 without loss of generality and set FR s f s 0, .

## A Differential Equation Analogue of the Vasicek Model (1977) with Perturbations

Let t 0 be  the  initial  time  in  years  of  a  given  time  interval,  usually t 0 0, and other times or dates in the time interval are stated in years from 0. The forward rate dynamical system appears in Kortanek et al. (1999, p. 52) and Kortanek et al. (2001, 9.12) as follows:

<!-- formula-not-decoded -->

2   The material underlying our ibid. . and our section on this topic has been in the literature for 20 years, and keeps us from rendering it to an appendix.

3   The effective annual rate r means investing $1 today returns $(1 + r ) n at the end of n years. Continuously compounded annual rate means investing $1 today returns $ e r at the end of one year. Having an effective annual rate r and compounding it daily

means $1 today returns  1 365 365 r ,  which is approximately e r for r small.

## Remark 13.1

Specifying a differential law of motion automatically determines that the bonds  (and  notes)  prices  are  'clean  prices',  which  by  definition  means that there is no consideration for accruals. However, each instrument has a settlement date from which one can specify the uniquely defined accrued interest  and  thereby  the  market  price,  or,  alternatively  named  the  bond's 'dirty price'.  4

Our method specialises the dynamic model to a finite discretisation time structure determined by a selected number, L , of time subintervals.

<!-- formula-not-decoded -->

Thus there are L 2 variables, y r 1 0 ,y 2 and y y L L 3 1 2 , , . Each subinterval has its own variable and those variables before it so that the expression for FR ( T ) uses all variables from time 0 up to and including those in the current time interval, giving a law of motion with an accumulation effect from the past.

We define  a  class  of  piecewise  constant  perturbation  functions, w · as follows:

<!-- formula-not-decoded -->

where w w * , * are preassigned bounds for the perturbations. Formally, the Cauchy formula Kortanek et al. (1999, p. 56) and Kortanek et al. (2001, 2.17) with t 0 0 develops the unique, closed-form solution of the differential equation (1) in exponential form:

<!-- formula-not-decoded -->

By using simplifications for the expression for the integral of the forward rate function into constants depending on T and variables y i L i , 1, , we find that the spot (zero) rate function ZR ( t ) is related to the forward rate function as follows, see Kortanek et al. (2001, 9.15):

4   LPN= #days from Last Paid coupon to the Next coupon date; LPS #days from Last Paid coupon date to Settlement date; FREQ = frequency of coupon payments in a year; Accrued Interest = (COUPON/FREQ)*(LPS/LPN).

<!-- formula-not-decoded -->

In this documentation, we select six time subintervals, so L 6 denoted as:

<!-- formula-not-decoded -->

For  this  example,  there  are  to  be  eight  variables: y r 1 0 , y 2 ,  and y i i i 2 1 6 , , .

Now for some structural detail of FR ( t ) (13.5) for a few time intervals in this example.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Another way of expressing the integral of the forward rate function given in (13.5) is the following one:

<!-- formula-not-decoded -->

where n is just a counter for the number variables of y i needed for its own interval, and where the a T s i are constants depending on time T . In the six-period example, n 3 for t t 0 1 ; n 4 for t t 1 2 ; and n 8 for t t 5 6 .

Because of the exponentiation in present value calculations, there is a convenient second set of strictly positive variables, x i n i , 1, which  are exponentiations of the y i variables, and this will lead to the required polynomial variables.

Since  we  are  interested  in  discounting  cash  flows,  we  need e T FR s ds 0 following the first edition of this book (3.48) on p. 161, which generate the products from (13.8), where corresponding to coupons there must be a strictly positive constant c i which we shall include here: 5

<!-- formula-not-decoded -->

where xi eyi, i 1,n and ci 0.

We note that the new x i variables appear with arbitrary exponents but must be strictly positive. With this observation we obtain generalised positive  coefficient  polynomials  in  an  optimisation  problem  which  is  simpler to  solve  than  general  nonlinear  programming  problems  called geometric programming .  See  (2.27)  for  an  example  of  a  polynomial  model  and Chapters 10 and 11 for more advanced polynomial models. Actually, (6) is merely called a term in geometric programming.

## Remark 13.2

As with ordinary linear programming, the primal 'geometric programming problem', has a dual programme constructed from the same input data and sharing similar duality properties of linear programming such as a common value  of  both  objective  values  at  optimality.  It  associates  a  dual  variable with each of its terms. An implication is that useful sensitivity analysis, [20], is available for an optimal pair of dual geometric programming problems.

We shall present an example of dual optimal GP solutions of a simple example in the Appendix.

We  do  not  present  the  model  development,  but  refer  the  reader  to Kortanek and Medvedev (2010). However, the general idea and overview of the model objective function can be described as follows:

1. Employ a minimising objective function:
2. ◾ constrain the shortest observed yield to maturity;
3. ◾ impose a mean reversion-type ratio constraint based upon the longest observed yield to maturity;
4. ◾ include a measure of smoothness placed upon the sought-for perturbations motivated by (13.10).
2. Observe  the  one-sided  inequality  constraints  relating  fitted  prices  to observed prices, and its companion.
3. Observe the one-sided reversed inequality constraints.

5   Basic mathematical tools are reviewed in [Choudhry (2001), pp. 87, 361].

At this point we note that FR is  continuous over t t L 0 , and continuously infinitely differentiable over this interval except at the L 1 number of 'break-points' t i , i 1 1 , L .

At these points we have:

<!-- formula-not-decoded -->

where FRk is FR restricted to t t k k 1 .

In  our  model  we  fix 0 0,  whose  non-positivity  is  related  to  a mean reversion property of the spot rate. However, in Duffin et al. (1967) is taken as a variable leading to a difficult but solvable nonconvex optimisation problem.

## AN APPROACH TO TREATING UNCERTAINTY QUANTIFICATION

The 'GP Approach' is an addition to  the  list  of  forward  rate  curve  fitting procedures at 12 International Banks kept by the Bank of International Settlements,  BIS  (2005). We  know  of  no  other  extraction  method  whose computations apply to the full set of published data, for example, all US Treasury bills and all Treasury notes and bonds on a given day. The total number of securities in this collection is about 300. However, in Sebastian T. Schich's 'The data for estimating the German term structure of interest rates' published in the BIS Papers No. 25, ibid . , he states that 'the sample of 303 issues seems to offer a good compromise between homogeneity and efficiency in estimation'.

In every published case of which we are aware, any implemented extraction applies to a significantly reduced set of instruments from the full available set. The generally accepted belief is that extracting from an appropriate reduced  set  of  instruments  will  faithfully  reflect  the  true  unknown  yield curve function. But no universal extraction method has emerged to justify this belief. It is not yet known what an 'appropriate reduced set of instruments' really is. It is our subjective experience that many authors recognise this open problem.

The Preface of Kortanek et al. (2001) [pp. xi-xii] gives a description tification.  A  shorter  and  more  elegant  description  appears  in  Gusev  and

on the methodology we are following in a treatment of uncertainty quanRomanov's book (2001, pp. 299-300), which we quote:

'A conventional approach to the study of uncertain systems relates to the assumption that uncertainty may be described as a random process with known characteristics. In many applied problems, however, there may be a limited number of observations, incomplete knowledge of the data, and no available statistics whatever. An alternative approach to the  uncertainty  treatment,  known  as  guaranteed  (see  references),  is based on set-membership (unknown but bounded) error description. In the problems considered here the set-membership of uncertainty is employed.'

We have embodied this non-stochastic approach to uncertainty in our initial approach to the problem of extracting the forward rate function from sovereign  fixed  income  data,  Kortanek  et  al.  (1999)  and  Kortanek  et  al. (2010) paper. 6

A common accuracy measure we use for the fitted yield curve is defined as follows, see Kortanek et al. (2010, Section 5).

## Definition 13.1

For an observed bond price time series P t ,  t 1 ,  n and a computed price series, Pt /circumflexnosp , the mean absolute percentage error, MAPE, is:

<!-- formula-not-decoded -->

The units are percentages, so 0.05 means 5 basis points.

Extensive  use  of  MAPE  occurs  in  the  technical  report  by  Bekdache and Baum (1997), although the authors prefer the use of median MAPE to measure average pricing errors. There is an interesting quotation from Bliss (1997), who states that there is, '. . . no particular economic rationale for using a squared-error loss function other than econometric convenience'. Computing MAPE for yields is another possibility whose information could be compared with the MAPE for prices.

Other illustrations to a non-stochastic approach to uncertainty include Kˇrivan (1998), Tichatschke (2002), and Wets (2006). [pp. 19, 25, 27].

6   Note that negative published Bills yields give prices above 100,000.

## TWO COALESCING YIELD CURVES PRODUCING POSSIBLE TRADING OPPORTUNITIES ON OCTOBER 18, 2017

We now turn to the full development, starting with real data for our   focus day, October 18, 2017, all the way down to illustrating a fictitious trade involving  three  bonds  appearing  on  the  full  list  of  258  bonds  listed  in 'Benchmarks Definitions from the Benchmark Curve', one of which has appeared on the Ancillary Curve. All this will be explained now. We begin by reviewing the some entries in the Wall Street Journal in Tables 13.1-13.3.

## On the Structure of the US Treasury Market

On reading the Wall Street Journal Fixed Income Data:

TABLE 13.1 Interest Earned from a Treasury Bond 4% Annual Interest

|             | Begin   | End    | 365   | 360   | Interest%                 |
|-------------|---------|--------|-------|-------|---------------------------|
| Period      | 3/1/03  | 7/3/03 | 124   | 122   | 1.348 124 / 184 × (4 / 2) |
| Ref. Period | 3/1/03  | 9/1/03 | 184   | 180   | 1.356                     |
|             |         |        |       |       | 122 / 180 × (4 / 2)       |

## About the Bond Equivalent Yield

Consider Table 13.3 where one buys at the Asked% as in line 3, followed by computing the AskY ld given in line 4. One checks that this AskY ld equals the BEY; checking either with Section 4.1 or the simplification on Sundaresan (2002, p. 132). The equation in line 4 gives readers an elucidation of the meaning of the BEY.

TABLE 13.2 T-Bill Pricing Formula: 360 Day Convention

| Price Today                                                                                 | Days to Maturity                                                                            | Discount Factor                                                                             | Value at Maturity                                                                           |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| P                                                                                           | n                                                                                           | DF bid or ask                                                                               | 100                                                                                         |
| Equate Maturity Values: P + DF × ( n/ 360) = 100, or Today's Price P = 100 - DF × ( n/ 360) | Equate Maturity Values: P + DF × ( n/ 360) = 100, or Today's Price P = 100 - DF × ( n/ 360) | Equate Maturity Values: P + DF × ( n/ 360) = 100, or Today's Price P = 100 - DF × ( n/ 360) | Equate Maturity Values: P + DF × ( n/ 360) = 100, or Today's Price P = 100 - DF × ( n/ 360) |

One could be at a quandary as to which Bill price to use in studying the yield curve when combining Bills with Notes and Bonds. The quandary is due to the fact that the discounted yield used with Bills gave a market price for which the bill actually traded, in spite of the two shortcomings reviewed in Sundaresan (2002, p. 131).

TABLE 13.3 BEY on Bill Data: DTM = days to maturity; 9/27/02

| Maturity                                                                                                                                                                                                                                                                        | DTM                                                                                                                                                                                                                                                                             | Bid%                                                                                                                                                                                                                                                                            | Asked%                                                                                                                                                                                                                                                                          | Chg%                                                                                                                                                                                                                                                                            | AskY ld %                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 27 Mar 03                                                                                                                                                                                                                                                                       | 181                                                                                                                                                                                                                                                                             | 1.57                                                                                                                                                                                                                                                                            | 1.56                                                                                                                                                                                                                                                                            | -0.02                                                                                                                                                                                                                                                                           | 1.59                                                                                                                                                                                                                                                                            |
| Rule: buy at (Ask) 100 - 1 . 56 × (181 / 360) = 99 . 2157 Equate values: 99 . 2157(1 + AskY ld (181 / 365)) = 100 For your rate of return AskY ld = 1 . 5941% ................................................................................................................. | Rule: buy at (Ask) 100 - 1 . 56 × (181 / 360) = 99 . 2157 Equate values: 99 . 2157(1 + AskY ld (181 / 365)) = 100 For your rate of return AskY ld = 1 . 5941% ................................................................................................................. | Rule: buy at (Ask) 100 - 1 . 56 × (181 / 360) = 99 . 2157 Equate values: 99 . 2157(1 + AskY ld (181 / 365)) = 100 For your rate of return AskY ld = 1 . 5941% ................................................................................................................. | Rule: buy at (Ask) 100 - 1 . 56 × (181 / 360) = 99 . 2157 Equate values: 99 . 2157(1 + AskY ld (181 / 365)) = 100 For your rate of return AskY ld = 1 . 5941% ................................................................................................................. | Rule: buy at (Ask) 100 - 1 . 56 × (181 / 360) = 99 . 2157 Equate values: 99 . 2157(1 + AskY ld (181 / 365)) = 100 For your rate of return AskY ld = 1 . 5941% ................................................................................................................. | Rule: buy at (Ask) 100 - 1 . 56 × (181 / 360) = 99 . 2157 Equate values: 99 . 2157(1 + AskY ld (181 / 365)) = 100 For your rate of return AskY ld = 1 . 5941% ................................................................................................................. |
| AskY ld = BEY with asked for buy; BEY = 365( . 0156) / (360 - 181( . 0156)) = 0 . 015941 Rule: sell at (Bid) 100 - 1 . 57 × (181 / 360) = 99 . 2106                                                                                                                             | AskY ld = BEY with asked for buy; BEY = 365( . 0156) / (360 - 181( . 0156)) = 0 . 015941 Rule: sell at (Bid) 100 - 1 . 57 × (181 / 360) = 99 . 2106                                                                                                                             | AskY ld = BEY with asked for buy; BEY = 365( . 0156) / (360 - 181( . 0156)) = 0 . 015941 Rule: sell at (Bid) 100 - 1 . 57 × (181 / 360) = 99 . 2106                                                                                                                             | AskY ld = BEY with asked for buy; BEY = 365( . 0156) / (360 - 181( . 0156)) = 0 . 015941 Rule: sell at (Bid) 100 - 1 . 57 × (181 / 360) = 99 . 2106                                                                                                                             | AskY ld = BEY with asked for buy; BEY = 365( . 0156) / (360 - 181( . 0156)) = 0 . 015941 Rule: sell at (Bid) 100 - 1 . 57 × (181 / 360) = 99 . 2106                                                                                                                             | AskY ld = BEY with asked for buy; BEY = 365( . 0156) / (360 - 181( . 0156)) = 0 . 015941 Rule: sell at (Bid) 100 - 1 . 57 × (181 / 360) = 99 . 2106                                                                                                                             |

Most of the days, starting  with  10/18/2017,  the  total  number  of  US Treasury Quotes-WSJ is about 306. We have developed two collections of bonds, each of which produces its own yield curve. But our data sets differ from those of Mark Fisher at the Federal Reserve. His group fits separate curves, one for T-bills and one for Coupon Bonds: 'we have noticed that coupon securities with less than one year to maturity were priced measurably differently from bills.' Our reaction to this phenomenon is to recognise that Bills are already zero-coupon bonds, and no coupon bond with maturity less than one year should be included in the set of bonds from which a yield curve should be extracted. In fact, we call the bonds 'earlies' and there usually are about 48 of them. As usual, there are about 33 Bills, implying that the number of securities in the extraction set is: 306 33 48 291, a set which we term to the entire Treasury market for our development. The yield curve which we extract from the large set is termed, the 'Benchmark Curve', with an apology for the double meaning of the word 'Benchmark'.

Of course, we usually think of 2YR, 5YR, 10YR, and 25YR bonds as benchmark bonds, (for example, see Chapter 13, Figure 13.1, p. 341 and Table 13.1, p. 348 in the First Edition of this book). The tables have guided the organisation of our approach to our example of relative value trades and butterfly trades, while giving us the opportunity to validate the computations in this figure and table.

Our approach mentions a special connection of our ancillary-base list of bonds in that they are more accurately connected to the yield curve, while over experiments since 2014 we have found that the benchmark extraction and the ancillary extraction visually coalesce. Their advantage seems to be developing a partition of the 30-year time horizon into estimated characteristics of the various sub-domains corresponding to social/market behaviour of the decomposition of the total market. Why not 2.5YR rather than 2YR? Which one has a better connection to the overall yield curve? How are the various  segments  pasted  together  in  a  practical  sense  to  form  an  overall market interest rate yield curve? We could benefit from more elaboration from the leaders of segmentation theory, where we read: 'The existence of different segments allows local factors to capture specific information about local information. Once the factors are restricted, they transfer local information to the whole yield curve. In contrast, in traditional term structure models, all the movements are directly related to the whole set of maturities in the spirit of principle components as in Litterman et al. (1991).' How? See Almeida et al. (2017).

FIGURE 13.1 Ancillary &amp; Benchmark Curves including Bills, 18 October 2017.

<!-- image -->

Next we address the accuracy question in the sense of requiring an eventual admissible Bond to have its own internal rate of return to be 'close enough' to the published 'Ask Yield', say nearly 1 basis point (bp), when measured with the Mean (or Median) Absolute Percentage Error,  MAPE. As mentioned above, extensive use of MAPE occurs in the technical report by Bekdache and Baum (1997), and Bliss (1997). We term the accurate bonds to comprise the Ancillary Collection, and with  the  Bills  (33)  to  comprise  the  Ancillary  Curve.  For  our  specific focus-date, 10/18/2017, there were 29 admissible bonds discovered from our list of 258 bonds in our extraction set. Hence our final extraction set  (for  the  computational  fitting  procedure)  of  admissible  Ancillary securities  is  62,  which  automatically  includes  the  33  Bills,  producing  a MAPE 0 0061 . .  During  the  last  20  years  we  have  always  chosen  the BEY for Treasury Bills as it appeared in the Wall Street Journal as the 'AskYield'.

## IMPLICATIONS FOR YIELD SPREAD TRADES

Recall in this case all 33 Bills are included. For each Note and Bond we compute  a  Newton-Raphson  internal  rate  of  return,  IRR  annual  %,  to compare with the WSJ published AskY ld annual  %  for  the  instrument. To accomplish this we select a number, such as 0.010. If the absolute value of the difference between the two %, Newton-Raphson IRR % and WSJ AskY ld %, is greater than 0.010, then the instrument is ignored. Clearly from this arithmetic 0.010, as the difference between the two % is also a % i.e. 1.0 basis point.

## Remark 13.3

In our study we consider only trading subsets of Bonds which include at least one bond from the Ancillary set. Our choice from the Ancillary list for our experiment is the 1.25 coupon maturing in 08/31/2019, with a dirty price of $99.595. A suggested trade is give in Section 6.

There  is  a  type  of  bond  trading  that  Moorad  Choudhry  was  undertaking  in  the  1990s.  Real  world  examples  appear  in  Chapter  13  of  the first edition of this book. Building on his earlier work on such 'butterfly trades', Martellini et al. (2003) examine more examples featuring different spread features.

We have selected a subset of 62 instruments which has achieved a better MAPE accuracy than with the full 291. The extraction from the reduced set of instruments appearing as the Ancillary Curve in Figure 13.1 has provided a yield curve which appears reasonable, based upon a visual comparison between the two extracted yield curves. The title of the graph has the number of instruments in each yield curve along with its MAPE; NA 62  instruments  for  the Ancillary  having MAPE 0 0061 . , while the Benchmark curve has 291 instruments (258 Bonds and Notes with 33 Bills) having MAPE 0 0329 . .

## A PROPOSED BUTTERFLY TRADE WITH THE SHORT

## POSITION STEMMING FROM THE ANCILLARY BOND: 01.868 TABLE 13.4

We have symbolically labelled the three variables to agree with those on

p. 348 in the first edition text (John Wiley &amp; Sons, 2014), noting that M 1 corresponds to the bond having price $99.595 being shorted.

We display the usual characteristics of the 29 bonds defined by the Ancillary Curve in Table 13.1, some of which, such as coupons and price, appear in the public literature; others such as 'convexity' and Modified Duration are offered in many textbooks such as Choudhry (2001) and Krgin (2002). We also create an excerpt as Table 13.5 from the larger one with these characteristics for all 258 bonds, which automatically include the 29 from the Ancillary Curve. Tables 13.4 and 13.5 are to be examined for creating a 'butterfly trade' analogous to the one studied in Chapter 13, pp. 348-349

of the First Edition of this book.

Equations (13.11) and (13.12) are non-singular, i.e. the matrix has an inverse yielding a unique optimal solution. The following LP can be solved via the Solver package of Excel, whose solution will use the invertibility of the constraint matrix with data from Table 13.5, so the linear objective function plays no role in the unique solution. The data appear in Tables 13.4-13.6 and the optimal solution appears in Table 13.7.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and M 2 and M 3 0 .

The coefficients of variable M 2 appears in row 1 in column 4 and column 7 in Table 13.5, while the coefficients of M 3 4 and column 7. The data for shorting 1,000 shares appears in row 2 col-

appear in row 3 in column umn 4 and column 7.

The solution states that we go long on M 2 and M 3 for a total of 996.200 shares, while we short the selected 1,000.

subject to:

The horizontal axis is in years, while the vertical axis is in decimal years. 7

TABLE 13.5 Excerpts from 258 Notes and Bonds 18/10/2017

.  .  ..  .

.01868 .  .  .  .  .  .  .  .  .  .  .  .  .  .  ..  .  .  ..  .  .    .  .  .  .  .  .

.  .  ..  .

.  .  ..  .

.  .  .

.  .  .

.  .  .

.  .  .

. .  .  .  .  .  .

.    .

.  .

.    .

.  .  .

.  .  ..  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .  .  .

| YRR                                                                                                 | TMM                                                                                                 | AI                                                                                                  | DirtyP                                                                                              | Coup Y                                                                                              | MDUR                                                                                                | DUR                                                                                                 | BPV                                                                                                 | Conv                                                                                                |                                                                                                     |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| 01.868                                                                                              | 08/31/19                                                                                            | 0.1386                                                                                              | 099.123                                                                                             | 1.000 1.56                                                                                          | 01.8322                                                                                             | 01.8464                                                                                             | 0.0182                                                                                              | 004.28                                                                                              |                                                                                                     |
| 01.868                                                                                              | 08/31/19                                                                                            | 0.1732                                                                                              | 099.595                                                                                             | 1.250 1.57                                                                                          | 01.8285                                                                                             | 01.8428                                                                                             | 0.0182                                                                                              | 004.27                                                                                              |                                                                                                     |
| 01.868                                                                                              | 08/31/19                                                                                            | 0.2252                                                                                              | 100.350                                                                                             | 1.625 1.56                                                                                          | 01.8232                                                                                             | 01.8374                                                                                             | 0.0183                                                                                              | 004.26                                                                                              |                                                                                                     |
| 02.288 ............................................................................................ | 02.288 ............................................................................................ | 02.288 ............................................................................................ | 02.288 ............................................................................................ | 02.288 ............................................................................................ | 02.288 ............................................................................................ | 02.288 ............................................................................................ | 02.288 ............................................................................................ | 02.288 ............................................................................................ | 02.288 ............................................................................................ |
| 02.288                                                                                              | 01/31/20                                                                                            | 0.2683                                                                                              | 099.432                                                                                             | 1.250 1.62                                                                                          | 02.2361                                                                                             | 02.2543                                                                                             | 0.0222                                                                                              | 006.15                                                                                              |                                                                                                     |
| 02.288                                                                                              | 01/31/20                                                                                            | 0.2952                                                                                              | 099.756                                                                                             | 1.375 1.62                                                                                          | 02.2333                                                                                             | 02.2513                                                                                             | 0.0223                                                                                              | 006.14                                                                                              |                                                                                                     |
| 02.575 ............................................................................................ | 02.575 ............................................................................................ | 02.575 ............................................................................................ | 02.575 ............................................................................................ | 02.575 ............................................................................................ | 02.575 ............................................................................................ | 02.575 ............................................................................................ | 02.575 ............................................................................................ | 02.575 ............................................................................................ | 02.575 ............................................................................................ |
| 02.575                                                                                              | 05/15/20                                                                                            | 0.6359                                                                                              | 100.206                                                                                             | 1.500 1.67                                                                                          | 02.4998                                                                                             | 02.5206                                                                                             | 0.0250                                                                                              | 007.59                                                                                              |                                                                                                     |
| 02.575                                                                                              | 05/15/20                                                                                            | 1.4837                                                                                              | 106.148                                                                                             | 3.500 1.64                                                                                          | 02.4341                                                                                             | 02.4539                                                                                             | 0.0258                                                                                              | 007.34                                                                                              |                                                                                                     |
| 02.575                                                                                              | 05/15/20                                                                                            | 3.7092                                                                                              | 121.741                                                                                             | 8.750 1.57                                                                                          | 02.2920                                                                                             | 02.3097                                                                                             | 0.0279                                                                                              | 006.80                                                                                              |                                                                                                     |
| 02.827 ............................................................................................ | 02.827 ............................................................................................ | 02.827 ............................................................................................ | 02.827 ............................................................................................ | 02.827 ............................................................................................ | 02.827 ............................................................................................ | 02.827 ............................................................................................ | 02.827 ............................................................................................ | 02.827 ............................................................................................ | 02.827 ............................................................................................ |
| 02.827                                                                                              | 08/15/20                                                                                            | 0.2609                                                                                              | 099.730                                                                                             | 1.500 1.69                                                                                          | 02.7474                                                                                             | 02.7706                                                                                             | 0.0274                                                                                              | 009.01                                                                                              |                                                                                                     |
| 02.827                                                                                              | 08/15/20                                                                                            | 0.4565                                                                                              | 103.019                                                                                             | 2.625 1.69                                                                                          | 02.7093                                                                                             | 02.7321                                                                                             | 0.0279                                                                                              | 008.84                                                                                              |                                                                                                     |
| 02.827                                                                                              | 08/15/20                                                                                            | 1.5217                                                                                              | 121.045                                                                                             | 8.750 1.64                                                                                          | 02.5389                                                                                             | 02.5594                                                                                             | 0.0307                                                                                              | 008.12                                                                                              |                                                                                                     |

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .

.  .  .  .

.

The following two bonds are interesting because of maturities one year apart; similar attributes

28.348 02/15/46 0.4348 093.607 2.500 2.85 19.7597 20.0418 0.1850 494.68

29.348 02/15/47

0.5217 103.561

3.000 2.85

19.4911

19.7667

0.2019

493.58

7   The nomenclature for the columns in Table 13.4 appear in the text, pp. 334, 339, and 348. An interesting history entitled 'Yield-Curve Arbitrage Rewards the Skillful' by Craig Torres appeared in The Wall Street Journal Thursday, July 27, 1989. An example of an $8.5 Billion Winning Trade made by Bear Stearns was reported. Bear Stearns failed in 2008 and was sold to JP Morgan Chase.

TABLE 13.6 Comparing IRRs: Ancillary and Benchmark

| Symbolic Price   |   Dirty Price |   Printed Ask-yld |   Coupon |   IRR by Newton |   Computed Ask-yld | Differences in the IRRs   |
|------------------|---------------|-------------------|----------|-----------------|--------------------|---------------------------|
| M 2              |        99.123 |              1.56 |    1.000 |     1.555450292 |              1.555 | 0.000450292               |
| M 1              |        99.595 |              1.57 |    1.250 |     1.566066643 |              1.566 | 0.000066426 a             |
| M 3              |       100.350 |              1.56 |    1.625 |     1.556263463 |              1.556 | 0.000263463               |

TABLE 13.7 LP Unique Solution

|   M 2 * |   M 3 * |   Solution Value |
|---------|---------|------------------|
| 304.491 | 691.709 |          996.200 |

## WHAT TO EXPECT WHEN BILLS ARE EXCLUDED FROM THE FITTING COMPUTATIONS

On the topic of Treasury Bills and Bonds, Fisher (2005, pp. 34-37) reports that during the practice of fitting the yield curve to measure deviations from the yield curve for coupon securities, his team noticed that coupon securities having less than one year to maturity were priced measurably different from bills. Several possible reasons for this were given, but with the conclusion that there should be separate yield curves for bills and coupon securities.

In keeping with the practical approach for this chapter, we have sought to numerically investigate the effect of this practice on properties we have presented for the two curves we extracted, namely 'Ancillary' and 'Benchmark' by treating the T-bills as zero-coupon bonds with maturities less than a year. We envision two practical questions regarding: (a) the inclusion of T-bills; or (b), i.e. not including them for a computationally extracted yield curve.

Since we are focusing on practical yield spread trades, we have required that at least one instrument be in the Ancillary set, which is among the closest to the yield curve itself in the sense of a lower possible MAPE among all the day's bonds. This policy raises two questions about computational results  arising  from  yield  curve  extractions  under  (a)  or  (b)  (i.e.  on  the 'fitting set').

Question I : Which case for the extracted Yield curve, with Bills, or without Bills gives the largest set of Ancillary Bonds?

Question  II :  Which  case  for  the  extracted Yield  curve,  with  Bills,  or without Bills gives the best possibility for sensitivity analysis?

We are continuing the investigation on general answers to these questions, but have chosen in this chapter to focus solely on the collection of the 306 bonds published on 10/18/2017.

## Properties Reached at Terminating Iteration 19 with 33 Bills Included with the 29 Bonds

The respective objective function values are:

Dual Objective Value E -. 6 339647992 00

Primal Objective E Value -. 6 587917939 00

Dual infeasibility E 01. Primal infeasibility E 1 261 9 222 0 . . 3, where in general E-n means times(10 n ), a standard way of indicating accuracy that is presented at the reaching of a stopping criterion.

The minus signs arise from the introduction of a minus sign in the logarithm of the dual GP objective function, establishing convexity, see Remark 13.4. Just as in linear programming, there is a duality inequality stemming from feasible solutions respectively of both programmes:

<!-- formula-not-decoded -->

illustrating  the  main  Lemma  of  Geometric  Programming,  Duffin  et  al. (1967, p. 114). [9, Lemma 1, p. 114].

Note that when 33 bills are present we have not obtained 'perfect duality', where both objective function values coincide. Hence, sensitivity analysis will not be available to us.

## Properties of a Convergent Solution for Perfect Duality: No Bills (illustrated at Figure 13.2 and Table 13.8)

Dual Objective Value = -6.324066327E+00

Primal Objective Val = -6.324066328E+00

Dual infeasibility = 5.331E-05

Primal infeasibility = 4.088E-08

Omitting  the  33  Bills  leads  to  perfect  duality ,  i.e. exp PrimalOV exp DualOV 556 596830 . , achieving perfect duality.

The progress of the iterative computation is the following:

track duality gap iteration 1 904.9464895189722

track duality gap iteration 2 519.0510368829888

track duality gap iteration 3 247.5663953134325

track duality gap iteration 4 32.8973697330057 track duality gap iteration 5 43.1769405506872 track duality gap iteration 6 59.3189197363036 track duality gap iteration 7 59.7704829864851 track duality gap iteration 8 28.0225173613330 track duality gap iteration 9 5.1793604528989 track duality gap iteration 10 0.8139640147618 track duality gap iteration 11 0.0029095258052 track duality gap iteration 12 0.0057922429451 track duality gap iteration 13 0.0023757132426 track duality gap iteration 14 0.0009086398832 track duality gap iteration 15 0.0003363496942 track duality gap iteration 16 0.0001712344308 track duality gap iteration 17 0.0000652578639 track duality gap iteration 18 0.0000367644735 track duality gap iteration 19 0.0000122955589 track duality gap iteration 20 0.0000065494430 track duality gap iteration 21 0.0000022085800 track duality gap iteration 22 0.0000012514129 track duality gap iteration 23 0.0000005111140 track duality gap iteration 24 0.0000003009382 track duality gap iteration 25 0.0000002316700 track duality gap iteration 26 0.0000001071440 track duality gap iteration 27 0.0000000534546 track duality gap iteration 28 0.0000000105986 track duality gap iteration 29 0.0000000023981 track duality gap iteration 30 0.0000000002212 track duality gap iteration 31 0.0000000007839

WSJ10182017 NA = 31  MAPE = 0.008869 No Bills

FIGURE 13.2 Ancillary Curve: No Bills, 18 October 2017.

<!-- image -->

## APPENDIX: GEOMETRIC PROGRAMMING

## The Underlying Polynomial Primal and Dual Programmes

Seek solutions for dual pair MA, MB of posynomial geometric programmes when constraints are present, where A designates the primal programme and B the dual programme.

<!-- image -->

where the a ij are arbitrary real constants but the c i are positive. A first observation is that under the transformation t e j z j Programme A becomes a convex program, the transformed GP problem.

## Remark 13.4

If  we denote the dual function by F, then replacing it with -lnF gives an equivalent linearly constrained convex program. Seek the minimum of:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where A is an (#primal variables + 1) by (#terms) matrix.  The function -lnF is infinitely differentiable except at its boundary where it is not differentiable, even if one uses the continuity at 0 of h(x) := (a/x) x  for x &gt; 0 and h(0) := 1. Degree of Difficulty = #terms - #primals -1, [9]. The expressions g t k p k 1, are termed polynomials. Should the c i be arbitrary, one uses the terminology signomials.

The standard statement about the size of the primal program is that, (a) there are m primal variables, (b) there are n 0 terms in g 0 , n n 1 0 terms in g n n p p 1 1 , , terms in g p , so there are n p total terms in the primal program, (c) the number of (only inequality) constraints is p, and (d) the degree of difficulty is n m 1.

p

## Remark 13.5

We illustrate these constants as follows: (a) there are 505 primal variables, (b) there are 487 terms, (c) the number of primal constraints is 568, and (d) the degree of difficulty is 981. The computational speed is essentially 'negligible' in this case.

## Appearing as Perfect Duality in '11 TABLE 13.4 NUD of Example 4.2 α = 0 . 25' in [5]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

PrimalOBJ Exp GPdual ( ln . 17 50358

Primal infeasibility 3 924 15 . E , Dual infeasibility 3 153 14 . E , Optimal solutions:

| i,j           |       1 |       2 |       3 | 4       | 5       |
|---------------|---------|---------|---------|---------|---------|
| Primalj = 1,3 | 0.43950 | 1.74847 | 0.90821 |         |         |
| Dual i 1 5 ,  | 0.79985 | 0.20014 | 0.06524 | 0.33247 | 0.27620 |

## WEBSITE

Instructions regarding the web site.

Open the web site in the browser using the following URL https://www.vgmconsultingllc.net:446/kwelproject/

<!-- image -->

When the web site is loaded, click on the 'Curves' button. The following view will be generated.

<!-- image -->

To select the date, click the 'Calendar' icon in the date selector.

<!-- image -->

## Then select the available date you want to generate curves.

<!-- image -->

## And click the 'Load' button.

The Benchmark and Ancillary curves will be generated.

<!-- image -->

## ADDENDUM: EXPERIMENTS FROM 17/12/2018

It is well known that markets for Bonds and Notes are different from markets for Bills, since the former uses the present value mechanism for valuations, which the latter does not. So, Treasury yield curves extracted from bonds and notes are valid from 2 years to 30 years out. Bills yields are valid from 0 to 1 year. While we can obtain Bill yield curves very accurately, we are  focusing  in  the  near  term  on  Bond  and  Note  yield  curves,  with  Bills Treasury yields to appear in the near future.

For T-Bills, DF2M simply denotes Days to Maturity. For DTM &gt; 182, we use  the  formula  for  convenience  on  page  132  in  Suresh  Sundaresan's  book (2002). Consequently, we use Bonds/Notes to present Treasury Yields beginning with one year to maturity. These are illustrated at Figure 13.3 and Figure 13.4.

A completely flat Treasury yield curve from one year out is characteristic in an economic recession. The yield curves extracted on 17/12/2018, indicate that the US economy is in a recession. It is interesting that for a relatively small number of instruments, here 37, judiciously chosen, upon extraction gives what we have been calling the Ancillary Curve, which coalesces visually well with what we have been calling the Benchmark Curve extracted from the full list of 310 reported Wall Street Journal Bonds and Notes over the period 1 to 30 years.

Here  we  see  two  pairs  of  yield  curves  corresponding  to  first  for 17/12/2018, the Ancillary extracted from 37 'judiciously' chosen instruments from the full set of 310 Notes and Bonds having MAPE 000896, and what we term the Benchmark curve extracted from the full set of 310 instruments, having MAPE 0.0180. The second display is for 19/12/2018 for 15 judiciously selected Bond/Notes (with MAPE 0,00956) and from the 310

FIGURE 13.3 Results from December 2018 (i)

<!-- image -->

FIGURE 13.4 Results from December 2018 (ii)

<!-- image -->

total having MAPE 0.0202. In presenting eight or nine Treasury Yields, we attempt to read them from the Ancillary curve since the accuracy is better than what has been achieved in the Benchmark curve.

We also get extractions for the 41 or so Treasury Bills for which we could present yields for one, two, three and six months, but for year one we must use yields from the Notes and Bonds, as the only instruments from which we perform the extractions, because of the yield on a Bill with time to maturity greater that 182 days [see Sundaresan (2002), p. 132]. We welcome comparisons of all  of  our Treasury Yields  with  the  Daily Treasury Yield Curve Rates. (For comments and queries, please email the author via the publishers for a PDF version of this chapter.)

## SELECTED BIBLIOGRAPHY AND REFERENCES

Almeida, C., Ardison, K., Kubudi, D., Simonsen, A. and Vincente, J., 'Forecasting Bond Yields with Segmented Term Structure Models', Journal of Financial Econometrics , Oxford University Press, https://doi.org/10.1093/jjfinec/nbx002, 14 February 2017.

- BIS. BIS Papers No. 25; Zero-coupon yield curves: Technical Documentation. Bank for International Settlements, CH-4002 Basel, Switzerland, 2005.
- Bekdache B. and Baum, C.F., The Ex ante predictive accuracy of alternate models of the term structure of interest rates . Technical report, Department of Economics, Wayne State University, Detroit, MI 58202, 1997. The Third Annual Conference of the Society for Computational Economics.

Bliss, R.R., 'Testing term structure estimation methods', Advances in Futures and Options Research , 9, 1997, pp. 197-231.

Bricker, D.L. and Kortanek, K.O., 'Perfect Duality in Solving Geometric Programming Problems under Uncertainty', Journal of Optimization Theory and Applications 173, Issue 3, 2017, pp. 1055-1065.

- Choudhry, M., Joannas, D., Landuyt, G., Pereira, R. and Pienaar, R., Capital Markets Instruments , FT Prentice Hall, 2001. Third Edition. Foreword by Vince Cable MP.
- Choudhry, M., Bond Market Securities , Pearson Education Limited. Edinburgh Gate, Harlow, 2001.
- Choudhry, M., Analysing &amp; Interpreting the Yield Curve , Wiley Finance. John Wiley &amp; Sons, 2004.
- Duffin, R.J., Peterson, E.L. and Zener, C.L., Geometric Programming - Theory and Applications . John Wiley and Sons: New York, 1967.
- Fisher, M., Fitting the U.S. term structure at the Federal Reserve Board , BIS Papers No. 25; Zero-coupon yield curves: Technical Documentation. Bank for International Settlements, CH-4002 Basel, Switzerland, 2005.
- Gusev, M.I. and Romanov, S.A., 'On stability of guaranteed estimation problems: error bounds for information domains and experimental design', In M.A. Goberna and M.A. L´opez (ed.), Semi-infinite Programming Recent Advances, Nonconvex Optimization and Its Applications Vol. 57, Massachusetts: Kluwer Academic Publishers, 2001.
- Kortanek, K.O. and Medvedev, V.G., E stimating the Term Structure of Interest Rates , March 26, 1998. The Courant Institute of Mathematical Sciences, New York University Mathematical Finance Seminar, 1997-1998.
- Kortanek, K.O. and Medvedev, V.G., 'Models for estimating the structure of interest rates from observations of yield curves', In M. Avellaneda (ed.), Quantitative Analysis in Financial Markets , World Scientific Publishing Company: Singapore, 1999, pp. 53-120.
- Kortanek, K.O. and Medvedev, V.G., Building and Using Dynamic Interest Rate Models , Wiley Finance. John Wiley &amp; Sons: Chichester, 2001.
- Kortanek, K.O. and Medvedev, V.G., 'An optimization model for extracting forward interest rates from a dynamical system under financial uncertainty', Dynamics of Continuous, Discrete &amp; Impulsive Systems: Series B Applications &amp; Algorithms 17, Special Issue on Optimization and Dynamics in Finance, 2010, pp. 1-21.
- Kortanek, K.O., Xu, X. and Ye, Y., 'An infeasible interior-point algorithm for solving primal and dual geometric programs', Mathematical Programming 76, 1996, pp. 155- 181.
- Krgin, D., Handbook of Global Fixed Income Calculations . Frank J. Fabozzi. John Wiley &amp; Sons: New York, 2002.
- Kˇrivan, V. and Colombo, G., 'A non-stochastic approach for modelling uncertainty in population dynamics', Bulletin of Mathematical Biology 60, 1998, pp. 721-751.
- Kyparisis, J., 'Sensitivity Analysis in Geometric Programming: Theory and Computations', Annal of Operations Research 2, 1990, pp. 39-64.
- Litterman, R. and Scheinkman, J., 'Common Factors Affecting Bond Returns', Journal of Fixed Income 1, 1991, pp. 54-61.
- Martellini, L., Priaulet, P. and Priaulet, S., Fixed-Income Securities Valuation, Risk Management and Portfolio Strategies , Wiley Finance Series, John Wiley &amp; Sons: Chichester, 2003.

- Medvedev, V.G., 'Optimal observations of initial state and input disturbances for dynamic systems', SAMS , 14, 1994, pp. 275-288.
- Sundaresan, S.M., Fixed Income Markets and their Derivatives , 2nd edition, SouthWestern: Cincinnati, 2002.
- Tichatschke, R., Kaplan, A., Voetmann, T. and Bohm, M., 'Numerical treatment of an asset price model with non-stochastic uncertainty', TOP Sociedad de Estadist´ıca e Investigaci´on Operativa 10, 2002, pp. 1-50.
- Vasicek, O., 'An equilibrium characterization of the term structure', Journal of Financial Economics 5, 1977, pp. 177-188.
- Wets, R.J.B. and Bianchi, S.W., 'Term and volatility structures', In S.A. Zenios and W.T. Ziemba (ed.), Handbook of Asset and Liability Management Vol. 1: Theory and Methodology, Elsievier Science, 2006, pp. 25-68, Chapter 2.

## APPENDIX

## Bond Yield Measurement

I n the Preface to this book, we noted the importance of the yield curve to an understanding of the bond markets. But before we discuss the yield curve, we must be familiar with the concept of bond yields and bond yield measurement. So in this Appendix we introduce the subject for beginners.

From  an  elementary  understanding  of  financial  arithmetic  we  know how to calculate the price of a bond using an appropriate discount rate known as the bond's yield. This  is  the  same  as  calculating  a net  present value of the bond's cash flows at the selected discount rate. We can reverse this procedure to find the yield of a bond where the price is known, which is equivalent to calculating the bond's internal rate of return (IRR) to a specified maturity date. There is no equation for this calculation and a solution is  obtained using numerical iteration. The IRR calculation is taken to be a bond's yield to maturity or redemption yield and is one of various yield measures used in the markets to estimate the return generated from holding a bond. We will consider these various measures as they apply to plain vanilla bonds.

In most markets, bonds are generally traded on the basis of their prices but because of the complicated patterns of cash flows that different bonds can have, they are generally compared in terms of their yields. This means that a market-maker will usually quote a two-way price at which he will buy or sell a particular bond, but it is the yield at which the bond is trading that is important to the market-maker's customer. This is because a bond's price does not actually tell us anything useful about what we are getting. Remember that in any market there will be a number of bonds with different issuers, coupons and terms to maturity. Even in a homogeneous market such as the UK government bond ( gilt ) market, different gilts trade according to their own specific characteristics. To compare bonds in the market, therefore, we need the yield on any bond and it is yields that we compare, not prices. A fund manager who is quoted a price at which he can buy a bond is instantly aware of what yield that price represents, and whether this yield represents fair value.

321

The yield on any investment is the interest rate that will make the present value of the cash flows from the investment equal to the initial cost (price) of the investment. Mathematically, the yield on any investment, represented by r , is the interest rate that satisfies equation (A.1):

<!-- formula-not-decoded -->

Cn is the cash flow in year n ;

P is the price of the investment;

n is the number of years.

The yield calculated from this relationship is the internal rate of return . But as we have noted, there are other types of yield measure used in the market for different purposes. The most important of these are bond redemption yields, spot rates, and forward rates. We will now discuss each type of yield measure and show how they are computed, followed by a discussion of the relative usefulness of each measure.

## CURRENT YIELD

The simplest measure of the yield on a bond is the current yield, also known as the flat yield , interest yield or running yield. The running yield is given by (A.2):

<!-- formula-not-decoded -->

C is the bond coupon;

rc is the current yield;

P is the clean price of the bond.

In (A.2) C is not expressed as a decimal. Current yield ignores any capital gain or loss that might arise from holding and trading a bond and does not consider the time value of money. It essentially calculates the bond coupon income as a proportion of the price paid for the bond, and to be accurate would have to assume that the bond was more like an annuity rather than a fixed-term instrument. It is not really an 'interest rate', though.

where:

where:

The current yield is useful as a 'rough-and-ready' interest rate calculation. It is often used to estimate the cost of or profit from a short-term holding of a bond. For example, if other short-term interest rates such as the one-week or three-month rates are higher than the current yield, holding the bond is said to involve a running cost . This is also known as negative carry or negative funding . The term is used by bond traders and market-makers and leveraged investors. The carry on a bond is a useful measure for all market practitioners as it illustrates the cost of holding or funding a bond. The funding rate is the bondholder's short-term cost of funds. A private investor could also apply this to a short-term holding of bonds.

## SIMPLE YIELD TO MATURITY

The simple yield  to  maturity makes  up  for  some  of  the  shortcomings  of the  current  yield  measure  by  taking  into  account  capital  gains  or  losses. The assumption made is that the capital gain or loss occurs evenly over the remaining life of the bond. The resulting formula is:

<!-- formula-not-decoded -->

P is the clean price;

rs is the simple yield to maturity;

n is the number of years to maturity.

For  a  bond  with  a  6%  coupon  and  with  a  price  of  97.89,  and  also assuming n 5 years:

<!-- formula-not-decoded -->

The simple  yield  measure  is  useful  for  rough-and-ready  calculations. However, its main drawback is that it does not take into account compound interest  or  the  time  value  of  money. Any  capital  gain  or  loss  resulting  is amortised equally over the remaining years to maturity. In reality, as bond coupons are paid they can be reinvested, and hence interest can be earned. This increases the overall return from holding the bond. As such, the simple yield measure is not overly useful and it is not commonly encountered in say, the gilt market. However, it is often the main measure used in the Japanese government bond market.

where:

## YIELD TO MATURITY

## Calculating Bond Yield to Maturity

The yield to maturity (YTM) or gross redemption yield is the most frequently used measure of return from holding a bond . 1  Yield to maturity takes into account the pattern of coupon payments, the bond's term to maturity, and the capital gain (or loss) arising over the remaining life of the bond. These elements are all related and are important components determining a bond's price. If we set the IRR for a set of cash flows to be the rate that applies from a start-date to an end-date we can assume the IRR to be the YTM for those cash flows. The YTM therefore is equivalent to the internal rate of return on the bond, the rate that equates the value of the discounted cash flows on the bond to its current price. The calculation assumes that the bond is held until maturity and therefore it is the cash flows to maturity that are discounted in the calculation. It also employs the concept of the time value of money.

As we would expect, the formula for YTM is essentially that for calculating the price of a bond. For a bond paying annual coupons, the YTM is calculated by solving equation (A.4), and we assume that the first coupon will be paid exactly one interest period now (which, for an annual coupon bond is exactly one year from now).

<!-- formula-not-decoded -->

where:

P d is the bond dirty price;

M is the par or redemption payment (100);

n is the number of interest periods;

C is the coupon rate;

rm is the annual yield to maturity (the YTM).

Note that the number of interest periods in an annual coupon bond is equal to the number of years to maturity, and so for these bonds n is equal to the number of years to maturity.

We can simplify (A.4) using ∑:

<!-- formula-not-decoded -->

1 In  this  book,  the  terms  yield  to  maturity  and  gross  redemption  yield  are  used synonymously. The latter term is common in sterling markets.

Note that the expression at (A.5) has two variable parameters, the price P d and yield rm . It cannot be rearranged to solve for yield rm explicitly and must be solved using numerical iteration. The process involves estimating a value for rm and calculating the price associated with the estimated yield. If the calculated price is higher than the price of the bond at the time, the yield estimate is lower than the actual yield, and so it must be adjusted until it converges to the level that corresponds with the bond price. 2

For YTM for a semi-annual coupon bond, we have to adjust the formula to allow for the semi-annual payments. Equation (A.5) is modified as shown by (A.6), again assuming there are precisely six months to the next coupon payment:

<!-- formula-not-decoded -->

where n is the now the number of interest periods in the life of the bond and therefore equal to the number of years to maturity multiplied by two .

For yield calculations carried out by hand ('long-hand'), we can simplify (A.5) and (A.6) to reduce the amount of arithmetic. For a semi-annual coupon bond with an actual/365 day-base count, (A.6) can be written out long-hand and rearranged to give us (A.7):

<!-- formula-not-decoded -->

where:

P d is the dirty price of the bond;

rm is the yield to maturity;

Ntc is the number of days between the current date and the next coupon date;

n is the number of coupon payments before redemption. If T is the number of complete years before redemption, then n T 2 if there is an even number of coupon payments before redemption, and n T 2 1 if there is an odd number of coupon payments before redemption.

2   Bloomberg ®  also uses the term yield-to-workout where 'workout' refers to the maturity date for the bond.

All the YTM equations above use rm to discount a bond's cash flows back to the next coupon payment and then discount the value at that date back to the date of the calculation. In other words, rm is the internal rate of return (IRR) that equates the value of the discounted cash flows on the bond to the current dirty price of the bond (at the current date). The internal rate of return is the discount rate, which, if applied to all of the cash flows, solves for a number that is equal to the dirty price of the bond (its present value). By assuming that this rate will be unchanged for the reinvestment of all the coupon cash flows, and that the instrument will be held to maturity, the IRR can then be seen as the yield to maturity. In effect both measures are identical - the assumption of uniform reinvestment rate allows us to calculate the IRR as equivalent to the redemption yield. It is common for the IRR measure to be used by corporate financiers for project appraisal, while the redemption yield measure is used in bond markets. The solution to the equation for rm cannot be found analytically and has to be solved through numerical iteration, that is, by estimating the yield from two trial values for rm, then solving by using the formula for linear interpolation. It is more common nowadays to use Microsoft Excel or a programmable calculator such as the Hewlett-Packard calculator.

For the equation at (A.7) we have altered the exponent used to raise the power of the discount rate in the first part of the formula to N/182.5. This is a special case and is only applicable to bonds with an actual/365 day-count base. The YTM in this case is sometimes referred to as the consortium yield, which is a redemption yield that assumes exactly 182.5 days between each semi-annual coupon date. As most developed-country bond markets now use actual/actual day bases, it is not common to encounter the consortium yield equation.

## Using the Redemption Yield Calculation

We have already alluded to the key assumption behind the YTM calculation, namely that the rate rm remains stable for the entire period of the life of the bond. By assuming the same yield, we can say that all coupons are reinvested at the same yield rm. For the bond noted above, this means that if all the cash flows are discounted at 6.56%, they will have a total present value or NPV of 97.89. At the same time, if all the cash flows received during the life of the bond are reinvested at 6.56% until the maturity of the bond, the final redemption yield will be 6.56% . This is patently unrealistic, since we can predict with virtual certainty that interest rates for instruments of similar maturity to the bond at each coupon date will not remain at 6.56% for five years.

In practice, however, investors require a rate of return that is equivalent to the price that they are paying for a bond and the redemption yield is, to put it simply, as good a measurement as any. A more accurate measurement might be to calculate present values of future cash flows using the discount rate  that  is  equal  to  the  market's  view  on  where  interest  rates  will  be  at that point, known as the forward interest rate. However, forward rates are implied interest rates, and a YTM measurement calculated using forward rates can be as speculative as one calculated using the conventional formula. This is because the actual market interest rate at any time is invariably different  from  the  rate  implied  earlier  in  the  forward  markets. Therefore  a YTM calculation made using forward rates would not be realised in practice either. 3  The zero-coupon interest rate is the true interest rate for any term

## Example A.1 COMPARING THE DIFFERENT YIELD MEASURES

The examples in this section illustrate a five-year bond with a coupon of 6% trading at a price of 97.89. Using the three common measures of return we have:

Running yield = 6.129% Simple yield = 6.560%

Redemption yield = 6.50%

The different yield measures are illustrated graphically in Figure A.1 below.

FIGURE A.1 Comparing yield measures for a 6% bond with five years to maturity.

<!-- image -->

3   However, such an approach is used to price interest rate swaps.

to maturity, however, the YTM is, despite the limitations presented by its assumptions, still the main measure of return used in the markets.

## Calculating Redemption Yield Between Coupon Payments

The yield formula (A.4) can be used whenever the settlement date for the bond falls on a coupon date, so that there is precisely one interest period to the next coupon date. If the settlement date falls in between coupon dates, the same price/yield relationship holds and the YTM is the interest rate that equates the NPV of the bond's cash flows with its dirty price. However, the formula is adjusted to allow for the uneven interest period, and this is given by (A.8) for an annual coupon bond:

<!-- formula-not-decoded -->

where:

w is number of days between the settlement date and the next coupon date number of days in the interest period

and n is the number of coupon payments remaining in the life of bond. The other parameters are as before. As before, the formula can be shortened as given by (A.9):

<!-- formula-not-decoded -->

## Yield Represented by Par Bond Price

A characteristic of bonds is that when the required yield is the same as a bond's coupon rate, the price is par (100%). We expect this because the cash flows represented by a bond result from a fixed coupon payment, and discounting these cash flows at the coupon rate will result in a net present value (NPV) of 100 again. As the yield required for the bond decreases below the coupon rate, the NPV will rise, and vice versa if the required yield increases above the coupon rate. We can approximate a  bond's price to par at any time that the yield is the same as the coupon. However, the price of a bond is only precisely equal to par in this case when the calculation is made on a coupon date. On any other date the price will not be exactly par when the yield equals the coupon rate. This is because accrued interest on the bond is calculated on a simple interest basis, whereas bond prices are calculated on a compound interest basis. The rule is that on a non-coupon date where a bond is priced at par, the redemption yield is just below the coupon rate. This effect is amplified the further away the bond settlement date lies from the coupon date and will impact more on short-dated bonds. In most cases, however, this feature of bonds does not have any practical impact.

In the context of yield represented by a par bond price, we might occasionally encounter yield to par or par yield , which is the yield for a bond trading at or near its par value (100%). In practice, this refers to a bond price between 99 and 101%, and the par yield is essentially the coupon rate for a bond trading at or near par.

## Yield on a Zero-Coupon Bond

Zero-coupon bonds, sometimes known as strips , have only one cash flow, the redemption payment on maturity. Hence the name: strips pay no coupon during their life. In virtually all cases, zero-coupon bonds make one payment on redemption, and this payment will be par (100). Therefore a zerocoupon bond is sold at a discount to par and trades at a discount during its life. For a bond with only one cash flow it is not necessary to use (A.4) and we can use (A.10) instead:

<!-- formula-not-decoded -->

where C is  the  final  redemption  payment,  usually  par  (100). This  is  the 'traditional' approach. Note that P , the price of a zero-coupon bond, has only one meaning because there is no 'dirty' price, since no accrued interest arises.

Equation (A.10) still uses n for  the  number of interest periods in the bond's life. Because no interest is actually paid by a zero-coupon bond, the interest periods are known as quasi-interest periods. A quasi-interest period is an assumed interest period, where the assumption is that the bond pays interest.  It  is  important  to  remember  this  because  zero-coupon  bonds  in markets that use a semi-annual convention have n equal to double the number of years to maturity. For annual coupon bond markets n is equal to the number of years to redemption. We can rearrange (A.10) for the yield, rm :

<!-- formula-not-decoded -->

## MODIFYING BOND YIELDS

## Very Short-Dated Bonds

A bond with one coupon remaining, often trades as a money market instrument because it has only one cash flow, its redemption payment and final coupon on maturity. In fact, a bond that was also trading below par would have the characteristics of a short-term zero-coupon bond. The usual convention in the markets is to adjust bond yields using money market convention by discounting the cash flow at a simple rate of interest instead of a compound rate.

The bond yield formula is the case of a short-term final coupon bond is given by (A.12):

<!-- formula-not-decoded -->

where B is the day-base count for the bond (360, 365 or 366).

## Money Market Yields 4

Price  and  yield  conventions  in  domestic  money  markets  are  often  different to those in use in the same country's bond markets. For example, the day-count convention for the US money market is Actual/360, while the Treasury bond market uses actual/actual. A list of the conventions in use in selected countries is given in the author's book Fixed Income Markets (Wiley 2014).

The different conventions in use in money markets compared to bond markets results in some difficulty when comparing yields across markets. It is important to adjust yields when comparisons are made, and the usual practice is to calculate a money market-equivalent yield for bond instruments. We can illustrate this by comparing the different approaches used in the Certificate of Deposit (CD) market compared to bond markets. Money market instruments make their interest payments as actual and not rounded amounts.  A  long-dated  CD  price  calculation  uses  exact  day  counts,  as opposed to the regular time intervals assumed for bonds, and the final discount from the nearest coupon date to the settlement date is done using simple, rather than continuous compounding. In order to compare bond yields to money market yields, we calculate a money market yield for the bond. In the US market the adjustment of the bond yield is given by (A.13), which shows the adjustment required to the Actual/360 day-count convention:

4   Money markets are covered in detail in the author's book The Money Markets Handbook (John Wiley &amp; Sons Limited, 2004).

where:

<!-- formula-not-decoded -->

r me is the bond money-market yield;

t is the fraction of the bond coupon period, on a money market basis.

## CONVERTING BOND YIELDS

## Discounting and Coupon Frequency

In  our  discussion  on  yield,  we  noted  the  difference  between  calculating redemption  yield  on  the  basis  of  both  annual  and  semi-annual  coupon bonds. Analysis of bonds that pay semi-annual coupons incorporates semiannual discounting of semi-annual coupon payments. This is appropriate for most UK and US bonds. However, government bonds in most of continental Europe, and most Eurobonds, for example, have annual coupon payments, and the appropriate method of calculating the redemption yield is to use annual discounting. The two yield measures are not therefore directly comparable. We could make a Eurobond directly comparable with a UK gilt by using semi-annual discounting of the Eurobond's annual coupon payments. Alternatively, we could make the gilt comparable with the Eurobond by using annual discounting of its semi-annual coupon payments.

The price/yield formulas for the different discounting possibilities we encounter in the markets are listed below. (As usual we assume that the

calculation takes place on a coupon payment date so that accrued interest is zero.)

- ◾ Semi-annual discounting of semi-annual payments:

<!-- formula-not-decoded -->

- ◾ Annual discounting of annual payments:

<!-- formula-not-decoded -->

- ◾ Semi-annual discounting of annual payments:

<!-- formula-not-decoded -->

- ◾ Annual discounting of semi-annual payments:

<!-- formula-not-decoded -->

Earlier, we considered a bond with a dirty price of 97.89, a coupon of 6% and five years to maturity. This bond would have the following gross redemption yields under the different yield calculation conventions:

| Discounting   | Payments    |   Yield to Maturity (%) |
|---------------|-------------|-------------------------|
| Semi-annual   | Semi-annual |                   6.500 |
| Annual        | Annual      |                   6.508 |
| Semi-annual   | Annual      |                   6.428 |
| Annual        | Semi-annual |                   6.605 |

This proves what we have already observed, namely that the coupon and discounting frequency impacts upon the redemption yield calculation for a bond. We can see that increasing the frequency of discounting decreases the yield, while increasing the frequency of payments increases the yield. When comparing yields for bonds that trade in markets with different conventions it is important to convert all the yields to the same calculation basis.

## Converting Yields

Intuitively we might think that doubling a semi-annual yield figure will give us the annualised equivalent - in fact this will result in an inaccurate figure due to the multiplicative effects of discounting and one that is an underestimate of the true annualised yield. The correct procedure for producing annualised yields from semi-annual and quarterly yields is given by the expressions below. The general conversion expression is given by (A.18):

<!-- formula-not-decoded -->

where m is the number of coupon payments per year. Specifically, we can convert  between  annual  and  semi-annual  compounded  yields  using  the expressions given at (A.19):

<!-- formula-not-decoded -->

or between annual and quarterly compounded yields using (A.20):

<!-- formula-not-decoded -->

where rmq , rms and rma are  respectively  the  quarterly,  semi-annually  and annually compounded yields to maturity.

## Assumptions of The Redemption Yield Calculation

While YTM is the most commonly used measure of yield, it does have a major disadvantage. Implicit in the calculation of the YTM is the assumption that each coupon payment as it becomes due is re-invested at the same rate rm. This is unlikely, due to the fluctuations in interest rates over time and as the bond approaches maturity. In practice, the measure itself will not equal the actual return from holding the bond, even if it is held to maturity. That said, the market standard is to quote bond returns as yields to maturity, bearing the key assumptions behind the calculation in mind. We can  demonstrate  the  inaccuracy  of  the  assumptions  by  multiplying  both sides of (A.14), the price/yield formula for a semi-annual coupon bond, by

2 N

1 1 2 rm , which gives us (A.21):

<!-- formula-not-decoded -->

The left-hand side of (A.21) gives the value of the investment in the bond on the maturity date, with compounding at the redemption yield. The righthand side gives the terminal value of the returns from holding the bond. The first coupon payment is reinvested for (2 1 N ) half-years at the yield to maturity, the second coupon payment is reinvested for (2 2 N ) half-years at the yield to maturity, and so on. This is valid only if the rate of interest is constant for all future time periods, that is, if we had the same interest rate for all loans or deposits, irrespective of the loan maturity. This would only apply under a flat yield curve environment. However, a flat yield curve implies that the yields to maturity of all bonds are identical, and this is very rarely encountered in practice. So we can discount the existence of flat yield curves in most cases.

Another disadvantage of the yield to maturity measure of return is where investors do not hold bonds to maturity. The redemption yield will not be of great use where the bond is not being held to redemption. Investors might

then be interested in other measures of return, which we can look at later.

To reiterate then, the redemption yield measure assumes that:

- ◾ the bond is held to maturity;
- ◾ all coupons during the bond's life are reinvested at the same (redemption yield) rate.

Therefore the YTM can be viewed as an expected or anticipated yield and is closest to reality perhaps where an investor buys a bond when it is first issued and holds it to maturity. Even then the actual realised yield on maturity would be different from the YTM figure because of the inapplicability of the second condition above.

In  addition,  as  coupons  are  discounted  at  the  yield  specific  for  each bond,  it  actually  becomes  inaccurate  to  compare  bonds  using  this  yield measure. For instance, the coupon cash flows that occur in two years' time from both a two-year and five-year bond will be discounted at different rates (assuming we do not have a flat yield curve). This occurs because the YTM for a five-year bond is invariably different to the YTM for a two-year bond. However, it would clearly not be correct to discount the two-year cash flows at different rates, because we can see that the present value calculated today of a cash flow in two years' time will be the same whether it is sourced from a short- or long-dated bond. Even if the first condition noted above for the YTM calculation is satisfied, it is clearly unlikely for any but the shortest maturity bond, that all coupons will be reinvested at the same rate. Market interest rates are in a state of constant flux and hence this  would  affect  money  reinvestment  rates. Therefore,  although  yield  to maturity is the main market measure of bond levels, it is not a true interest rate. This is an important result and we shall explore the concept of a true interest rate later in the book.

## Bonds with Embedded Options

Up to now we have discussed essentially plain vanilla coupon bonds. Bonds with certain special characteristics require slightly different yield analysis and we will introduce some of the key considerations here. A common type of non-vanilla bond is one described as featuring an embedded option . This refers to a bond that can be redeemed ahead of its specified maturity date. A bond that carries uncertainty as to its redemption date introduces an extra element to its yield analysis. This is because certain aspects of its cash flows, such as the timing or present value of individual payments, are not known with  certainty.  Contrast  this  with  conventional  bonds  that  have  clearly defined cash flow patterns. It is the certainty of the cash flows associated with vanilla bonds that enables us to carry out the yield to maturity analysis we have discussed so far. When cash flows are not known with certainty we need to adjust our yield analysis. In this section, we discuss the yield calculations for bonds with embedded options built into their features. The main types of such bonds are callable bonds, putable bonds and bonds with a sinking fund attached to them.

A callable bond is a bond containing a provision that allows the borrower to redeem all or part of the issue before the stated maturity date, which  is  referred  to  as calling the  bond.  The  issuer  therefore  has  a call option on the bond. The price at which the issuer calls the bond is known as the call price , and this might be a fixed price from a specific point in time or a series of prices over time, known as a call schedule . The bond might be callable over a continuous period of time or at certain specified dates, which is referred to as being continuously or discretely callable. In many cases, an issue will not be callable until a set number of years has passed, in which case the bond is said to have a deferred call .

A bond that allows the bondholder to sell back the bond, or put the bond, to the issuer at par on specified dates during its life is known as a putable bond. Therefore a bond with a put provision allows investors to change the term to maturity of the bond. The issue terms of a putable bond specify periods during which or dates on which the bond can be put back to the issuer. The put price is usually par but sometimes there is a schedule of prices at which the bond may be put.

Some bonds are issued with a sinking fund attached to them. A sinking fund is a deposit of funds kept in a separate custody account that is used to redeem the nominal outstanding on a bond in accordance with a predetermined schedule, regardless of changes in the price of the bond in the secondary market. It is common for sinking fund requirements to be satisfied through the redemption of a specified amount of the issue at certain points during the bond's life. In other cases the sinking fund requirement is met through purchases of amounts of the issue in the open market. Whatever the specific terms are for the sinking fund provision, all or part of the bond are redeemed ahead of the maturity date. This makes yield analysis more complex.

The usual way to look at callable and putable bond yields is by using binomial models and option-adjusted spread analysis. The key issues associated with all bonds with embedded options are the same, and in this section we introduce the basic concepts associated with callable and putable bonds.

## Yield Analysis for Callable Bonds

An issuer of a callable bond retains the right to buy, or call, the issue from bondholders before the specified redemption date. The details of the call structure  are  set  out  in  the  bond's  issue prospectus .  The  issuer  generally calls a bond when falling interest rates or an improvement in their borrowing status makes it worthwhile to cancel existing loans and replace them at a lower rate of interest. Since a callable bond can be redeemed early at a point when investors would probably prefer to hold onto it, the call provision acts as a 'cap' on the value of the bond, so that the price does not rise above a certain point (more relevantly, its yield does not fall below a certain point at which the bond would be called). A callable bond has more than one possible maturity date, comprised of the call dates (or any date during a continuous call period) and the final maturity date. Therefore, the cash flows associated with the issue are not explicit. The uncertainty of the cash flows arises from this fact, and yield calculations for such bonds are based on assumed maturity dates.

As a callable bond can be called at the option of the issuer, it is likely to be called when the market rate of interest is lower than the coupon on the bond. When this occurs, the bond will be trading above the call price (usually par). However, consider a bond that is issued with 15 years to maturity on 3 August 1999 and is callable after 5 years, so that on issue the bond had a 5-year deferred call. The bond has the following call schedule:

| Call date             |   Call price |
|-----------------------|--------------|
| 3 August 2004         |       102.00 |
| 3 August 2005         |       101.50 |
| 3 August 2006         |       101.00 |
| 3 August 2007         |       100.50 |
| 3 August 2008 onwards |       100.00 |

The first par call date for the bond is 3 August 2008 and it is callable at par from that date until maturity in August 2014. The yield to first call is the yield to maturity assuming that the bond is redeemed on the first call date. It can be calculated using equation (A.4) and setting M 102 00 . . Similarly the yield to next call is the yield to maturity assuming the bond is called on the next available call date. The operative life of a callable bond is the bond's expected life. This depends on both the current price of the bond and the call schedule. If the bond is currently trading below par, its operative life is likely to be the number of years to maturity, as this means that the market interest rate is above the coupon rate and there is therefore no advantage to the issuer in calling the bond. If the current price is above par, the operative life of the bond depends on the date on which the call price falls below the current price. For example, if the current price for the bond is 100.65, the bond is not likely to be called until a year before the par call date. Similarly, the operative yield is either the yield to maturity or the yield to relevant call, depending on whether the bond is trading above or below par.

In general then, for a callable bond, a bondholder will calculate YTM based on an assumed call date. This yield-to-call is  the discount rate that equates the NPV of the bonds cash flows (up to the assumed call date) to the current dirty price of the bond. For an annual coupon bond the general expression for yield-to-call, assuming settlement on a coupon date, is given by the expression at (A.22):

<!-- formula-not-decoded -->

where:

r ca is the yield-to-call;

Nc is the number of years to the assumed call date;

P c is the call price at the assumed call date (par, or as given in call schedule).

For a semi-annual coupon bond (A.22) is adjusted to allow for semiannual discounting and semi-annual coupon payments, in the normal manner for vanilla bonds.

Expression (A.22) is usually written as (A.23):

<!-- formula-not-decoded -->

## Yield Analysis for Putable Bonds

A putable bond grants the bondholder the right to sell the bond back to the issuer, usually in accordance with specified terms and conditions. For a putable bond, we calculate a yield-to-put, assuming a selected put date for the bond. The yield-to-put is calculated in a similar manner to the yieldto-call. The difference is that a bond with a put feature is redeemable at the option of the investor, and the investor will exercise the put only if this maximises the value of the bond. Therefore a bond with a put option always trades on the basis of the yield to maturity or the yield-to-put, whichever is greater.

The price/yield formula we use to calculate yield-to-put is identical to the formula used for yield-to-call, exchanging assumed call date and call price for assumed put date and put price. The general expression for a bond paying annual coupons and valued for settlement on a coupon date is given at (A.24):

<!-- formula-not-decoded -->

where:

r p is the yield-to-put;

N is the number of years to the assumed put date;

P p is the put price on the assumed put date.

## Bonds with Call and Put Features

The US domestic market includes bonds that are both callable and putable under certain conditions. For these bonds, it is possible to calculate both a yield-to-call and a yield-to-put for selected future dates, under the usual assumptions. In these circumstances the practice is to calculate the yield to maturity for the bond to the redemption date that gives the lowest possible yield for the bond. Bloomberg™ analytics uses the expression yield-to-worst in relation to calculating such a yield. The term is commonly encountered for bonds with embedded options. It is used to describe the yield to the first callable date for a bond trading above par and callable at par and where the bond is trading below par the yield-to-worst is the yield to maturity. A bond that is callable at par and trading above par will be called by the issuer, as the price indicates that the issuer can borrow money at a cheaper rate. Therefore the appropriate date to use when calculating the redemption yield is the first call date, hence the term yield-to-worst. For a bond that was both callable and putable, yield-to-worst is the yield to the redemption date that gives the lowest yield, irrespective of whether this is a call or put date (or indeed if it was both callable and putable on that date).

## Yield to Average Life

As we noted at the start of this section, some corporate bonds have a sinking fund or purchase fund attached to them. Where bonds are issued under these provisions, a certain amount of the issue is redeemed before maturity, ranging from a set percentage to the entire issue. The partial or full redemption process is carried out randomly on the basis of selecting bond serial numbers, or sometimes through direct purchase of some of the issue in the secondary market. Bonds are issued with a redemption schedule that specifies the dates, the proportions and (in the case where the process takes place randomly) the values of the redemption payments.

Investors holding and trading bonds that are issued with these provisions sometimes use a different yield measure to the conventional YTM one. A common measure of return is the yield-to-average life . The average life of a bond is defined as the weighted average time to redemption using relative redemption cash flows as the weights. The expression for calculating average life is given by equation (A.25):

<!-- formula-not-decoded -->

where:

At is the proportion of bonds outstanding redeemed in year t ;

Mt is the redemption price of bonds redeemed in year t ;

N is the number of years to maturity.

The yield-to-average life calculation makes use of the bond's average redemption price, which can be determined from the redemption schedule. The average redemption price is calculated using (A.26):

<!-- formula-not-decoded -->

where P ave is the average redemption price.

## Index-Linked Bonds

Index-linked bonds are bonds where the return is linked to the movement of an external reference index such as retail prices or a consumer price index. The return is in the form of linked coupon, principal or both. The yield calculation for such bonds is slightly more involved and is discussed in the following section.

In certain markets including the UK market, the government and certain corporate entities issue bonds that have either or both of their coupon and principal linked to a price index, such as the retail price index (RPI), a commodity price index (for example, wheat) or a stock market index. 5  In the UK, we refer to the RPI whereas in other markets the price index is the consumer price  index  (CPI ) . 6 If  we  wish  to  calculate  the  yield  on  such index-linked bonds it is necessary to make forecasts of the relevant index, which are then used in the yield calculation. As an example, let us use the case of indexlinked government bonds, which were first introduced in the UK in March 1981. Both the principal and coupons on UK index-linked government bonds are linked to the RPI and are therefore designed to give a constant real yield. When index-linked gilts were first introduced, the Bank of England allowed only pension funds to buy them, under the reasoning that these funds had index-linked pensions to deliver to their clients. However, a wide range of investors are potential investors in bonds which have cash flows linked to prices, so that shortly after their introduction, all investors were permitted to hold index-linked gilts. Most of the index-linked stocks that have been issued by the UK government have coupons of 2 or 2.5%. This is because the return from an index-linked bond represents in theory real return,  as  the  bond's cash flows rise in line with inflation. Historically, the real rate of return on UK market debt stock over the long-term has been roughly 2.5%.

5   'Principal' is the usual term for the maturity or redemption payment of a bond.

6   In  the  June  2003  announcement  of  the  government's 'five  tests'  evaluated  as part of an evaluation for Britain joining the European Union's euro currency, the Chancellor  (Gordon  Brown)  stated  that  the  UK's  measure  of  inflation  would  be

Indexed-bonds differ  in  their  characteristics  across  markets.  In  some markets, only the principal payment is linked, whereas other indexed bonds link only their coupon payments and not the redemption payment. Indexed gilts 7  in the UK market link both their coupons and principal payment to the RPI. Therefore each coupon and the final principal on index-linked gilts are scaled up by the ratio of two values of the RPI. The main RPI measure is the one reported for eight months before the issue of the gilt, and is known as the base RPI. The base RPI is the denominator of the index measure. The numerator is the RPI measure for eight months prior to the month coupon payment, or eight months before the bond maturity date.

The coupon payment of an index-linked gilt is given by (A.27) below:

<!-- formula-not-decoded -->

Expression  (A.27)  shows  the  coupon  divided  by  two  before  being scaled up, because index-linked gilts pay semi-annual coupons. The formula for calculating the size of the coupon payment for an annual-paying indexed bond is modified accordingly. The principal repayment is given by (A.28):

<!-- formula-not-decoded -->

where:

C is the annual coupon payment;

RPI 0 is the RPI value eight months prior to the issue of the bond (the base RPI);

RPI C -8 is the RPI value eight months prior to the month in which the coupon is paid;

RPI M -8 is the RPI value eight months prior to the bond redemption.

changed from the RPI-X measure to a Consumer Prices Index. The latter is used in other EU countries, and as the Bank of England's target inflation rate would be moved over to the new CPI measure, and so now UK index-linked gilts would pay

a CPI-linked return.

7 Called 'linkers'  in  the  gilt  market.  Like  conventional  gilts,  these  pay  a  semiannual coupon.

Note how in the UK gilt market, the indexation calculation given by (A.27) and (A.28) uses the RPI values for eight months prior to the date of each cash flow. For bonds issued after 2005, the time lag is three months.

To solve for the real yield one uses (A.29) as applicable to semi-annual coupon bonds:

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

RPI 0 is the base index level as initially described. RPI a / RPI 0 is the rate of inflation between the bond's issue date and the date the yield calculation is carried out.

## Assessing Yield for Index-Linked Bonds

Index-linked bonds do not offer complete protection against a fall in real value of an investment. That is, the return from index-linked bonds, including index-linked gilts, is not in reality a guaranteed real return, in spite of the cash flows being linked to a price index such as the RPI. The reason for this is the lag in indexation, which for index-linked gilts is eight months. The time lag means that an indexed bond is not protected against inflation for the last interest period of its life, which for gilts is the last six months. Any inflation occurring during this final interest period will not be reflected in the bond's cash flows and will reduce the real value of the redemption payment and hence the real yield. This can be a concern for investors in high inflation environments. The only way effectively for bondholders to eliminate inflation risk is to reduce the time lag in indexation of payments to something like one or two months.

Bond analysts frequently compare the yields on index-linked bonds with those  on  conventional  bonds,  as  this  implies  the  market's  expectation  of inflation rates. In order to compare returns between index-linked bonds and conventional bonds, analysts calculate the break-even inflation rate. This is the inflation rate that makes the money yield on an index-linked bond equal to the redemption yield on a conventional bond of the same maturity. Roughly speaking, the difference between the yield on an indexed bond and a conventional bond of the same maturity is what the market expects inflation during the life of the bond to be - part of the higher yield available on the conventional bond is therefore the inflation premium. In August 1999, the redemption yield on the 5.75% Treasury 2009, the 10-year benchmark gilt, was 5.17%. The real yield on the 2.5% index-linked 2009 gilt, assuming a constant inflation rate of 3%, was 2.23%. Using (A.29) this gives us an implied break-even inflation rate of:

<!-- formula-not-decoded -->

If we accept that an advanced, highly developed and liquid market such as the gilt market is of at least semi-strong form, if not strong form, then the inflation expectation in the market is built into these gilt yields. However, if this implied inflation rate understated what is expected by certain market participants, investors will start holding more of the index-linked bond rather than the conventional bond. This activity will then force the indexed yield down (or the conventional yield up). If investors had the opposite view and thought that the implied inflation rate overstated inflation expectations, they would hold the conventional bond. In our illustration above, the market is expecting long-term inflation to be at around 2.9% or less, and the higher yield of the 5.75% 2009 bond reflects this inflation expectation. A fund manager will take into account their view of inflation, amongst other factors, in deciding how much of the index-linked gilt to hold compared to the conventional gilt. It is often the case that investment managers hold indexed bonds in a portfolio against specific index-linked liabilities, such as pension contracts, that increase their payouts in line with inflation each year.

The premium on the yield of the conventional bond over that of the index-linked bond is therefore compensation against inflation to investors holding it. Bondholders will choose to hold index-linked bonds instead of conventional bonds if they are worried by unexpected inflation. An individual's view on expected inflation will depend on several factors, including the current macro-economic environment and the credibility of the monetary authorities, be they the central bank or the government. In certain countries such as the UK and New Zealand, the central bank has explicit inflation targets and investors may feel that over the long term these targets will be met. If the track record of the monetary authorities is proven, investors may feel further that inflation is no longer a significant issue. In these situations the case for holding index-linked bonds is weakened.

The real yield level on indexed bonds in other markets is also a factor. As capital markets around the world have become closely integrated in the last 20 years, global capital mobility means that high-inflation markets are shunned by investors. Therefore, over time expected returns, certainly in developed and liquid markets, should be roughly equal, so that real yields are at similar levels around the world. If we accept this premise, we would then expect the real yield on index-linked bonds to be at approximately similar levels, whatever market they are traded in. For example, we would expect indexed bonds in the UK to be at a level near to that in say, the US market. In fact in May 1999, long-dated index-linked gilts traded at just over 2% real yield, while long-dated indexed bonds in the US were at the higher real yield level of 3.8%. This was viewed by analysts as a reflection of the fact that international capital was not as mobile as had previously been thought, and that productivity gains and technological progress in the US economy had boosted demand for capital there to such an extent that real yields had had to increase. However, there is no doubt that there is considerable information contained in index-linked bonds and analysts are always interested in the yield levels of these bonds compared to conventional bonds.

## Floating Rate Notes (FRNs)

Securities known as floating rate notes (FRNs) are bonds that do not pay a fixed coupon but instead pay coupon that changes in line with another specified reference interest rate. The FRN market in countries such as the US and UK is large and well-developed and floating-rate bonds are particularly popular with short-term investors and financial institutions such as banks. With the exception of its coupon arrangement, an FRN is similar to a conventional bond. Maturity lengths for FRNs range from two years to over thirty years. The coupon on a floating-rate bond 'floats' in line with market interest rates. According to the payment frequency, which is usually quarterly or semi-annually, the coupon is re-fixed in line with a money market index such as the London Inter-bank Offer Rate or LIBOR. Often an FRN will pay a spread over LIBOR, and this spread is fixed through the life of the bond. For example, a sterling FRN issued by the Nationwide Building Society in the UK matured in August 2001 and paid semi-annual coupons at a rate of LIBOR plus 5.7 basis points. 8  This means that every six months the coupon was set in line with the six-month LIBOR rate, plus the fixed spread. The rate with which the FRN coupon is set is known as the reference rate . This will be three-month or six-month LIBOR or another interest rate index. In the US market, FRNs frequently set their coupons in line with the Treasury bill rate. The spread over the reference note is called the index spread. The index spread is the number of basis points over the reference rate. In a few cases, the index spread is negative, so it is subtracted from the reference rate.

## Yield Measurement

As the coupon on an FRN is re-set every time it is paid, the bond's cash flows cannot be determined with certainty in advance. It is not possible therefore to calculate a conventional yield to maturity measure for an FRN. Instead the markets use a measure called the discounted margin to estimate the return received from holding a floating-rate bond. The discounted margin measures the average spread (margin) over the reference rate that is received during the life of the bond, assuming that the reference rate stays at a constant level throughout. The assumption of a stable reference rate is key to enabling the calculation to be made, and although it is slightly unrealistic, it does enable comparisons to be made between yields on different bonds. In addition, the discount margin method also suffers from the same shortcoming as the conventional redemption yield calculation, namely the assumption of a stable discount rate.

To calculate the discounted margin, select a reference rate and assume that this remains unchanged up to the bond's maturity date. The common practice is to set the rate at its current level. The bond's margin or index spread is then added to this reference rate (or subtracted if the spread is negative). With a 'fixed' rate in place, it is possible to determine the FRN's cash flows, which are then discounted at the fixed rate selected. The correct discount rate is the one that equates the present values of the discounted cash flows to the bond's price. Since the reference rate is fixed, we need to alter the margin element in order to obtain the correct result. When we have equated the NPV to the price at a selected discount rate, we know what the discounted margin for the bond is.

Due to the way that each coupon is reset every quarter or every six months, FRNs trade very close to par (100%) and on the coupon reset date the price is always par. When a floating-rate bond is priced at par, the discounted margin is identical to the fixed spread over the reference rate. Note that some FRNs feature a spread over the reference rate that is itself floating, and such bonds are known as variable rate notes .

8   A basis point is one-hundredth of 1%, that is l bp = 0.01%.

## EXAMPLE A.2

Consider  a  floating-rate  note  trading  at  a  price  of  £99.95  per  100 notional. The bond pays semi-annual coupons at six-month LIBOR plus 10 basis points and has exactly three years to maturity (so that the discount margin calculation is carried out for value on a coupon date). Table A.1 shows the present value calculations, from which we can see that at the price of 99.95 this represents a discounted margin of 12 basis points on an annualised basis.

Three-year  FRN,  Price:  99.95,  six-month  LIBOR  +  10  basis points, LIBOR 5.5%.

In our calculation, the six-month LIBOR rate is 5.50%, so we assume that this rate stays constant for the life of the bond. As this is an annual rate, the semi-annual equivalent for our purposes is 2.75%. There are two coupon payments per year, so that there  are  six  interest  periods  and  six remaining cash flows until maturity. As we have assumed a constant reference rate, we can set the bond coupons and redemption payment, shown as 'cash flow' in the table. Each coupon payment is half of the annual reference rate plus half the annual spread. This works out as 2.75% plus 5 basis points, which is a semi-annual coupon of £2.80. The last cash flow is the final coupon of £2.80 plus the redemption payment of £100.00. We then discount all the cash flows at the selected margin levels until we find a level that results in a net present value to equal the current bond price. From the table we see that the price equates to a discounted margin of six basis points on a semi-annual basis, or 12 basis points annually.

## Measuring Yield for a Bond Portfolio

An investor holding a portfolio of two or more bonds will often be interested in measuring the return from the portfolio as a whole, rather than simply the return from individual bonds. This is often the case when, for example, a portfolio is tasked with tracking or out-performing a particular bond index, or has a target return to aim for. It then becomes too important to measure portfolio return and not bond return. The markets adopt two main methods of measuring portfolio return, the weighted average yield, and the IRR or total rate of return. The internal rate of return method has more basis in logic; however, it is common to encounter the weighted average method, used as a 'quick-and-dirty' yield measure.

## Weighted average portfolio yield

When determining the yield for a portfolio of bonds, investors commonly calculate the weighted average portfolio, using the redemption yields of individual constituent bonds in the portfolio. This is not an accurate measure, however, and it should be avoided for all portfolios that do not hold roughly equal amounts of each bond, each of which is roughly similar maturity.

To calculate the weighted average yield, set the following, where:

MVp is the market value of bond p as a proportion of total portfolio market value;

r p is the yield to maturity for bond p ;

n is the number of securities in the portfolio.

The weighted average yield for the portfolio is then given by (A.30):

<!-- formula-not-decoded -->

where r port is the weighted average portfolio yield.

## Portfolio Internal Rate of Return

In the previous section, we discussed the weighted average rate of return for a bond portfolio, and while this may appear intuitively to be the best way to measure yield for a portfolio, the arithmetically more accurate method is to apply the NPV procedure used for individual bonds to the entire portfolio. This is essentially measuring the yield to maturity for the portfolio as a whole, and is also known as the portfolio internal rate of return.

We encountered internal rate of return (IRR) earlier. The IRR of a bond, if we assume a constant reinvestment rate up to the maturity of the bond, is the bond's yield to maturity. We can calculate the IRR for a portfolio in the same manner, by applying the procedure to the portfolio's cash flows. The IRR, or yield, is calculated by ascertaining the cash flows resulting from the portfolio as a whole and then determining the internal rate of return for these cash flows in the normal manner. For a portfolio holding say, five bonds, whose coupons all fall on the same day, the IRR will be the rate that equates the present value of the total cash flows with the current market value of the portfolio. The portfolio market value is simply the sum of the market values of all five bonds.

## Total Rate of Return

We have seen that in calculating a bond's redemption yield, we are required to make certain assumptions and where these assumptions are not met, the yield measure will be inaccurate. The assumption that coupon payments are reinvested at the same rate as the redemption yield is not realistic. Interest earned on coupon interest may be responsible for a significant proportion of a bond's total return and reinvestment at a lower rate than the yield will result in a total return being lower than the redemption yield. If an investor wishes to calculate a total rate of return from holding a bond, it is still necessary to make an assumption, an explicit one about the reinvestment rate that will be realised during the life of the bond. For instance, in a steep yield curve or high-yield environment, the investor may wish to assume a higher rate of reinvestment and apply this to the yield calculation. The reinvestment rate assumed will need to be based on the investor's personal view of future market conditions. The total rate of return is the yield measure that incorporates this assumption of a different reinvestment rate.

When computing total return, a portfolio manager must first calculate the total cash value that will accrue from investing in a bond assuming an explicit reinvestment rate. The total return is then calculated as the interest culated total cash value. The procedure for calculating the total return for a bond held over a specified investment horizon, and paying semi-annual

rate that will make the initial investment in the bond increase to the calcoupons is summarised below.

First, we calculate the value of all coupon payments plus the interest-oninterest, based on the assumed interest rate. If we denote this as I , then this can be done using equation (A.31):

<!-- formula-not-decoded -->

where r is the semi-annual reinvestment rate and N is the number of interest  periods  to  maturity  (for  a  semi-annual coupon bond it will be twice the  number of years to maturity). The investor then needs to determine the projected sale price at the end of the planned investment horizon. The projected sale price will be a function of the anticipated required yield at the end of the investment horizon, and will equal the present value of the remaining cash flows of the bond, discounted at the anticipated required yield. The sum of these two values, the total interest income and projected sale price, is the total cash value that will be received from investing in the bond, using our assumed reinvestment rate and the projected required yield at  the  end  of  the  investment  horizon. To  calculate  the  semi-annual total return we use (A.32):

<!-- formula-not-decoded -->

where n is the number of six-month periods in the investment horizon. This formula is derived from (A.11), which was our formula for obtaining the yield for a zero-coupon bond. This semi-annual total return is doubled to obtain the total return. The equations are modified in the normal way for bonds that pay annual coupons.

## The Price/Yield Relationship

The  last  two  sections  have  illustrated  a  fundamental  property  of  bonds, namely that an upward change in the price results in a downward move in the yield, and vice-versa. This is immediately apparent since the price is the present value of the cash flows. For example, as the required yield for a bond decreases, the present value, and hence the price of the cash flow for the bond will increase. It also reflects the fact that for plain vanilla bonds the coupon is fixed, therefore it is the price of the bond that fluctuates to reflect changes in market yields. It is useful to plot the relationship between the  yield  and  price  of  a  bond. A  typical  price/yield  profile  is  represented graphically in Figure A.2, which shows a convex curve. To reiterate, for a plain vanilla bond with a fixed coupon, the price is the only variable that can change to reflect changes in the market environment. When the coupon rate of a bond is equal to the market rate, the bond price will be par (100). If  the  required  interest  rate  in  the  market  moves  above  a  bond's  coupon rate at any point in time, the price of the bond will adjust downward in order for the bondholder to realise the additional return required. Similarly, if the required yield moves below the coupon rate, the price will move up to equate the yield on the bond to the market rate. As a bond will redeem at par, the capital appreciation realised on maturity acts as compensation when the coupon rate is lower than the market yield.

FIGURE A.2 The bond price/yield relationship.

<!-- image -->

The price of a bond will change for a variety of reasons, including the market-related ones noted here:

- ◾ a change in the yield required by the market, either because of changes in  the  base  rate  or  a  perceived  change  in  credit  quality  of  the  bond issuer  (credit  considerations  do  not  affect  developed  country government bonds);
- ◾ as  the  bond  is  approaching  maturity,  its  price  moves  gradually towards par;
- ◾ a change in the market-required yield due to a change in the yield on comparable bonds.

Bond prices also move for liquidity reasons and normal supply-and-demand reasons, for example, if there is a large amount of a particular bond on issue it is easier to trade the bond. Also, if there is demand due to a large customer base for the bond. Liquidity is a general term used here to mean the ease with which a market participant can trade in or out of a position. If there is always a ready buyer or seller for a particular bond, it will be easier to trade in the market.

## SUMMARY

We have discussed the market conventions for calculating bond yields. The key issues are the price/yield relationship that all bonds exhibit and the assumptions behind the various yield calculations. The different conventions used across various markets, although not impacting the economic fundamentals of any particular instrument, make it important to convert yields to the same calculation basis, to ensure that we are comparing like-for-like. In some markets such as the UK gilt strips market, bonds trade on a yield rather than price basis. We suggested earlier that it is the yield that is the primary information required by investors. When analysing bonds across markets, the pricing and yield conventions are not important as such, but serve to remind us of what is important - that we conduct analysis under the same terms for

all financial instruments.

The other main topics we have considered are:

- ◾ simple interest and compound interest: certain markets including the US Treasury and the German government bond market calculate the yield for a bond with only one remaining coupon using simple rather than compound interest;
- ◾ compounding method: the  most  common  market  convention  discounts  cash flows using compounding in whole years. This results in a discount factor as given by (A.33):

<!-- formula-not-decoded -->

It  is  also  common  to  encounter  the  more  accurate  measurement  for compounding as given by (A.34):

<!-- formula-not-decoded -->

- ◾ annualised yields: the yield quoted for a bond generally follows the coupon payment frequency for that bond, so that annual coupon bonds quote an annualised yield, semi-annual bonds a semi-annual yield, and so on. When comparing bonds of different coupon conventions it is important to convert one so that we are comparing like-for-like.

The redemption yield or yield to maturity for a bond is the bond's IRR, assuming that re-investment rates for subsequent cash flows are identical to the yield itself. This is an important feature of the redemption yield measurement. We have also discussed a variation on the basic calculation, whereby a selected fixed reinvestment rate is assumed and then used to determine future cash flows from a bond. In the main body of the book we discuss zero-coupon or spot yields, and the concept of a true interest rate. This then sets us up for our detailed look at the yield curve.

## Index

| 30 Year bonds 8 A ALM see Asset-liability management Analysis callable bonds 336-339 compounding 222-224 continuous time 66-89 expectations hypothesis 32-38 forward yield curve 30-32 liquidity preference theory 38-40 negative interest rates 219-227 post-2008 193-210 putable bonds 338-339 relative value 9, 283-288 segmentation hypothesis 40-42 spot rates 23-24, 52-53 yield measurement 321-352 see also Pricing Ancillary yield curves 291-319 Anderson-Sleath model 266-271 Arbitrage 68-70, 73-75 Arbitrage-free models 96, 150-157, 172 Black-Derman-Toy model 140, 156-157 fitting 157-158 Ho-Lee model 151-153, 158 Hull-White model 100, 147, 153-156, 158 multi-factor HJM model 166-169 Arithmetic average 81 Assessment of models 170-171 Asset-liability management (ALM) 40, 219-227 Asset price dynamics 115-136 bond price equation 129-130   | Brownian motion 117-120, 126-127 generalised Wiener process 122-124, 148-149 Ho-Lee model 151-153, 158 interest rate uncertainty 130-131 Itô's lemma 100-101, 127-128, 132-134 Martingale property 120-122 modelling 124-135 Poisson processes 117-118 stochastic processes 116-124, 126-134 Wiener processes 117-120, 127-128 Assumed inflation rates 187-188 Average return 27, 76 B Bank of England 45, 268-271 Banking, COF curves 207-217 Barbell trades 288-289, 301-306 Base RPI 187, 341 Basis point value (BPV) 286-287 BDT model see Black-Derman- Toy model Benchmarks 10, 197-198, 306-309, 313-316 'Best fit' 15 BEY see Bond equivalent yield BGM model see Brace-Gatarek- Musiela model Black-Derman-Toy (BDT) model 140, 156-157 Black-Scholes model 131 Bloomberg system 11-15 Bond equivalent yield (BEY) 298-301 Bond price equations 129-130, 188-189, 255-256   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Bonds callable 335-339 carry 323 clean price 293 convertible 226 converting yields 331-347 corporate 23-24 coupon 65-66, 325, 328, 331-335 coupon process 67 current yield 322-323 dirty price 66, 72, 293 embedded options 335-340 equivalent yield 298-301 floating rate notes 344-346 forward rates 53-54, 72-77, 83-86 government 5-6, 9, 11-13, 46, 55-56, 225, 279-288 index-linked 181-190, 340-344 market information 255-257 modifying yields 330-331 money market yields 330-331 mortgage-backed 189 plain vanilla 350 portfolio yields 348-350 price/yield relationship 350-351 putable 336, 338-339 sinking funds 336 spot rates 23-24, 52-53 spot vs. forward rates 80-85 spread 23-24 spread trades 288-289, 301-306 yield to average life 339-340 yield to maturity 10-15 yield measurement 321-352 zero-coupon 10, 62-65,   | Brownian motion 98-99, 108, 109-110, 117-120, 126-127 B-splines 51, 240-241 Butterfly trades 288-289, 301-306 C Calculation current yield 322-323 redemption yield 326-329 spot rates 77-79 yield to maturity 324-329 yield measurement 321-352 Calibration 96-97, 157-158, 175, see also Fitting Callable bonds 335-339 Capital gains tax 15 Cash market 24-25 CCPs see Centralised clearing counterparties Centralised clearing counterparties (CCPs) 58 Cheapest-to-deliver (CTD) discounting 195, 203 Choice of models 172-174 Clean price 293 COF see Cost of funds Collateralised discount curves 205-207 Collateralised swaps 193-210 Collateral remuneration rates 194-195 Composite variables 247 Compounding 222-224 Consistency 176 Consortium yield 326 Constraints, splines 248-249   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| short rate 67-70 spot rates 77-79 spot vs. forward rates 80-83 stochastic rates 70-71 Continuous variables 98, 105-106 Conventional yield curve 30 Convergence 45 Convertible bonds 226 Corporate bonds 11, 13-14, 23-24 Cost of funds (COF) curves 207-217 Coupon bonds 65-66, 69-70, 71-72, 325, 328, 331-335 Coupon frequency 331-333 Coupon process 67 Coupon yield curve 15-16, 26 Cox-Ingersoll-Ross (CIR) model 140, 149 CPI see Consumer price index Credit Support Annexe (CSA) agreements 194-217 collateral funding 204-210 optionalities 204-205 Credit valuation adjustment (CVA) 195 Cross-currency (XCCY) curves 195, 203, 206-207, 211-217 CSA see Credit Support Annexe agreements CTD discounting see Cheapest-to- deliver discounting Cubic polynomials 236-238 Cubic splines 50-51, 56-58, 184-186, 239-241, 246-249, 262-266, 272-273 Current yield 66, 322-323 Curvature trades 288-289, 301-306   | fitting 46-52, 231-275 flat 43-44 forward yield 24-46, 75-76 government bonds 5-6, 11-13, 55-56 government policy 44-46 humped 30, 39, 241-242 indexed-linked 181-190 interest-rate swap 11, 14, 55-56 multi-currency 195, 203, 206-207, 211-217 negative 25, 30, 39, 44-45 negative interest rates 219-227 Nelson and Siegel 241-242, 259-262 oscillation 208-209, 233-235, par 16, 186, 328-329 polynomial models 49-50, 236-238, 246-249, 295-296, 309-313 positive 8, 25, 30, 38, 43, 44 regression models 51-52 spot 267-271 yield to maturity 10 zero-coupon 17-23, 26-27, 75-76 see also Interpolation; Smoothing CVA see Credit valuation adjustment D Deferred call 336 Dependent variables 243 Derivation Itô's formula 133-134 of yield curve 7-8, 15-23, 187-188 Derivatives 193-217 collateral funding 204-210 cost of funds curves 207-217   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Discount functions 79, 256 cubic polynomials 236-238 index-linked bonds 184-185, 186-187 negative interest rates 219-224 Discrete variables 98 DK see Discount factor function Dollar value of a basis point 286-287 Downward-sloping curve 30 see also Negative yield curve Drift 100, 103-104, 116, 120, 127 Dummy variables 246, 249 Duration 186, 194 Dynamics asset prices 115-136   | Fitting 46-52, 231-275 cubic polynomials 236-238 cubic splines 50-51, 56-58, 239-241, 246-249, 262-266, 272-273 discount functions 186-187 interest rate models 157-158 interpolation 47-49 Nelson and Siegel curves 241-242, 259-262 non-parametric 238-241, 243-249 parametric 78-79, 235-238, 241-242, 258-273 polynomial models 49-50, 236-238, 246-249, 295-296, 309-313 regression models 51-52   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Funds transfer pricing (FTP) 203-204, 208-210                                                              | I IM see Initial margin                                                                      |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Futures 9                                                                                                  | Implied forward rates 184-185,                                                               |
| FVA see Funding valuation adjustment                                                                       | 187-188, 198-199, 254                                                                        |
| G                                                                                                          | Nelson and Siegel curves 241-242, 259-262                                                    |
| Gaussian models 103, 140-141, 143-147                                                                      | Implied one-year rates 18 Independent variables 243                                          |
| GCV see Generalised cross-validation                                                                       | Index                                                                                        |
| Generalised cross-validation (GCV) 265                                                                     | OIS curves 198 retail price 187, 340-342                                                     |
| Generalised Wiener process 122-124, 148-149                                                                | Index-linked yield curve 181-190 discount functions 184-185,                                 |
| Geometric average 81                                                                                       | 186-187                                                                                      |
| Geometric Brownian motion 98-99, 108, 109-110, 117-120                                                     | estimating term structure 185-186 implied forward rates 184-185                              |
| Geometric mean 25                                                                                          | real term structure 183-184,                                                                 |
| Geometric programming (GP) 295-296, 309-313                                                                | 187-188 real yields 182-183, 188, 340-344                                                    |
| Government bonds 5-6, 9, 11-13, 46, 55-56, 225, 279-288                                                    | Index spread 344-345 Inflation 9, 181-189                                                    |
| relative value 283-288 Government policy 44-46                                                             | Inflation premium 343 Initial margin (IM) 56                                                 |
|                                                                                                            | Inputs 175                                                                                   |
| GP see Geometric programming                                                                               | Instantaneous rate 67-70                                                                     |
| Grid points, regression 52                                                                                 | Integrals 86-87, 120, 135                                                                    |
| Gross redemption yield (GRY) 5                                                                             | Interest rate derivatives 9                                                                  |
| see also Yield to maturity                                                                                 | Interest rate modelling 95-178 Anderson-Sleath model                                         |
| Growth rates 117 H                                                                                         | 268-271 arbitrage-free models 96, 150-157                                                    |
| Heath-Jarrow-Morton (HJM) models 98, 163-171 jump 169 multi-factor 166-169 single factor 164 two-state 165 | asset price dynamics 115-136 basic concepts 95-112, 139-142 Black-Derman-Toy model 140,      |
|                                                                                                            | 156-157 bond price equation 129-130 calibration 96-97, 157-158, 175 choosing a model 172-174 |
| Hedge rates 53-54 see also Forward rates                                                                   | consistency 176 expectations hypothesis 32-38                                                |
| Hedging instruments 101 HJM see Heath-Jarrow-Morton                                                        | fitting 157-158 generalised Wiener process 122-124,                                          |
| Ho-Lee model 151-153, 158 Hull-White model 100, 147,                                                       | 148-149 Geometric Brownian motion 98-99,                                                     |
| 153-156, 158                                                                                               | 108, 109-110, 117-120                                                                        |
| Humped yield curve 30, 39, 42, 241-242                                                                     | Heath-Jarrow-Morton models                                                                   |
|                                                                                                            | 98, 163-171                                                                                  |

| Ho-Lee model 151-153, 158 Hull-White model 100, 147, 153-156, 158 inputs 175 integrals 120, 135 Itô's lemma 100-101, 127-128, 132-134 jump models 169 liquidity preference theory 38-40 Martingale property 120-122 Merton model 148-149 model assessment 170-171 multi-factor 103, 164-172 non-parametric 238-241, 243-249 one-factor 97, 102-103, 142-143 parametric 100, 140, 143-158, 169, 238, 241-242, 258-273   | ordinary least squares 78-79, 107, 243-246 real term structures 184-185 regression splines 246-249 Interpretation forward yield curve 30-32 see also Analysis Inverted yield curve 30, 44-45 see also Negative yield curve IRR see Internal rate of return Itô's lemma 100-101, 127-128, 132-134 IYC screen 11-13 J Jensen's inequality 32 Jump models 169   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| M McCulloch method 184-185, 257, 272-273 MAPE see Mean absolute percentage error Marginal return 27, 76 Market information 255-257 Markov processes 108, 126-127 Mark-to-market (MTM) 197 Martingale property 120-122 Mathematics primer 104-109 Mean absolute percentage error (MAPE) 297 Mean reversion 100, 117, 120 Measurement of inflation 183-184 Merton model 148-149 Microsoft Excel 7, 21 Modelling asset price dynamics 124-135 continuous time 66-89 cubic splines 50-51, 56-58 expectations hypothesis 32-38 fitting 48-52 integrals 86-87, 120, 135 interpolation 47-51, 56-58 liquidity preference theory 38-40 non-parametric 238-241, 243-249 parametric 238, 241-242 polynomial 49-50, 236-238, 246-249, 295-296, 309-313 regression 51-52 segmentation hypothesis 40-42 see also Fitting; Interest rate   | Multi-currency yield curves 195, 203, 206-207, 211-217 Multi-factor Heath-Jarrow-Morton model 166-169 Multi-factor models 103, 164-172 assessment 170-171 Heath-Jarrow Morton 166-169 jump 169 N Negative carry/funding 323 Negative interest rates 219-227 Negative yield curve 25, 30, 39, 44-45 Nelson and Siegel curves 241-242, 259-262 Net Present Value (NPV) 193, 194, 328-329 Newtonian terms 120 No-arbitrage pricing 96, 101 see also Arbitrage-free models Noise 98, 116 Nominal rate 183, 187-188 Non-parametric fitting 238-241, 243-249 Normal processes 140, 148-149 see also Gaussian models Normal yield curve 30 NPV see Net Present Value n -th order splines 239 O OIS curve see Overnight index swap curve OLS see Ordinary least squares One-factor models 97, 170-171   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| P Parameters, volatility 99, 103-104, 108-110, 120 Parametric fitting 238, 241-242 Partitions 131, 135 Par value 62 Par yield curve 16, 186, 328-329 Perfect market 44 Piecewise linear regression 246 Plain vanilla bonds 350 Poisson process 117-118 Polynomial models 49-50, 236-238, 246-249, 295-296, 309-313 Portfolios of bonds 346, 348-350 Positive sloping curve 8, 25, 30, 38, 43, 44 Post-2008 analytics 193-210 Pricing 52-54 arbitrage 68-70, 73-75 bond price equations 129-130, 188-189, 255-256 callable bonds 336-338 continuous time 66-89 coupon bonds 71-72, 325, 328, 331-335 derivation of equation 88-89 forward rates 72-77, 83-86 generalised Wiener process 122-124, 148-149 index-linked bonds 182-183, 189 integrals 86-87 Martingale property 120-122 Poisson processes 117-118 portfolios 348-350 putable bonds 338-339 short rate 67-70 spot vs. forward rates 83-85 stochastic processes 117-124 stochastic rates 70-71 swaps 194-196 yield to average life 339-340 yield relationship 350-351 zero-coupon bonds 69-71, 77-79 Primary market 16 Principal 62, 72   | Probability distributions 98-99, 103, 105 Purchase funds 336, 339-340 Pure expectations hypothesis 33-35, 36 Putable bonds 336, 338-339 Q Quanto options 174 Quasi-interest periods 329 R Random function see Stochastic processes Random variables 98-99, 105-106, 107-110, 117-124, 131-132 see also Brownian motion; Martingale property; Wiener processes Random walks 126-127 Rate of return 21, 27 internal 321-322, 324-326, 348 portfolios 348 total 348-350 Real implied forward rate 184-185, 187-188 Real yield curves 182-183, 188 see also Index-linked yield curve Recessions 45 Recovery-rate (RR) adjustment 211-214 Redemption yield 23-24, 326-329, 333-335 Reference rate 344-345 Regression 51-52, 78-79, 107 linear 78-79, 107, 235, 243-248 ordinary least squares 78-79, 107, 243-246 splines 50-51, 56-58, 78-79, 238-241, 246-249, 262-266 Regulatory effects 44-46 Reinvestment risk 10 Relative value 277-319 analysis 9, 20, 283-288 geometric programming 295-296   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| spreads 286-289 uncertainty quantification 296-297 US Treasury market 291-319 yield curves 279-289 271-272 rates 271-272 price index (RPI) 187,   | spline methods 50-51, 56-58, 184-186, 238-241, 246-249,         |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
|                                                                                                                                                   | 262-266                                                         |
|                                                                                                                                                   | Waggoner model 262-266                                          |
| Repo                                                                                                                                              | see also Fitting                                                |
| Repo                                                                                                                                              | SONIA see Sterling overnight index                              |
| Retail 340-342                                                                                                                                    | swap curve                                                      |
| Return to maturity expectations hypothesis 35, 36-37                                                                                              | Sovereign bond curve 55-56 see also Government bonds            |
| Riemann integral 86-87                                                                                                                            | Spline estimation 78-79                                         |
| Rising curve 30                                                                                                                                   | Spline function 247-248                                         |
| see also Positive sloping curve interest rate 9, 55,                                                                                              | Splines                                                         |
| 'Risk-free' 194-196                                                                                                                               | Anderson-Sleath model 268-271 B- 240-241                        |
| Risk-neutral measure 70                                                                                                                           | constraints 248-249                                             |
| Roughness penalties 262-266 RPI see Retail price index                                                                                            | cubic 50-51, 56-58, 239-241, 246-249, 262-266, 272-273          |
| RR see Recovery-rate                                                                                                                              | McCulloch model 257, 272-273                                    |
| Running yield 66, 322-323 S                                                                                                                       | methodology 246-249 Waggoner model 262-266 Spot market 24-25    |
| Sample regression function (SRF) 245                                                                                                              | Spot rates 17-23, 28-30, 52-53,                                 |
| Sample space 105                                                                                                                                  | 61-90, 255-257                                                  |
| Scaling 187 see also Fitting                                                                                                                      | Anderson-Sleath method 267-271 continuous time 66-89            |
| Schaefer method 185-186                                                                                                                           | coupon bonds 65-66                                              |
| SDE see Stochastic differential equations                                                                                                         | forward rate relationship 80-83 in practice 77-79               |
| Segmented markets theory 40-42                                                                                                                    | stochastic rates 70-71                                          |
| Short rate 67-70, 97-100, 98-100, 103-104                                                                                                         | zero-coupon bonds 62-65, 77-79 see also Zero-coupon yield       |
| Simple yield to maturity 323                                                                                                                      | Spread 23-24, 286-289                                           |
| Simulation of prices 119 Single-factor Heath-Jarrow-Morton                                                                                        | Square root models/squared Gaussian models 140-141              |
| model 164 Sinking funds 336, 339-340                                                                                                              | SRF see Sample regression function State variables 67, 174      |
| Smoothing 48-52, 232-275 cubic polynomials                                                                                                        | Static spread 24 Sterling overnight index                       |
| 236-238 cubic splines 50-51, 56-58 interpolation 47-51 non-parametric 238-241,                                                                    | swap (SONIA) curve 193-207 Stochastic calculus 108-110, 126-130 |
| 243-249 parametric 78-79, 107, 235-238, 241-242, 258-273                                                                                          | Stochastic differential equations (SDE) 127-128, 130-131        |
| polynomial 49-50, 236-238, 246-249, 295-296, 309-313                                                                                              | Stochastic processes 98-101, 107-110, 116-120, 117-124,         |
|                                                                                                                                                   | 126-134                                                         |
| models 51-52                                                                                                                                      |                                                                 |
|                                                                                                                                                   | Stochastic rates 70-71                                          |
| regression                                                                                                                                        |                                                                 |

| Stop-loss 287 Strips see Zero-coupon bonds Submartingale 122 Sum of squared errors 245-246 Supermartingale 122 Svensson 94 242, 260 Swap, curves 193-210 Swap pricing 194-196 SWCV screen 11, 14 T Tax capital gains 15 index-linked bonds 186   | Uncollateralised swaps 195 Upward-sloping curve 30 see also Positive sloping curve US index-linked Treasuries (TIPS) market 181 US Treasury market bond equivalent yields 298-301 excluding bills 306-309 geometric programming 295-296, 309-313 models 292-296 relative value 291-319 uncertainty quantification 296-297   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

```
Yield curve modelling  48-52 Nelson and Siegel curves  241-242, Yield curves  5-59 multi-currency  195, 203, 206-207, oscillation  208-209, 233-235, 264
```

```
floating rate notes  344-346 government bonds  279-282 index-linked bonds  182-183, 188, 340-344 internal rate of return  321-322 to par  329 portfolios  348-350 price relation  350-351 putable bonds  338-339 redemption  23-24, 326-329 zero-coupon bonds  329 Anderson-Sleath  268-271 continuous time  66-89 cubic splines  50-51, 56-58 interest-rates  95-178 asset prices  115-136 basic concepts  95-112 interpolation  47-51 259-262 non-parametric fitting  238-241, 243-249 parametric fitting  238, 241-242, 258-275 polynomial  49-50, 236-238, 246-249, 295-296, 309-313 regression models  51-52 spline methods  50-51, 56-58, 184-186, 238-241, 246-249, 262-266 Waggoner method  262-266 ancillary  291-319 arbitrage-free models  96, 150-157 combined theory  42-43 concepts  6-9, 64 coupon yield  15-16, 26 deriving  7-8, 187-188 discount factors  17, 20-23, 65-66 downward-sloping  25, 30, 39, 44-45
```

```
dynamics  96-97 Euro  6 fitting  46-52, 231-275 flat  43-44 forward  24-46, 75-76 government  5-6, 11-13, 55-56 humped  30, 39, 241-242 indexed-linked  181-190 interest-rate swap  11, 14, 55-56 main uses  8-9 211-217 negative interest rates  219-227 OIS  193-207 par  16, 186, 328-329 short rates  103-104 upward-sloping  8, 25, 30, 38, 43, 44 yield to maturity  10-15 zero-coupon  17-23, 26-27, 75-76 Yield to maturity (YTM)  5, 10-15 calculation  324-329 coupon bonds  65-66, 333-335 expectations hypothesis  35, 37-38 negative interest rates  225-226 simple  323 zero-coupon bonds  62-65, 77-79 Z Zero-coupon bonds  10, 62-65, 69-71, 77-79 Black-Scholes model  131 implied forward inflation rates  184-185 pricing  69-70, 77-79 stochastic rates  70-71 yield  329 Zero-coupon curve  17-23, 26-27 Zero-coupon yield  17-23, 63, 327-328 Zero-volatility spread  24
```