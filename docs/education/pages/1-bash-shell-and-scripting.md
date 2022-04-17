
# Bash Shell and Scripting

Having a working knowledge of the command line interface (CLI)
interface is essential to having complete control of your
computer whether that be your local PC, a remote server,
or a whole cluster of resources. The bash shell provides access
to a machine's command line interface and scripting allows us to
automate and program these commands.

## What is the Bash Shell (CLI)?

All computers require some form of interface to interact with it
in real time. A modern PC uses a graphical user interface (GUI) 
to interact with the computers operating system (OS). GUIs are 
optimized to be human-friendly and are not the best option for all 
types of interactions with computing resources.

The command line interface (CLI) uses text only commands to interact with
a computer directly. This could be the whole of the OS, like an old DOS 
machine; a GUI window within a modern OS, like Terminal in Macs; or a 
program which allows access to a remote machine, like an SSH client. 
While using text commands may seem old-fashioned, the half-century old
practice is utilized now more than ever.

## Why CLI?

Most important reason is you **will** need to some day but below are some
general reasons why it's a useful tool:

- **Precision:** Using text only commands allows for exact precision in
both sending instructions to a computer and sharing commands with others.
- **Functionality:** Adding functions and different configurations is easy
in a text based commands so much more is possible using the CLI than any GUI.
- **Computer Friendly:** Using the CLI is in itself a programming language
where each time you enter a command you are entering a line of code. These 
means the power of the CLI can be automated in scripts.
- **Universal:** TODO
- **No "Click on" Tutorials:** Part of learning is reading online docs and
tutorials and using the CLI removes the need for confusing "click on" steps.
Instead, sets of commands are shared which are exact and can be modified
if necessary.

## Shell Implementations

A "shell" is any program which exposes the functionality of a computers OS
to the user of the program. We use the GUI shell of our OS every day but 
your computer also offers a CLI shell, which also differs depending on
your OS/configuration. There are many types of shells but they all have
the same purpose of granting control of a computer.

### Unix vs Microsoft

The biggest difference in CLI shell implementation will be Unix vs Microsoft
based OSs. Mac and Linux machines are Unix based and have very similar CLI
implementations which have massive libraries and are used universally by
devops, engineers, and developers. Microsoft offers a command line (cmd) and
now PowerShell which can be useful for Microsoft specific things but is not
useful as a developer.

Options are listed below for Microsoft users but going forward all discussion
will be based on the Unix CLI. These implementations are run via a specific
program which differ slightly but not enough to matter for this doc. Historically
`bash` has been the most popular shell for Unix systems but now Z-Shell `zsh` is
gaining popularity amongst others. Your OS may be using an updated type of shell
without you evening knowing, but it doesn't matter here. We will be using well 
established `bash` commands which are included in all modern implementations.

The shell program can be accessed using the OS's Terminal/Console program, 
an IDE,  a remote SSH connection, a shell script, or other methods. While there 
may be different reasons to use each, the same shell program is utilized via
the same text commands.

### Microsoft Options

TODO

## How to Learn

### The Book

There is no single book to read on the topic but having a book covering a
range of `bash` commands, general linux/unix mechanics and shell scripting.
I have recommendations listed below but there are many options, some probably 
cheaper or free. 

What is important to have a Unix book that is broad enough to act as reference 
material and can be browsed to find new commands or topics to learn. Do not 
try to read the book cover to cover but do read full chapters on subjects as 
they become relevant. 

TODO Pic

[<img src="http://www.google.com.au/images/nav_logo7.png">](http://google.com.au/)

_The Linux Command Line: William Shotts_ - Great modern book covering everything 
you need.

TODO pic
https://upload.wikimedia.org/wikipedia/en/4/43/English4.gif

<img src="https://upload.wikimedia.org/wikipedia/en/4/43/English4.gif">

_The Unix Programming Environment:_ Brian Kernighan - Published in 1984 and still 
found used online for under 10$ today, this forty-year-old book teaches Unix 
commands and programming as still used today. I would highly recommend looking 
through a copy to gain perspective on how long the same Unix tools have been in use.

- https://www.gnu.org/software/bash/manual/bash.html

### Practice

Generally you won't be writing shell script regularly like you would other 
languages in the modern day to day. To advance your knowledge of `bash` script
you should find excuses to practice. For example, using your terminal to find
and move files instead of the file explorer or writing a script to automate
any manual computer tasks you do regularly. The more you use the command line
the more comfortable and useful it becomes.

One big benefit of this practice is that it becomes vital when working with
remote server based resources which do not provide a GUI interface. Even with
today's modern web tools there is still a need to know how interface with a
server directly which requires practice to do confidently. Also, the ability
to shell script allows you to quickly write "mini-programs" without installing
anything new.

### Script Examples

Bash scripting has been around a long time and was used more liberally in
the past. There is a wealth of script examples in books and online which
can show you what's possible within Unix. Nowadays, the tasks of many 
examples would be performed within a real language or tool but knowing
how to perform complex tasks with the CLI is very useful when no other 
tools are convenient or accessible.

TODO

_Wicked Cool Shell Scripts: Dave Taylor and Brandon Perry_ - A definite
tour de force of the CLI shell with great breakdowns of the code steps.
Also contains a collection of scripts highly relevant to computing tasks
frequent in the modern day.

## Common Shell Commands

I will not go into these commands in detail but will provide some context
on their usage. Use the online resources below and via searching to learn
more about each command. 

Google Tip: `bash <command> <question>`

TODO - Explain options and arguments

These are only two of the many potential uses of the Unix command line.

### File System

Having control of a computers file system is skill number one to learn
for the command line. The `bash` file system is simple but requires an
older computer mindset. Each command is occupied by a folder location
called your **Current Working Directory** which is the current folder
you are "in" (which can be viewed with the `pwd` command). This
location may be used directly by the command or many used as a 
reference point for any specified file/folder locations.

For example, the change directories command `cd` is used to move the 
current working directory. The argument following the command is the
new location which can be given as the full path (example A) or the
shorter relative path (example B). The dot notion allows you to move
backwards from the relative location as example C with a different
root folder can be accessed releatively by example D. 

TODO

### Text Processing

## Bash Scripting


```
The Peoples Plans  Copyright (C) 2022  Ross Palmer
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.
```