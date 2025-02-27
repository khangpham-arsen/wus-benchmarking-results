# Benchmark Summary Report

## 1. Overall Statistics

- **Total runs**: 128
- **Total test cases**: 56
- **Total batches**: 3
- **Timestamp**: 20250227_111351

## 2. Performance Metrics

### 2.1 Duration Statistics

- **Average duration**: 15.65s
- **Median duration**: 14.70s
- **Minimum duration**: 1.22s
- **Maximum duration**: 54.51s
- **Standard deviation**: 7.54s

### 2.2 Duration Percentiles

| Percentile | Duration (s) |
|------------|-------------|
| 10% | 6.13 |
| 25% | 11.19 |
| 50% | 14.70 |
| 75% | 19.68 |
| 90% | 23.54 |
| 95% | 26.57 |
| 99% | 36.75 |

### 2.3 Error Statistics

- **Overall error rate**: 12.50%

**Error rates by complexity**:

- advanced: 20.00%
- basic: 15.00%
- intermediate: 4.17%

## 3. Context Analysis

### 3.1 Chat Context Depth Distribution

| Context Depth | Test Count | Percentage |
|---------------|------------|------------|
| 0 | 36 | 52.9% |
| 2 | 24 | 35.3% |
| 4 | 8 | 11.8% |

### 3.2 Error Rates by Context Depth

| Context Depth | Error Rate |
|---------------|------------|
| 0 | 13.89% |
| 2 | 20.83% |
| 4 | 0.00% |

### 3.3 Performance by Context Depth

| Context Depth | Average Duration (s) |
|---------------|----------------------|
| 0 | 15.57 |
| 2 | 17.18 |
| 4 | 19.83 |

## 4. Language Analysis

### 4.1 Language Distribution

| Language | Test Count | Percentage |
|----------|------------|------------|
| en | 68 | 53.1% |
| jp | 60 | 46.9% |

### 4.2 Language Performance Comparison

| Language | Avg Duration (s) | Median Duration (s) | Std Dev (s) | Error Rate |
|----------|------------------|---------------------|-------------|------------|
| en | 15.53 | 15.20 | 5.34 | 14.71% |
| jp | 15.79 | 13.33 | 9.48 | 10.00% |

## 5. Feature Analysis

### 5.1 Top Features by Occurrence

| Feature | Occurrences | Percentage |
|---------|-------------|------------|
| error_recovery | 32 | 10.5% |
| correlation | 24 | 7.8% |
| context_dependent | 24 | 7.8% |
| grouping | 20 | 6.5% |
| aggregation | 20 | 6.5% |
| schema_validation | 16 | 5.2% |
| progressive_refinement | 16 | 5.2% |
| join | 12 | 3.9% |
| quoted_reference | 12 | 3.9% |
| trend_analysis | 10 | 3.3% |
| pattern_matching | 10 | 3.3% |
| semantic_similarity | 10 | 3.3% |
| counting | 8 | 2.6% |
| conditional | 8 | 2.6% |
| pattern_detection | 8 | 2.6% |

### 5.2 Feature Impact on Performance

| Feature | Avg Duration (s) | Error Rate |
|---------|------------------|------------|
| trend_analysis | 20.86 | 0.00% |
| correlation | 17.84 | 16.67% |
| context_dependent | 17.14 | 8.33% |
| progressive_refinement | 16.80 | 12.50% |
| quoted_reference | 16.27 | 33.33% |
| error_recovery | 14.33 | 12.50% |
| join | 14.13 | 16.67% |
| grouping | 13.43 | 10.00% |
| aggregation | 12.65 | 0.00% |
| schema_validation | 11.86 | 12.50% |

## 6. Operation Time Analysis

### 6.1 Overall Operation Time Statistics

