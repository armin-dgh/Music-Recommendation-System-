# 🎵 Music Recommendation System 

## 📌 Overview
This project is a **content-based music recommendation system**.  
Given a song name, it finds and returns the most similar songs based on textual data (e.g., lyrics or descriptions) using **TF-IDF vectorization** and **Cosine Similarity**.

---

## ⚙️ How It Works
1. **Preprocessing**
   - Tokenization: split text into words.
   - Stopword removal: remove common words like `the`, `and`, `is`.
   - Stemming: reduce words to their root form.

2. **Vectorization (TF-IDF)**
   - Converts text into numerical vectors.
   - **Formula:**
     \[
     TF\!-\!IDF(t,d) = TF(t,d) \times \log\frac{N}{df(t)}
     \]
     where `TF` = term frequency, `IDF` = inverse document frequency.

3. **Similarity Calculation**
   - Uses **Cosine Similarity** to compare songs:
     \[
     \text{similarity}(A,B) = \frac{A \cdot B}{||A|| \times ||B||}
     \]
     Result is between 0 (no similarity) and 1 (identical).

4. **Recommendation**
   - Finds the input song in the dataset.
   - Retrieves its similarity scores to all other songs.
   - Sorts and returns the top N most similar songs.

---

## 📊 Example
```python
recommendation("Song A")
# Output:
["Song B", "Song C", "Song D", ...]

```
## 📥 Installation
```bash
git clone https://github.com/armin-dgh/Music-Recommendation-System-
cd music-recommendation
pip install -r requirements.txt
```