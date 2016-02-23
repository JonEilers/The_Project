# The_Project
Bio-497 environmental genomics class project: Shelby and Jon

### To do list

__Shelby__
{x}* What numbers in the jplace file correspond to fields? tree and placements
{x}* what is named multiplicity? corresponds to the "nm" value in the jplace file
  * If you scroll down to "multiplicity" it talks about what it is. I am finding the documentation about guppy is helpful in general too. http://matsen.github.io/pplacer/generated_rst/guppy.html#id8
* draw a small tree and make a small jplace file and show how they correspond to eachother.
* Figure how to tell if placement on the tip vs internal 
* look into EDPL

__Jon__
* What is the likelihood and why is negative. What is more likely vs less likely
* what are the values that corresponde to the reference tree numbers
* figure out how to change what information is displayed on the tree using archaeoptryx
* How to find leaves in the tree section of the jplace file
* Talk to statistican about hidden markov models and other math shit
* Newick file format
* look for figures to use. figure for jplace file, fat tree with placement labels, example of python code

### Project proposal paper:


- __Introduction__
  - Background: talk metagenomics -> phylogenetic trees -> pipeline -> pplacer and fat trees
  - Questions/state of the field: No easy way to extract data. 
  - Primary goals: Write a script to extract a variety of data from jplace
  - Hypothesis: We will write a fucking mind blowing script null: it won't be fucking mind blowing or....analysis of internal vs leaves will alter tree interpretation.
- __Methods__
  - Data type: jplace file/json
  * Annotation pipeline: phylosift
  * Statistics: summary statistics 
     *We should probably ask what sort of stats we will be doing. She will probably have a better idea that my vaguery  
  * Software packages: phylosift
- __Expected Outcomes__
  * What we expect to find: Fucking awesome script. extrapolate on how abundance data will influence interpretation
  * Mock figures: Psuedo code, concept map, phylogenetic fat tree vs normal tree 
- __References__
  * Ten references: uuhhhh

### Resources

__Online Arhaeoptryx example__ 
http://matsen.fredhutch.org/pplacer/demo/p4z1r36.html

__Papers__
Some papers we could possible reference for our final project presentation/paper? 
http://matsen.fredhutch.org/pplacer/
http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-11-538

__Python JSON Parsing__
http://docs.python-guide.org/en/latest/scenarios/json/



__Guppy Documentation__
http://matsen.github.io/pplacer/generated_rst/guppy.html#id8
This contains tidbits on guppy. 
* Interestingly, guppy has a command (info) which writes the number of leaves on the tree and how many partial placements are on each leaf. http://matsen.github.io/pplacer/generated_rst/guppy_info.html#guppy-info
* Also, the guppy command for making fat trees counts the number reads mapped to internal edges. If we can look at the code and make sense of it we might be able to convert to python. http://matsen.github.io/pplacer/generated_rst/guppy_fat.html#guppy-fat

__DAP__
Hmmm, maybe we should poke around the DAP to see if any of it could be useful for us? I have access to its github repository. __JE__

__Newick Format__
* At the bottom of the wikipedia page on newick format is a setion on parsing newick formats. Some interesting bits down there. https://en.wikipedia.org/wiki/Newick_format __JE__
* Also, it appears there is a python module for doing things with newick trees. I haven't looked, but I am guessing it might contain hints as to how we could do things to the 'tree' section of the jplace file
https://github.com/glottobank/python-newick and https://pypi.python.org/pypi/newick/0.4.0 __JE__

__Nested Dictionaries__
Ok, in rereading the jplace paper I noticed that not only are the sections of the jplace file treated as a dictionary, but also certain subsections are (I think). For example, each placement 'p' has keys and values associated with it. I haven't checked to see how this plays out (mentally out of it at the moment), but there is a python module for nested dictionary. I am assuming that is what this data structure is. Feel free to let me know how wrong i am :-) 
https://pypi.python.org/pypi/nested_dict __JE__

