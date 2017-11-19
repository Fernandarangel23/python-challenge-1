## Unit 3 | Assignment - Py Me Up, Charlie

##  Option 3: PyBoss

![Boss](Images/boss.jpg)

In this challenge, you get to be the _boss_. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.

Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:

* Import the `employee_data1.csv` and `employee_data2.csv` files, which currently holds employee records like the below:


```
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
```

* Then convert and export the data to use the following format instead:


```
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
```

* In summary, the required conversions are as follows:

  * The `Name` column should be split into separate `First Name` and `Last Name` columns.

  * The `DOB` data should be re-written into `DD/MM/YYYY` format.

  * The `SSN` data should be re-written such that the first five numbers are hidden from view.

  * The `State` data should be re-written as simple two-letter abbreviations.

* Special Hint: You may find this link to be helpful—[Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).


## Hints and Considerations

* Consider what we've learned so far. To date, we've learned how to import modules like `csv`; to read and write files in various formats; to store contents in variables, lists, and dictionaries; to iterate through basic data structures; and to debug along the way. Using what we've learned, try to break down you tasks into discrete mini-objectives. This will be a _much_ better course of action than attempting to Google Search for a miracle.

* As you will discover, for some of these challenges, the datasets are quite large. This was done purposefully, as it showcases one of the limits of Excel-based analysis. While our first instinct, as data analysts, is often to head straight into Excel, creating scripts in Python can provide us with more robust options for handling "big data".

* Feel encouraged to work in groups, but don't shortchange yourself by copying someone else's work. You get what you put in, and the art of programming is extremely unforgiving to smoochers. Dig your heels in, burn the nigh oil, and learn this while you can! These are skills that will pay dividends in your future career.

* Start early, and reach out for help often! Challenge yourself to identify _specific_ questions for your instructors and TAs. Don't resign yourself to simply saying, "I'm totally lost." Come prepared to show your effort and thought patterns, we'll be happy to help along the way.

* Always commit your work and back it up with GitHub pushes. You don't want to lose hours of your work because you didn't push it to GitHub every half hour or so.

  * **Commit often**.

* Don't spend too much time trying to choose the "right" challenge. Each of these is fairly comparable in difficulty level, and you'll need to use most of the same techniques in each. Waffling won't get you anywhere. Pick your battle, and stick with it! Good luck!

## Copyright

Coding Boot Camp © 2016. All Rights Reserved.