| Operation | Avg Time (s) | Std Dev (s) | Frequency | % of Total Time |
|-----------|--------------|-------------|-----------|----------------|
| User Intent Analysis | 2.19 | 1.23 | 106 (82.8%) | 18.3% |
| VannaAI SQL Generation | 1.96 | 2.91 | 56 (43.8%) | 16.3% |
| Answer Generation | 1.90 | 2.75 | 95 (74.2%) | 15.9% |
| Table Retrieval | 1.16 | 1.69 | 55 (43.0%) | 9.7% |
| Query Execution | 0.93 | 2.45 | 111 (86.7%) | 7.7% |
| Query Fixing | 0.83 | 1.47 | 35 (27.3%) | 6.9% |
| Basic Chat Processing | 0.82 | 0.59 | 98 (76.6%) | 6.8% |
| Retry Analysis | 0.81 | 2.39 | 16 (12.5%) | 6.8% |
| Column Extraction | 0.63 | 0.93 | 55 (43.0%) | 5.2% |
| Error Response Generation | 0.48 | 1.08 | 27 (21.1%) | 4.0% |
| Query Execution 1 | 0.20 | 0.96 | 35 (27.3%) | 1.7% |
| Query Execution 2 | 0.07 | 0.52 | 17 (13.3%) | 0.6% |

### 6.2 Operation Time by Complexity

#### Complexity Level: advanced

- **Total average time**: 12.33s
- **Breakdown**:

| Operation | Time (s) | % of Total |
|-----------|----------|------------|
| User Intent Analysis | 2.78 | 22.6% |
| VannaAI SQL Generation | 2.26 | 18.3% |
| Answer Generation | 1.61 | 13.1% |
| Query Fixing | 1.31 | 10.6% |
| Table Retrieval | 1.16 | 9.4% |
| Basic Chat Processing | 0.80 | 6.5% |
| Error Response Generation | 0.70 | 5.7% |
| Query Execution | 0.67 | 5.4% |
| Column Extraction | 0.61 | 4.9% |
| Query Execution 2 | 0.22 | 1.8% |
| Query Execution 1 | 0.22 | 1.7% |

#### Complexity Level: basic

- **Total average time**: 10.67s
- **Breakdown**:

| Operation | Time (s) | % of Total |
|-----------|----------|------------|
| User Intent Analysis | 1.73 | 16.3% |
| Answer Generation | 1.48 | 13.9% |
| VannaAI SQL Generation | 1.36 | 12.8% |
| Retry Analysis | 1.34 | 12.5% |
| Table Retrieval | 1.20 | 11.3% |
| Basic Chat Processing | 0.85 | 8.0% |
| Column Extraction | 0.74 | 6.9% |
| Query Execution | 0.68 | 6.4% |
| Query Fixing | 0.60 | 5.6% |
| Error Response Generation | 0.53 | 5.0% |
| Query Execution 1 | 0.13 | 1.3% |
| Query Execution 2 | 0.01 | 0.1% |

#### Complexity Level: intermediate

- **Total average time**: 12.80s
- **Breakdown**:

| Operation | Time (s) | % of Total |
|-----------|----------|------------|
| Answer Generation | 2.50 | 19.5% |
| VannaAI SQL Generation | 2.19 | 17.1% |
| User Intent Analysis | 2.08 | 16.3% |
| Query Execution | 1.35 | 10.6% |
| Table Retrieval | 1.14 | 8.9% |
| Retry Analysis | 1.06 | 8.3% |
| Basic Chat Processing | 0.81 | 6.3% |
| Query Fixing | 0.63 | 4.9% |
| Column Extraction | 0.55 | 4.3% |
| Query Execution 1 | 0.25 | 2.0% |
| Error Response Generation | 0.24 | 1.9% |
| Query Execution 2 | 0.00 | 0.0% |

### 6.3 Operation Time Variability

| Operation | Coefficient of Variation |
|-----------|---------------------------|
| Query Execution 1 | 5.26 |
| Query Execution 2 | 3.04 |
| Error Response Generation | 2.70 |
| Query Execution | 2.69 |
| Retry Analysis | 2.34 |
| Query Fixing | 1.91 |
| VannaAI SQL Generation | 1.73 |
| Answer Generation | 1.63 |
| Column Extraction | 1.28 |
| Table Retrieval | 1.22 |

## 7. Error Type Analysis

### 7.1 Overall Error Distribution

**Total errors**: 16 (12.5% of all tests)

| Error Type | Count | % of Errors |
|------------|-------|------------|
| PROMPTFLOW | 13 | 81.2% |
| UNEXPECTED | 3 | 18.8% |

### 7.2 Error Types by Complexity

#### Complexity Level: advanced

- No Error: 32 (80.0%)
- PROMPTFLOW: 8 (20.0%)
- UNEXPECTED: 0 (0.0%)
#### Complexity Level: basic

