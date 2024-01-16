# Git, Github, and Conventional commit for ultimate collaboration

**Pre-requisite** for this tutorial is familiarity with Git functionalities
covered in the Software Carpentry's
[Version Control with Git](https://swcarpentry.github.io/git-novice/) tutorial.

**Note: As you're working through this tutorial, you can use
the [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf).**

## Motivation / Learning Objectives

- Learn what it means to use `git` as a tool for open-source collaboration
- Learn the usage of conventional commit to structure commit messages
- Learn and familiarize with the Git Forking workflow for collaboration

## Git Review

### A Basic Collaborative Workflow (From Software Carpentry)

In practice, it is good to be sure that you have an updated version of the repository
you are collaborating on, so you should `git pull` before making our changes.

The basic collaborative workflow would be:

1. update your local repo with `git pull origin main`,
2. make your changes and stage them with `git add`,
3. commit your changes with `git commit -m`, and
4. upload the changes to GitHub with `git push origin main`

It is better to make **many commits with smaller changes** rather
than of one commit with massive changes: **small commits are easier to read and review**.

### Expanding on the basic

The main branch is usually called `main`. You would create another branch so we can make changes safely.
Branches are cheap so create as many as you want! It is recommended that branches are named based on
the **function or feature** that will be the **focus of the branch**.

With that in mind the expanded workflow would look like:

1. update your local repo with `git pull origin main`,
2. create a feature branch with `git checkout -b gh-username/feature-focus`
3. make your changes and stage them with `git add`,
4. commit your changes with `git commit -m`, and
5. upload the changes to GitHub with `git push origin gh-username/feature-focus`
6. create a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) on GitHub for review from `gh-username/feature-focus` -> `main`

## Collaborating effectively

TIP: The two basic workflows in [the Git review](#git-review) above should be familiar to you before moving forward
with the tutorial as it is very important to be able to mindfully navigate through
various branches and commits.

Yet another expansion to the workflow is the notion of **"Forks"**.
A single "upstream" repository can have many number of forks.
Additionally, having a structure to commit messages can make it easy
for collaborators to understand each changes as well as build
automated tools to parse these messages for analytics or other uses.

### What is a fork?

No, not the tool you use to eat. 🍴

A fork is a new repository that shares code and visibility settings with the original "upstream" repository.
This fork repository can be hosted within a Github Organization or User. Forks are used when you don't have
write access, but wanting to contribute back to the "upstream" repository.

### Commit message structure

The community has developed a standard for commit message called the [conventional commit v1.0](https://www.conventionalcommits.org/en/v1.0.0/).

The commit message should be structured as follows:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

At the very least, the `type` and `description` of the commit are **required**.

In the [Commit messages convention](../fundamentals/conventional-commits.md) page within the fundamental section,
you should find the various types and detailed options for this convention. For this tutorial, we will
use `type`, `description`, and a short summary `body` for the changes we make.

## Let's get our hands dirty

Okay, so now you're familiar with the basic collaborative workflow and the ideas behind "Fork" and "Pull Request".
This way of working is also known as the ["Fork and pull model"](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models#fork-and-pull-model). Additionally, "conventional commits" provides a structure
for clear commit messages so that we have clear communication of changes that have been made.

The rest of the tutorial we will essentially practice the steps outlined in the [Github Collaboration Step by step](../fundamentals/git-github.md#github-collaboration-step-by-step).
