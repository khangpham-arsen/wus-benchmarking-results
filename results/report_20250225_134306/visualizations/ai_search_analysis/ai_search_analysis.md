# AI Search vs Normal Flow Analysis

## Overall Performance Comparison

```
             Mean Duration  Std Duration  Min Duration  Max Duration  Error Rate (%)
ai_search                                                                           
AI Search           12.281         4.579         1.598        23.853          26.562
Normal Flow         17.146         9.314         1.458        50.844           6.250
```

## Query Time Comparison

```
                            mean    std    min     max
Mode        Complexity                                
AI Search   advanced       5.928  2.640  3.653  13.966
            basic          3.901  2.374  0.000   9.712
            intermediate   3.816  3.225  0.000  13.354
Normal Flow advanced      12.643  5.131  6.320  27.640
            basic          9.717  5.464  0.000  19.204
            intermediate   8.005  7.042  0.000  27.421
```

## Key Findings

- Average Duration: AI Search is 28.4% faster than Normal Flow
- Error Rate: AI Search has 20.3% higher error rate than Normal Flow
- Total Query Time: AI Search is 54.9% faster than Normal Flow