---
title: "Fixed Income - Alexander During-11"
type: raw_source
source_pdf: "Fixed Income - Alexander During-11.pdf"
extractor: docling
---

<!-- image -->

Two

## Cash Instruments

## CHAPTER 10

## Contract and Instrument Types

F ixed income markets are governed by a plethora of contracts. These cover the relationships between lenders and borrowers, securities issuers and securities holders, dealers and their customers and so on. In addition to formal contracts, informal customs provide further frameworks to the mutual behaviour of market participants. This chapter introduces some of these concepts.

## 10.1 SECURITIES AND BILATERALCONTRACTS

Fixed income instruments can generally be divided into transferrable securities and bilateral contracts 1 . In either case the obligations of the parties to the contract are documented in one or more legal instruments, i.e., physical documents. In most cases, the same parties will conduct a series of very similar transactions, so in the interest of economy, a general legal instrument will outline the common features of all related transactions and each specific transaction will then only require a short document outlining the specific details of this one transaction. Claims against a borrower can be evidenced in a number of ways and such evidence need not necessarily be in the form of a legal instrument. Indeed, in a bond transaction with physical bond certificates (now rare), the actual bond contract would specify the number and denomination of bond certificates to be printed and those certificates would then represent the claims under the bond contract. However, these certificates would only represent evidence of the claim under contract, not the contract itself.

Transferrable securities come in two general forms, namely bearer securities and registered securities. Note that there is an apparent third form, namely book-entry securities, discussed below. In the case of a bearer security, ownership of the beneficial interest is evidenced by possession of the security. This makes bearer securities very easy to trade because all that is needed to transfer the beneficial claim is to transfer pieces of paper. However, bearer securities carry significant risk of destruction, theft, and counterfeiting 2 . Indeed, counterfeiting of bearer securities such as shares and bonds was at some time more lucrative for criminals than counterfeiting currency. Bearer securities also present a problem in terms of denomination. If they are issued in very small denominations, the cost of printing the certificates in a way that is sufficiently hard to forge is very costly, while issuing large denominations restricts the amounts that can be traded. Last but not least, bearer securities are very useful for criminal activity such as money laundering and tax evasion because proof of ownership does not require any audit trail.

1 The definitions used here are not related to legal definitions of securities or contracts that may differ between different jurisdictions.

2 The Hollywood movie 'Die Hard' can serve as an example.

FIGURE 10.1 Security types.

<!-- image -->

In contrast, registered securities are securities where beneficial interest is recorded by the issuer or an agent of the issuer, the registrar. There may be physical certificates of ownership as well, but unlike bearer securities, holding such certificates does not prove beneficial interest. Trading in registered securities is more cumbersome than for bearer securities because each transaction has to be reported to the registrar for the new owner to be registered. At the same time, trading is technically possible in any denomination.

German law recognises a mixed form of security called a Schuldschein. Translated literally, the term means 'promissory note', but a more accurate description would be 'transferrable loan'. A Schuldschein does by itself not constitute a debt by the issuer, but is evidence of a separate loan contract. Schuldscheine are usually documented to allow a limited number of transfers (usually three) and transfers are registered on the certificate itself. The reason to see a Schuldschein as a mix between registered and bearer securities is that a physical and transferrable certificate evidencing ownership exists, but ownership is still registered and change of registration is limited.

The ease of trading in a security has important implications for the accounting treatment of investments in the security. If trading in a security is difficult, it cannot be assumed that a meaningful market for that security exists and there is therefore no market price. One of the motivations to still issue debt certificates with transfer restrictions, such as German Schuldscheine, is to permit holders to avoid mark-to-market accounting of such securities while permitting liquidation of investments when needed.

Modernsecurities markets are generally too fast to permit physical transfer of paper certificates although this still happens. Instead, securities are now generally traded in book-entry form. Legally, the securities are issued as bearer securities with only one physical certificate denoting the beneficial interest in the entire issue. This certificate, called a global note is deposited with a trusted intermediary, the custodian which in this case is more appropriately known as a central securities depository (CSD). Such institutions are further divided into local and global CSDs, known as LCSD and GCSD.

