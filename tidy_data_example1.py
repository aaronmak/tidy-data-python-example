import pandas as pd

test_scores = pd.read_csv('tidy_data_example1.csv')
print(test_scores)

test_scores_clean = pd.melt(
    test_scores,
    id_vars=['Student'],
    var_name=['Subject'],
    value_name='Score'
)
print(test_scores_clean)

test_scores_clean.to_csv('tidy_data_example1-clean.csv',
                         index=False)
