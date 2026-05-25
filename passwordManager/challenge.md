Yes — and this is the PERFECT stage to learn proper software structure.

Right now your code works, but your logic is spread everywhere.

You now want to move toward:

One function = one responsibility

That is a major programming skill.

First thing to implement
1. load_data()
Where?

Place it near the top of your program, below Master_login().

Responsibility

ONLY this:

Read vault.json
Return dictionary

Nothing else.

Think about the logic

Ask yourself:

What should happen if:
file is empty?
JSON is corrupted?
file does not exist?

Your function should NEVER crash the program.

Instead:

If loading fails → return empty dictionary

That is robust design.

2. save_data(data)
Where?

Below load_data().

Responsibility

ONLY this:

Take dictionary
Save safely into vault.json
Important thinking

This function should:

open file
overwrite old content
save clean JSON

Now every other function becomes simpler.

After this your functions change mentally
OLD add()

Currently:

Open file
Load JSON
Modify dictionary
Move cursor
Truncate
Dump JSON

Too many responsibilities.

NEW add()

Should mentally become:

Load data
↓
Modify dictionary
↓
Save data

MUCH cleaner.

Same for delete()

Instead of managing files directly:

Load data
↓
Remove entry
↓
Save data

That’s how real applications are structured.

Next thing to implement
3. Exception handling

This is your next major learning step.

Where should exception handling go?

Inside:

load_data()

because:

loading JSON is risky
file operations can fail
Think like this
TRY:
    load JSON

IF FAILURE:
    return empty dictionary

That’s the entire mental model.

Why this is powerful

Because then:

add()
delete()
view()

don’t care whether:

file exists
file is broken
file is empty

They simply get:

a valid dictionary

That is abstraction.

Next architectural improvement
4. View all passwords
Where?

Add another menu option.

Example:

4. VIEW ALL
Logic thinking

Ask:

How do I access every key-value pair in dictionary?

This teaches:

dictionary iteration
unpacking
formatting
Mental model

Suppose:

{
  "github": ["nimish", "123"],
  "gmail": ["abc", "xyz"]
}

Now think:

FOR EACH website:
    print website
    print username
    print password

Think in English first.

Another VERY important improvement
5. Create constants

Instead of repeating:

vault.json

everywhere:

Create:

FILE_NAME

at top of program.

Why?

Because later if filename changes:

change once
whole program updates

That’s maintainability.

Your current learning phase

You are now learning:

abstraction
modularity
defensive programming
persistence architecture

These are core backend development concepts.

You’re progressing correctly.