#  Book Recommender System

A machine learning-based system that recommends books using collaborative filtering and content-based filtering techniques.

---

##  Features
- Personalized book recommendations.
- Hybrid filtering approach (collaborative + content-based).
- Easy-to-use Streamlit interface for interaction.

---

##  Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Streamlit  
- **Dataset:** Book-Crossing dataset (Kaggle)

---

##  Datasets & Model Files  
Due to file size constraints, the dataset and trained model are hosted on Google Drive:

[ Download Dataset & Model ](https://drive.google.com/drive/folders/1y8SFSMuUHEd9jPt11o3peK8O3pXwthEQ?usp=drive_link)

> After downloading, place your files into the following directories:
> - Dataset (e.g., `.csv` files) → `data/`  
> - Trained model (`.pkl`) → `models/`

---

##  Installation & Usage

```bash
git clone https://github.com/faizaan90/Book-Recommendor-System.git
cd Book-Recommendor-System

# (Recommended) Set up a virtual environment:
python -m venv venv
# Activate it:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
# source venv/bin/activate

# Install dependencies:
pip install -r requirements.txt

# Ensure you’ve downloaded and placed the dataset and model correctly.
pip install streamlit
streamlit run app.py

#Screenshot
<img width="1248" height="854" alt="image" src="https://github.com/user-attachments/assets/bd9f3656-23f3-4529-b03c-e5b80ce77a1f" />
