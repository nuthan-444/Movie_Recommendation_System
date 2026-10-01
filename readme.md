# 🎬 Movie Recommendation System

A **content-based Movie Recommendation System** built using Machine Learning and Natural Language Processing (NLP).

The system recommends movies that are similar to a movie selected by the user. It uses movie information such as **genres, keywords, cast, crew, and overview** to determine the similarity between movies.

---

## 🚀 How It Works

The recommendation system follows these main steps:

```text
Movie Dataset
      ↓
Data Preprocessing
      ↓
Feature Selection
      ↓
Feature Combination
      ↓
Text Processing
      ↓
Vectorization
      ↓
Cosine Similarity
      ↓
Movie Recommendations
```

The movie information is converted into numerical vectors using text vectorization. The system then calculates the similarity between movies using **Cosine Similarity**.

When a user enters a movie name, the system finds movies with similar feature vectors and returns the most similar movies.

---

## 🧠 Machine Learning Approach

This project uses a **Content-Based Filtering** approach.

Instead of using ratings from multiple users, the system recommends movies based on the characteristics of the selected movie.

For example:

```text
User selects:

The Dark Knight

        ↓

System finds movies with similar features

        ↓

Recommendations:

Batman Begins
The Dark Knight Rises
...
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Natural Language Processing (NLP)
* CountVectorizer
* Cosine Similarity
* Joblib
* Jupyter Notebook

---

## 📂 Project Structure

The project contains the source code, dataset, trained model files, and the recommendation script.

```text
Movie-Recommendation-System/
│
├── model.ipynb
├── recommend.py
└── dataset/
     └── tmdb_5000_credits.csv
     └──tmdb_5000_movies.csv
├── vectors.pkl
├── DF.pkl
├── requirements.txt
└── README.md
```

### Files

| File                    | Description                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------- |
| `model.ipynb`           | Notebook used for preprocessing, feature engineering, vectorization, and model creation |
| `recommend.py`          | Python script used to generate movie recommendations                                    |
| `tmdb_5000_credits.csv` | Movie credits dataset                                                                   |
| `tmdb_5000_movies.csv`  | Movie information dataset                                                               |
| `vectors.pkl`           | Pre-generated movie feature vectors                                                     |
| `DF.pkl`                | Pre-generated movie dataframe                                                           |
| `requirements.txt`      | Required Python dependencies                                                            |
| `README.md`             | Project documentation                                                                   |

---

## 🤗 Pre-trained Model Files

The pre-generated model files are available here:

**Hugging Face Repository:**

https://huggingface.co/nuthan-444/Movie-Recommendation-System

The repository contains the files required to run the recommendation system without recreating the model from the notebook.

### Model Files

| File               | Description                                  |
| ------------------ | -------------------------------------------- |
| `DF.pkl`           | Contains the movie dataset/dataframe         |
| `vectors.pkl`      | Contains the vectorized movie features       |
| `requirements.txt` | Required Python dependencies                 |
| `recommend.py`     | Python script for generating recommendations |

---

## ⚙️ Installation

### 1. Download the Project

Clone the repository:

```bash
git clone https://github.com/nuthan-444/Movie_Recommendation_System.git
```

Move into the project directory:

```bash
cd Movie_Recommendation_System
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 Using the Pre-trained Model

If you want to use the already-generated model files without running the complete notebook, follow these steps.

### Step 1 — Download the Model Files

Download the following files:

```text
DF.pkl
vectors.pkl
```

from:

https://huggingface.co/nuthan-444/Movie_Recommendation_System

Place both files in the **same directory** as your Python script.

Your folder should look like:

```text
movie-recommendation/
│
├── DF.pkl
├── vectors.pkl
├── requirements.txt
└── recommend.py
```

---

### Step 2 — Install Dependencies

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```

---

### Step 3 — Create `recommend.py`

Create a Python file named:

```text
recommend.py
```

Add the following code:

```python
import joblib
from sklearn.metrics.pairwise import cosine_similarity

DF = joblib.load('DF.pkl')
vectors = joblib.load('vectors.pkl')

similarity = cosine_similarity(vectors)


def recommend(movie):
    movie_index = DF[DF['title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    for i in movie_list:
        print(DF.iloc[i[0]].title)


recommend('Avatar')
```

---

## ▶️ Run the Recommendation System

Run the Python script:

```bash
python recommend.py
```

For example:

```python
recommend('Avatar')
```

The system will print the **5 most similar movies** to `Avatar`.

You can change the movie name:

```python
recommend('Titanic')
```

or:

```python
recommend('The Dark Knight')
```

> Make sure the movie title exactly matches a title available in the `title` column of `DF.pkl`.

---

## 🔍 Example

### Input

```text
The Dark Knight
```

### Output

```text
Batman Begins
The Dark Knight Rises
Batman
...
```

The recommendations are generated based on the similarity between the selected movie and the other movies in the dataset.

---

## 📊 Similarity Technique

The project uses **Cosine Similarity** to measure how similar two movie vectors are.

Cosine Similarity measures the angle between two vectors.

A higher cosine similarity indicates that two movies have more similar features.

The similarity matrix is generated using:

```python
similarity = cosine_similarity(vectors)
```

---

## 🧩 Recommendation Process

When a movie is provided:

```text
Movie Name
    ↓
Find Movie in Dataset
    ↓
Get Its Vector
    ↓
Compare With All Movie Vectors
    ↓
Calculate Cosine Similarity
    ↓
Sort Similarity Scores
    ↓
Select Top 5
    ↓
Display Recommendations
```

---

## 💡 Why Content-Based Filtering?

Content-based filtering is useful when recommendations need to be based on the actual characteristics of an item.

In this project, movie metadata is used instead of relying on user ratings or user-to-user behavior.

This allows the system to recommend movies based on the characteristics of the selected movie.

---

## ⚠️ Important Notes

* Keep `DF.pkl`, `vectors.pkl`, and `recommend.py` in the same directory when using the pre-trained model files.
* Do not rename `DF.pkl` or `vectors.pkl` unless you also update the filenames in the Python code.
* The movie name must exactly match a title available in the `title` column of `DF.pkl`.
* The recommendation system returns the **top 5 similar movies**.
* The `.pkl` files are pre-generated and do not need to be recreated to use the recommendation script.
* The complete model-building process can be reproduced using `model.ipynb` to download goto below link.
* https://github.com/nuthan-444/Movie_Recommendation_System.

---

## 📓 Training / Development

The complete model-building process is available in:

```text
model.ipynb
```

The notebook covers:

* Data preprocessing
* Feature selection
* Feature engineering
* Feature combination
* Text processing
* Vectorization
* Cosine similarity
* Saving the generated model files

---

## 👨‍💻 Author

**Nuthan Prasad K G**

GitHub:

https://github.com/nuthan-444

---

## ⭐ If You Find This Project Useful

Feel free to explore the code, experiment with the recommendation system, and improve the project.
