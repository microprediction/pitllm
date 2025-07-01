# Temporal Granularity Guide for Open Source Corpus Development

This document outlines the possible temporal granularity options for different open source data sources when building point-in-time corpora. Understanding these granularity options is crucial for designing effective temporal corpus development strategies.

## Overview

Temporal granularity refers to the smallest time unit at which data can be meaningfully segmented for corpus development. The choice of granularity affects:
- **Corpus Size**: Finer granularity = more corpora but smaller individual files
- **Processing Complexity**: Finer granularity = more processing overhead
- **Temporal Precision**: Finer granularity = more precise temporal analysis
- **Storage Requirements**: Finer granularity = higher storage needs
- **Update Frequency**: How often new data becomes available

## Temporal Granularity Matrix

| Data Source | Hourly | Daily | Weekly | Bi-weekly | Monthly | Bi-monthly | Quarterly | Yearly | Decadal | **Recommended** |
|-------------|--------|-------|--------|-----------|---------|------------|-----------|--------|---------|-----------------|
| **Twitter (Academic API)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **Quarterly** |
| **Reddit (Pushshift)** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **Monthly** |
| **Wikipedia (Dumps)** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **Monthly** |
| **SEC EDGAR** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **Quarterly** |
| **Financial News (Common Crawl)** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **Monthly** |
| **FRED Economic Data** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **Monthly** |
| **arXiv Papers** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **Monthly** |
| **Historical Newspapers** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **Yearly** |
| **Historical Literature (COHA)** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | **Decadal** |
| **Congressional Record** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **Yearly** |
| **Court Opinions** | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **Yearly** |

**Legend**: ✅ = Supported, ❌ = Not Supported, **Bold** = Recommended for our project

## Detailed Granularity Specifications

### Social Media Corpora

#### Twitter (Academic Research API)
- **Raw Granularity**: Extremely fine timestamps (to the second)
- **Recommended**: Quarterly (matches TimeLMs approach, manageable size)
- **Volume**: 45-180GB per quarter
- **Processing Notes**: Large tweet corpora often batched by month or quarter for manageability

#### Reddit (Pushshift Historical Data)
- **Raw Granularity**: Timestamped posts/comments
- **Recommended**: Monthly (Pushshift distributes monthly data dumps)
- **Volume**: 30-150GB per month
- **Processing Notes**: Monthly snapshots are standard for Reddit corpora

#### Wikipedia (Edit History & Dumps)
- **Raw Granularity**: Edit-level timestamps
- **Recommended**: Monthly (full content dumps roughly twice per month)
- **Volume**: 10-50GB per month
- **Processing Notes**: Monthly snapshots of entire encyclopedia are standard

### Financial and Economic Corpora

#### SEC EDGAR Filings
- **Raw Granularity**: Daily filing timestamps
- **Recommended**: Quarterly (EDGAR offers quarterly index files)
- **Volume**: 3-15GB per quarter
- **Processing Notes**: Quarterly aggregation matches business reporting cycles

#### Financial News (Common Crawl)
- **Raw Granularity**: Article publication dates
- **Recommended**: Monthly (Common Crawl provides monthly web crawl snapshots)
- **Volume**: 3-15GB per month
- **Processing Notes**: Filter Common Crawl for financial news content

#### Federal Reserve Data (FRED)
- **Raw Granularity**: Varies by series (daily to quarterly)
- **Recommended**: Monthly (CPI, employment data)
- **Volume**: 30-300MB per month
- **Processing Notes**: Can aggregate monthly data to annual frequency

### Academic and Research Corpora

#### Open Research Papers (arXiv, PubMed)
- **Raw Granularity**: Paper submission/publication dates
- **Recommended**: Monthly (all papers published in a month)
- **Volume**: 300MB-1.5GB per month
- **Processing Notes**: Each article has clear publication timestamp

### Historical Corpora

#### Historical Newspapers (Chronicling America)
- **Raw Granularity**: Daily publication dates (1756-1963)
- **Recommended**: Yearly (combining all issues from a year)
- **Volume**: 300MB-3GB per year
- **Processing Notes**: Often aggregated by year to preserve historical context

#### Historical Literature (COHA, Google Books)
- **Raw Granularity**: Publication dates
- **Recommended**: Decadal (COHA organized by decade)
- **Volume**: 100MB-1GB per decade
- **Processing Notes**: Historical texts often grouped in multi-year spans

### Government and Legal Corpora

#### Government Records (Congressional Record)
- **Raw Granularity**: Daily when Congress in session
- **Recommended**: Yearly (annual session-based volumes)
- **Volume**: 300MB-3GB per year
- **Processing Notes**: Daily transcripts compiled into annual volumes

#### Court Opinions (Caselaw Access Project)
- **Raw Granularity**: Opinion publication dates
- **Recommended**: Yearly (all decisions from a year)
- **Volume**: 300MB-3GB per year
- **Processing Notes**: Can compile by year or larger spans as needed

## Recommended Granularity by Use Case

### High-Frequency Analysis
- **Granularity**: Daily or Weekly
- **Use Cases**: Real-time monitoring, rapid trend detection
- **Data Sources**: Twitter, Reddit, Financial news
- **Considerations**: High processing overhead, large storage requirements

### Standard Temporal Analysis
- **Granularity**: Monthly or Quarterly
- **Use Cases**: Language evolution, trend analysis, research applications
- **Data Sources**: Most sources support this granularity
- **Considerations**: Balanced approach, manageable processing

### Long-Term Historical Analysis
- **Granularity**: Yearly or Decadal
- **Use Cases**: Historical research, long-term evolution studies
- **Data Sources**: Historical newspapers, literature, government records
- **Considerations**: Lower processing overhead, stable corpora

## Implementation Considerations

### Processing Complexity
- **Finer Granularity**: More processing overhead, more frequent updates
- **Coarser Granularity**: Less processing overhead, more stable corpora
- **Hybrid Approach**: Different granularities for different sources

### Quality Control
- **Temporal Boundaries**: Ensure no future information leakage
- **Consistency**: Maintain consistent granularity within domains
- **Validation**: Verify temporal accuracy across all sources

## Best Practices for Corpus Development

### 1. Start with Standard Granularity
- Begin with monthly or quarterly granularity for most sources
- Allows for manageable processing and storage requirements
- Provides sufficient temporal resolution for most use cases

### 2. Consider Domain-Specific Requirements
- **Social Media**: Quarterly (matches existing TimeLMs)
- **Financial**: Quarterly (matches business cycles)
- **Historical**: Yearly (preserves historical context)
- **Academic**: Monthly (matches publication cycles)

### 3. Plan for Scalability
- Design pipelines that can handle multiple granularities
- Consider storage and processing requirements
- Plan for future granularity adjustments

### 4. Maintain Consistency
- Use consistent granularity within each domain
- Document granularity choices and rationale
- Ensure temporal boundaries are clearly defined

## Conclusion

The choice of temporal granularity significantly impacts corpus development strategy. For our open source corpus project, we recommend:

- **Twitter**: Quarterly (following TimeLMs precedent)
- **Financial**: Quarterly (matching business cycles)
- **Historical**: Yearly (preserving historical context)
- **Academic**: Monthly (matching publication cycles)

This approach balances temporal precision with practical considerations for processing, storage, and maintenance while ensuring high-quality, accessible temporal corpora for the research community. 