Trading in the security is then done through transfers of book entries with a clearer or clearing house. Security clearers are specialist banks that focus on keeping records of beneficial ownership in securities and transfer such ownership, usually though maintaining accounts with an GCSD or being a GCSD themselves. Put differently, the custodian of a global note holds the certificate in trust for one of the large clearers and the chain of ownership from the securities holders to the global note is closed through a trust agreement between the clearer and the custodian. Of course, the clearing houses also act as custodians for a number of securities transactions, but that is not a necessary condition.

There are currently two global firms that handle the bulk of securities transfers, namelyEuroclearandClearstream.WhileEuroclearisownedbyaconsortiumofbanks, Clearstream is a subsidiary of Deutsche Börse AG, the German stock exchange. Other securities clearers exist in local markets and most clearers have links with one another so that transfers of ownership can be handled effectively across different clearers. For instance, Italian securities are usually held in a LCSD called Monte dei Titoli, German government bonds at the Bundesschuldenverwaltung, but all of them can be traded through most clearing systems. This gives investors unfettered access to local markets.

## 10.2 SECURITY IDENTIFIERS

Securities need to be identified in order to trade them. There are various ways to do that. Between human beings, it is common to use descriptions related to important characteristics of the security such as 'Federal government bond 1% coupon of 2015' for a bond issued in 2015. More commonly, securities have a ticker (short for ticker tape symbol) that identifies the issuer to some degree. The security above could have the tickers T, DBR, or RAGB, depending on which federal government (United States, Germany or Austria) issued the security. Using the ticker, the same bond may therefore be identified as 'DBR 1% 2025' or 'DBR 1% 08/25' where the last part refers to the maturity of the bond which in this case is 15 August 2025. German financial reports somewhat confusingly refer to securities by coupon and issuance date rather than maturity date.

For the automation of settlement procedures, it is vital that securities are identified in a way that does not require human ingenuity to resolve potential misunderstandings. The market has therefore developed security identifier systems that rely on fixed-length codes. ISINs, discussed below, are most widely used in international transfers. The most common domestic systems are the US CUSIP 3 , the German WKN (Wertpapierkennnummer), the Japanese meigara code 4 .

## 10.2.1 ISIN codes

ISINs (international securities identification numbers) are security identifiers governed by an ISO standard (ISO 6166:2013) but assigned by a private company. They are the most prevalent security identifiers in global markets. ISINs are therefore sometimes mistakenly equated with securities themselves. In practice, not every security has an ISIN and not every ISIN corresponds to a security. Not every securities issuer wants to incur the expense and effort to obtain an ISIN for every security issued, while ISINs have also be assigned, for instance, to futures contracts and iBoxx indices.

3 Theabbreviation CUSIP stands not for the codes themselves but for the committee that proposed the system, the Committee on Uniform Security Identification Procedures.

4 The term 'meigara code' can refer in common usage to a 4-digit listed equity identifier, or a 9-digit bond (k¯ oshasaikoy¯ umei) code. The second usage is intended here.

Adding to the confusion is the practice by some issuers to issue new tranches of existing securities (taps) with a new ISIN. Although the cash flows of the new tranche usually match those of the existing security, the new ISIN ensures that concerns like non-standard settlement dates of the new security (for instance, first settlement 5 days after issuance rather than T + 2 for the existing security) can be handled properly. After a certain period of time, the new ISIN is merged (funged 5 in market parlance) into the existing security. The new ISIN therefore ceases to exist and a position in the tap security changes ISIN. In other words, the same security can have different ISINs at different times.