- No Error: 34 (85.0%)
- PROMPTFLOW: 4 (10.0%)
- UNEXPECTED: 2 (5.0%)
#### Complexity Level: intermediate

- No Error: 46 (95.8%)
- PROMPTFLOW: 1 (2.1%)
- UNEXPECTED: 1 (2.1%)
## 8. Retry Analysis

**Total retry attempts**: 44
**Successful retries**: 38 (86.4%)

### 8.1 Error Types Triggering Retries

| Error Type | Count | % of Retries |
|------------|-------|-------------|
| PROMPTFLOW | 5 | 11.4% |

### 8.2 Performance Impact

**Average duration change**: 1.67s (retries take longer on average)

| Operation | Time Change (s) |
|-----------|----------------|
| Retry Analysis | 6.86 |
| VannaAI SQL Generation | 1.18 |
| Answer Generation | -0.71 |
| Query Fixing | 0.47 |
| Query Execution | 0.38 |
| Column Extraction | -0.29 |
| Query Execution 1 | 0.21 |
| User Intent Analysis | -0.17 |
| Error Response Generation | -0.14 |
| Basic Chat Processing | -0.14 |
| Table Retrieval | -0.07 |
| Query Execution 2 | 0.00 |

## 9. AI Search Analysis

### 9.1 Distribution

| Mode | Count | % of Total |
|------|-------|------------|
| AI Search | 64 | 50.0% |
| Normal Flow | 64 | 50.0% |

### 9.2 Performance Comparison

| Mode | Avg Duration (s) | Median Duration (s) | Std Dev (s) | Error Rate |
|------|------------------|---------------------|-------------|------------|
| AI Search | 12.67 | 12.09 | 6.89 | 25.00% |
| Normal Flow | 18.63 | 19.55 | 7.00 | 0.00% |

### 9.3 Performance by Complexity

#### Complexity Level: advanced

| Mode | Count | Avg Duration (s) | Error Rate |
|------|-------|------------------|------------|
| AI Search | 20 | 12.69 | 40.00% |
| Normal Flow | 20 | 20.36 | 0.00% |

#### Complexity Level: basic

| Mode | Count | Avg Duration (s) | Error Rate |
|------|-------|------------------|------------|
| AI Search | 20 | 11.22 | 30.00% |
| Normal Flow | 20 | 16.77 | 0.00% |

#### Complexity Level: intermediate

| Mode | Count | Avg Duration (s) | Error Rate |
|------|-------|------------------|------------|
| AI Search | 24 | 13.87 | 8.33% |
| Normal Flow | 24 | 18.75 | 0.00% |

## 10. Key Findings and Recommendations

### 10.1 Performance Bottlenecks

Top time-consuming operations:

- **User Intent Analysis**: 2.19s (18.3% of total time)
- **VannaAI SQL Generation**: 1.96s (16.3% of total time)
- **Answer Generation**: 1.90s (15.9% of total time)

### 10.2 Error Patterns

Most common error types:

- **PROMPTFLOW**: 13 occurrences (81.2% of all errors)
- **UNEXPECTED**: 3 occurrences (18.8% of all errors)

### 10.3 Challenging Query Types

Categories with highest error rates:

- **behavioral_analysis**: 50.00% error rate, 14.02s avg duration
- **ai_search**: 25.00% error rate, 14.41s avg duration
- **data_verification**: 16.67% error rate, 18.11s avg duration

### 10.4 Recommendations

1. **Optimize User Intent Analysis**: This operation consumes the most time on average.
2. **Address PROMPTFLOW errors**: This is the most common error type.
3. **Improve handling of advanced complexity queries**: These have the highest error rate.
4. **Expand retry coverage**: Current retry success rate is 86.4%.
5. **Improve en language support**: This language has the highest error rate.

## 11. Conclusion

This benchmark analysis provides a comprehensive overview of the database query flow system's performance across various dimensions. The results highlight both strengths and areas for improvement, with specific recommendations for optimizing performance and reducing errors.

Key metrics to track in future benchmark runs include:

1. Overall error rate and distribution of error types
2. Operation time breakdown, especially for the most time-consuming operations
3. Performance differences across complexity levels and languages
4. Effectiveness of retry mechanisms and AI search capabilities

Regular benchmarking will help track progress and identify regressions as the system evolves.
