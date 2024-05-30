---
layout: post
title: Test my equation
lesson: lesson3
---

## This is my third page

Good!

haha 

{% assign post = site.jekyll | find: "pageid", "cts"  %}

show [one of our related page is avalable here!]({{ post.url | absolute_url }})


[one of our related page is avalable here!]({{site.url}}/jekyll/2024-05-20-my-second-blog/index.html)

中文支持

<p>
    \begin{align}
    \dot{x} & = \sigma(y-x) \\
    \dot{y} & = \rho x - y - xz \\
    \dot{z} & = -\beta z + xy
    \end{align}
 </p>

 test inline equation $ \frac{a}{b} = c $