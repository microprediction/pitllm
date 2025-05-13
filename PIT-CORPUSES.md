# Point-in-Time Corpus Sequences

This document lists major corpora and datasets that provide chronologically consistent text sequences, organized by domain and time period.

## News and Media Corpora

### American Stories Dataset
- **Coverage**: 17th-20th century
- **Size**: 1+ billion historical newspaper articles
- **Source**: [Discover Magazine (2023)](https://discovermagazine.com)
- **Features**: 
  - Yearly clustering of major stories
  - Historical context preservation
  - Cultural trend analysis
- **Use Cases**: Historical research, cultural studies, media analysis

### New York Times Annotated Corpus
- **Coverage**: 1987-2007
- **Size**: 1.8 million articles
- **Source**: [NYT](https://catalog.ldc.upenn.edu/LDC2008T19)
- **Features**:
  - Article metadata
  - Topic categorization
  - Named entity annotations
- **Use Cases**: News analysis, temporal event tracking

### Reuters News Archive
- **Coverage**: 1996-present
- **Size**: Millions of articles
- **Source**: [Reuters](https://www.reuters.com)
- **Features**:
  - Real-time news updates
  - Financial news focus
  - Global coverage
- **Use Cases**: Financial analysis, event detection

## Social Media Corpora

### Twitter TimeLMs Corpus
- **Coverage**: 2019-Q4 → 2022-Q4
- **Size**: Quarterly snapshots
- **Source**: [TimeLMs Project](https://github.com/cardiffnlp/timelms)
- **Features**:
  - Quarterly updates
  - Language evolution tracking
  - Trend analysis
- **Use Cases**: Social media analysis, language change studies

### Reddit Historical Data
- **Coverage**: 2005-present
- **Size**: Monthly dumps
- **Source**: [Pushshift](https://pushshift.io)
- **Features**:
  - Subreddit-specific data
  - User interactions
  - Content evolution
- **Use Cases**: Community analysis, trend tracking

## Historical and Literary Corpora

### Corpus of Historical American English (COHA)
- **Coverage**: 1810-2009
- **Size**: 400+ million words
- **Source**: [BYU](https://www.english-corpora.org/coha/)
- **Features**:
  - Decade-by-decade sampling
  - Multiple genres
  - Balanced representation
- **Use Cases**: Historical linguistics, cultural studies

### Google Books Ngram Corpus
- **Coverage**: 1500-2019
- **Size**: Trillions of words
- **Source**: [Google Books](https://books.google.com/ngrams)
- **Features**:
  - Yearly word frequencies
  - Multiple languages
  - Massive scale
- **Use Cases**: Lexical change, cultural trends

## Scientific and Technical Corpora

### PubMed Central Archive
- **Coverage**: 1781-present
- **Size**: Millions of articles
- **Source**: [NCBI](https://www.ncbi.nlm.nih.gov/pmc/)
- **Features**:
  - Full-text articles
  - Medical/scientific focus
  - Citation networks
- **Use Cases**: Scientific progress tracking, medical history

### arXiv Papers
- **Coverage**: 1991-present
- **Size**: 2+ million papers
- **Source**: [arXiv](https://arxiv.org)
- **Features**:
  - Multiple disciplines
  - Version history
  - Citation data
- **Use Cases**: Scientific progress analysis, knowledge evolution

## Legal and Government Corpora

### U.S. Supreme Court Opinions
- **Coverage**: 1791-present
- **Size**: All published opinions
- **Source**: [CourtListener](https://www.courtlistener.com)
- **Features**:
  - Full text opinions
  - Citation networks
  - Justice voting patterns
- **Use Cases**: Legal history, precedent analysis

### Congressional Record
- **Coverage**: 1873-present
- **Size**: Complete proceedings
- **Source**: [Congress.gov](https://www.congress.gov)
- **Features**:
  - Daily proceedings
  - Legislation tracking
  - Policy evolution
- **Use Cases**: Political history, policy analysis

## Financial and Economic Corpora

### SEC EDGAR Database
- **Coverage**: 1993-present
- **Size**: All SEC filings
- **Source**: [SEC](https://www.sec.gov/edgar)
- **Features**:
  - Company filings
  - Financial statements
  - Regulatory documents
- **Use Cases**: Financial analysis, regulatory compliance

### Federal Reserve Economic Data (FRED)
- **Coverage**: 1774-present
- **Size**: 800,000+ time series
- **Source**: [FRED](https://fred.stlouisfed.org)
- **Features**:
  - Economic indicators
  - Historical data
  - Cross-country comparisons
- **Use Cases**: Economic analysis, policy research

## Best Practices for Using Temporal Corpora

1. **Data Validation**
   - Verify temporal boundaries
   - Check for data leakage
   - Validate chronological consistency

2. **Preprocessing Considerations**
   - Handle changing formats
   - Account for OCR errors in historical texts
   - Normalize temporal references

3. **Analysis Methods**
   - Use appropriate time windows
   - Consider temporal dependencies
   - Account for data sparsity in early periods

4. **Ethical Considerations**
   - Respect copyright and licensing
   - Consider privacy implications
   - Handle sensitive historical content appropriately

## Resources for Corpus Creation

### Tools
- [TemporalWiki](https://github.com/joeljang/temporalwiki) - Framework for temporal knowledge extraction
- [ChroKnowBench](https://github.com/ChroKnowBench) - Benchmarking tools for temporal corpora
- [FinGPT](https://github.com/fingpt) - Financial temporal analysis toolkit

### Guidelines
- [Temporal Data Best Practices](https://arxiv.org/abs/2204.14211)
- [Historical Corpus Construction](https://arxiv.org/abs/2106.15110)
- [Temporal Evaluation Metrics](https://arxiv.org/abs/2410.09870) 