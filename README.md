# Boolean-Minimization

## User Guide
`git clone https://github.com/k3liang/Boolean-Minimization`  
`cd Boolean-Minimization/`  

After cloning the github directory and making it the working directory, you can run the algorithm with input redirection:  
`py quine-mccluskey/quine-mccluskey.py < path/to/inputfile`  
The input file is expected to have a bitstring on every line representing each minterm. Examples can be seen in the `tests/` folder.

To generate a test input (that contains random minterms), run the following:  
`py tests/createtests.py`  
The program will prompt you for input on how many variables and how many minterms you want to generate, and it will put the test input file in `tests/`

To run the algorithm without input redirection (and just input minterms via the terminal), run:  
`py quine-mccluskey/quine-mccluskey.py`  
Then proceed to input minterms one at a time (where each minterm is represented as its bitstring). Press `Enter` after entering each minterm, then proceed to enter the next minterm. To end input, press `Enter` twice in a row.
