# AI Search vs Normal Flow Analysis

## Overall Performance Comparison

```
             Mean Duration  Std Duration  Min Duration  Max Duration  Error Rate (%)
ai_search                                                                           
AI Search           12.673         6.891         1.216        54.508            25.0
Normal Flow         18.632         6.999         1.674        38.644             0.0
```

## Query Time Comparison

```
                           mean    std  min     max
Mode        Complexity                             
AI Search   advanced      5.609  2.856  0.0  14.357
            basic         3.666  2.442  0.0   8.329
            intermediate  6.375  9.009  0.0  46.610
Normal Flow advanced      7.267  3.021  0.0  12.688
            basic         5.797  3.919  0.0  15.043
            intermediate  5.856  3.153  0.0  14.993
```

## Key Findings

- Average Duration: AI Search is 32.0% faster than Normal Flow
- Error Rate: AI Search has 25.0% higher error rate than Normal Flow
- Total Query Time: AI Search is 15.8% faster than Normal Flow