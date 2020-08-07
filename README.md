# family-tree-maker	

### What is it?		
Make a png file of a family tree from excel sheet/google form. [familytreemaker by adrienverge](https://github.com/adrienverge/familytreemaker) generates the required ouput, and takes in a `.txt` file in a specific format. For someone wishing to make a family tree, a more convenient method might be to send out a short Google Form, and have the text file be created automatically, in the required format, and syntax.

#### Requirements: 
1. [familytreemaker by adrienverge](https://github.com/adrienverge/familytreemaker)
2. Excel sheet of given format - (Timestamp, Name, Father's name, Mother's name, Partner's name, Sex). A google form with all of these formats as questions will atomatically create this sheet. 
<img src="Google_Form.png" alt="Google Form" width="500"/>

#### How to use:		
1. Move the `maketreemaker.py` file from the above source into this repo's folder.
2. Move the excel file into the rep's folder, name it `"Family_Tree_Responses.xlsx"`.
3. Run 
```
./png_maker.py
```
`./png_maker.py` makes a call to [familytreemaker by adrienverge](https://github.com/adrienverge/familytreemaker). Hence, it is important that, Adrien's `familytreemaker.py` is in the repo's folder. Only that single file from the dependency is required for this program to run.

If it does not work, try running `chmod +x <filename.py>`.

This repo also includes a `menu.py` file, this gives lookup features for the people in the excel sheet. These include:
1. Searching for members by Name
2. Getting relative's information (mother, father, children, spouse)

**IMPORTANT**: 
1. The file requires a connected tree without any disconnected elements. If a disconnected tree is present, multiple `.png` files will be created for each connected subtree.

2. This does not supported cyclic connections. This only happens when siblings have children, or a person is a child of themselves. [Adrien Verge](https://github.com/adrienverge) kindly let'\s us know that something is, `Seriously wrong`. This can happen due to a mistake during data input. Therefore, recheck the excel sheet if this error is shown.


### How does it work?		

Excel Sheet is read and converted to a JSON file. (This JSON file is handy to have and can be used for other projects as well)		
JSON file is read, and `Member` data structures are created for each entry. Each `Member` has attributes as each column of the excel sheet.		
`Member` is wrapped by a `Node` data structure. This has a `data` attribute which is a pointer to its respective the `Member` class.		
`Node` has other attributes like `mother`, `father`, and `spouse`, which are references to `Member` objects, and `children` which is an array of references to `Member` objects.		

A "Tree" is then created by adding references to each `Node`'s attributes.		
This tree may be a disconnected tree, as there might be people who do not have entries, which leaves empty spots in a family tree. The missing responses that would complete the tree will then need to be added in manually

Structure can be seen by this picture, made by using `./png_maker.py ` (ignore the spouse nodes).

<img src="template.png" alt="Google Form" width="500"/>

This example also does an excellent job of displaying some of the limitations of making the image. For [familytreemaker by adrienverge](https://github.com/adrienverge/familytreemaker) to work, and therefore `png_maker.py` to work, people without a spouse cannot have children. A spouse is always required. However if running `menu.py` with the same information, this is allowed. `menu.py` allows for people to have children without having a spouse, and for children to have a single parent. 

Therefore in the case of a single parent, they will cause issues in making of the png, but will be available for lookup. I recommend adding in a dummy spouse entry in the excel sheet, and assign it as the other parent. This won't affect the working of `menu.py`, and will allow `png_maker.py` to run as well. 
