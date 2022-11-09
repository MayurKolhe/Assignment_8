## Program Instructions
1. Write a Python class that performs as a Tuffy Titan Inventory Management class which contains a dictionary of inventory items, methods to allow updates to the dictionary, and stores the contents of the dictionary in JSON format on the drive for later use.
1. The dictionary should use the following structure:
     ```
	inventory dictionary:
		key : barcode as a string (formatted as BCnnnn, where BC are the literal BC characters and nnnn is an integer)
		value : item list

	item list:
		element 0 : description as a string
		element 1 : quantity in inventory as an integer
     ``` 
1. Create an `inventory` module to meet the following requirements:
     1. Create a file named `inventory.py`.
          1. Define a class named `Inventory`.  
               1. Define a member function named `__init__` to meet the following requirements:
                    1. Take a `self` object as a positional parameter.
                    1. Take a `filename` string as a keyword parameter.
                    1. Define a `self.data` instance variable to hold the dictionary.
                    2. Open the `filename` JSON file, if it exists and contains data, assign the JSON deserialized data (a dictionary) to `self.data`, otherwise cleanly handle the error.
               1. Define a member function named `add_item` to meet the following requirements:
                    1. Take a `self` object as a positional parameter.
                    1. Take a `barcode` string as a keyword parameter.  Return an integer value of `109` if the value of the barcode does not meet the required format identified in the dictionary structure above.  Return an integer value of `101` if the barcode already exists in the dictionary.
                    1. Take a `description` string as a keyword parameter.
                    1. Add the item to the dictionary by setting the dictionary key to `barcode` and the value to the list made up of the `description` and the quantity of zero.
                    1. Write the updated dictionary to the `filename` provided in the `__init__` function.
                    1. Return an integer value of `100` for a successful add.
               1. Define a member function named `modify_description` to meet the following requirements:
                    1. Take a `self` object as a positional parameter.
                    1. Take a `barcode` string as a keyword parameter.  Return an integer value of `102` if the barcode does not exist in the dictionary.
                    1. Take a `description` string as a keyword parameter.
                    1. Update the item in the dictionary by setting the dictionary key to `barcode` and the value to the list made up of the `description` and the existing quantity (i.e the quantity should not change).
                    1. Write the updated dictionary to the `filename` provided in the `__init__` function.
                    1. Return an integer value of `100` for a successful add.
               1. Define a member function named `add_qty` to meet the following requirements:
                    1. Take a `self` object as a positional parameter.
                    1. Take a `barcode` string as a keyword parameter.  Return an integer value of `102` if the barcode does not exist in the dictionary.
                    1. Take a `qty` integer as a keyword parameter.  Return an integer value of `108` if the value of the qty does not meet the required format identified in the dictionary structure above (i.e. an integer).
                    1. Update the item in the dictionary by setting the dictionary key to `barcode` and the value to the list made up of the existing `description` and the existing quantity plus `qty` .
                    1. Write the updated dictionary to the `filename` provided in the `__init__` function.
                    1. Return an integer value of `100` for a successful add.
               1. Define a member function named `remove_qty` to meet the following requirements:
                    1. Take a `self` object as a positional parameter.
                    1. Take a `barcode` string as a keyword parameter.  Return an integer value of `102` if the barcode does not exist in the dictionary.
                    1. Take a `qty` integer as a keyword parameter.  Return an integer value of `108` if the value of the qty does not meet the required format identified in the dictionary structure above (i.e. an integer).
                    1. Return an integer value of `103` if the value of the qty is greater than the existing quantity in inventory. 
                    1. Update the item in the dictionary by setting the dictionary key to `barcode` and the value to the list made up of the existing `description` and the existing quantity minus `qty` .
                    1. Write the updated dictionary to the `filename` provided in the `__init__` function.
                    1. Return an integer value of `100` for a successful add.
               1. Define a member function named `get_inventory` to meet the following requirements:
                    1. Take a `self` object as a positional parameter.
                    1. Return a formatted string that contains all the items in the dictionary, each on a separate line.  The format should allow 8 characters for the barcode, 20 characters for the description, and 5 characters for the quantity, indicated as follows (note: the top line is for illustrative purposes only and should not be included in the return string):
		    <pre>
<i>|--8---||-------20---------||-5-|</i>
   			BC9001  Paper                 173
			BC9034  Notebook               84
			BC9026  Computer                7
			BC9072  Pencil                 21
   </pre>
1. While the main.py file does not need to be submitted and will not be graded, I strongly suggest you create your own very simple main.py file to create the object instance and make all the function calls with various data, to test the return strings and the dictionary of data.

    ```
    python3 -m main
    ```

1. Run the unit testing program to ensure that your program runs as expected.

    ```
    ./test.sh
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./test.sh` repeatedly until it passes all the test.

## Submission
Periodically throughout the exercise, and when you have completed the exercise, **submit the complete repository to Github**.

   <pre>git add .<br>git commit -m "<i>your comment</i>"<br>git push</pre>

In case it asks you  to configure global variables for an email and name, just copy the commands it provides then replace the dummy text with your email and Github token.

   <pre>git config --global user.email "<i>tuffy@csu.fullerton.edu</i>"<br>git config --global user.name "<i>Tuffy Titan</i>"<br>git commit -m "<i>your comment</i>"<br>git push</pre>

When you completed the final Github push, go back into github.com through the browser interface and ensure all your files have been correctly updated.  You should have the following files:
```
inventory.py
test.txt
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|initial git clone of this repository to your Tuffix machine|
|6|inventory.py file submitted and meets the program requirements |
|2|unit test passes Test01_CreatObjectNoFile|
|2|unit test passes Test02_CreatObjectWithFile|
|2|unit test passes Test03_AddItemBarcodeNotString|
|2|unit test passes Test04_AddItemBarcodeTooLong|
|2|unit test passes Test05_AddItemBarcodeDoesNotContainBC|
|2|unit test passes Test06_AddItemBarcodeEndsWithChar|
|2|unit test passes Test07_AddItemBarcodeValid|
|2|unit test passes Test08_AddItemBarcodeDuplicate|
|2|unit test passes Test09_AddItemBarcodeValidDataWrite|
|2|unit test passes Test10_ModifyDescriptionBarcodeNotFound|
|2|unit test passes Test11_ModifyDescriptionBarcodeValid|
|2|unit test passes Test12_ModifyDescriptionBarcodeValidDataWrite|
|2|unit test passes Test13_AddQtyBarcodeNotFound|
|2|unit test passes Test14_AddQtyNotInt|
|2|unit test passes Test15_AddQtyValid|
|2|unit test passes Test16_AddQtyValidDataWrite|
|2|unit test passes Test17_RemoveQtyBarcodeNotFound|
|2|unit test passes Test18_RemoveQtyNotInt|
|2|unit test passes Test19_RemoveQtyNotEnoughSupply|
|2|unit test passes Test20_RemoveQtyValid|
|2|unit test passes Test21_RemoveQtyValidDataWrite|
|2|unit test passes Test22_GetInventory|
