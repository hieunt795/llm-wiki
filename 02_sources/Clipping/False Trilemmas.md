---
title: "False Trilemmas"
source: "https://rocarmenter.substack.com/p/false-trilemmas"
author:
  - "[[Roc Armenter]]"
published: 2026-03-12
created: 2026-04-23
description: "A policy \"trilemma\" is the same as saying that status quo is already at the frontier--an equivalence that can help with policy advising. No BS whatsoever."
tags:
  - "clippings"
---
Real life gives us plenty of true dilemmas, and I assume most of you are familiar with the ‘false dilemma’ fallacy, when you are given two options to choose from, but there are alternatives available—perhaps unknown to the dilemma utterer, perhaps just less convenient.

Note that a dilemma can be false without any need to introduce further options. Exclusive or (“xor”) can be tautologically false, for example, to say, you can go to either Istanbul or Constantinople, but not both. More generally, if the two options are not mutually exclusive, the dilemma is false, though it is not commonly referred to as a fallacy.

For reasons still totally obscure to you, dear reader, I call the latter falsifiability “local,” in the sense that the dilemma is disproved within the context initially given; and the former, the fallacy, “global,” as it arises from an option not initially included in the context.

We are ready to talk about trilemmas, only after losing about half of my readership.

## Trilemmas

We are going to rain on trilemmas. Yep, those that tell us that out of three options, say {X, Y, Z}, only any two are feasible—all three are impossible.[^1] To no one’s surprise, I am interested in *policy* trilemmas, so let me include two famous examples:

- **The impossible trinity**, aka Mundell-Fleming: a country cannot simultaneously have X = {fixed exchange rate}, Y = {free capital flows}, and Z = {independent monetary policy}.
- **The globalization trilemma**, aka Rodrik’s 15 minutes of fame: a country cannot simultaneously have X = {globalization}, Y = {sovereignty}, and Z = {democracy}.

There are more examples, including a recent one—but I promised no BS. Since my criticism right here right now is not specific to any example, I will stay with X, Y, and Z—though I will return to the examples occasionally.

You say I may want to leave math, logic, and category theory out of Substack if I want to keep any readers in *your* Substack?

Hold my fifth cup of coffee today.

