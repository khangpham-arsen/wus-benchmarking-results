# Operation Time Analysis Summary

## Top 10 Operations by Average Time

| Operation | Mean (s) | Std Dev (s) | Frequency | CV |
|-----------|----------|-------------|-----------|----|
| User Intent Analysis | 2.192 | 1.23 | 106 | 0.561 |
| VannaAI SQL Generation | 1.956 | 2.912 | 56 | 1.489 |
| Answer Generation | 1.903 | 2.753 | 95 | 1.447 |
| Table Retrieval | 1.165 | 1.691 | 55 | 1.452 |
| Query Execution | 0.928 | 2.45 | 111 | 2.639 |
| Query Fixing | 0.831 | 1.466 | 35 | 1.763 |
| Basic Chat Processing | 0.817 | 0.589 | 98 | 0.721 |
| Retry Analysis | 0.815 | 2.39 | 16 | 2.934 |
| Column Extraction | 0.626 | 0.931 | 55 | 1.486 |
| Error Response Generation | 0.476 | 1.076 | 27 | 2.258 |

## Key Observations

### Most Time-Consuming Operations
- User Intent Analysis: 2.192s
- VannaAI SQL Generation: 1.956s
- Answer Generation: 1.903s

### Most Variable Operations (Highest CV)
- Query Execution 2: CV = 7.065
- Query Execution 1: CV = 4.708
- Retry Analysis: CV = 2.934

### Most Frequent Operations
- Query Execution: 111 occurrences
- User Intent Analysis: 106 occurrences
- Basic Chat Processing: 98 occurrences
