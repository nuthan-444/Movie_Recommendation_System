# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using Machine Learning and Natural Language Processing (NLP).

The system recommends movies that are similar to a movie selected by the user. It uses information about movies such as their genres, keywords, cast, crew, and overview to determine similarity between movies.

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
* NLP
* CountVectorizer
* Cosine Similarity
* Joblib

---

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── movie_recommendation.ipynb
├── movies.csv
├── requirements.txt
├── README.md
│
└── model/            (to download this .pkl file goto  My Hugging Face Profile)
    ├── vectors.pkl 
    └── DF.pkl
```


---

## 📦 Model Files

The trained model files are hosted separately on **Hugging Face** because the `.pkl` files are too large for GitHub's normal file-size limit.

🤗 **Hugging Face Model:**
https://huggingface.co/

Download the required `.pkl` files from the Hugging Face repository before running the recommendation system locally.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/nuthan-444/Movie_Recommendation_System
cd Movie-Recommendation-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 Download the Model

Download the required `.pkl` files from the Hugging Face repository and place them in the appropriate project directory.


---

## ▶️ Running the Recommendation System

Open the Jupyter Notebook / VS code:

Then open:

```text
movie_recommendation.ipynb
```

Run the cells and provide a movie name to get recommendations.

Example:

```python
recommend("The Dark Knight")
```

Output:

```text
Batman Begins
The Dark Knight Rises
Batman
...
```

---

## 🔍 Example

### Input

```text
The Dark Knight
```

### Output

```text
1. Batman Begins
2. The Dark Knight Rises
3. Batman
4. ...
```

The recommendations are generated based on the similarity between the selected movie and other movies in the dataset.

---

## 📊 Similarity Technique

The project uses **Cosine Similarity** to measure how similar two movie vectors are.

The similarity score is based on the angle between two vectors.

A higher cosine similarity indicates that two movies have more similar features.

```text
Similarity → Higher
      ↓
More similar movies
```

---

## 💡 Why Content-Based Filtering?

Content-based filtering is useful when recommendations need to be based on the actual characteristics of an item.

In this project, movie metadata is used instead of relying on user ratings or user-to-user behavior.

This means the system can recommend movies based on the selected movie's content.


---

## 👨‍💻 Author

**Nuthan Prasad K G**

GitHub:
https://github.com/nuthan-444

---

## ⭐ If You Find This Project Useful

Feel free to explore the code, experiment with the model, and improve the recommendation system.
