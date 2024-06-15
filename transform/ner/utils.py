
def tokens_to_entities(entities):
    scored_entities = []
    current_entity = ""
    current_label = None
    current_score = 0
    num_tokens = 0

    for entity in entities:
        word = entity['word']
        label = entity['entity']
        score = entity['score']

        if label.startswith("B-") or (label.startswith("I-") and current_label and label[2:] != current_label[2:]):
            if current_entity:
                average_score = current_score / num_tokens if num_tokens > 0 else 0
                scored_entities.append((current_entity, average_score))
            current_entity = word
            current_label = label
            current_score = score
            num_tokens = 1
        elif label.startswith("I-") and current_label and label[2:] == current_label[2:]:
            if word.startswith("##"):
                current_entity += word[2:]
            else:
                current_entity += " " + word
            current_score += score
            num_tokens += 1
        else:
            if current_entity:
                average_score = current_score / num_tokens if num_tokens > 0 else 0
                scored_entities.append((current_entity, average_score))
            current_entity = word
            current_label = label
            current_score = score
            num_tokens = 1

    if current_entity:
        average_score = current_score / num_tokens if num_tokens > 0 else 0
        scored_entities.append((current_entity, average_score))

    return scored_entities


def get_unique_entities(scored_entities):
    entity_dict = {}
    for entity, score in scored_entities:
        if entity in entity_dict:
            entity_dict[entity]['total_score'] += score
            entity_dict[entity]['count'] += 1
        else:
            entity_dict[entity] = {'total_score': score, 'count': 1}

    # unique_combined_entities = [(entity, data['total_score']) for entity, data in entity_dict.items()]
    unique_combined_entities = [(entity, data['total_score'] / data['count']) for entity, data in entity_dict.items()]

    # Sort combined entities by average score in descending order
    sorted_combined_entities = sorted(unique_combined_entities, key=lambda x: x[1], reverse=True)

    return sorted_combined_entities


