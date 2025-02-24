Prachi Shah | Arizona State University | ppshah@asu.edu | LinkedIn: https://www.linkedin.com/in/prachi-shah-04ba66203/


1) Where is the dataset from?

    - After doing some searching on the internet, I found a website called dolt.com what filters through public datasets. The following I found to use for this challenge is stored publicly on Github: https://github.com/Netflix/metaflow/blob/master/metaflow/tutorials/01-playlist/movies.csv
    
    - **PLEASE NOTE: The original database is too large. It has been cut down to 500 rows (without sorting) as per the challenge's specifications. 

2) Setup (Windows OS)

    - Python Version: 3.13.2:
    I used the following link's instructions to download and install the latest Python version:
    https://www.pythoncentral.io/how-to-update-python/

    - Python Dependencies:
    Make sure to run the following dependencies for the code to run:
        pip install pandas scikit-learn

    - IDE: Visual Studio Code:
    My choice of IDE was V.S. Code. The following link has a list of instructions to run python code for this IDE:
    https://code.visualstudio.com/docs/setup/windows#_install-vs-code-on-windows

    Extensions:
    - For easier execution, I use the Code Runner Extention on V.S. Code. Just head over to the Extentions tab on left of the window and type "Code Runner." Install it, then go to your code and click on the Run/Play Button. 
    - This is a great extention to use compared to typing out the whole directory path for a .py file.

3) Running Code

    - Make sure to download the "movies.csv" file of the movies dataset and put it within your project folder.
    - The code resides within the Main.py file. Click on the Run/Play Button. You will be met with the following question: "What movie genres do you feel like watching?"
    - Answer the question by typing at least one genre you like (E.g. Fantasy, Adventure, etc.).
    - Press the "Enter" key and the top five results closest to your input will display, along with the "Similarity Score".

4) Results

    - Sample Query: "I like D&D, so how about I watch a movie with Fantasy, Romance, and Adventure?"
    - Results: 

        Based on your input, you may like the following top 5 picks. Enjoy!

        Prince of Persia: The Sands of Time - Similarity Score: 0.9332846116984514
        Spider-Man 2 - Similarity Score: 0.9332846116984514
        Spider-Man - Similarity Score: 0.9332846116984514
        The Twilight Saga: Breaking Dawn - Part 2 - Similarity Score: 0.8599389206686123
        The Twilight Saga: Breaking Dawn - Part 2 - Similarity Score: 0.8599389206686123

