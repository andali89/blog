---
layout: post
title: How to control autocrlf for LaTeX in Git
---

If you are using LaTeX with TexStudio on windows and need to control the version of the manuscript with Git, the autocrlf option should be turned off.


The Git option to locally turn off `autocrlf` is below:

```shell
$ git config --local core.autocrlf false
```

The Git option to globally turn off `autocrlf` is below:

```shell
$ git config --global core.autocrlf false
```

The Git option to check the status of configuration are:

Global

```shell
$ git config --global --list
```

Local

```shell
$ git config --local --list
```