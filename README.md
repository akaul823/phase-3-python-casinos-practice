# Object Relations Code Challenge - Casinos

For this assignment, you will be working with a Casino domain.

We have three models: `Gambler`, `Bid`, and `Dealer`.

For our purposes, a `Gambler` has many `Bids`, a `Dealer` has many `Bids`, and `Bid` belong to both `Gambler` and `Dealer`.

`Gambler` - `Dealer` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed in a suggested order, but you can feel free to tackle the ones you think are easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge does not have tests. You cannot run `pytest`. You'll need to create your own sample instances so that you can try out your code on your own. Make sure your relationships and methods work in the console before submitting.

We've provided you with a tool that you can use to test your code. To use it, run `python tools/debug.py` from the command line. This will start a `ipdb` session with your classes defined. You can test out the methods that you write here. You can add code to the `tools/debug.py` file to define variables and create sample instances of your objects.

Writing error-free code is more important than completing all of the deliverables listed - prioritize writing methods that work over writing more methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First, prioritize getting things working. Then, if there is time at the end, refactor your code to adhere to best practices. When you encounter duplicated logic, extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you expect. If you have any methods that are not working yet, feel free to leave comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.

### Initializers, Readers, and Writers

#### Gambler

- `Gambler __init__(self, name,type)`
  - An gambler is initialized with a name as a string and type as a string where type can only equal light,moderate,or heavy.
  - A name **cannot** be changed after it is initialized.
- `Gambler name()`
  - Returns the name of the gambler
- `Gambler type()`
  - Returns the type of gambler ie.light,moderate,or heavy

#### Dealer

- `Dealer __init__(self, name)`
  - A dealer is initialized with a name as a string 
  - The name of the dealer **cannot** be changed after being initialized.
- `Dealer name()`
  - Returns the name of this dealer

#### Bid

- `Bid __init__(self, gambler,dealer, amount)`
  - A Bid is initialized with a gambler as a Gambler object, a dealer as a Dealer object, and amount as a float.
- `Bid amount()`
  - Returns the amount for that given bid

### Object Relationship Methods

#### Bid

- `Bid gambler()`
  - Returns the gambler for that given bid
- `Bid dealer()`
  - Returns the dealer for that given bid

#### Gambler

- `Gambler bids()`
  - Returns an list of Bid instances the gambler has made
- `Gambler dealers()`
  - Returns a **unique** list of Dealer instances for which the gambler has made bids to

#### Dealer

- `Dealer gamblers()`
  - Returns an list of Gambler instances with whom the Dealer has made bids

- `Dealer bid_amounts()`
  - Returns a **unique** list of floats of the bid amounts the dealer has made with gamblers

### Associations and Aggregate Methods

#### Gambler

- `Gambler make_bid(dealer, amount)`
  - Given a dealer (as Dealer instance) and an amount (as a float), creates a new Bid instance and associates it with that gambler and that dealer.
- `Gambler highest_dealer()`
  - Returns the dealer with whom the gambler has made the highest average bids

#### Dealer

- `Dealer gambler_types()`
  - Returns an list of strings of the types of gamblers the dealer has made bids with
- `Dealer heaviest_gambler()`
  - Returns the gambler that has made the highest average bids with the dealer
