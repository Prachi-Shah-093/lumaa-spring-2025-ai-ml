# Movie Recommendation System

## Prachi Shah | Arizona State University  
📧 Email: ppshah@asu.edu  
🔗 LinkedIn: [Prachi Shah](https://www.linkedin.com/in/prachi-shah-04ba66203/)  

---

## 1. Where is the dataset from?

After searching online, I found a website called [dolt.com](https://www.dolt.com) that filters through public datasets. The dataset used for this challenge is publicly stored on GitHub:  
🔗 [Netflix Metaflow Movies Dataset](https://github.com/Netflix/metaflow/blob/master/metaflow/tutorials/01-playlist/movies.csv)

**⚠️ Note:** The original dataset was too large. It has been reduced to 500 rows (without sorting) as per the challenge's specifications.

---

## 2. Setup (Windows OS)

### Python Version: 3.13.2
Follow the instructions in the link below to download and install the latest Python version:  
🔗 [How to Update Python](https://www.pythoncentral.io/how-to-update-python/)

### Python Dependencies
Run the following command to install the necessary dependencies:
```sh
pip install pandas scikit-learn
```

### IDE: Visual Studio Code
My choice of IDE was Visual Studio Code. Follow the instructions in the link below to set it up:  
🔗 [VS Code Setup Guide](https://code.visualstudio.com/docs/setup/windows#_install-vs-code-on-windows)

#### Recommended Extensions
- **Code Runner Extension**: This extension allows for easier execution of Python code. To install it:
  1. Open VS Code
  2. Go to the Extensions tab (left panel)
  3. Search for **Code Runner**
  4. Click **Install**
  5. Now, simply click the **Run/Play** button to execute your script

This extension is more convenient than manually typing out the full directory path for a `.py` file.

---

## 3. Running the Code

1. Download the `movies.csv` file and place it inside your project folder.
2. Open `Main.py` and click the **Run/Play** button.
3. You will be prompted with the following question:
   ```sh
   What movie genres do you feel like watching?
   ```
4. Type at least one genre you like (e.g., Fantasy, Adventure, etc.).
5. Press **Enter**, and the top five recommended movies will be displayed along with their **Similarity Score**.

---

## 4. Results

### Sample Query
```sh
I like D&D, so how about I watch a movie with Fantasy, Romance, and Adventure?
```

### Sample Output
```sh
Based on your input, you may like the following top 5 picks. Enjoy!

1. Prince of Persia: The Sands of Time - Similarity Score: 0.9333
2. Spider-Man 2 - Similarity Score: 0.9333
3. Spider-Man - Similarity Score: 0.9333
4. The Twilight Saga: Breaking Dawn - Part 2 - Similarity Score: 0.8599
5. The Twilight Saga: Breaking Dawn - Part 2 - Similarity Score: 0.8599
```

Happy Watching! 🎬🍿

