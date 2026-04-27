from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


stored_assets = {
    "template_1": [0.9, 0.1, 0.2],
    "template_2": [0.2, 0.8, 0.3],
    "template_3": [0.7, 0.2, 0.6]
}


def find_similar_asset():
    query_vector = np.array([[0.8, 0.2, 0.2]])

    best_match = None
    best_score = -1

    for asset_name, vector in stored_assets.items():
        score = cosine_similarity(
            query_vector,
            np.array([vector])
        )[0][0]

        if score > best_score:
            best_score = score
            best_match = asset_name

    return best_match, round(best_score, 2)