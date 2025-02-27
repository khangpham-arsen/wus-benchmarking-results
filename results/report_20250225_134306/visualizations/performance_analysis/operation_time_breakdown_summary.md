# Operation Time Analysis Summary

## Top 10 Operations by Average Time

| Operation | Mean (s) | Std Dev (s) | Frequency | CV |
|-----------|----------|-------------|-----------|----|
| User Intent Analysis | 1.996 | 1.581 | 104 | 0.792 |
| Answer Generation | 1.815 | 1.577 | 98 | 0.869 |
| VannaAI SQL Generation | 1.759 | 2.194 | 55 | 1.247 |
| Initial Query Generation | 1.267 | 1.801 | 55 | 1.422 |
| Table Retrieval | 1.235 | 1.649 | 55 | 1.336 |
| Retry Analysis | 1.008 | 3.366 | 16 | 3.34 |
| Basic Chat Processing | 0.972 | 1.234 | 98 | 1.269 |
| Query Fixing | 0.813 | 1.695 | 30 | 2.084 |
| Query Execution | 0.726 | 1.358 | 110 | 1.87 |
| Column Extraction | 0.664 | 0.965 | 55 | 1.453 |

## Key Observations

### Most Time-Consuming Operations
- User Intent Analysis: 1.996s
- Answer Generation: 1.815s
- VannaAI SQL Generation: 1.759s

### Most Variable Operations (Highest CV)
- Query Execution 2: CV = 8.35
- Query Execution 1: CV = 4.009
- Retry Analysis: CV = 3.34

### Most Frequent Operations
- Query Execution: 110 occurrences
- User Intent Analysis: 104 occurrences
- Answer Generation: 98 occurrences
