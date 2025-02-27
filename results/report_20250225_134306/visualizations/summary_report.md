# Benchmark Summary Report

## 1. Overall Statistics

- **Total runs**: 128
- **Total test cases**: 56
- **Total batches**: 3
- **Timestamp**: 20250225_134306

## 2. Performance Metrics

### 2.1 Duration Statistics

- **Average duration**: 14.71s
- **Median duration**: 13.44s
- **Minimum duration**: 1.46s
- **Maximum duration**: 50.84s
- **Standard deviation**: 7.71s

### 2.2 Duration Percentiles

| Percentile | Duration (s) |
|------------|-------------|
| 10% | 5.25 |
| 25% | 10.48 |
| 50% | 13.44 |
| 75% | 18.27 |
| 90% | 23.88 |
| 95% | 26.91 |
| 99% | 39.84 |

### 2.3 Error Statistics

- **Overall error rate**: 16.41%

**Error rates by complexity**:

- intermediate: 25.00%
- basic: 12.50%
- advanced: 10.00%

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
| 0 | 11.11% |
| 2 | 33.33% |
| 4 | 0.00% |

### 3.3 Performance by Context Depth

| Context Depth | Average Duration (s) |
|---------------|----------------------|
| 0 | 14.58 |
| 2 | 15.19 |
| 4 | 20.60 |

## 4. Language Analysis

### 4.1 Language Distribution

| Language | Test Count | Percentage |
|----------|------------|------------|
| en | 68 | 53.1% |
| jp | 60 | 46.9% |

### 4.2 Language Performance Comparison

| Language | Avg Duration (s) | Median Duration (s) | Std Dev (s) | Error Rate |
|----------|------------------|---------------------|-------------|------------|
| en | 15.61 | 13.32 | 8.03 | 17.65% |
| jp | 13.69 | 13.57 | 7.25 | 15.00% |

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
| trend_analysis | 20.55 | 0.00% |
| quoted_reference | 17.32 | 16.67% |
| correlation | 16.61 | 8.33% |
| schema_validation | 16.00 | 25.00% |
| context_dependent | 15.69 | 8.33% |
| error_recovery | 13.59 | 34.38% |
| grouping | 12.72 | 15.00% |
| aggregation | 12.61 | 15.00% |
| join | 12.20 | 8.33% |
| progressive_refinement | 11.18 | 43.75% |

## 6. Operation Time Analysis

### 6.1 Overall Operation Time Statistics

| Operation | Avg Time (s) | Std Dev (s) | Frequency | % of Total Time |
|-----------|--------------|-------------|-----------|----------------|
| User Intent Analysis | 2.00 | 1.58 | 104 (81.2%) | 14.9% |
| Answer Generation | 1.81 | 1.58 | 98 (76.6%) | 13.5% |
| VannaAI SQL Generation | 1.76 | 2.19 | 55 (43.0%) | 13.1% |
| Initial Query Generation | 1.27 | 1.80 | 55 (43.0%) | 9.4% |
| Table Retrieval | 1.23 | 1.65 | 55 (43.0%) | 9.2% |
| Retry Analysis | 1.01 | 3.37 | 16 (12.5%) | 7.5% |
| Basic Chat Processing | 0.97 | 1.23 | 98 (76.6%) | 7.2% |
| Query Fixing | 0.81 | 1.69 | 30 (23.4%) | 6.1% |
| Query Execution | 0.73 | 1.36 | 110 (85.9%) | 5.4% |
| Column Extraction | 0.66 | 0.96 | 55 (43.0%) | 4.9% |
| Query Optimization | 0.62 | 2.09 | 14 (10.9%) | 4.7% |
| Error Response Generation | 0.40 | 0.96 | 21 (16.4%) | 2.9% |
| Query Execution 1 | 0.11 | 0.45 | 30 (23.4%) | 0.8% |
| Query Execution 2 | 0.04 | 0.36 | 15 (11.7%) | 0.3% |

### 6.2 Operation Time by Complexity

#### Complexity Level: advanced

- **Total average time**: 14.98s
- **Breakdown**:

| Operation | Time (s) | % of Total |
|-----------|----------|------------|
| User Intent Analysis | 2.62 | 17.5% |
| VannaAI SQL Generation | 2.35 | 15.7% |
| Answer Generation | 1.87 | 12.5% |
| Table Retrieval | 1.57 | 10.5% |
| Initial Query Generation | 1.49 | 10.0% |
| Query Fixing | 1.31 | 8.7% |
| Basic Chat Processing | 0.98 | 6.6% |
| Column Extraction | 0.90 | 6.0% |
| Query Execution | 0.80 | 5.4% |
| Query Optimization | 0.59 | 3.9% |
| Error Response Generation | 0.23 | 1.5% |
| Query Execution 1 | 0.16 | 1.0% |
| Query Execution 2 | 0.11 | 0.8% |

#### Complexity Level: basic

- **Total average time**: 14.31s
- **Breakdown**:

| Operation | Time (s) | % of Total |
|-----------|----------|------------|
| Answer Generation | 2.26 | 15.8% |
| Retry Analysis | 1.93 | 13.5% |
| User Intent Analysis | 1.68 | 11.8% |
| VannaAI SQL Generation | 1.49 | 10.4% |
| Basic Chat Processing | 1.28 | 9.0% |
| Initial Query Generation | 1.25 | 8.8% |
| Table Retrieval | 1.22 | 8.5% |
| Query Execution | 0.80 | 5.6% |
| Query Fixing | 0.73 | 5.1% |
| Query Optimization | 0.63 | 4.4% |
| Column Extraction | 0.59 | 4.1% |
| Error Response Generation | 0.34 | 2.4% |
| Query Execution 1 | 0.08 | 0.5% |
| Query Execution 2 | 0.02 | 0.2% |

#### Complexity Level: intermediate

- **Total average time**: 11.41s
- **Breakdown**:

| Operation | Time (s) | % of Total |
|-----------|----------|------------|
| User Intent Analysis | 1.74 | 15.2% |
| VannaAI SQL Generation | 1.49 | 13.1% |
| Answer Generation | 1.40 | 12.3% |
| Initial Query Generation | 1.09 | 9.5% |
| Retry Analysis | 1.08 | 9.4% |
| Table Retrieval | 0.97 | 8.5% |
| Basic Chat Processing | 0.70 | 6.2% |
| Query Optimization | 0.65 | 5.7% |
| Query Execution | 0.60 | 5.3% |
| Error Response Generation | 0.58 | 5.1% |
| Column Extraction | 0.53 | 4.6% |
| Query Fixing | 0.47 | 4.1% |
| Query Execution 1 | 0.11 | 1.0% |
| Query Execution 2 | 0.00 | 0.0% |

### 6.3 Operation Time Variability

| Operation | Coefficient of Variation |
|-----------|---------------------------|
| Query Execution 2 | 4.90 |
| Query Optimization | 3.85 |
| Query Execution 1 | 3.76 |
| Retry Analysis | 2.48 |
| Query Fixing | 2.36 |
| Query Execution | 2.11 |
| Error Response Generation | 1.83 |
| Initial Query Generation | 1.68 |
| Column Extraction | 1.53 |
| Table Retrieval | 1.41 |

## 7. Error Type Analysis

### 7.1 Overall Error Distribution

**Total errors**: 21 (16.4% of all tests)

| Error Type | Count | % of Errors |
|------------|-------|------------|
| PROMPTFLOW | 16 | 76.2% |
| UNEXPECTED | 5 | 23.8% |

### 7.2 Error Types by Complexity

#### Complexity Level: advanced

- No Error: 36 (90.0%)
- PROMPTFLOW: 4 (10.0%)
- UNEXPECTED: 0 (0.0%)
#### Complexity Level: basic

- No Error: 35 (87.5%)
- PROMPTFLOW: 3 (7.5%)
- UNEXPECTED: 2 (5.0%)
#### Complexity Level: intermediate

- No Error: 36 (75.0%)
- PROMPTFLOW: 9 (18.8%)
- UNEXPECTED: 3 (6.2%)
## 8. Retry Analysis