![](https://substackcdn.com/image/fetch/$s_!DQCm!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0dba5075-8fef-45ec-9082-c074ec3a6e71_2048x2048.png)

## Feasibility

Policy trilemmas are about what is feasible. A policy trilemma does not say “it is not good to do all three options,” it is saying that all three are simply not possible.[^2]

Feasibility can be easily encoded with a function, so let’s map X, Y, and Z into a function that takes non-positive values when X=x, Y=y, and Z=z are feasible:

$F \left(\right. x , y , z \left.\right) \leq 0.$

You are right if you think I should be careful. Does this function even exist? This is an excellent question that maps back to the trilemma:

- **Is (X,Y,Z) all there is to know to determine feasibility**? <=> **Does F exist**? In other words, if we know X, Y, and Z, are we ready to call it feasible or not? Are we assuming something about the rest of the world when we do so, or is it truly the case that the rest of the world can go and fry asparagus for all we care—the trilemma will still stand?

You should thank me for not going into a 1000-word poorly-worded piece on category theory. Instead, we just assume that F exists and is continuous, which in turn implies that (X, Y, Z) are continuous variables.[^3]

Every policy trilemma has an implicit context in which the options are desirable (for the policymaker). So, a bit of a normalization: Let’s agree that more is always better, i.e., if

$x > x_{0} , y > y_{0} , z > z_{0} ;$

then the policymaker prefers (x,y,z) to the status quo allocations, denoted by subscript 0. The direction is without loss of generality.

## At the Frontier

Now things fall into place easily. If there is *any* feasible allocation that satisfies (`better`), then the trilemma is false. Bring in F being continuous, and it is rather immediate that

$F \left(\right. x_{0} , y_{0} , z_{0} \left.\right) = 0.$

That is, status quo policy is already at the frontier of what is feasible.

Maybe it was obvious from the beginning: If a single superior policy were feasible, then for sure the status quo was not at the frontier. However, note that this by itself does *not* imply that if a superior policy is not feasible, then we are at the frontier.[^4] If *none* of the superior policies are feasible, *then* we can conclude that we are at the frontier.

Obvious or not, believe me, a policymaker does not respond the same to “you cannot do that” and to “you are already doing the best possible.” As frameworks for attacking a policy problem, they seem to take a very different approach, with the trilemma version being frankly a bit discouraging, while the frontier version just recognizes the need to think outside the ~~box~~ triangle.

Next, we establish whether a trilemma is true or false.

## False Trilemmas

Now that we have formalized the dilemma through a definition of feasibility, we can stare at it and ask WTF, meaning, What The Function, of course.

The immediate reaction is the right one: Something could be missing in F.[^5] Like, the rest of the world may matter for our trilemma; should we use instead

$F \left(\right. x , y , z ; a , b , c , \ldots \left.\right) \leq 0$

recognizing that if a,b,c,… change, it may be possible to achieve a (`better`) policy. I assume that a,b,c,… do not have policy implications—they are neither better nor worse by themselves.

In words, if you can tweak some other variable or parameter and break out of the trilemma, then you got a “false trilemma” fallacy.

Also in words, but from the “at the frontier” approach, if you can move the frontier out, then you are a policy genius (and likely do not care that you proved your first definition of frontier wrong in the process).

Oh, dear surviving reader, if you exist, now I can shed light on the distinction between local and global falsibiability:

- **Locally false**, whether disproving the trilemma by showing that (x,y,z) are feasible after all—or by knowing that the status quo is not at the frontier.
- **Globally false**, by showing an additional variable or parameter can change, by a bit or by a lot, and that enables (x,y,z) as feasible.

Among other fabulous possibilities that I have yet to encounter, this distinction allows you to answer a trilemma with yes and no, without being accused of being a two-armed economist.[^6] Why? Because it is logically consistent to say that the trilemma is locally true—we are doing our best under the current system configuration—and the trilemma is globally false—there are other configurations that enable us to have the cake and eat it, too.

## Taking the Colimit

There are connections to category theory. We mapped a set of logical properties of a set (e.g., x and y imply no z) to properties of a function, with both being equivalent representations of feasibility.

However, the functor I want to close with is the trilemma-frontier map to policy advising. I showed the mathematical equivalence between a trilemma and being at the frontier. But, in terms of policy advising, the two approaches “feel” very different. I would say, both succeed at highlighting the existing trade-offs (that is, assuming that they are right locally), but then…

- The trilemma presents itself as globally true, that is, there is nothing you can do or glue outside X, Y, and Z that will get you X, Y, and Z. This approach is one that emphasizes caution and keeping expectations in check, perhaps invites the policymaker to place his or her priorities elsewhere.
- The frontier approach instead sets up the global search of a,b,c,… that will get you X, Y, and Z. We are now calling out the need for changes, for thinking outside the box… to achieve the desired objectives.

If someone tells you that you cannot say the same thing, but differently… tell them that is a false dilemma.

[^1]: After several attempts to type the last sentence, I discovered that (1) Substack does not do inline math and (2) it cannot because it has reserved the dollar sign for stocks: [Z -1.96%↓](https://substack.com/search/%24Z) is what happens if you type “dollar sign” + “Z”.

[^2]: “You can't do it or you won't do it?” as the Gang tries to sell gas back to the gas station—proving again that *It’s Always Sunny in Philadelphia* lives in the future.

[^3]: Theoretically, a trilemma (or dilemma) should have Boolean dimensions, i.e., X is either True or False, etc., etc. In practice, capital flows can be more or less free, and a country can be more or less sovereign. I will just go with X, Y, and Z being dimensions: If the variables are not continuous, I would need to adjust the definition of “frontier” later, but that’s all.

[^4]: “P => no Q” does NOT imply “no P => Q.”

[^5]: Alternatively, there are other functions, “technologies” or “frameworks,” say G(x,y,z). The idea is the same.

[^6]: Guilty. Cervantes wrote *El Quijote* with only one arm. What do you think he would have written if he had two arms?