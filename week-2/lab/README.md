# Gap Inc. Sales

## The Story
One of my summer jobs in high school was as a sales associate at the Gap. We never got much foot traffic, to the point where some of the shelves collected dust (not kidding). Meanwhile, my friend working at the nearby Old Navy would get swamped underneath mountains of $10 tees – I was just glad to have shorter shifts. Fast forward a few years, and turns out Gap wasn't doing so great financially. Old Navy, their only profitable brand, wanted to spin off, and Gap's longtime CEO stepped down.

Was it the $80 denim that turned customers away? Or the riduculous G-A-P sweaters that should've been retired in 2003? Naturally, I turned to data science for answers. Since Gap Inc. doesn't make their store-by-store sales data public, *we made up our own*.

## The Task
Pretend you're a data scientist at Gap Inc., tasked with exploring sales trends in the Virginia market. Leadership has provided a list of questions, which you can find in the lab notebook itself. 
 
#### Assignment
| Interactive Notebook | Source Code  |
| :-----------: | :------------: |
| [![Link](../../tools/buttons/open-colab.svg)](https://colab.research.google.com/github/ishaandey/node/blob/master/week-2/lab/gap_notes_f21.ipynb) | [![Link](../../tools/buttons/download-ipynb.svg)](https://files.node.ishaandey.com/week-2/lab/gap_notes_f21.ipynb) |

#### Key
| Interactive Notebook | Source Code  |
| :-----------: | :------------: |
| [![Link](../../tools/buttons/open-colab.svg)](https://colab.research.google.com/github/ishaandey/node/blob/master/week-2/lab/gap_key_f21.ipynb) | [![Link](../../tools/buttons/download-ipynb.svg)](https://files.node.ishaandey.com/week-2/lab/gap_key_f21.ipynb) |

**Tips**:
* Convert each question into a **set of actions**. If you want to look at some attribute of Gap sales, think about subsetting the dataframe to where the store == Gap, before tackling the rest.
* Build your answer part by part: take a look at the output on each step to verify you're getting what you want.
* **Google** is your best friend. Look for StackOverflow or Pandas documentation in particular. 
* **Read the errors**. They can be intimidating, but its there for a reason. 
* If you can't figure out what a specific part of code is doing, either try running just that part, or use `type( )` to see what type of object is being returned 
* **Ask for help!** Go to your peers around you, then the instructor if that doesn't help!

## The Data
This data represents individual transactions in Banana Republic and Gap stores in VA from Q1 of FY2020. We've got granular information on every attribute: Each order, each item purchased in that order, which customer bought it, where, when, and how the purchase was made.