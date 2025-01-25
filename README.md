# CSC 310 HW 01
Instructions:
Write a program that will:

Read from a comma delimited text file called us-contacts.csv into the appropriate dynamic array structure for the language (e.g., ArrayList for Java or std::vector in C++). Initially, you could test your code with a much smaller file (e.g., maybe something like five lines of input).

Note: in some cases, we might instead be reading in from a database and also wouldn't know exactly how many records might be returned. Note also that a CSV file is simply a text file. On windows, you can open it with any normal text editor (including notepad in Windows).
For your language of interest, you could ask a GPT something general like "What is the modern way to do dynamic arrays in C++?", or ask something more specific to this problem (e.g., related to reading in a CSV file).

Each row from the contact list should be stored in a "Contact" object or struct, and thus overall the contacts will be stored in a dynamic array of contacts.

The contacts are in the form: First name, Last name, Street, City, State, Zip, Phone, Email.
Sort the contacts by Last name. Ideally the language has a built in sort.

Print every 50th contact until you run out of contacts (starting with the 50th contact, not the first). If the language uses indexing that starts at 0, the first contact to print will be at index 49. This should require that you only access the array 10 times, and it should be a direct access. A linked list would not allow such direct access.

Extra credit (5 pts):

Solve the same problem in two programming languages.

Using an online random data generator, generate a CSV test file with 10,000 records and the same fields as us-contacts.csv. There are various sites so please explore and let me know if you find something you like. mockaroo is popular, but it's now capped at 1000 records with a free account. https://cobbl.io/ seems to work well and is easy to use. It will generate a header line in the CSV - write your code to skip this, or edit the text file to remove the first line. https://randomtools.io/dev-tools/data-generator/ will generate over 10,000 records although the site crashed while I was using it.

Instead of printing every 50th record, print every 1000th record (starting with the 1000th). This should print 10 records overall.

Include code in your programs that determine the overall running time (including reading in the file), and print out that running time. Do you notice much of a difference between the two languages for such a small file?
