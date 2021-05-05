import numpy as np
import pandas as pd


def precision(predictions, label_ids, id2tkn, only_age=False, any_future_event=True, ignore_id=-100, shifted_labels=False, predictions_are_scores=True,
              old_data=None):
    r''' Calculate precision for next concept prediction.

    Args:
        predictions:
            Expected shape <batch_size> x <sequence_length> x <vocabulary_size>
        label_ids:
            Expected shape <batch_size> x <sequence_length>
        only_age:
            Calcualte only for tokens that represent age
        any_future_event:
            If set to true something is positive if it occured at any point in the future
            and not just at the next step.
        ignore_id:
            label_ids with this ID will be ignored
        shifted_labels:
            Are labels == input_ids, or shifted by one to the left
        predictions_are_scores:
            Are predictions scores for each label_id or really label_ids already
        old_data:
            If set it will load old values for tp/fp/positives/negatives and continue ontop of those

    Return (Dict[str, ]):
        precision:
            Precision
        tp:
            Number of True positives
        fp:
            Number of False positives
        positives:
            For each label ID a count of positive examples
        negatives
            For each label ID a count of negative examples
    '''
    if predictions_are_scores:
        outputs = np.argmax(predictions, axis=2)
    else:
        outputs = predictions
    tp = 0
    fp = 0
    positives = {}
    negatives = {}
    start = 1
    if shifted_labels:
        start = 0

    if old_data:
        tp = old_data['tp']
        fp = old_data['fp']
        positives = old_data['positives']
        negatives = old_data['negatives']

    for ind, lbl in enumerate(label_ids):
        for i in range(start, len(lbl)):
            # We start from 1 because there is no prediction of token at position 0, that
            #is the start token
            tkn = str(id2tkn.get(lbl[i], lbl[i]))
            is_age = True if tkn.isdecimal() and int(tkn) >= 0 and int(tkn) <= 300 else False
            if lbl[i] != ignore_id:
                if (is_age and only_age) or (not is_age and not only_age):
                    end = i+1 if not any_future_event else len(lbl)
                    if outputs[ind][i-start] in lbl[i:end]:
                        tp += 1
                        positives[tkn] = positives.get(tkn, 0) + 1
                    else:
                        fp += 1
                        negatives[tkn] = negatives.get(tkn, 0) + 1

    prec = tp / (tp + fp)

    return {'precision': prec, 'tp': tp, 'fp': fp, 'positives': positives, 'negatives': negatives}


def sort_precision_output(precision_output, cdb, main='positives'):
    d = precision_output
    if main == 'positives':
        other = 'negatives'
    else:
        other = 'positives'

    out = sorted([(
        "{:.2f}".format(tp / (tp + d[other].get(cui, 1))), 
        cdb.get_name(cui),
        tp,
        d[other].get(cui, 0),
        cui) for cui, tp in sorted(d[main].items(), key=lambda x: x[1], reverse=True)],
        key=lambda x: x[0], reverse=True)

    out = pd.DataFrame(out, columns=['precision', 'name', main, other, 'cui'])

    return out