ISINs consist of 12 characters (uppercase letters or numbers) divided into three blocks. The first 2 characters are letters that identify the country of issuance 6 in line with ISO standard 3166-1 (US for United States of America, JP for Japan, DE for Germany, and so on). Note that the country of issuance is not the same as the country of incorporation of the issuer. The special code 'XS' is used for eurobonds. The next nine characters are referred to as national securities identification numbers. These are in most cases domestic security identifiers, padded by leading zeros in case they are shorter than 9 characters. For instance, a German domestic Wertpapierkennnummer (WKN) is six characters long and therefore German ISINs start with DE000 (country code plus three padding characters ahead of the WKN). In the US, CUSIP numbers, which are 9 characters long, are used for the national securities identification numbers. Importantly, this convention is not followed everywhere. Japanese ISINs start with JP but the following 9 characters for bonds are constructed in a way that is completely different from the domestic identifiers (meigara code). As a result, ISINs of Japanese bonds cannot be constructed from the meigara code 7 .

The 12th and last character of an ISIN is a check digit calculated from the first 11 characters. The presence of that check number reduces the scope for human error, such as transposed characters. Exchanging any adjacent characters leads to a different check character, as do most changes of a single character. Comparing the check digit calculated from the first 11 characters of an ISIN with the 12th character is therefore a useful check for transmission errors.

The calculation of the check digit is somewhat complicated in modern programming languages. The first step is to write down a numerical representation of the first 11 characters of the ISIN, using 0 for the digit 0 and so on, and the digits 1 and 0 for the letter A, the digits 1 and 1 for the letter B and so on. For instance, the 11 characters starting the ISIN of JB321:

J P 1 1 0 3 2 1 1 C 3

5 The verb 'funge' does not exist in most English dictionaries but the derived adjective 'fungible' does.

6 More precisely the country of residence of the central securities depository holding the security.

7 The 9 domestic characters of a Japanese ISIN are known in Japan as the 'New security code' (shinsh¯ oken k¯ odo).

become:

## 1 9 2 5 1 1 0 3 2 1 1 1 2 3

By construction, the result of the first step is a series of numbers. In the next step, every other number, starting with the second, is doubled. In the example above, this doubling and again replacing every 2-digit result by 2 single-digit numbers (shown in bold) delivers:

## 2 1 8 2 1 0 1 2 0 6 2 2 1 2 2 6

Next, these digits are added up in a simple sum, resulting here in the number 44. The 10s modulus of this sum, here 7, is subtracted from 10 and the 10s modulus taken again on the result (3), so that the check digit and therefore the 12th character of this ISIN is 3 8 .

## 10.2.2 CUSIP codes

A CUSIP is a 9-character code. Like ISIN codes, CUSIPs have an internal structure, including a check digit at the end. The first 6 characters of a CUSIP identify the issuer, the next 2 an individual issue, and the last is a check digit. Of the 6 issuer code characters, the last 3 may be alphanumeric while the first 3 are always numeric. Some issuer id combinations are reserved, and multiple issuer ids may be given to large-scale issuers like the US Federal Government. That being said, the large number of possible issue codes means that at the time of writing, the issuer codes 912796 for bills and 912810 or 912828 for bonds and TIPS suffice to cover the extant US government securities.

The issue code is fully numeric for equity securities and contains at least 1 letter for debt securities, with the letters O and I as well as the numbers 0 and 1 omitted for fixed income securities to avoid confusion 9 , making it straightforward to distinguish between debt and equity instruments.

The CUSIP check digit serves the same purpose as the ISIN check digit but is calculated in a subtly different way 10 . Using a US Treasury example (T 8.75% 08/20), the CUSIP starting with 912810EG is first translated into a series of numbers, where digits retain their value and letters become numbers starting with 10 for A. This CUSIP therefore becomes:

9 1 2 8 1 0 14 16

Similar to the ISIN calculation, every other of these 8 numbers is then doubled:

9 2 2 16 1 0 14 32

8 The final modulus operation ensures that if the 10s modulus of the last sum is 0, the check digit is 0 instead of 10, or A.

9 This allows for 100 equity and 1008 debt securities per issuer id.

10 The difference is indeed so subtle that one wonders whether it is the result of deliberation or confusion.

The resulting digits are then added up:

9 + 2 + 2 + 1 + 6 + 1 + 0 + 1 + 4 + 3 + 2

which here results in the number 31. The 10s complement of this number, calculated in the same way as for an ISIN, is the check digit 9. The full CUSIP is therefore 912810EG9.