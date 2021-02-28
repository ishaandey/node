# Gap Inc. Sales (Part II)
## The Story
One of my summer jobs in high school was as a sales associate at the Gap. We never got much foot traffic, to the point where some of the shelves collected dust (not kidding). Meanwhile, my friend working at the nearby Old Navy would get swamped underneath mountains of $10 tees- I was just glad to have shorter shifts. Fast forward a few years, and turns out Gap wasn't doing so great financially. Old Navy, their only profitable brand, wanted to spin off, and Gap's longtime CEO stepped down.

Was it the $80 denim that turned customers away? Or the riduculous G-A-P sweaters that should've been retired in 2003? Naturally, I turned to data science for answers. Since Gap Inc. doesn't make their store-by-store sales data public, we made up our own.

## The Task
Pretend you're a data scientist at Gap Inc., tasked with exploring sales trends in the Virginia market. Leadership has provided a list of questions, which you can find in the lab notebook itself. 

### Notes
| Interactive Notebook | Source Code  |
| :-----------: | :------------: |
| [![Link](../../tools/buttons/open-colab.svg)](https://colab.research.google.com/github/ishaandey/node/blob/master/week-3/lab/gap_cleaning_notes.ipynb) | [![Link](../../tools/buttons/download-ipynb.svg)](https://files.node.ishaandey.com/week-3/lab/gap_cleaning_notes.ipynb) |

### Key
| Interactive Notebook | Source Code  |
| :-----------: | :------------: |
| [![Link](../../tools/buttons/open-colab.svg)](https://colab.research.google.com/github/ishaandey/node/blob/master/week-3/lab/gap_cleaning_key.ipynb) | [![Link](../../tools/buttons/download-ipynb.svg)](https://files.node.ishaandey.com/week-3/lab/gap_cleaning_key.ipynb) |

**Note**: These questions are fairly open ended, and some of them can be quite hard. **We don't expect you to finish**; however much you get through in an hour is more than enough. Think of the rest as extra practice if you'd like. 

**Tips**:
* Convert each question into a **set of actions**. If you want to look at some attribute of Gap sales, think about subsetting the dataframe to where the store == Gap, before tackling the rest.
* Build your answer part by part: take a look at the output on each step to verify you're getting what you want.
* **Google** is your best friend. Look for StackOverflow or Pandas documentation in particular. 
* **Read the errors**. It's scary, but its there for a reason. 
* If you can't figure out what a specific part of code is doing, either try running just that part, <br>or use **type(...)** to see what type of object is being returned 
* **Slack** one of the instructors with (a) what you've tried, and (b) specific questions (not "help pls"). Ask your peers too!

## The Data
This data represents individual transactions in Banana Republic and Gap stores in VA from Q1 of FY2020. We've got granular information on every attribute: Each order, each item purchased in that order, which customer bought it, where, when, and how the purchase was made.

### Documentation

| **Feature** | **Description**    | **Sample Value(s)**  |
| ------- | -----------    | ------------- |
| OrderID | Unique identifier per transaction (7-digit) | DRW7C20   |
| CustomerID | Unique identifier per customer (5-digit) | KP441   |
| ProductID  | Unique identifier per item (8-digit) | 13-817-239 |
| StoreID | Unique identifier per store (4-digit) | #4176 |
| OrderType | How purchase was completed  | InStore, HomeDelivery, Online |
| Timestamp | Timestamp of transaction (YYYY-MM-DD) | 2020-01-18 10:13:56	 |
| Brand | Which reporting segment of Gap Inc. bought from | Banana Republic |
| ItemSize | Size of item | XS, S, M, L, X, XL |
| ProductName | Name of item associated with item identifier | Pink Polo by Kanye |
| Collection | Which part of store | Denim Shop |
| Price | Listed price of item | $29.95 |
| ClearanceType | Type of clearance | Retail, Clearance, Final Sale |
| DiscountType | If Gap Card rewards was used | Reward points, Promotion, GapCash, Other |
| StoreName | Store name or facility where order was purchased from | Fair Oaks Mall |
| Location | State of store location | VA |

#### Quick note on IDs 

IDs are a really important part of many, if not most datasets. Each unique *thing*, whether that's a product, or store, or customer, gets assigned **it's own unique identifier**. 

This is important in case two stores have the same name (i.e. Gap and Banana Republic at the Fair Oaks Mall). When we group by Store Name, for example, we want to make sure we're not accidentally clumping up both both stores, and instead keep the two seperate. 