**Total retry attempts**: 44
**Successful retries**: 34 (77.3%)

### 8.1 Error Types Triggering Retries

| Error Type | Count | % of Retries |
|------------|-------|-------------|
| PROMPTFLOW | 6 | 13.6% |

### 8.2 Performance Impact

**Average duration change**: 1.43s (retries take longer on average)

| Operation | Time Change (s) |
|-----------|----------------|
| Retry Analysis | 6.55 |
| Query Fixing | -1.52 |
| Error Response Generation | 1.27 |
| VannaAI SQL Generation | 1.11 |
| Initial Query Generation | -0.88 |
| Query Optimization | -0.65 |
| Query Execution 1 | -0.40 |
| Answer Generation | -0.19 |
| Column Extraction | -0.15 |
| Query Execution | 0.13 |
| Table Retrieval | -0.09 |
| Basic Chat Processing | 0.04 |
| User Intent Analysis | 0.04 |
| Query Execution 2 | -0.00 |

## 9. AI Search Analysis

### 9.1 Distribution

| Mode | Count | % of Total |
|------|-------|------------|
| AI Search | 64 | 50.0% |
| Normal Flow | 64 | 50.0% |

### 9.2 Performance Comparison

| Mode | Avg Duration (s) | Median Duration (s) | Std Dev (s) | Error Rate |
|------|------------------|---------------------|-------------|------------|
| AI Search | 12.28 | 12.12 | 4.58 | 26.56% |
| Normal Flow | 17.15 | 15.76 | 9.31 | 6.25% |

### 9.3 Performance by Complexity

#### Complexity Level: advanced

| Mode | Count | Avg Duration (s) | Error Rate |
|------|-------|------------------|------------|
| AI Search | 20 | 13.80 | 20.00% |
| Normal Flow | 20 | 19.96 | 0.00% |

#### Complexity Level: basic

| Mode | Count | Avg Duration (s) | Error Rate |
|------|-------|------------------|------------|
| AI Search | 20 | 12.58 | 20.00% |
| Normal Flow | 20 | 18.54 | 5.00% |

#### Complexity Level: intermediate

| Mode | Count | Avg Duration (s) | Error Rate |
|------|-------|------------------|------------|
| AI Search | 24 | 10.77 | 37.50% |
| Normal Flow | 24 | 13.63 | 12.50% |

## 10. Key Findings and Recommendations

### 10.1 Performance Bottlenecks

Top time-consuming operations:

- **User Intent Analysis**: 2.00s (14.9% of total time)
- **Answer Generation**: 1.81s (13.5% of total time)
- **VannaAI SQL Generation**: 1.76s (13.1% of total time)

### 10.2 Error Patterns

Most common error types:

- **PROMPTFLOW**: 16 occurrences (76.2% of all errors)
- **UNEXPECTED**: 5 occurrences (23.8% of all errors)

### 10.3 Challenging Query Types

Categories with highest error rates:

- **trend_analysis**: 75.00% error rate, 8.35s avg duration
- **error_handling**: 43.75% error rate, 11.18s avg duration
- **retry_scenarios**: 25.00% error rate, 16.00s avg duration

### 10.4 Recommendations

1. **Optimize User Intent Analysis**: This operation consumes the most time on average.
2. **Address PROMPTFLOW errors**: This is the most common error type.
3. **Improve handling of intermediate complexity queries**: These have the highest error rate.
4. **Expand retry coverage**: Current retry success rate is 77.3%.
5. **Improve en language support**: This language has the highest error rate.

## 11. Conclusion

This benchmark analysis provides a comprehensive overview of the database query flow system's performance across various dimensions. The results highlight both strengths and areas for improvement, with specific recommendations for optimizing performance and reducing errors.

Key metrics to track in future benchmark runs include:

1. Overall error rate and distribution of error types
2. Operation time breakdown, especially for the most time-consuming operations
3. Performance differences across complexity levels and languages
4. Effectiveness of retry mechanisms and AI search capabilities

Regular benchmarking will help track progress and identify regressions as the system evolves.
