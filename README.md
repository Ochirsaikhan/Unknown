# Course Project

<div class="alert alert-block alert-danger">
    <p>Please note that all of the deadlines listed below are <b>hard deadlines</b>. This means that you need to meet them. Given the short nature of this course, the time I have to evaluate your work is likewise truncated. Turning things in on time is the <i>only way</i> that I have to make sure that I can meet my deadlines <i>and</i> be fair to you.</p>
</div>

* Assigned: 19 April, 2021
* Due: 17 May, 2021, 11:59 PM

## Table of Contents

* [Overview](#Overview)
* [Supporting Readings](#Supporting-readings)
  * [More examples](#More-examples)
* [Evaluation](#Evaluation)
  * [Requirements](#Requirements)
    * [The docs](#The-docs)
    * [The code](#The-code)
    * [The repository](#The-repository)
* [Some resources](#Some-resources)

## Overview

This semester, in the course of learning fundamental computational concepts using Python, you've been using structured, semi-guided exercises to explore topics. This project invites you to explore and expand your knowledge in greater detail by applying your skills to a different kind of "problem": one of creating an art work.

What do I mean when I write "art work"? The term is, like so many we use, necessarily ambigious. It could be a translator that [turns all words in a text into variations of the word "meow"](https://github.com/hugovk/meow.py/blob/master/meow.py); it could be a graphic novel generator that uses Flickr images and some image magic to [create visual detective comics](http://gregborenstein.com/comics/generated_detective/); it could even be someting madlib-like that tells us [what some random fictional, nameless person in a random place is doing as the clock rolls on](http://opentranscripts.org/transcript/translating-world-clock).

For the more graphically inclined, it could be a series of still pictures generated from data, like [these](https://github.com/gkaramanis/aRtist) or something inspired by the [NFT craze](https://www.hicetnunc.xyz/).

Heck, it could be a list of fake names of people on a list to go to the Moon aboard the next SpaceX mission.

Your goal is deceptively complex: come up with an interesting concept and figure out how to make that concept happen -- in code. You could figure out a way to extract every word beginning with the letter `p` from _Pride & Prejudice_. You could choose 20 of your favorite (**_public domain_**) texts and select random words from each randomly until you've finished the requirements. Heck, you could even create a graphic novel about ellipses, rectangles, and polygons trying to avoid being erased by using `PIL` to generate shapes and paste text.

## Supporting readings

These readings will be the subject for our activity to close out this week. Concentrate on the Kazemi reading and one or two of the projects there and one or two of the projects I've provided.

They are all much less complex than they seem. Don't focus on the code, though (I provide it as a reference), focus on the _process you think the author used to make them_. This is less about "load a file and read a line" and more about thinking (using _Generative Detective_ as a sample):

1. I would find a picture and do something to it to make it look like a comic book
2. I would find some detective novel or text that's interesting
3. I would randomly take a line from that text using some keywords
4. I'd then paste that line at the bottom in a box that looks like comic book descriptions
5. I will not care if it only vaguely makes sense, but it's better if it does

This post from [notoriously great internet person Darius Kazemi](https://tinysubversions.com/) should help break down some of the "OMIGOSHICAN'TDOTHATWUT" that tends to accompany the first time you do someting like this:

* [Even a beginner programmer can make a novel generator](https://tinysubversions.com/notes/nanogenmo-2019/)

### More examples

* [Translating _World Clock_](http://opentranscripts.org/transcript/translating-world-clock/)
  * This source is less about the translation and more about the process
  * Also, like most computational art, [the whole thing is available on the internet](https://nickm.com/poems/world_clock.pdf) (courtesy of the author)
* [Generative Detective](http://gregborenstein.com/comics/generated_detective/)
  * And, read about the process in [this thread](https://github.com/dariusk/NaNoGenMo-2014/issues/70)
* [_Moby Dick_ in 50,000 Meows](https://www.theatlahttps://github.com/hugovk/meow.pyntic.com/technology/archive/2014/12/moby-dick-in-50000-meows-and-other-tales-that-computers-tell/383340/)
  * Of course, the [source and more is here](https://github.com/hugovk/meow.py)

## Evaluation

|Type                      |Point value |
|--------------------------|------------|
|Documentation             |120 pts.    |
|Working code and output   |80 pts.     |
|                          |            |
|Total                     |200 pts.     |
|                          |20% of course|

Being a 100% arbitrary measure, your creative intent with this project is the goal.

Simply put, the outcome of this project should be one of the following:

* A single text file containing the complete output of one run of your program, or
  * This text file must contain _at least_ 5000 individual words
  * This text must be consistent with the documentation accompanying it
* A series of _at least_ 10 images, named according to the order to "read" them
  * This might be best achieved by numbering or letterin them

But those general goals are a bit too easy. I have more requirements.

### Requirements

|Component              |Due Date     | Weight |
|-----------------------|-------------|--------|
|Idea                   | 29 April    |40 pts. |
|Progress report        | 9 May       |40 pts. |
|Final report           | 17 May      |40 pts. |
|Final code and output  | 17 May      |80 pts. |
|                       |             |        |
|Total                  |             |200 pts.|

<div class="alert alert-block alert-danger">
    <p>For this assignment, <b>I will not accept any adventure games or "madlibs"</b>. I am glad to discuss my reasoning with you.</p>
    <p>In addition, <b>I must be able to run your program when I grade it</b>. I I can't run it, the "<b>Working code and output</b>" category will be a <b>0</b>, which means that the maximum score for any project <em>not</em> running will be a 60% (120 out of 200).
</div>

<div class="alert alert-block alert-warning">
<p>This project assumes a very high level of autonomy. Meeting due dates is a key way to demonstrate that you're on track and that you're doing well with this kind of "free-range" project. I advise you to work iteratively (that is, in pieces over time) to complete the work and not let the due date sneak up on you. A project like this is no fun if you start it the night before.</p>
<p>Plus, by that time, you've already missed a bunch of deadlines.</p>
</div>

#### The docs

Each of these documents already exists in the `docs` directory. It is up to you to complete them.

* An `idea` of no fewer than 100 words which:
  * Proposes a tentative/working/permanent title for your project
  * Describes the project you intend to create
  * Your motivation or interest in doing so
  * Potential roadblocks or perceived challenges
  * A description of the _ideal_ outcome/output
  
  
* A `progress report` of no fewer than 200 words that:
  * Describes the state of your project: where are you at? What do you still need to complete?
    * This should take the form of a Markdown list of outstanding tasks and a brief paragraph describing your progress
  * Summarizes your current challenges: where are you stuck? What could you use help with?
  * Celebrates your successes: surely you have some.
  
  
* A `final report` of at least 300 words which:
  * Contains the final title
  * Summarizes your end-of-project thoughts: how do you feel about the outcome of your project?
  * Describes how your project changed over time -- did you need to make it more complex? Simpler? How/why?
  * Contains a "post-mortem" which thinks about: 
    * what worked? 
    * what didn't? 
    * what would you have done differently?
    * what was the biggest challenge that you overcame? How did you do it?

#### The code

<div class="alert alert-block alert-info">
This section refers to custom or self-written modules. Using a self-written module is highly encouraged, but not required.
</div>

This code should be written in the [main.py file](src/main.py) in the `src` folder and write all of its output to the `output` folder. With respect to the last objective, you'll find using `../output` as the beginning of your file path helpful.

Any data source that you use should be placed in the `data` folder. Like the above `output` folder example, loading these files in `main.py` should use the `../data` prefix to the path.

Your code should:

* Contain at least one function
  * If your project uses a custom module, functions like `__init__`, et al. do not count
* Use at least one kind of data structure (`list`, `tuple`, `dictionary`)
* Reads at least one file as input
* `import`s (and _uses_) at least one additional module
  * If you write your own module, this counts
* Contains at least one `for` or `while` loop
  * Though, I trust you'll have to use more
* Use a productive number of single-line comments
  * Here, the number is _at least_ 15, though I imagine you'll need many more
* Be completed in a `*.py` file
  * I am, however, open to projects which think about Jupyter notebooks as a storytelling device
    * Think about this one; it could be interesting
    * You need to tell me that's what you want to do, though
* If your program requires input, you will need to provide an example of each prompt's input in the [src/inputs](src/inputs) file.

##### A note on external libraries and modules

You do not have the ability to install additional libraries on the server. However, if you request an additional module, I _can_. **I reserve the right to choose not to install a requested module _and_ provide a reason why**. We do have some additional functionality already on the server:

* `markovify`
* `PIL`
* `opencv`
* `spaCy`
* `textwrap3`

Some of these we haven't seen or discussed. Odds are, if there's a module you'd like to use, we haven't. Though I am glad to talk with you about using any "non-standard" modules, it's up to you to really integrate them into your project through exploration or trial-and-error. I suggest reviewing documentation as a start.

**This project can be completed with interesting output using only the modules we already have.**

#### The repository

Because this work should take place iteratively, this repository requires at least _10_ `commit`s.

## Some resources

Struggling for what to do with a text or with images? Here are two resources which may help:

* [Darius K.'s corpora madness](https://github.com/dariusk/corpora/tree/master/data)
  * These are all `json` files, which seem intimidating, but are relatively easy to use; we'll talk about them in class.
* [Project Gutenberg](https://www.gutenberg.org/)
* [Creative Commons image search](https://search.creativecommons.org/)